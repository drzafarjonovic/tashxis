"""
Simptom registri — savol va simptom kalitlari uchun YAGONA manba.

Har bir simptomning id'si bir vaqtning o'zida uning kalitidir.
Kasalliklar (medical/) faqat shu yerda e'lon qilingan kalitlardan foydalanishi mumkin.
`tests/` bu qoidani avtomatik tekshiradi.

Tuzilma:
    QUESTIONS[symptom_id] = {"uz": ..., "ru": ..., "en": ...}
    CANDIDATE_SYMPTOMS[category] = [savol berilishi mumkin bo'lgan simptom id'lari]
"""

from __future__ import annotations

from typing import Dict, List

# ─────────────────────────────────────────────────────────────────
#  SAVOLLAR (hammasi "ha/yo'q" turida)
# ─────────────────────────────────────────────────────────────────

QUESTIONS: Dict[str, Dict[str, str]] = {
    # ── OG'RIQ TURI ──────────────────────────────────────────────
    "spontaneous_pain": {
        "uz": "Tish o'z-o'zidan og'riyaptimi (hech narsa tegmasa ham)?",
        "ru": "Зуб болит сам по себе (без какого-либо воздействия)?",
        "en": "Does the tooth ache on its own (without any trigger)?",
    },
    "night_pain": {
        "uz": "Og'riq tunda kuchayib, uyquni bezovta qiladimi?",
        "ru": "Боль усиливается ночью и мешает спать?",
        "en": "Does the pain worsen at night and disturb sleep?",
    },
    "pain_attacks": {
        "uz": "Og'riq xurujlar shaklida keladimi (kelib, ketib turadimi)?",
        "ru": "Боль приходит приступами (то появляется, то проходит)?",
        "en": "Does the pain come in attacks (comes and goes)?",
    },
    "short_pain_attacks": {
        "uz": "Og'riq xurujlari qisqami (10-30 daqiqa), orasidagi tinch oraliqlar uzoqmi?",
        "ru": "Болевые приступы короткие (10-30 минут), а промежутки между ними длительные?",
        "en": "Are the pain attacks short (10-30 min) with long pain-free intervals between them?",
    },
    "pain_triggered": {
        "uz": "Og'riq faqat biror narsa tekkanda boshlanadimi (sovuq, shirin, chaynash)?",
        "ru": "Боль начинается только при воздействии (холодное, сладкое, жевание)?",
        "en": "Does pain start only when triggered (cold, sweet, chewing)?",
    },
    "cold_short": {
        "uz": "Sovuq/issiq tekkanda og'riq tez o'tib ketadimi (30 sekunddan kam)?",
        "ru": "При воздействии холодного/горячего боль быстро проходит (менее 30 секунд)?",
        "en": "When cold/hot touches the tooth, does the pain go away quickly (under 30 seconds)?",
    },
    "cold_prolonged": {
        "uz": "Sovuq tekkandan keyin og'riq uzoq davom etadimi (1 daqiqadan ko'p)?",
        "ru": "После воздействия холода боль продолжается долго (больше минуты)?",
        "en": "After cold stimulus, does the pain last a long time (more than a minute)?",
    },
    "hot_increases_pain": {
        "uz": "Issiq narsa (choy, ovqat) tekkanda og'riq kuchayadimi?",
        "ru": "Горячее (чай, еда) усиливает боль?",
        "en": "Does hot food/drink increase the pain?",
    },
    "cold_relieves_pain": {
        "uz": "Sovuq suv og'riqni vaqtincha kamaytiradi yoki yengillatadimi?",
        "ru": "Холодная вода временно уменьшает или облегчает боль?",
        "en": "Does cold water temporarily reduce or relieve the pain?",
    },
    "percussion_pain": {
        "uz": "Tishga barmoq bilan urilganda yoki chaynaganda kuchli og'riq bo'ladimi?",
        "ru": "При постукивании по зубу пальцем или при жевании возникает сильная боль?",
        "en": "When you tap the tooth with your finger or chew, is there sharp pain?",
    },
    "pressure_pain": {
        "uz": "Tishga bosish yoki chaynash paytida og'riq bo'ladimi?",
        "ru": "При надавливании на зуб или жевании есть боль?",
        "en": "Is there pain when pressing on the tooth or chewing?",
    },
    "irradiation": {
        "uz": "Og'riq boshqa joyga ham tarqaladimi — quloq, chakka, bo'yinga?",
        "ru": "Боль отдаёт в другие места — ухо, висок, шею?",
        "en": "Does the pain radiate to other areas — ear, temple, neck?",
    },
    "localized_pain": {
        "uz": "Og'riq aniq bir tishda — uni qo'l bilan ko'rsata olasizmi?",
        "ru": "Боль чётко в одном зубе — можете указать его пальцем?",
        "en": "Is the pain clearly in one tooth — can you point to it?",
    },
    "dull_ache": {
        "uz": "Og'riq bo'g'iq, past darajali, doim mavjud bo'lganmi?",
        "ru": "Боль тупая, невыраженная, постоянно присутствует?",
        "en": "Is the pain a dull, low-level, constant ache?",
    },
    "severe_pain": {
        "uz": "Og'riq juda kuchli — 10 dan 7-8 dan yuqori deb baholaysizmi?",
        "ru": "Боль очень сильная — оцениваете её выше 7–8 из 10?",
        "en": "Is the pain very severe — would you rate it above 7-8 out of 10?",
    },
    "hot_sensitivity": {
        "uz": "Issiq ovqat/ichimlik tishga tekkanda og'riq bo'ladimi?",
        "ru": "Горячая еда/напитки вызывают боль при контакте с зубом?",
        "en": "Does hot food/drink cause pain when it contacts the tooth?",
    },
    "cold_sensitivity": {
        "uz": "Sovuqqa (suv, havo) sezuvchanlik bormi?",
        "ru": "Есть ли чувствительность к холодному (вода, воздух)?",
        "en": "Is there sensitivity to cold (water, air)?",
    },
    "sweet_sensitivity": {
        "uz": "Shirin ovqat yoki ichimlik tekkanda noqulaylik yoki og'riq bo'ladimi?",
        "ru": "При контакте со сладкой едой или напитками возникает дискомфорт или боль?",
        "en": "Does sweet food or drink cause discomfort or pain?",
    },
    # ── TISH KO'RINISHI ─────────────────────────────────────────
    "cavity_visible": {
        "uz": "Tishda qora yoki kulrang kovak (teshik) ko'rinib turadimi?",
        "ru": "Видна ли в зубе тёмная или серая полость (дырка)?",
        "en": "Is there a visible dark or grey cavity (hole) in the tooth?",
    },
    "old_filling": {
        "uz": "Og'riyotgan tishda avval qo'yilgan plomba bormi?",
        "ru": "В беспокоящем зубе есть ранее установленная пломба?",
        "en": "Does the aching tooth have a previously placed filling?",
    },
    "tooth_discoloration": {
        "uz": "Tish rangi o'zgarganmi — qoraygan, kulrang yoki sariq bo'lib qolganmi?",
        "ru": "Изменился ли цвет зуба — потемнел, стал серым или жёлтым?",
        "en": "Has the tooth changed colour — darkened, turned grey or yellow?",
    },
    "visible_white_spot": {
        "uz": "Tish yuzasida oq, bo'r rangidagi dog' ko'rinib turadimi?",
        "ru": "Видно ли на поверхности зуба белое меловидное пятно?",
        "en": "Is there a white chalky spot visible on the tooth surface?",
    },
    "no_sensitivity": {
        "uz": "Tish hech narsaga sezuvchan emasmi — sovuqqa ham, issiqqa ham javob bermaydimi?",
        "ru": "Зуб совсем не реагирует ни на холодное, ни на горячее?",
        "en": "Does the tooth not respond to cold or heat at all?",
    },
    "no_pain": {
        "uz": "Hozirda hech qanday og'riq yo'qmi?",
        "ru": "Сейчас нет никакой боли?",
        "en": "Is there no pain at all right now?",
    },
    "pulp_polyp": {
        "uz": "Kavakda go'sht kabi to'qima o'sib chiqib, tashqariga ko'rinib turadimi?",
        "ru": "Виднеется ли из полости мягкое мясистое образование (полип)?",
        "en": "Is there a fleshy soft tissue growth visible from inside the tooth cavity?",
    },
    "bleeding_on_chewing": {
        "uz": "Chaynash paytida tish sohasidan qon keladimi?",
        "ru": "При жевании появляется кровь в области зуба?",
        "en": "Is there bleeding from the tooth area when chewing?",
    },
    # ── QO'SHIMCHA TISH BELGILARI ────────────────────────────────
    "bad_smell": {
        "uz": "Og'izdan yoqimsiz hid keladimi (o'zingiz yoki yaqinlaringiz sezadimi)?",
        "ru": "Есть ли неприятный запах изо рта (замечаете сами или близкие)?",
        "en": "Is there an unpleasant smell from the mouth (noticed by yourself or others)?",
    },
    "fistula": {
        "uz": "Milkda kichik teshikcha yoki yiring chiqadigan kanal ko'rinib turadimi?",
        "ru": "Видна ли в десне маленькая дырочка или свищевой ход, из которого выходит гной?",
        "en": "Is there a small hole or pus-draining channel visible in the gum?",
    },
    # ── NOKARIOZ / RIVOJLANISH (qattiq to'qima) BELGILARI ───────
    "multiple_teeth_affected": {
        "uz": "Muammo bitta emas, bir nechta tishda bir vaqtda ko'rinadimi?",
        "ru": "Проблема видна не на одном, а сразу на нескольких зубах?",
        "en": "Is the problem visible on several teeth at once, not just one?",
    },
    "since_childhood": {
        "uz": "Bu o'zgarish tishlar chiqqanidan beri (bolalikdan) bormi?",
        "ru": "Это изменение есть с момента прорезывания зубов (с детства)?",
        "en": "Has this change been present since the teeth erupted (since childhood)?",
    },
    "family_history": {
        "uz": "Oilangizdagilarda ham xuddi shunday tish muammosi bormi (nasliy)?",
        "ru": "Есть ли такая же проблема с зубами у членов семьи (наследственная)?",
        "en": "Do family members have the same kind of tooth problem (hereditary)?",
    },
    "brown_stains": {
        "uz": "Tishlarda jigarrang dog'lar yoki chipor (notekis rangli) yuzalar bormi?",
        "ru": "Есть ли на зубах коричневые пятна или крапчатая (пёстрая) поверхность?",
        "en": "Are there brown stains or a mottled (speckled) surface on the teeth?",
    },
    "enamel_pits": {
        "uz": "Emal yuzasida chuqurchalar, egatlar yoki notekis nuqsonlar bormi?",
        "ru": "Есть ли на эмали ямки, бороздки или неровные дефекты?",
        "en": "Are there pits, grooves or uneven defects on the enamel surface?",
    },
    "enamel_missing": {
        "uz": "Tishning ba'zi joylarida emal umuman yo'q — ostidagi dentin ochiq ko'rinadimi?",
        "ru": "На некоторых участках зуба эмаль полностью отсутствует — обнажён дентин?",
        "en": "Is enamel completely absent in places — is the underlying dentin exposed?",
    },
    "wedge_defect": {
        "uz": "Tish bo'ynida (milkka yaqin) ponasimon, V-shaklidagi nuqson bormi?",
        "ru": "Есть ли у шейки зуба (у десны) клиновидный, V-образный дефект?",
        "en": "Is there a wedge-shaped, V-shaped defect at the tooth neck (near the gum)?",
    },
    "occlusal_wear": {
        "uz": "Tishlarning chaynov (yuqori) yuzasi yedirilib, tekislanib qolganmi?",
        "ru": "Жевательная (верхняя) поверхность зубов стёрлась и стала плоской?",
        "en": "Has the chewing (top) surface of the teeth worn down and flattened?",
    },
    "bruxism": {
        "uz": "Tish g'ichirlatish yoki qattiq tishlash odatingiz bormi (ayniqsa uyquda)?",
        "ru": "Есть ли привычка скрежетать зубами или сильно их сжимать (особенно во сне)?",
        "en": "Do you grind or strongly clench your teeth (especially during sleep)?",
    },
    "hard_brushing": {
        "uz": "Tishni juda qattiq, kuch bilan yoki haddan tashqari ko'p cho'tkalaysizmi?",
        "ru": "Чистите ли вы зубы очень жёстко, с нажимом или слишком часто?",
        "en": "Do you brush your teeth very hard, with force, or excessively often?",
    },
    "acid_exposure": {
        "uz": "Tez-tez nordon narsa (limon, gazli ichimlik) yoki kislota (qusish/reflyuks) ta'siri bormi?",
        "ru": "Часто ли есть контакт с кислым (лимон, газировка) или кислотой (рвота/рефлюкс)?",
        "en": "Is there frequent contact with acid (lemon, soda) or stomach acid (vomiting/reflux)?",
    },
    "smooth_shiny_surface": {
        "uz": "Yedirilgan joy silliq, yaltiroq va botiq (kosacha shaklida) ko'rinadimi?",
        "ru": "Стёртый участок выглядит гладким, блестящим и вогнутым (как чашечка)?",
        "en": "Does the worn area look smooth, shiny and concave (cupped)?",
    },
    "chalky_enamel": {
        "uz": "Emal bo'rga o'xshab oqargan, mo'rt yoki to'kiluvchan bo'lib qolganmi?",
        "ru": "Эмаль стала меловидной, хрупкой или крошащейся?",
        "en": "Has the enamel become chalky, brittle or crumbling?",
    },
    "abnormal_tooth_color": {
        "uz": "Tishlar tug'malik bilan g'ayritabiiy rangda — sarg'ish-jigarrang, kulrang yoki yarim shaffofmi?",
        "ru": "Зубы с рождения необычного цвета — желтовато-коричневые, серые или полупрозрачные?",
        "en": "Are the teeth an unusual colour from birth — yellow-brown, grey or translucent?",
    },

    # ── MILK / PERIODONTAL ───────────────────────────────────────
    "gum_bleeding": {
        "uz": "Milkdan qon keladimi — tish yuvganda yoki ovqat yeyishda?",
        "ru": "Кровоточат ли дёсны — при чистке зубов или еде?",
        "en": "Do the gums bleed — when brushing or eating?",
    },
    "gum_swelling": {
        "uz": "Milk shishganmi yoki ko'tarilib qolganmi?",
        "ru": "Отекла ли десна или набухла?",
        "en": "Is the gum swollen or puffy?",
    },
    "gum_recession": {
        "uz": "Milklar chekinib, tishning ildizi ko'rinib qolganmi?",
        "ru": "Дёсны отступили и обнажили корень зуба?",
        "en": "Have the gums receded exposing the tooth root?",
    },
    "tooth_mobility": {
        "uz": "Tish qimirlab qolganmi — tilingiz bilan itarsa siljiyaptimi?",
        "ru": "Зуб стал подвижным — смещается ли, если надавить языком?",
        "en": "Has the tooth become loose — does it shift when you push it with your tongue?",
    },
    "periodontal_pocket": {
        "uz": "Tish va milk orasida chuqurcha (cho'ntak) borligini shifokor aytganmi?",
        "ru": "Говорил ли врач о кармане между зубом и десной?",
        "en": "Has a dentist told you there is a pocket between the tooth and gum?",
    },
    "gum_pain": {
        "uz": "Milk o'zi og'riyaptimi (tishdan alohida)?",
        "ru": "Десна болит сама по себе (отдельно от зуба)?",
        "en": "Does the gum hurt on its own (separately from the tooth)?",
    },
    "gum_redness": {
        "uz": "Milk qizarib, rangi o'zgarganmi (odatdagidan to'qroq)?",
        "ru": "Покраснела ли десна, изменился ли её цвет (стала темнее обычного)?",
        "en": "Has the gum become red or changed colour (darker than usual)?",
    },
    "gum_enlargement": {
        "uz": "Milk tishni qoplay boshlaganmi — kattalashib, ustiga chiqib qolganmi?",
        "ru": "Десна начала перекрывать зуб — увеличилась и нависла?",
        "en": "Has the gum grown and started to cover the tooth?",
    },
    "gum_ulcer": {
        "uz": "Milkda yara yoki nekroz (qorayish) ko'rinib turadimi?",
        "ru": "Видна ли на десне язва или некроз (потемнение)?",
        "en": "Is there an ulcer or necrosis (darkening) visible on the gum?",
    },
    "wisdom_tooth_pain": {
        "uz": "Og'riq eng orqa tish (aql tishi) sohasidami?",
        "ru": "Боль в области самого заднего зуба (зуба мудрости)?",
        "en": "Is the pain in the area of the very back tooth (wisdom tooth)?",
    },
    "rapid_progression": {
        "uz": "Holat tez rivojlanayaptimi — bir-ikki oyda ko'plab tishlar ta'sirlandi?",
        "ru": "Состояние быстро прогрессирует — за 1-2 месяца поражено много зубов?",
        "en": "Is the condition progressing rapidly — many teeth affected in 1-2 months?",
    },
    "no_bone_loss": {
        "uz": "Shifokor hali suyak yo'qotilmagan degan (yoki rentgeningiz normal bo'lgan)?",
        "ru": "Врач сказал, что потери кости пока нет (или рентген был в норме)?",
        "en": "Has a dentist said there is no bone loss yet (or your X-ray was normal)?",
    },
    "no_inflammation": {
        "uz": "Milkda qizarish yoki shish yo'qmi — ko'rinish normal?",
        "ru": "Нет ли покраснения или отёка десны — выглядит нормально?",
        "en": "Is there no redness or swelling of the gums — looks normal?",
    },
    "young_patient": {
        "uz": "Yoshingiz 35 dan pastmi?",
        "ru": "Вам меньше 35 лет?",
        "en": "Are you under 35 years old?",
    },
    # ── SHILLIQ QAVAT ────────────────────────────────────────────
    "ulcer": {
        "uz": "Og'iz ichida yara (shilliq qavat teshilgan, achishadi) bormi?",
        "ru": "Есть ли во рту язва (нарушение слизистой, жжение)?",
        "en": "Is there an ulcer inside the mouth (breach in the mucosa, burning)?",
    },
    "white_patch": {
        "uz": "Og'iz ichida oq qatlam yoki oq dog' ko'rinib turadimi?",
        "ru": "Виден ли во рту белый налёт или белое пятно?",
        "en": "Is there a white patch or coating visible inside the mouth?",
    },
    "blisters": {
        "uz": "Og'iz ichida yoki labda suvli pufakchalar toshganmi?",
        "ru": "Появились ли во рту или на губах водянистые пузырьки?",
        "en": "Have watery blisters appeared inside the mouth or on the lips?",
    },
    "removable_patch": {
        "uz": "Oq qatlam toza tampon bilan artilganda ko'tarilib tushib ketadimi?",
        "ru": "Белый налёт снимается при протирании чистым ватным тампоном?",
        "en": "Does the white patch come off when wiped with a clean cotton swab?",
    },
    "non_removable": {
        "uz": "Oq dog' artib tushmaydimi — mahkam yopishib turganmi?",
        "ru": "Белое пятно не снимается — крепко держится?",
        "en": "Does the white patch NOT come off — is it firmly attached?",
    },
    "white_center_red_halo": {
        "uz": "Yarada oq/sarg'ish markaz va atrofida qizil halqa bormi?",
        "ru": "Есть ли у язвы белый/желтоватый центр и красный ободок вокруг?",
        "en": "Does the ulcer have a white/yellowish centre with a red halo around it?",
    },
    "white_lacy_pattern": {
        "uz": "Og'iz ichida to'r shaklidagi yoki chiziqli oq naqsh ko'rinib turadimi?",
        "ru": "Виден ли во рту кружевной или линейный белый узор?",
        "en": "Is there a lacy or linear white pattern visible inside the mouth?",
    },
    "multiple_lesions": {
        "uz": "Og'iz ichida bir nechta joylarda (ko'plab) yara/toshmalar bormi?",
        "ru": "Есть ли во рту поражения в нескольких местах (множественные)?",
        "en": "Are there lesions in multiple places inside the mouth?",
    },
    "recurrent": {
        "uz": "Bu holat avvaldan ham tez-tez qaytalanadimi (oyda bir yoki ko'proq)?",
        "ru": "Это состояние часто повторяется (раз в месяц или чаще)?",
        "en": "Does this condition recur frequently (once a month or more)?",
    },
    "trauma_history": {
        "uz": "Bu yara yaqinda tish, protez yoki qattiq ovqat ta'sir qilgan joyda paydo bo'ldimi?",
        "ru": "Появилась ли язва там, где недавно было травматическое воздействие (зуб, протез, твёрдая еда)?",
        "en": "Did the ulcer appear where there was recent trauma (tooth, denture, hard food)?",
    },
    "antibiotic_history": {
        "uz": "So'nggi 2-3 haftada antibiotik ichganmisiz?",
        "ru": "Принимали ли антибиотики в последние 2-3 недели?",
        "en": "Have you taken antibiotics in the last 2-3 weeks?",
    },
    "bilateral": {
        "uz": "Bu belgilar og'izning ikkala tomonida ham (simmetrik) ko'rinib turadimi?",
        "ru": "Эти признаки видны с обеих сторон полости рта (симметрично)?",
        "en": "Are these signs visible on both sides of the mouth (symmetrically)?",
    },
    "stress_trigger": {
        "uz": "Bu holat asosan stress yoki kasallikdan (immunitet pasayganda) keyin paydo bo'ladimi?",
        "ru": "Это состояние появляется обычно после стресса или болезни (при снижении иммунитета)?",
        "en": "Does this condition appear usually after stress or illness (when immunity drops)?",
    },
    "burning": {
        "uz": "Og'iz ichida kuyish yoki achishish hissi bormi?",
        "ru": "Есть ли ощущение жжения или щипания во рту?",
        "en": "Is there a burning or stinging sensation inside the mouth?",
    },
    "dry_mouth": {
        "uz": "Og'iz qurib qolganligini his qilyapsizmi?",
        "ru": "Ощущаете ли вы сухость во рту?",
        "en": "Do you feel dryness in the mouth?",
    },
    "smoking_history": {
        "uz": "Chekasizmi yoki ilgari chekkanmisiz?",
        "ru": "Курите ли вы или курили раньше?",
        "en": "Do you smoke or have you smoked before?",
    },
    "erosion": {
        "uz": "Oq naqsh joylashgan joyda yaraga o'xshash eroziya (qizil yuzali) ham bormi?",
        "ru": "Есть ли в месте белого узора эрозия (покрасневшая поверхность)?",
        "en": "Is there erosion (reddened surface) where the white pattern is?",
    },
    "redness": {
        "uz": "Og'iz ichidagi shilliq qavat umumiy qizarganmi (keng maydon)?",
        "ru": "Слизистая оболочка полости рта в целом покраснела (на большой площади)?",
        "en": "Is the mouth lining generally red (over a wide area)?",
    },
    "swelling_mucosa": {
        "uz": "Shilliq qavat shishgan ko'rinayaptimi?",
        "ru": "Слизистая выглядит отёчной?",
        "en": "Does the mucosa appear swollen?",
    },
    "localized": {
        "uz": "Yara yoki belgi faqat bitta aniq joyda (kichik maydon)da joylashganmi?",
        "ru": "Язва или признак находится только в одном конкретном месте (небольшая площадь)?",
        "en": "Is the ulcer or sign located only in one specific spot (small area)?",
    },
    "pain": {
        "uz": "Shu sohada og'riq yoki achishish bormi?",
        "ru": "Есть ли в этой области боль или жжение?",
        "en": "Is there pain or burning in this area?",
    },
    # ════════════════════════════════════════════════════════════
    #  PERIODONTAL — qo'shimcha
    # ════════════════════════════════════════════════════════════
    "root_exposure": {
        "uz": "Tish ildizi yalang'ochlanib, sezgir bo'lib qolganmi (bo'yi uzun ko'rinadi)?",
        "ru": "Обнажился ли корень зуба, стал ли он чувствительным (зуб «удлинился»)?",
        "en": "Is the tooth root exposed and sensitive (tooth looks longer)?",
    },
    "gum_desquamation": {
        "uz": "Milk yuzasi qizil, yaltiroq bo'lib po'st tashlayaptimi (yuza ko'chadi)?",
        "ru": "Поверхность десны красная, блестящая и слущивается (отслаивается)?",
        "en": "Is the gum surface red, shiny and peeling (sloughing)?",
    },
    "has_implant": {
        "uz": "Muammo joyida implant (sun'iy tish ildizi) o'rnatilganmi?",
        "ru": "В месте проблемы установлен имплант (искусственный корень)?",
        "en": "Is there a dental implant placed at the problem site?",
    },
    "generalized": {
        "uz": "Muammo og'izning ko'p qismida — deyarli barcha tishlar atrofida bormi?",
        "ru": "Проблема охватывает большую часть рта — почти вокруг всех зубов?",
        "en": "Does the problem affect most of the mouth — around almost all teeth?",
    },
    "furcation_defect": {
        "uz": "Ko'p ildizli tish ildizlari orasida bo'shliq borligini shifokor aytganmi (furkatsiya)?",
        "ru": "Говорил ли врач о дефекте между корнями многокорневого зуба (фуркация)?",
        "en": "Has a dentist mentioned a defect between the roots of a multi-rooted tooth (furcation)?",
    },

    # ════════════════════════════════════════════════════════════
    #  JAG' SUYAGI — qo'shimcha
    # ════════════════════════════════════════════════════════════
    "recent_extraction": {
        "uz": "So'nggi kunlarda shu sohada tish oldirganmisiz (ekstraksiya)?",
        "ru": "Удаляли ли вы зуб в этой области в последние дни (экстракция)?",
        "en": "Did you have a tooth extracted in this area in the last few days?",
    },
    "empty_socket_pain": {
        "uz": "Tish olingan katakcha bo'sh, kuchli og'riydi (3-4 kundan keyin kuchaydi)?",
        "ru": "Лунка после удаления пустая и сильно болит (усилилась через 3-4 дня)?",
        "en": "Is the extraction socket empty and severely painful (worsened after 3-4 days)?",
    },
    "slow_growth": {
        "uz": "Shish/zichlik juda sekin, oylar davomida kattalashganmi?",
        "ru": "Отёк/уплотнение растёт очень медленно, в течение месяцев?",
        "en": "Has the swelling/mass grown very slowly, over months?",
    },
    "recurrence_history": {
        "uz": "Bu o'simta/kista olib tashlangandan keyin yana qaytalanganmi?",
        "ru": "Это образование/киста рецидивировало после удаления?",
        "en": "Has this lesion/cyst recurred after being removed before?",
    },

    # ════════════════════════════════════════════════════════════
    #  TMJ — chakka-pastki jag' bo'g'imi
    # ════════════════════════════════════════════════════════════
    "jaw_clicking": {
        "uz": "Og'izni ochib-yopganda bo'g'imda shiqillash yoki qarsillash eshitiladimi?",
        "ru": "При открывании/закрывании рта слышен щелчок или хруст в суставе?",
        "en": "Is there a click or popping in the joint when opening/closing the mouth?",
    },
    "joint_pain": {
        "uz": "Quloq oldidagi bo'g'im sohasida og'riq bormi (ayniqsa chaynaganda)?",
        "ru": "Есть ли боль в области сустава перед ухом (особенно при жевании)?",
        "en": "Is there pain in the joint area in front of the ear (especially when chewing)?",
    },
    "joint_crepitus": {
        "uz": "Bo'g'imda qum g'ichirlashiga o'xshash ovoz (krepitatsiya) bormi?",
        "ru": "Есть ли в суставе звук, похожий на скрип песка (крепитация)?",
        "en": "Is there a grating, sand-like sound in the joint (crepitus)?",
    },
    "jaw_locking": {
        "uz": "Jag' ba'zan qotib/qulflanib qoladimi (ocholmay yoki yopolmay)?",
        "ru": "Челюсть иногда заклинивает (не открыть или не закрыть)?",
        "en": "Does the jaw sometimes lock (cannot open or close)?",
    },
    "jaw_deviation": {
        "uz": "Og'iz ochilganda jag' bir tomonga og'ib ketadimi?",
        "ru": "При открывании рта челюсть смещается в сторону?",
        "en": "Does the jaw shift to one side when opening the mouth?",
    },
    "cannot_open_progressive": {
        "uz": "Og'iz ochilishi vaqt o'tishi bilan butunlay yopilib (qotib) qolganmi?",
        "ru": "Открывание рта со временем полностью ограничилось (срослось)?",
        "en": "Has mouth opening become permanently restricted (fused) over time?",
    },
    "morning_stiffness": {
        "uz": "Ertalab jag'da qotishish yoki harakat qiyinligi bo'ladimi?",
        "ru": "По утрам есть скованность или тугоподвижность челюсти?",
        "en": "Is there morning stiffness or difficulty moving the jaw?",
    },

    # ════════════════════════════════════════════════════════════
    #  TRAVMA
    # ════════════════════════════════════════════════════════════
    "recent_injury": {
        "uz": "Yaqinda tish/jag'ga zarba yoki jarohat bo'ldimi (yiqilish, urilish)?",
        "ru": "Была ли недавно травма зуба/челюсти (падение, удар)?",
        "en": "Was there a recent injury to the tooth/jaw (fall, blow)?",
    },
    "tooth_fractured": {
        "uz": "Tish sinib, bir bo'lagi uchib ketganmi?",
        "ru": "Зуб сломался, откололся ли его кусок?",
        "en": "Is the tooth fractured, with a piece broken off?",
    },
    "fracture_enamel_only": {
        "uz": "Faqat kichik chekka (emal) uchgan, og'riq yo'q va dentin ochilmaganmi?",
        "ru": "Откололся только маленький край (эмаль), без боли и без обнажения дентина?",
        "en": "Did only a small edge (enamel) chip off, with no pain and no exposed dentin?",
    },
    "fracture_dentin": {
        "uz": "Siniqda sarg'ish qatlam (dentin) ochilgan va sovuq/havoga sezgirmi?",
        "ru": "В сколе обнажён желтоватый слой (дентин), чувствителен к холоду/воздуху?",
        "en": "Is a yellowish layer (dentin) exposed in the fracture, sensitive to cold/air?",
    },
    "pulp_exposed_bleeding": {
        "uz": "Siniqning o'rtasida qizil nuqta yoki qon ko'rinadimi (nerv ochilgan)?",
        "ru": "В центре скола видна красная точка или кровь (обнажён нерв)?",
        "en": "Is there a red dot or bleeding in the centre of the fracture (exposed pulp)?",
    },
    "tooth_displaced": {
        "uz": "Tish o'rnidan siljiganmi — chiqib qolgan yoki yon tomonga og'ganmi?",
        "ru": "Зуб сместился — выдвинулся или сдвинулся в сторону?",
        "en": "Has the tooth been displaced — pushed out or shifted sideways?",
    },
    "tooth_intruded": {
        "uz": "Tish ichkariga (suyak ichiga) kirib ketib, kaltaroq ko'rinadimi?",
        "ru": "Зуб вдавился внутрь (в кость) и выглядит короче?",
        "en": "Has the tooth been pushed inward (into the bone), looking shorter?",
    },
    "tooth_avulsed": {
        "uz": "Tish butunlay o'rnidan chiqib (tushib) ketganmi?",
        "ru": "Зуб полностью выбит (выпал) из лунки?",
        "en": "Has the tooth been completely knocked out of its socket?",
    },
    "tooth_tender_after_injury": {
        "uz": "Zarbadan keyin tish og'riydi, lekin qimirlamaydi va siljimaganmi?",
        "ru": "После удара зуб болит, но не подвижен и не смещён?",
        "en": "After the blow the tooth hurts but is not loose or displaced?",
    },

    # ════════════════════════════════════════════════════════════
    #  TISH RIVOJLANISHI / ORTODONTIK ANOMALIYALAR
    # ════════════════════════════════════════════════════════════
    "teeth_missing_congenital": {
        "uz": "Ba'zi tishlar tug'ilishdan umuman chiqmaganmi (yo'q)?",
        "ru": "Некоторые зубы отсутствуют с рождения (не прорезались)?",
        "en": "Are some teeth congenitally missing (never erupted)?",
    },
    "many_teeth_missing": {
        "uz": "Yetishmayotgan tishlar ko'pmi (oltidan ortiq yoki deyarli barchasi)?",
        "ru": "Отсутствует много зубов (более шести или почти все)?",
        "en": "Are many teeth missing (more than six, or almost all)?",
    },
    "all_teeth_missing": {
        "uz": "Tishlar umuman yo'qmi (to'liq tishsizlik, tug'ma)?",
        "ru": "Зубы отсутствуют полностью (полная адентия, врождённая)?",
        "en": "Are teeth completely absent (full congenital absence)?",
    },
    "extra_teeth": {
        "uz": "Ortiqcha (qo'shimcha) tish/tishlar bormi?",
        "ru": "Есть ли лишние (сверхкомплектные) зубы?",
        "en": "Are there extra (supernumerary) teeth?",
    },
    "abnormal_tooth_shape": {
        "uz": "Biror tish shakli g'ayritabiiy — juda katta, ikkita qo'shilib ketgan ko'rinishdami?",
        "ru": "Есть ли зуб необычной формы — очень крупный или как два сросшихся?",
        "en": "Is a tooth an abnormal shape — very large or looking like two fused together?",
    },
    "teeth_crowded": {
        "uz": "Tishlar qiyshiq, zich joylashgan — ularga joy yetishmaydimi?",
        "ru": "Зубы скучены, расположены тесно — им не хватает места?",
        "en": "Are the teeth crowded/crooked — not enough room for them?",
    },
    "spacing_gaps": {
        "uz": "Tishlar orasida bo'shliq (yoriqlar) bormi — old tishlar orasida ham?",
        "ru": "Есть ли промежутки между зубами — в том числе между передними?",
        "en": "Are there gaps between the teeth — including between the front teeth?",
    },
    "upper_teeth_protrude": {
        "uz": "Yuqori old tishlar oldinga sezilarli chiqib turadimi?",
        "ru": "Верхние передние зубы заметно выступают вперёд?",
        "en": "Do the upper front teeth noticeably stick out forward?",
    },
    "lower_jaw_protrudes": {
        "uz": "Pastki jag'/tishlar yuqori tishlardan oldinga chiqqanmi?",
        "ru": "Нижняя челюсть/зубы выступают вперёд за верхние зубы?",
        "en": "Does the lower jaw/teeth jut out ahead of the upper teeth?",
    },
    "front_teeth_no_contact": {
        "uz": "Old tishlar yopilganda tegmaydi — orasida ochiq oraliq qoladimi (ochiq tishlash)?",
        "ru": "Передние зубы не смыкаются — остаётся открытая щель (открытый прикус)?",
        "en": "Do the front teeth not meet when closed — leaving an open gap (open bite)?",
    },
    "deep_overbite": {
        "uz": "Yuqori old tishlar pastki tishlarni juda ko'p (deyarli to'liq) qoplaydimi?",
        "ru": "Верхние передние зубы перекрывают нижние слишком сильно (почти полностью)?",
        "en": "Do the upper front teeth overlap the lower ones excessively (deep bite)?",
    },
    "crossbite": {
        "uz": "Tishlashda ba'zi pastki tishlar yuqori tishlardan tashqarida qoladimi (kesishgan tishlash)?",
        "ru": "При смыкании некоторые нижние зубы оказываются снаружи верхних (перекрёстный прикус)?",
        "en": "When biting, do some lower teeth sit outside the upper ones (crossbite)?",
    },
    "tooth_wrong_position": {
        "uz": "Biror tish noto'g'ri joydan yoki noto'g'ri burchakda chiqqanmi?",
        "ru": "Какой-то зуб прорезался не на своём месте или под неправильным углом?",
        "en": "Has a tooth erupted in the wrong place or at the wrong angle?",
    },

    # ════════════════════════════════════════════════════════════
    #  SO'LAK BEZLARI
    # ════════════════════════════════════════════════════════════
    "gland_swelling": {
        "uz": "Quloq oldida yoki jag' ostida so'lak bezi shishi (do'mboq) bormi?",
        "ru": "Есть ли припухлость слюнной железы перед ухом или под челюстью?",
        "en": "Is there a salivary gland swelling in front of the ear or under the jaw?",
    },
    "swelling_with_meals": {
        "uz": "Bez shishi ovqatdan oldin/paytida kattalashib, keyin kichrayadimi?",
        "ru": "Припухлость железы увеличивается перед/во время еды, затем спадает?",
        "en": "Does the gland swelling enlarge before/during meals, then subside?",
    },
    "gland_pain": {
        "uz": "Bez sohasida og'riq va bosganda og'riydigan zichlik bormi?",
        "ru": "Есть ли боль в области железы и болезненное уплотнение при надавливании?",
        "en": "Is there pain in the gland area and tenderness on pressing?",
    },
    "pus_from_duct": {
        "uz": "Bez yo'lidan (og'iz ichiga) yiring yoki bulutli so'lak chiqadimi?",
        "ru": "Из протока железы (в рот) выделяется гной или мутная слюна?",
        "en": "Does pus or cloudy saliva come from the gland duct (into the mouth)?",
    },
    "dry_eyes": {
        "uz": "Og'iz bilan birga ko'zlar ham doimiy quruq bo'ladimi?",
        "ru": "Вместе с сухостью рта есть ли постоянная сухость глаз?",
        "en": "Along with dry mouth, are your eyes also persistently dry?",
    },
    "bluish_soft_swelling": {
        "uz": "Lab ichida yoki og'iz tubida ko'kimtir, yumshoq, suvli pufak (kista) bormi?",
        "ru": "Есть ли на губе или дне рта синеватый мягкий пузырь (киста)?",
        "en": "Is there a bluish, soft, fluid-filled bump (cyst) on the lip or floor of mouth?",
    },
    "floor_of_mouth_swelling": {
        "uz": "Til ostida katta, ko'kimtir, qurbaqa qorni kabi shish (ranula) bormi?",
        "ru": "Под языком крупная синеватая припухлость, как у лягушки (ранула)?",
        "en": "Is there a large bluish swelling under the tongue, like a frog's belly (ranula)?",
    },

    # ════════════════════════════════════════════════════════════
    #  TIL KASALLIKLARI
    # ════════════════════════════════════════════════════════════
    "tongue_lesion": {
        "uz": "Belgi/o'zgarish tilda joylashganmi?",
        "ru": "Признак/изменение расположено на языке?",
        "en": "Is the sign/change located on the tongue?",
    },
    "map_like_patches": {
        "uz": "Tilda xarita kabi qizil-oq dog'lar bo'lib, ularning joyi vaqt o'tib o'zgaradimi?",
        "ru": "На языке красно-белые пятна, как карта, меняющие расположение со временем?",
        "en": "Are there map-like red-white patches on the tongue that change location over time?",
    },
    "hairy_coating": {
        "uz": "Til usti tukli ko'rinishdagi qora yoki jigarrang qoplama bilan qoplanganmi?",
        "ru": "Спинка языка покрыта «волосатым» чёрным или коричневым налётом?",
        "en": "Is the tongue surface covered with a hairy black or brown coating?",
    },
    "smooth_red_patch_tongue": {
        "uz": "Til o'rtasida (orqaroq) silliq, qizil, papillasiz romb/oval dog' bormi?",
        "ru": "По средней линии языка гладкое красное ромбовидное пятно без сосочков?",
        "en": "Is there a smooth, red, papilla-free rhomboid patch in the middle of the tongue?",
    },

    # ════════════════════════════════════════════════════════════
    #  LAB KASALLIKLARI (XEYLIT)
    # ════════════════════════════════════════════════════════════
    "lip_lesion": {
        "uz": "Belgi/o'zgarish lab(lar)da joylashganmi?",
        "ru": "Признак/изменение расположено на губе(ах)?",
        "en": "Is the sign/change located on the lip(s)?",
    },
    "lip_cracking_weather": {
        "uz": "Sovuq, shamol yoki quruqlikdan lab(lar) yorilib, qaqrab qoladimi?",
        "ru": "От холода, ветра или сухости губы трескаются и шелушатся?",
        "en": "Do the lips crack and chap from cold, wind or dryness?",
    },
    "lip_persistent_scaling": {
        "uz": "Lab doimiy po'st tashlaydi, qoraqo'ng'ir qatlamlar bilan qoplanadimi (uzoq davom etgan)?",
        "ru": "Губа постоянно шелушится, покрывается чешуйками-корками (длительно)?",
        "en": "Does the lip persistently peel and form scaly crusts (long-standing)?",
    },
    "lip_sun_damage": {
        "uz": "Pastki lab uzoq quyosh ta'siridan qo'pol, quruq, oq-qizil dog'li bo'lib qolganmi?",
        "ru": "Нижняя губа от долгого солнца стала шершавой, сухой, с бело-красными участками?",
        "en": "Is the lower lip rough, dry and white-red from chronic sun exposure?",
    },
    "angular_cracks": {
        "uz": "Lab burchaklarida yoriq, yara yoki achishuvchi qoq (zaeda) bormi?",
        "ru": "В уголках губ есть трещины, ранки или мокнущие заеды?",
        "en": "Are there cracks, sores or fissures at the corners of the mouth (angular)?",
    },

    # ════════════════════════════════════════════════════════════
    #  INFEKSION (virusli / bakterial)
    # ════════════════════════════════════════════════════════════
    "grouped_vesicles": {
        "uz": "Lab/burun atrofida guruh bo'lib turgan mayda pufakchalar (oldin achishib) toshdimi?",
        "ru": "На губе/у носа высыпали сгруппированные мелкие пузырьки (с предшествующим жжением)?",
        "en": "Did grouped small blisters erupt on the lip/around the nose (preceded by tingling)?",
    },
    "unilateral_rash": {
        "uz": "Toshma yuzning faqat bitta tomonida, chiziq bo'ylab va kuchli og'riq bilan paydo bo'ldimi?",
        "ru": "Сыпь появилась только на одной стороне лица, по ходу нерва, с сильной болью?",
        "en": "Did the rash appear only on one side of the face, along a nerve line, with severe pain?",
    },
    "wart_like_growth": {
        "uz": "Gulkaram yoki so'galsimon mayda, qattiqroq o'simta bormi?",
        "ru": "Есть ли мелкое бородавчатое разрастание, похожее на цветную капусту?",
        "en": "Is there a small wart-like or cauliflower-like growth?",
    },
    "hand_foot_rash": {
        "uz": "Og'iz bilan birga qo'l va oyoqlarda ham toshma bor (ko'pincha bolada, isitma bilan)?",
        "ru": "Вместе со ртом сыпь есть и на кистях и стопах (чаще у ребёнка, с лихорадкой)?",
        "en": "Along with the mouth, is there a rash on hands and feet (often a child, with fever)?",
    },
    "painless_firm_ulcer": {
        "uz": "Yara qattiq qirrali, og'riqsiz va o'z-o'zidan bitayotgandek ko'rinadimi (shankr)?",
        "ru": "Язва с плотными краями, безболезненная и будто заживает сама (шанкр)?",
        "en": "Is the ulcer firm-edged, painless and seemingly self-healing (chancre)?",
    },
    "chronic_nonhealing_ulcer": {
        "uz": "Yara 3 haftadan ko'p bitmay, sekin kattalashib boryaptimi?",
        "ru": "Язва не заживает более 3 недель и медленно увеличивается?",
        "en": "Has the ulcer not healed for more than 3 weeks and is slowly enlarging?",
    },
    "woody_swelling": {
        "uz": "Qattiq, yog'ochsimon shish bo'lib, undan ko'p fistula va sarg'ish donachalar chiqadimi?",
        "ru": "Плотная деревянистая припухлость с множественными свищами и желтоватыми зёрнами?",
        "en": "Is there a hard, woody swelling with multiple fistulas draining yellow granules?",
    },

    # ════════════════════════════════════════════════════════════
    #  O'SMA / PREKANSEROZ
    # ════════════════════════════════════════════════════════════
    "soft_painless_lump": {
        "uz": "Yumshoq, og'riqsiz, sekin o'sgan tugun/do'mboq bormi?",
        "ru": "Есть ли мягкий, безболезненный, медленно растущий узел/шишка?",
        "en": "Is there a soft, painless, slowly growing lump/nodule?",
    },
    "red_blue_blanching_lesion": {
        "uz": "Qizil-ko'kimtir qon tomir o'simtasi bo'lib, bosganda rangi oqaradimi?",
        "ru": "Есть ли красно-синюшное сосудистое образование, бледнеющее при надавливании?",
        "en": "Is there a red-blue vascular lesion that blanches (pales) when pressed?",
    },
    "red_velvety_patch": {
        "uz": "Artilmaydigan qizil, baxmaldek silliq dog' bormi?",
        "ru": "Есть ли несоскабливаемое красное бархатистое гладкое пятно?",
        "en": "Is there a non-scrapable red, velvety smooth patch?",
    },
    "progressive_trismus_fibrosis": {
        "uz": "Og'iz ochilishi asta-sekin qiyinlashib, shilliq qavat oqarib qotganmi (betel/nos iste'moli)?",
        "ru": "Открывание рта постепенно ограничилось, слизистая побледнела и уплотнилась (бетель/нас)?",
        "en": "Has mouth opening gradually become limited with pale, stiff mucosa (betel/areca use)?",
    },
    "indurated_lesion": {
        "uz": "O'simta yoki yara qattiq, o'rnashgan (asosida zich) va atrofga yopishganmi?",
        "ru": "Образование/язва плотное, фиксированное (с уплотнением в основании), спаяно с тканями?",
        "en": "Is the lesion/ulcer hard, fixed (indurated base) and attached to surrounding tissue?",
    },
    "easy_bleeding_growth": {
        "uz": "O'simta arzimas teginishdan ham oson qonaydimi?",
        "ru": "Образование легко кровоточит даже при незначительном касании?",
        "en": "Does the growth bleed easily even with slight contact?",
    },
    "numbness": {
        "uz": "Shu sohada uvishish yoki sezuvchanlik yo'qolishi (karaxtlik) bormi?",
        "ru": "Есть ли в этой области онемение или потеря чувствительности?",
        "en": "Is there numbness or loss of sensation in this area?",
    },
    "tobacco_risk": {
        "uz": "Tamaki, nos yoki betel/nasvoy iste'mol qilasizmi (yoki ko'p chekasizmi)?",
        "ru": "Употребляете ли табак, нас или бетель (или много курите)?",
        "en": "Do you use tobacco, snus or betel/areca (or smoke heavily)?",
    },

    # ── JAG' ─────────────────────────────────────────────────────
    "jaw_swelling": {
        "uz": "Jag' atrofida yoki yuzda ko'rinib turuvchi shish bormi?",
        "ru": "Есть ли видимый отёк в области челюсти или лица?",
        "en": "Is there a visible swelling around the jaw or face?",
    },
    "trismus": {
        "uz": "Og'izni to'liq ocholmayapsizmi — og'iz ochish qiyinmi?",
        "ru": "Не получается широко открыть рот — затруднено ли открывание?",
        "en": "Can you not open your mouth fully — is mouth opening difficult?",
    },
    "jaw_deformity": {
        "uz": "Jag' shakli o'zgarganmi yoki notekislashganmi?",
        "ru": "Изменилась ли форма челюсти или она стала неровной?",
        "en": "Has the jaw shape changed or become irregular?",
    },
    "retained_tooth": {
        "uz": "Suyak ichida qolib ketgan (chiqmagan) tish borligini shifokor aytganmi?",
        "ru": "Говорил ли врач о зубе, который остался в кости (не прорезался)?",
        "en": "Has a dentist told you there is a tooth retained inside the bone (unerupted)?",
    },
    "causative_tooth": {
        "uz": "Shishning yonida og'riydigan, qoraygan yoki plombalangan tish bormi?",
        "ru": "Рядом с отёком есть больной, потемневший или запломбированный зуб?",
        "en": "Near the swelling, is there a painful, darkened or filled tooth?",
    },
    "sequestrum": {
        "uz": "Og'izdagi yarachadan ba'zan qattiq (suyak) parchalari chiqib turadimi?",
        "ru": "Выходят ли иногда из свища твёрдые (костные) фрагменты?",
        "en": "Do hard (bone) fragments sometimes come out through the fistula?",
    },
    # ── UMUMIY ───────────────────────────────────────────────────
    "fever": {
        "uz": "Tana harorati ko'tarilganmi (37.5°C dan yuqori)?",
        "ru": "Повышена ли температура тела (выше 37.5°C)?",
        "en": "Is your body temperature elevated (above 37.5°C)?",
    },
    "high_fever": {
        "uz": "Isitma juda balandmi — 38.5°C dan yuqorimi?",
        "ru": "Температура очень высокая — выше 38.5°C?",
        "en": "Is the fever very high — above 38.5°C?",
    },
    "lymph_nodes": {
        "uz": "Bo'yin yoki jag' osti limfa tugunlari kattalashib, og'riq berayaptimi?",
        "ru": "Увеличены ли и болезненны ли лимфоузлы шеи или под челюстью?",
        "en": "Are the lymph nodes in the neck or under the jaw enlarged and tender?",
    },
    "general_weakness": {
        "uz": "Umumiy holsizlik, charchoq yoki ishtaha yo'qligi bormi?",
        "ru": "Есть ли общая слабость, усталость или отсутствие аппетита?",
        "en": "Is there general weakness, fatigue or loss of appetite?",
    },
    "pus_discharge": {
        "uz": "Yiring ajralishi ko'rinadimi — og'izda sarg'ish yoki oqish suyuqlik?",
        "ru": "Есть ли выделение гноя — желтоватая или белёсая жидкость во рту?",
        "en": "Is there pus discharge — yellowish or whitish fluid in the mouth?",
    },
    "pressure_sensation": {
        "uz": "Shu sohada bosim yoki to'liqlik hissi bormi (og'riqsiz)?",
        "ru": "Есть ли ощущение давления или распирания в этой области (без боли)?",
        "en": "Is there a feeling of pressure or fullness in the area (without pain)?",
    },
}

# ─────────────────────────────────────────────────────────────────
#  HAR KATEGORIYA UCHUN NOMZOD SAVOLLAR PULI
#  (selector shu puldan information-gain bo'yicha eng yaxshisini tanlaydi)
# ─────────────────────────────────────────────────────────────────

CANDIDATE_SYMPTOMS: Dict[str, List[str]] = {
    # "tooth" — barcha tish kasalliklari (karies + pulpit + periapikal) uchun
    # birlashtirilgan savollar puli. Tartib muhim emas (selector info-gain bo'yicha tanlaydi),
    # ammo ajratuvchi savollar boshida turadi.
    "tooth": [
        "spontaneous_pain",
        "night_pain",
        "percussion_pain",
        "pain_triggered",
        "cavity_visible",
        "cold_short",
        "no_pain",
        "visible_white_spot",
        "old_filling",
        "sweet_sensitivity",
        "hot_sensitivity",
        "pain_attacks",
        "short_pain_attacks",
        "hot_increases_pain",
        "cold_relieves_pain",
        "cold_prolonged",
        "irradiation",
        "tooth_discoloration",
        "bad_smell",
        "no_sensitivity",
        "pulp_polyp",
        "bleeding_on_chewing",
        "dull_ache",
        "localized_pain",
        "pressure_pain",
        "gum_swelling",
        "fistula",
        "pus_discharge",
        "pressure_sensation",
        "fever",
        "lymph_nodes",
        # nokarioz / rivojlanish belgilarini ajratuvchi savollar
        "multiple_teeth_affected",
        "since_childhood",
        "family_history",
        "brown_stains",
        "enamel_pits",
        "enamel_missing",
        "wedge_defect",
        "occlusal_wear",
        "bruxism",
        "hard_brushing",
        "acid_exposure",
        "smooth_shiny_surface",
        "chalky_enamel",
        "abnormal_tooth_color",
        "cold_sensitivity",
        "gum_recession",
        "tooth_mobility",
    ],
    # pulp/periapical — ichki bo'linish (hozir engine to'g'ridan "tooth" guruhini ishlatadi,
    # bu pullar kelajakdagi batafsil tahlil uchun saqlanadi)
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
        "cold_short",
        "dull_ache",
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
        "no_pain",
        "spontaneous_pain",
        "night_pain",
        "cold_short",
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
        "fever",
        "general_weakness",
        "pressure_pain",
        "spontaneous_pain",
        "root_exposure",
        "gum_desquamation",
        "has_implant",
        "generalized",
        "furcation_defect",
        "bilateral",
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
        "no_pain",
        "general_weakness",
        "bad_smell",
        # til kasalliklari
        "tongue_lesion",
        "map_like_patches",
        "hairy_coating",
        "smooth_red_patch_tongue",
        # lab kasalliklari (xeylit)
        "lip_lesion",
        "lip_cracking_weather",
        "lip_persistent_scaling",
        "lip_sun_damage",
        "angular_cracks",
        # infeksion
        "grouped_vesicles",
        "unilateral_rash",
        "wart_like_growth",
        "hand_foot_rash",
        "painless_firm_ulcer",
        "chronic_nonhealing_ulcer",
        "woody_swelling",
        # o'sma / prekanseroz
        "soft_painless_lump",
        "red_blue_blanching_lesion",
        "red_velvety_patch",
        "progressive_trismus_fibrosis",
        "indurated_lesion",
        "easy_bleeding_growth",
        "numbness",
        "tobacco_risk",
        "slow_growth",
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
        "no_pain",
        "spontaneous_pain",
        "dull_ache",
        "pressure_sensation",
        "recent_extraction",
        "empty_socket_pain",
        "slow_growth",
        "recurrence_history",
        "bad_smell",
    ],
    "tmj": [
        "jaw_clicking",
        "joint_pain",
        "joint_crepitus",
        "jaw_locking",
        "jaw_deviation",
        "cannot_open_progressive",
        "morning_stiffness",
        "trismus",
        "irradiation",
        "bruxism",
        "recent_injury",
        "severe_pain",
        "fever",
    ],
    "trauma": [
        "recent_injury",
        "tooth_fractured",
        "fracture_enamel_only",
        "fracture_dentin",
        "pulp_exposed_bleeding",
        "tooth_displaced",
        "tooth_intruded",
        "tooth_avulsed",
        "tooth_tender_after_injury",
        "tooth_mobility",
        "cold_sensitivity",
        "gum_bleeding",
        "no_pain",
        "tooth_discoloration",
    ],
    "dentition": [
        "teeth_missing_congenital",
        "many_teeth_missing",
        "all_teeth_missing",
        "extra_teeth",
        "abnormal_tooth_shape",
        "teeth_crowded",
        "spacing_gaps",
        "upper_teeth_protrude",
        "lower_jaw_protrudes",
        "front_teeth_no_contact",
        "deep_overbite",
        "crossbite",
        "tooth_wrong_position",
        "retained_tooth",
        "family_history",
        "since_childhood",
        "no_pain",
    ],
    "salivary": [
        "gland_swelling",
        "swelling_with_meals",
        "gland_pain",
        "pus_from_duct",
        "dry_mouth",
        "dry_eyes",
        "bluish_soft_swelling",
        "floor_of_mouth_swelling",
        "fever",
        "lymph_nodes",
        "slow_growth",
        "soft_painless_lump",
        "indurated_lesion",
        "numbness",
        "bad_smell",
    ],
}


# ─────────────────────────────────────────────────────────────────
#  YORDAMCHI FUNKSIYALAR
# ─────────────────────────────────────────────────────────────────

def question_text(symptom_id: str, lang: str = "uz") -> str:
    """Berilgan simptom uchun tanlangan tildagi savol matnini qaytaradi."""
    block = QUESTIONS.get(symptom_id, {})
    return block.get(lang, block.get("uz", symptom_id))


def all_symptom_keys() -> set[str]:
    """Registrda e'lon qilingan barcha simptom kalitlari."""
    return set(QUESTIONS.keys())


def candidates_for(category: str) -> List[str]:
    """Kategoriya uchun savol berilishi mumkin bo'lgan simptomlar puli."""
    return CANDIDATE_SYMPTOMS.get(category, [])
