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
