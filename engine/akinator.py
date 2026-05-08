"""
Akinator mexanizmi — ketma-ket aqlli savollar orqali tashxisni toraytiradi.

Ishlash prinsipi:
  1. Har bir qadam bemor bergan javoblarga qarab keyingi ENG MUHIM savolni tanlaydi.
  2. Savol tanlash: hozirgi simptomlar bilan barcha kasalliklarni baholaydi,
     keyin eng ko'p ma'lumot beradigan (differensirovka qiladigan) simptomni tanlaydi.
  3. Minimun 5, maksimum 12 savol beradi.
  4. Erta to'xtatish (early stop): agar bir kasallik boshqalardan aniq ustun tursa —
     to'xtatib, diagnoz qaytaradi.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Tuple
from medical import DISEASES_BY_CATEGORY, ALL_DISEASES
from medical.disease_model import Disease

# ─────────────────────────────────────────────────────────────────
#  SAVOL BANKI  (savol_id -> {uz, ru, en, symptom_key})
# ─────────────────────────────────────────────────────────────────
QUESTIONS: Dict[str, Dict] = {

    # ── TRIAGE ────────────────────────────────────────────────────
    "location": {
        "uz": "Muammo qayerda?\n\n"
              "1️⃣ Tishda (og'riq, sezuvchanlik, kovak)\n"
              "2️⃣ Milkda (qonash, shish, og'riq)\n"
              "3️⃣ Og'iz ichida (yara, oq qatlam, pufakcha)\n"
              "4️⃣ Jag' yoki yuzda (shish, og'riq, og'iz ochilmaydi)",
        "ru": "Где проблема?\n\n"
              "1️⃣ В зубе (боль, чувствительность, полость)\n"
              "2️⃣ В дёснах (кровоточивость, отёк, боль)\n"
              "3️⃣ В полости рта (язва, белый налёт, пузырьки)\n"
              "4️⃣ В челюсти или лице (отёк, боль, не открывается рот)",
        "en": "Where is the problem?\n\n"
              "1️⃣ In the tooth (pain, sensitivity, cavity)\n"
              "2️⃣ In the gums (bleeding, swelling, pain)\n"
              "3️⃣ In the mouth (ulcer, white patch, blisters)\n"
              "4️⃣ In the jaw or face (swelling, pain, can't open mouth)",
        "type": "choice4",
        "keys": ["tooth", "periodontal", "mucosa", "jaw"],
        "symptom_map": None,   # triage savoli — alohida ishlanadi
    },

    # ── OG'RIQ TURI ───────────────────────────────────────────────
    "spontaneous_pain": {
        "uz": "Tish o'z-o'zidan og'riyaptimi (hech narsa tegmasa ham)?",
        "ru": "Зуб болит сам по себе (без какого-либо воздействия)?",
        "en": "Does the tooth ache on its own (without any trigger)?",
        "type": "yes_no",
        "symptom_key": "spontaneous_pain",
        "categories": ["tooth", "pulp", "periapical"],
    },
    "night_pain": {
        "uz": "Og'riq tunda kuchayib, uyquni bezovta qiladimi?",
        "ru": "Боль усиливается ночью и мешает спать?",
        "en": "Does the pain worsen at night and disturb sleep?",
        "type": "yes_no",
        "symptom_key": "night_pain",
        "categories": ["tooth", "pulp"],
    },
    "pain_attacks": {
        "uz": "Og'riq xurujlar shaklida keladimi (kelib, ketib turadimi)?",
        "ru": "Боль приходит приступами (то появляется, то проходит)?",
        "en": "Does the pain come in attacks (comes and goes)?",
        "type": "yes_no",
        "symptom_key": "pain_attacks",
        "categories": ["pulp"],
    },
    "pain_triggered": {
        "uz": "Og'riq faqat biror narsa tekkanda boshlanadimi (sovuq, shirin, chaynash)?",
        "ru": "Боль начинается только при воздействии (холодное, сладкое, жевание)?",
        "en": "Does pain start only when triggered (cold, sweet, chewing)?",
        "type": "yes_no",
        "symptom_key": "pain_triggered",
        "categories": ["tooth", "pulp"],
    },
    "cold_short": {
        "uz": "Sovuq/issiq tekkanda og'riq tez o'tib ketadimi (30 sekunddan kam)?",
        "ru": "При воздействии холодного/горячего боль быстро проходит (менее 30 секунд)?",
        "en": "When cold/hot touches the tooth, does the pain go away quickly (under 30 seconds)?",
        "type": "yes_no",
        "symptom_key": "cold_short",
        "categories": ["tooth", "pulp"],
    },
    "cold_prolonged": {
        "uz": "Sovuq tekkandan keyin og'riq uzoq davom etadimi (1 daqiqadan ko'p)?",
        "ru": "После воздействия холода боль продолжается долго (больше минуты)?",
        "en": "After cold stimulus, does the pain last a long time (more than a minute)?",
        "type": "yes_no",
        "symptom_key": "cold_prolonged",
        "categories": ["pulp"],
    },
    "hot_increases_pain": {
        "uz": "Issiq narsa (choy, ovqat) tekkanda og'riq kuchayadimi?",
        "ru": "Горячее (чай, еда) усиливает боль?",
        "en": "Does hot food/drink increase the pain?",
        "type": "yes_no",
        "symptom_key": "hot_increases_pain",
        "categories": ["pulp"],
    },
    "cold_relieves_pain": {
        "uz": "Sovuq suv og'riqni vaqtincha kamaytiradi yoki yengillatadimi?",
        "ru": "Холодная вода временно уменьшает или облегчает боль?",
        "en": "Does cold water temporarily reduce or relieve the pain?",
        "type": "yes_no",
        "symptom_key": "cold_relieves_pain",
        "categories": ["pulp"],
    },
    "percussion_pain": {
        "uz": "Tishga barmoq bilan urilganda yoki chaynaganda kuchli og'riq bo'ladimi?",
        "ru": "При постукивании по зубу пальцем или при жевании возникает сильная боль?",
        "en": "When you tap the tooth with your finger or chew, is there sharp pain?",
        "type": "yes_no",
        "symptom_key": "percussion_pain",
        "categories": ["periapical", "tooth"],
    },
    "pressure_pain": {
        "uz": "Tishga bosish yoki chaynash paytida og'riq bo'ladimi?",
        "ru": "При надавливании на зуб или жевании есть боль?",
        "en": "Is there pain when pressing on the tooth or chewing?",
        "type": "yes_no",
        "symptom_key": "pressure_pain",
        "categories": ["periapical", "periodontal"],
    },

    # ── TISH KO'RINISHI ───────────────────────────────────────────
    "cavity_visible": {
        "uz": "Tishda qora yoki kulrang kovak (teshik) ko'rinib turadimi?",
        "ru": "Видна ли в зубе тёмная или серая полость (дырка)?",
        "en": "Is there a visible dark or grey cavity (hole) in the tooth?",
        "type": "yes_no",
        "symptom_key": "cavity_visible",
        "categories": ["tooth", "pulp"],
    },
    "old_filling": {
        "uz": "Og'riyotgan tishda avval qo'yilgan plomba bormi?",
        "ru": "В беспокоящем зубе есть ранее установленная пломба?",
        "en": "Does the aching tooth have a previously placed filling?",
        "type": "yes_no",
        "symptom_key": "old_filling",
        "categories": ["tooth"],
    },
    "tooth_discoloration": {
        "uz": "Tish rangi o'zgarganmi — qoraygan, kulrang yoki sariq bo'lib qolganmi?",
        "ru": "Изменился ли цвет зуба — потемнел, стал серым или жёлтым?",
        "en": "Has the tooth changed colour — darkened, turned grey or yellow?",
        "type": "yes_no",
        "symptom_key": "tooth_discoloration",
        "categories": ["pulp", "periapical"],
    },
    "visible_white_spot": {
        "uz": "Tish yuzasida oq, chalky (bo'r rangidagi) dog' ko'rinib turadimi?",
        "ru": "Видно ли на поверхности зуба белое меловидное пятно?",
        "en": "Is there a white chalky spot visible on the tooth surface?",
        "type": "yes_no",
        "symptom_key": "visible_white_spot",
        "categories": ["tooth"],
    },
    "no_sensitivity": {
        "uz": "Tish hech narsaga sezuvchan emasmi — sovuqqa ham, issiqqa ham javob bermaydimi?",
        "ru": "Зуб совсем не реагирует ни на холодное, ни на горячее?",
        "en": "Does the tooth not respond to cold or heat at all?",
        "type": "yes_no",
        "symptom_key": "no_sensitivity",
        "categories": ["pulp", "periapical"],
    },

    # ── QOʻSHIMCHA BELGILAR ───────────────────────────────────────
    "bad_smell": {
        "uz": "Og'izdan yoqimsiz hid keladimi (o'zingiz yoki yaqinlaringiz sezadimi)?",
        "ru": "Есть ли неприятный запах изо рта (замечаете сами или близкие)?",
        "en": "Is there an unpleasant smell from the mouth (noticed by yourself or others)?",
        "type": "yes_no",
        "symptom_key": "bad_smell",
        "categories": ["pulp", "periapical", "periodontal"],
    },
    "fistula": {
        "uz": "Milkda kichik teshikcha yoki yiring chiqadigan kanal ko'rinib turadimi?",
        "ru": "Видна ли в десне маленькая дырочка или свищевой ход, из которого выходит гной?",
        "en": "Is there a small hole or pus-draining channel visible in the gum?",
        "type": "yes_no",
        "symptom_key": "fistula",
        "categories": ["periapical", "periodontal", "jaw"],
    },
    "irradiation": {
        "uz": "Og'riq boshqa joyga ham tarqaladimi — quloq, chakka, bo'yinga?",
        "ru": "Боль отдаёт в другие места — ухо, висок, шею?",
        "en": "Does the pain radiate to other areas — ear, temple, neck?",
        "type": "yes_no",
        "symptom_key": "irradiation",
        "categories": ["pulp"],
    },
    "localized_pain": {
        "uz": "Og'riq aniq bir tishda — uni qo'lla ko'rsata olasizmi?",
        "ru": "Боль чётко в одном зубе — можете указать его пальцем?",
        "en": "Is the pain clearly in one tooth — can you point to it?",
        "type": "yes_no",
        "symptom_key": "localized_pain",
        "categories": ["periapical", "tooth"],
    },

    # ── MILK / PERIODONTAL ────────────────────────────────────────
    "gum_bleeding": {
        "uz": "Milkdan qon keladimi — tish yuvganda yoki ovqat yeyishda?",
        "ru": "Кровоточат ли дёсны — при чистке зубов или еде?",
        "en": "Do the gums bleed — when brushing or eating?",
        "type": "yes_no",
        "symptom_key": "gum_bleeding",
        "categories": ["periodontal"],
    },
    "gum_swelling": {
        "uz": "Milk shishganmi yoki ko'tarilib qolganmi?",
        "ru": "Отекла ли десна или набухла?",
        "en": "Is the gum swollen or puffy?",
        "type": "yes_no",
        "symptom_key": "gum_swelling",
        "categories": ["periodontal", "periapical"],
    },
    "gum_recession": {
        "uz": "Milklar chekinib, tishning ildizi ko'rinib qolganmi?",
        "ru": "Дёсны отступили и обнажили корень зуба?",
        "en": "Have the gums receded exposing the tooth root?",
        "type": "yes_no",
        "symptom_key": "gum_recession",
        "categories": ["periodontal"],
    },
    "tooth_mobility": {
        "uz": "Tish qimirlab qolganmi — tilingiz bilan itarsa siljiyaptimi?",
        "ru": "Зуб стал подвижным — смещается ли, если надавить языком?",
        "en": "Has the tooth become loose — does it shift when you push it with your tongue?",
        "type": "yes_no",
        "symptom_key": "tooth_mobility",
        "categories": ["periodontal"],
    },
    "periodontal_pocket": {
        "uz": "Tish va milk orasida chuqurcha (cho'ntak) borligini shifokor aytganmi?",
        "ru": "Говорил ли врач о кармане между зубом и десной?",
        "en": "Has a dentist told you there is a pocket between the tooth and gum?",
        "type": "yes_no",
        "symptom_key": "periodontal_pocket",
        "categories": ["periodontal"],
    },
    "gum_pain": {
        "uz": "Milk o'zi og'riyaptimi (tishdan alohida)?",
        "ru": "Десна болит сама по себе (отдельно от зуба)?",
        "en": "Does the gum hurt on its own (separately from the tooth)?",
        "type": "yes_no",
        "symptom_key": "gum_pain",
        "categories": ["periodontal"],
    },
    "gum_redness": {
        "uz": "Milk qizarib, rangi o'zgarganmi (odatdagidan to'qroq)?",
        "ru": "Покраснела ли десна, изменился ли её цвет (стала темнее обычного)?",
        "en": "Has the gum become red or changed colour (darker than usual)?",
        "type": "yes_no",
        "symptom_key": "gum_redness",
        "categories": ["periodontal"],
    },
    "gum_enlargement": {
        "uz": "Milk tishni qoplay boshlaganmi — kattalashib, ustiga chiqib qolganmi?",
        "ru": "Десна начала перекрывать зуб — увеличилась и нависла?",
        "en": "Has the gum grown and started to cover the tooth?",
        "type": "yes_no",
        "symptom_key": "gum_enlargement",
        "categories": ["periodontal"],
    },
    "gum_ulcer": {
        "uz": "Milkda yara yoki nekroz (qorayish) ko'rinib turadimi?",
        "ru": "Видна ли на десне язва или некроз (потемнение)?",
        "en": "Is there an ulcer or necrosis (darkening) visible on the gum?",
        "type": "yes_no",
        "symptom_key": "gum_ulcer",
        "categories": ["periodontal"],
    },
    "wisdom_tooth_pain": {
        "uz": "Og'riq eng orqa tish (aql tishi) sohasidami?",
        "ru": "Боль в области самого заднего зуба (зуба мудрости)?",
        "en": "Is the pain in the area of the very back tooth (wisdom tooth)?",
        "type": "yes_no",
        "symptom_key": "wisdom_tooth_pain",
        "categories": ["periodontal"],
    },

    # ── SHILLIQ QAVAT ─────────────────────────────────────────────
    "ulcer": {
        "uz": "Og'iz ichida yara (shilliq qavat teshilgan, achishadi) bormi?",
        "ru": "Есть ли во рту язва (нарушение слизистой, жжение)?",
        "en": "Is there an ulcer inside the mouth (breach in the mucosa, burning)?",
        "type": "yes_no",
        "symptom_key": "ulcer",
        "categories": ["mucosa"],
    },
    "white_patch": {
        "uz": "Og'iz ichida oq qatlam yoki oq dog' ko'rinib turadimi?",
        "ru": "Виден ли во рту белый налёт или белое пятно?",
        "en": "Is there a white patch or coating visible inside the mouth?",
        "type": "yes_no",
        "symptom_key": "white_patch",
        "categories": ["mucosa"],
    },
    "blisters": {
        "uz": "Og'iz ichida yoki labda suvli pufakchalar toshganmi?",
        "ru": "Появились ли во рту или на губах водянистые пузырьки?",
        "en": "Have watery blisters appeared inside the mouth or on the lips?",
        "type": "yes_no",
        "symptom_key": "blisters",
        "categories": ["mucosa"],
    },
    "removable_patch": {
        "uz": "Oq qatlam toza tampon bilan artilganda ko'tarilib tushib ketadimi?",
        "ru": "Белый налёт снимается при протирании чистым ватным тампоном?",
        "en": "Does the white patch come off when wiped with a clean cotton swab?",
        "type": "yes_no",
        "symptom_key": "removable_patch",
        "categories": ["mucosa"],
    },
    "non_removable": {
        "uz": "Oq dog' artib tushmaydimi — mahkam yopishib turganmi?",
        "ru": "Белое пятно не снимается — крепко держится?",
        "en": "Does the white patch NOT come off — is it firmly attached?",
        "type": "yes_no",
        "symptom_key": "non_removable",
        "categories": ["mucosa"],
    },
    "white_center_red_halo": {
        "uz": "Yarada oq/sarg'ish markaz va atrofida qizil halqa bormi?",
        "ru": "Есть ли у язвы белый/желтоватый центр и красный ободок вокруг?",
        "en": "Does the ulcer have a white/yellowish centre with a red halo around it?",
        "type": "yes_no",
        "symptom_key": "white_center_red_halo",
        "categories": ["mucosa"],
    },
    "white_lacy_pattern": {
        "uz": "Og'iz ichida to'r shaklidagi yoki chiziqli oq naqsh ko'rinib turadimi?",
        "ru": "Виден ли во рту кружевной или линейный белый узор?",
        "en": "Is there a lacy or linear white pattern visible inside the mouth?",
        "type": "yes_no",
        "symptom_key": "white_lacy_pattern",
        "categories": ["mucosa"],
    },
    "multiple_lesions": {
        "uz": "Og'iz ichida bir nechta joylarda (ko'plab) yara/toshmalar bormi?",
        "ru": "Есть ли во рту поражения в нескольких местах (множественные)?",
        "en": "Are there lesions in multiple places inside the mouth?",
        "type": "yes_no",
        "symptom_key": "multiple_lesions",
        "categories": ["mucosa"],
    },
    "recurrent": {
        "uz": "Bu holat avvaldan ham tez-tez qaytalanadimi (oyda bir yoki ko'proq)?",
        "ru": "Это состояние часто повторяется (раз в месяц или чаще)?",
        "en": "Does this condition recur frequently (once a month or more)?",
        "type": "yes_no",
        "symptom_key": "recurrent",
        "categories": ["mucosa"],
    },
    "trauma_history": {
        "uz": "Bu yara yaqinda tish, protez yoki qattiq ovqat ta'sir qilgan joyda paydo bo'ldimi?",
        "ru": "Появилась ли язва там, где недавно было травматическое воздействие (зуб, протез, твёрдая еда)?",
        "en": "Did the ulcer appear where there was recent trauma (tooth, denture, hard food)?",
        "type": "yes_no",
        "symptom_key": "trauma_history",
        "categories": ["mucosa"],
    },
    "antibiotic_history": {
        "uz": "So'nggi 2-3 haftada antibiotik ichganmisiz?",
        "ru": "Принимали ли антибиотики в последние 2–3 недели?",
        "en": "Have you taken antibiotics in the last 2–3 weeks?",
        "type": "yes_no",
        "symptom_key": "antibiotic_history",
        "categories": ["mucosa"],
    },
    "bilateral": {
        "uz": "Bu belgilar og'izning ikkala tomonida ham (nosimmetrik) ko'rinib turadimi?",
        "ru": "Эти признаки видны с обеих сторон полости рта (симметрично)?",
        "en": "Are these signs visible on both sides of the mouth (symmetrically)?",
        "type": "yes_no",
        "symptom_key": "bilateral",
        "categories": ["mucosa"],
    },

    # ── JAG' ──────────────────────────────────────────────────────
    "jaw_swelling": {
        "uz": "Jag' atrofida yoki yuzda ko'rinib turuvchi shish bormi?",
        "ru": "Есть ли видимый отёк в области челюсти или лица?",
        "en": "Is there a visible swelling around the jaw or face?",
        "type": "yes_no",
        "symptom_key": "jaw_swelling",
        "categories": ["jaw"],
    },
    "trismus": {
        "uz": "Og'izni to'liq ocholmayapsizmi — og'iz ochish qiyinmi?",
        "ru": "Не получается широко открыть рот — затруднено ли открывание?",
        "en": "Can you not open your mouth fully — is mouth opening difficult?",
        "type": "yes_no",
        "symptom_key": "trismus",
        "categories": ["jaw", "periodontal"],
    },
    "jaw_deformity": {
        "uz": "Jag' shakli o'zgarganmi yoki notekislashganmi?",
        "ru": "Изменилась ли форма челюсти или она стала неровной?",
        "en": "Has the jaw shape changed or become irregular?",
        "type": "yes_no",
        "symptom_key": "jaw_deformity",
        "categories": ["jaw"],
    },
    "retained_tooth": {
        "uz": "Suyak ichida qolib ketgan (chiqmagan) tish borligini shifokor aytganmi?",
        "ru": "Говорил ли врач о зубе, который остался в кости (не прорезался)?",
        "en": "Has a dentist told you there is a tooth retained inside the bone (unerupted)?",
        "type": "yes_no",
        "symptom_key": "retained_tooth",
        "categories": ["jaw"],
    },

    # ── UMUMIY ────────────────────────────────────────────────────
    "fever": {
        "uz": "Tana harorati ko'tarilganmi (37.5°C dan yuqori)?",
        "ru": "Повышена ли температура тела (выше 37.5°C)?",
        "en": "Is your body temperature elevated (above 37.5°C)?",
        "type": "yes_no",
        "symptom_key": "fever",
        "categories": ["jaw", "mucosa", "periodontal", "periapical"],
    },
    "high_fever": {
        "uz": "Isitma juda balandmi — 38.5°C dan yuqorimi?",
        "ru": "Температура очень высокая — выше 38.5°C?",
        "en": "Is the fever very high — above 38.5°C?",
        "type": "yes_no",
        "symptom_key": "high_fever",
        "categories": ["jaw"],
    },
    "lymph_nodes": {
        "uz": "Bo'yin yoki jag' osti limfa tugunlari kattalashib, og'riq berayaptimi?",
        "ru": "Увеличены ли и болезненны ли лимфоузлы шеи или под челюстью?",
        "en": "Are the lymph nodes in the neck or under the jaw enlarged and tender?",
        "type": "yes_no",
        "symptom_key": "lymph_nodes",
        "categories": ["jaw", "mucosa", "periapical"],
    },
    "general_weakness": {
        "uz": "Umumiy holsizlik, charchoq yoki ishtaha yo'qligi bormi?",
        "ru": "Есть ли общая слабость, усталость или отсутствие аппетита?",
        "en": "Is there general weakness, fatigue or loss of appetite?",
        "type": "yes_no",
        "symptom_key": "general_weakness",
        "categories": ["jaw", "mucosa"],
    },
    "pus_discharge": {
        "uz": "Yiring ajralishi ko'rinadimi — og'izda sarg'ish yoki oqish suyuqlik?",
        "ru": "Есть ли выделение гноя — желтоватая или белёсая жидкость во рту?",
        "en": "Is there pus discharge — yellowish or whitish fluid in the mouth?",
        "type": "yes_no",
        "symptom_key": "pus_discharge",
        "categories": ["jaw", "periapical", "periodontal"],
    },
    "pulp_polyp": {
        "uz": "Kavakda go'sht kabi to'qima o'sib chiqib, tashqariga ko'rinib turadimi?",
        "ru": "Виднеется ли из полости мягкое мясистое образование (полип)?",
        "en": "Is there a fleshy soft tissue growth visible from inside the tooth cavity?",
        "type": "yes_no",
        "symptom_key": "pulp_polyp",
        "categories": ["pulp"],
    },
    "bleeding_on_chewing": {
        "uz": "Chaynash paytida tish sohasidan qon keladimi?",
        "ru": "При жевании появляется кровь в области зуба?",
        "en": "Is there bleeding from the tooth area when chewing?",
        "type": "yes_no",
        "symptom_key": "bleeding_on_chewing",
        "categories": ["pulp"],
    },
    "rapid_progression": {
        "uz": "Holat tez rivojlanayaptimi — bir-ikki oyda ko'plab tishlar ta'sirlandi?",
        "ru": "Состояние быстро прогрессирует — за 1–2 месяца поражено много зубов?",
        "en": "Is the condition progressing rapidly — many teeth affected in 1–2 months?",
        "type": "yes_no",
        "symptom_key": "rapid_progression",
        "categories": ["periodontal"],
    },
    "stress_trigger": {
        "uz": "Bu holat asosan stress yoki kasallikdan (immunitet pasayganda) keyin paydo bo'ladimi?",
        "ru": "Это состояние появляется обычно после стресса или болезни (при снижении иммунитета)?",
        "en": "Does this condition appear usually after stress or illness (when immunity drops)?",
        "type": "yes_no",
        "symptom_key": "stress_trigger",
        "categories": ["mucosa"],
    },
    "burning": {
        "uz": "Og'iz ichida kuyish yoki achishish hissi bormi?",
        "ru": "Есть ли ощущение жжения или щипания во рту?",
        "en": "Is there a burning or stinging sensation inside the mouth?",
        "type": "yes_no",
        "symptom_key": "burning",
        "categories": ["mucosa"],
    },
    "dry_mouth": {
        "uz": "Og'iz qurib qolganligini his qilyapsizmi?",
        "ru": "Ощущаете ли вы сухость во рту?",
        "en": "Do you feel dryness in the mouth?",
        "type": "yes_no",
        "symptom_key": "dry_mouth",
        "categories": ["mucosa"],
    },
    "smoking_history": {
        "uz": "Chekasizmi yoki ilgari chekkanmisiz?",
        "ru": "Курите ли вы или курили раньше?",
        "en": "Do you smoke or have you smoked before?",
        "type": "yes_no",
        "symptom_key": "smoking_history",
        "categories": ["mucosa"],
    },
    "causative_tooth": {
        "uz": "Shishning yonida og'riydigan, qoraygan yoki plombalangan tish bormi?",
        "ru": "Рядом с отёком есть больной, потемневший или запломбированный зуб?",
        "en": "Near the swelling, is there a painful, darkened or filled tooth?",
        "type": "yes_no",
        "symptom_key": "causative_tooth",
        "categories": ["jaw"],
    },
    "severe_pain": {
        "uz": "Og'riq juda kuchli — 10 dan 7-8 dan yuqori deb baholaysizmi?",
        "ru": "Боль очень сильная — оцениваете её выше 7–8 из 10?",
        "en": "Is the pain very severe — would you rate it above 7–8 out of 10?",
        "type": "yes_no",
        "symptom_key": "severe_pain",
        "categories": ["jaw", "pulp"],
    },
    "dull_ache": {
        "uz": "Og'riq bo'g'iq, past darajali, doim mavjud bo'lganmi?",
        "ru": "Боль тупая, невыраженная, постоянно присутствует?",
        "en": "Is the pain a dull, low-level, constant ache?",
        "type": "yes_no",
        "symptom_key": "dull_ache",
        "categories": ["periapical", "pulp"],
    },
    "pressure_sensation": {
        "uz": "Shu sohada bosim yoki to'liqlik hissi bormi (og'riqsiz)?",
        "ru": "Есть ли ощущение давления или распирания в этой области (без боли)?",
        "en": "Is there a feeling of pressure or fullness in the area (without pain)?",
        "type": "yes_no",
        "symptom_key": "pressure_sensation",
        "categories": ["periapical", "jaw"],
    },
    "erosion": {
        "uz": "Oq naqsh joylashgan joyda yaraga o'xshash eroziya (qizil yuzali) ham bormi?",
        "ru": "Есть ли в месте белого узора эрозия (покрасневшая поверхность)?",
        "en": "Is there erosion (reddened surface) where the white pattern is?",
        "type": "yes_no",
        "symptom_key": "erosion",
        "categories": ["mucosa"],
    },
    "redness": {
        "uz": "Og'iz ichidagi shilliq qavat umumiy qizarganmi (keng maydon)?",
        "ru": "Слизистая оболочка полости рта в целом покраснела (на большой площади)?",
        "en": "Is the mouth lining generally red (over a wide area)?",
        "type": "yes_no",
        "symptom_key": "redness",
        "categories": ["mucosa"],
    },
    "swelling_mucosa": {
        "uz": "Shilliq qavat shishgan ko'rinayaptimi?",
        "ru": "Слизистая выглядит отёчной?",
        "en": "Does the mucosa appear swollen?",
        "type": "yes_no",
        "symptom_key": "swelling_mucosa",
        "categories": ["mucosa"],
    },
    "localized": {
        "uz": "Yara yoki belgi faqat bitta aniq joyda (kichik maydon)da joylashganmi?",
        "ru": "Язва или признак находится только в одном конкретном месте (небольшая площадь)?",
        "en": "Is the ulcer or sign located only in one specific spot (small area)?",
        "type": "yes_no",
        "symptom_key": "localized",
        "categories": ["mucosa"],
    },
    "pain": {
        "uz": "Shu sohada og'riq yoki achishish bormi?",
        "ru": "Есть ли в этой области боль или жжение?",
        "en": "Is there pain or burning in this area?",
        "type": "yes_no",
        "symptom_key": "pain",
        "categories": ["mucosa", "periodontal"],
    },
    "no_pain": {
        "uz": "Hozirda hech qanday og'riq yo'qmi?",
        "ru": "Сейчас нет никакой боли?",
        "en": "Is there no pain at all right now?",
        "type": "yes_no",
        "symptom_key": "no_pain",
        "categories": ["tooth", "periapical"],
    },
    "no_bone_loss": {
        "uz": "Shifokor hali suyak yo'qotilmagan degan (yoki rentgeningiz normal bo'lgan)?",
        "ru": "Врач сказал, что потери кости пока нет (или рентген был в норме)?",
        "en": "Has a dentist said there is no bone loss yet (or your X-ray was normal)?",
        "type": "yes_no",
        "symptom_key": "no_bone_loss",
        "categories": ["periodontal"],
    },
    "no_inflammation": {
        "uz": "Milkda qizarish yoki shish yo'qmi — ko'rinish normal?",
        "ru": "Нет ли покраснения или отёка десны — выглядит нормально?",
        "en": "Is there no redness or swelling of the gums — looks normal?",
        "type": "yes_no",
        "symptom_key": "no_inflammation",
        "categories": ["periodontal"],
    },
    "cold_sensitivity": {
        "uz": "Sovuqqa (suv, havo) sezuvchanlik bormi?",
        "ru": "Есть ли чувствительность к холодному (вода, воздух)?",
        "en": "Is there sensitivity to cold (water, air)?",
        "type": "yes_no",
        "symptom_key": "cold_sensitivity",
        "categories": ["periodontal", "tooth"],
    },
    "sweet_sensitivity": {
        "uz": "Shirin ovqat yoki ichimlik tekkanda noqulaylik yoki og'riq bo'ladimi?",
        "ru": "При контакте со сладкой едой или напитками возникает дискомфорт или боль?",
        "en": "Does sweet food or drink cause discomfort or pain?",
        "type": "yes_no",
        "symptom_key": "sweet_sensitivity",
        "categories": ["tooth"],
    },
    "young_patient": {
        "uz": "Yoshingiz 35 dan pastmi?",
        "ru": "Вам меньше 35 лет?",
        "en": "Are you under 35 years old?",
        "type": "yes_no",
        "symptom_key": "young_patient",
        "categories": ["periodontal"],
    },
    "sequestrum": {
        "uz": "Og'izdagi yarachadan ba'zan qattiq (suyak) parchalari chiqib turadimi?",
        "ru": "Выходят ли иногда из свища твёрдые (костные) фрагменты?",
        "en": "Do hard (bone) fragments sometimes come out through the fistula?",
        "type": "yes_no",
        "symptom_key": "sequestrum",
        "categories": ["jaw"],
    },
    "hot_sensitivity": {
        "uz": "Issiq ovqat/ichimlik tishga tekkanda og'riq bo'ladimi?",
        "ru": "Горячая еда/напитки вызывают боль при контакте с зубом?",
        "en": "Does hot food/drink cause pain when it contacts the tooth?",
        "type": "yes_no",
        "symptom_key": "hot_sensitivity",
        "categories": ["tooth", "pulp"],
    },
}

# ─────────────────────────────────────────────────────────────────
#  CATEGORY -> SAVOL TARTIBI  (akinator yo'li)
# ─────────────────────────────────────────────────────────────────

QUESTION_FLOW: Dict[str, List[str]] = {
    "tooth": [
        "cavity_visible",
        "old_filling",
        "visible_white_spot",
        "pain_triggered",
        "cold_short",
        "sweet_sensitivity",
        "no_pain",
        "spontaneous_pain",
        "night_pain",
        "hot_sensitivity",
    ],
    "pulp": [
        "spontaneous_pain",
        "night_pain",
        "pain_attacks",
        "hot_increases_pain",
        "cold_relieves_pain",
        "cold_prolonged",
        "irradiation",
        "tooth_discoloration",
        "bad_smell",
        "no_sensitivity",
        "pulp_polyp",
        "bleeding_on_chewing",
    ],
    "periapical": [
        "percussion_pain",
        "localized_pain",
        "pressure_pain",
        "tooth_discoloration",
        "bad_smell",
        "gum_swelling",
        "fistula",
        "pus_discharge",
        "dull_ache",
        "pressure_sensation",
        "fever",
        "lymph_nodes",
    ],
    "periodontal": [
        "gum_bleeding",
        "gum_swelling",
        "gum_redness",
        "gum_pain",
        "tooth_mobility",
        "periodontal_pocket",
        "gum_recession",
        "gum_enlargement",
        "gum_ulcer",
        "bad_smell",
        "wisdom_tooth_pain",
        "trismus",
        "fistula",
        "pus_discharge",
        "rapid_progression",
        "no_bone_loss",
        "no_inflammation",
        "cold_sensitivity",
        "young_patient",
    ],
    "mucosa": [
        "ulcer",
        "white_patch",
        "blisters",
        "white_lacy_pattern",
        "redness",
        "swelling_mucosa",
        "removable_patch",
        "non_removable",
        "white_center_red_halo",
        "multiple_lesions",
        "bilateral",
        "recurrent",
        "pain",
        "burning",
        "dry_mouth",
        "fever",
        "lymph_nodes",
        "trauma_history",
        "antibiotic_history",
        "stress_trigger",
        "smoking_history",
        "erosion",
        "localized",
    ],
    "jaw": [
        "jaw_swelling",
        "causative_tooth",
        "trismus",
        "fever",
        "high_fever",
        "severe_pain",
        "pus_discharge",
        "lymph_nodes",
        "general_weakness",
        "fistula",
        "jaw_deformity",
        "retained_tooth",
        "sequestrum",
    ],
}

# ─────────────────────────────────────────────────────────────────
#  AKINATOR MEXANIZMI
# ─────────────────────────────────────────────────────────────────

MIN_QUESTIONS = 5
MAX_QUESTIONS = 14
EARLY_STOP_GAP = 6   # top kasallik ikkinchidan shu ball bilan ustun tursa — to'xtat
EARLY_STOP_MIN_Q = 4  # kamida shu savol berilgan bo'lsin


def _score_disease(symptoms: Dict[str, bool], disease: Disease) -> int:
    score = 0
    for feat, expected in disease.core_features.items():
        if expected and symptoms.get(feat, False):
            score += 3
    for feat, expected in disease.optional_features.items():
        if expected and symptoms.get(feat, False):
            score += 1
    for feat, expected in disease.negative_features.items():
        if expected and symptoms.get(feat, False):
            score -= 3
    return score


def _rank_diseases(symptoms: Dict[str, bool], diseases: List[Disease]):
    ranked = [{"disease": d, "score": _score_disease(symptoms, d)} for d in diseases]
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


def get_next_question(
    category: str,
    symptoms: Dict[str, bool],
    asked: List[str],
    lang: str = "uz",
) -> Optional[Dict]:
    """
    Keyingi berilishi kerak bo'lgan savolni qaytaradi.
    Qaytarilgan dict:
      { "id": str, "text": str, "type": str }
    Agar savol qolmagan bo'lsa — None.
    """
    flow = QUESTION_FLOW.get(category, [])
    for qid in flow:
        if qid in asked:
            continue
        q = QUESTIONS.get(qid)
        if q is None:
            continue
        return {
            "id": qid,
            "text": q.get(lang, q["uz"]),
            "type": q["type"],
        }
    return None


def should_stop_early(
    category: str,
    symptoms: Dict[str, bool],
    asked_count: int,
) -> bool:
    """
    Erta to'xtatish: kamida MIN_QUESTIONS savol berilgan bo'lsa
    va birinchi kasallik ikkinchisidan EARLY_STOP_GAP ball ustun bo'lsa.
    """
    if asked_count < max(MIN_QUESTIONS, EARLY_STOP_MIN_Q):
        return False
    diseases = DISEASES_BY_CATEGORY.get(category, [])
    if len(diseases) < 2:
        return True
    ranked = _rank_diseases(symptoms, diseases)
    if len(ranked) < 2:
        return True
    gap = ranked[0]["score"] - ranked[1]["score"]
    return gap >= EARLY_STOP_GAP


def get_diagnosis(
    category: str,
    symptoms: Dict[str, bool],
    lang: str = "uz",
) -> Dict:
    """
    Yakuniy tashxisni qaytaradi.
    """
    diseases = DISEASES_BY_CATEGORY.get(category, [])
    if not diseases:
        return {"diagnosis": "Aniqlanmadi", "confidence": 0.0, "alternatives": []}

    ranked = _rank_diseases(symptoms, diseases)
    top = ranked[0]
    alternatives = [r["disease"].get_name(lang) for r in ranked[1:3] if r["score"] > 0]

    # Ishonchlilik hisoblash
    max_possible = len(top["disease"].core_features) * 3 + len(top["disease"].optional_features)
    confidence = min(0.95, top["score"] / max_possible) if max_possible > 0 else 0.5

    return {
        "diagnosis": top["disease"].get_name(lang),
        "disease_id": top["disease"].id,
        "confidence": round(max(0.5, confidence), 2),
        "score": top["score"],
        "alternatives": alternatives,
        "red_flags": top["disease"].red_flags,
        "discriminators": top["disease"].discriminators,
        "category": category,
    }
