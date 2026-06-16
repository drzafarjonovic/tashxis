"""
Tish qattiq to'qimalari (karies + nokarioz) va pulpa kasalliklari.

Toifalar (foydalanuvchi triage'i uchun barchasi bitta "tooth" guruhida
birlashtiriladi — bemor karies/pulpit/periapikalni o'zi ajrata olmaydi,
Akinator esa ajratuvchi savollarni info-gain orqali o'zi tanlaydi):

  1. KARIES guruhi          (category="tooth")
  2. NOKARIOZ shikastlanishlar (category="tooth")
  3. PULPA kasalliklari       (category="pulp")
"""

from medical.disease_model import Disease

# ═════════════════════════════════════════════════════════════════
#  1. KARIES GURUHI
# ═════════════════════════════════════════════════════════════════

white_spot = Disease(
    id="white_spot",
    name_uz="Boshlang'ich karies (oq dog' bosqichi)",
    name_ru="Начальный кариес (стадия белого пятна)",
    name_en="Initial caries (white spot stage)",
    category="tooth",
    core_features={
        "no_pain": True,
        "visible_white_spot": True,
    },
    optional_features={
        "sweet_sensitivity": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "cavity_visible": True,
        "night_pain": True,
        "multiple_teeth_affected": True,
    },
    discriminators=[
        "og'riq yo'q",
        "emalda bo'r rangidagi oq dog'",
        "kovak hali hosil bo'lmagan",
    ],
    red_flags=[
        "pigmentatsiya kuchayishi",
        "kovak shakllanishi",
    ],
)

superficial_caries = Disease(
    id="superficial_caries",
    name_uz="Yuzaki karies",
    name_ru="Поверхностный кариес",
    name_en="Superficial caries",
    category="tooth",
    core_features={
        "cavity_visible": True,
        "pain_triggered": True,
    },
    optional_features={
        "sweet_sensitivity": True,
        "cold_short": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "percussion_pain": True,
        "multiple_teeth_affected": True,
    },
    discriminators=[
        "faqat emal zararlangan",
        "qisqa, tez o'tuvchi og'riq",
        "spontan og'riq yo'q",
    ],
    red_flags=[
        "og'riq davomiyligi uzayishi",
        "issiqqa reaksiya paydo bo'lishi",
    ],
)

medium_caries = Disease(
    id="medium_caries",
    name_uz="O'rta karies",
    name_ru="Средний кариес",
    name_en="Medium caries",
    category="tooth",
    core_features={
        "cavity_visible": True,
        "pain_triggered": True,
        "cold_short": True,
    },
    optional_features={
        "sweet_sensitivity": True,
        "hot_sensitivity": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "percussion_pain": True,
    },
    discriminators=[
        "dentin zararlangan",
        "stimulga qisqa og'riq",
        "spontan og'riq yo'q",
    ],
    red_flags=[
        "og'riq davomiyligi ortishi",
        "spontan og'riq paydo bo'lishi",
    ],
)

deep_caries = Disease(
    id="deep_caries",
    name_uz="Chuqur karies",
    name_ru="Глубокий кариес",
    name_en="Deep caries",
    category="tooth",
    core_features={
        "cavity_visible": True,
        "pain_triggered": True,
        "cold_short": True,
    },
    optional_features={
        "sweet_sensitivity": True,
        "hot_sensitivity": True,
        "bad_smell": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "percussion_pain": True,
    },
    discriminators=[
        "chuqur kovak, pulpa yaqin",
        "stimuldan qisqa og'riq",
        "perkussiyada og'riq yo'q",
    ],
    red_flags=[
        "spontan og'riq paydo bo'lishi",
        "issiqdan kuchayuvchi og'riq",
    ],
)

secondary_caries = Disease(
    id="secondary_caries",
    name_uz="Ikkilamchi (residiv) karies",
    name_ru="Вторичный (рецидивный) кариес",
    name_en="Secondary (recurrent) caries",
    category="tooth",
    core_features={
        "old_filling": True,
        "pain_triggered": True,
    },
    optional_features={
        "cold_short": True,
        "sweet_sensitivity": True,
        "bad_smell": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "percussion_pain": True,
    },
    discriminators=[
        "eski plomba atrofida",
        "marginal bo'shliq mavjud",
        "stimulga qisqa og'riq",
    ],
    red_flags=[
        "og'riq kuchayishi",
        "spontan og'riq (pulpitga o'tish)",
    ],
)

# ═════════════════════════════════════════════════════════════════
#  2. NOKARIOZ SHIKASTLANISHLAR
# ═════════════════════════════════════════════════════════════════

enamel_hypoplasia = Disease(
    id="enamel_hypoplasia",
    name_uz="Emal gipoplaziyasi",
    name_ru="Гипоплазия эмали",
    name_en="Enamel hypoplasia",
    category="tooth",
    core_features={
        "enamel_pits": True,
        "since_childhood": True,
    },
    optional_features={
        "multiple_teeth_affected": True,
        "brown_stains": True,
        "no_pain": True,
    },
    negative_features={
        "cavity_visible": True,
        "spontaneous_pain": True,
        "old_filling": True,
    },
    discriminators=[
        "emalda chuqurcha/egat va nuqsonlar",
        "tishlar chiqqanidan beri mavjud",
        "karies kovagi emas",
    ],
    red_flags=[
        "nuqson joyida karies rivojlanishi",
    ],
)

enamel_aplasia = Disease(
    id="enamel_aplasia",
    name_uz="Emal aplaziyasi",
    name_ru="Аплазия эмали",
    name_en="Enamel aplasia",
    category="tooth",
    core_features={
        "enamel_missing": True,
        "since_childhood": True,
    },
    optional_features={
        "multiple_teeth_affected": True,
        "cold_sensitivity": True,
        "family_history": True,
    },
    negative_features={
        "cavity_visible": True,
        "spontaneous_pain": True,
    },
    discriminators=[
        "emal umuman yo'q, dentin ochiq",
        "tug'ma og'ir nuqson",
        "sezuvchanlik yuqori",
    ],
    red_flags=[
        "kuchli sezuvchanlik",
        "tez yeyilish",
    ],
)

dental_fluorosis = Disease(
    id="dental_fluorosis",
    name_uz="Dental fluoroz",
    name_ru="Флюороз зубов",
    name_en="Dental fluorosis",
    category="tooth",
    core_features={
        "brown_stains": True,
        "multiple_teeth_affected": True,
        "since_childhood": True,
    },
    optional_features={
        "no_pain": True,
        "enamel_pits": True,
    },
    negative_features={
        "cavity_visible": True,
        "spontaneous_pain": True,
        "old_filling": True,
    },
    discriminators=[
        "chipor/jigarrang dog'lar",
        "ko'p tishda simmetrik",
        "ortiqcha ftor (suv/pasta) bilan bog'liq",
    ],
    red_flags=[
        "emal yuzasining yemirilishi",
    ],
)

tooth_erosion = Disease(
    id="tooth_erosion",
    name_uz="Tish eroziyasi",
    name_ru="Эрозия зубов",
    name_en="Tooth erosion",
    category="tooth",
    core_features={
        "acid_exposure": True,
        "smooth_shiny_surface": True,
    },
    optional_features={
        "cold_sensitivity": True,
        "multiple_teeth_affected": True,
        "occlusal_wear": True,
    },
    negative_features={
        "cavity_visible": True,
        "enamel_pits": True,
        "since_childhood": True,
    },
    discriminators=[
        "kislota ta'siri (ovqat/reflyuks/qusish)",
        "silliq, yaltiroq, botiq yuza",
        "kovaksiz to'qima yo'qotilishi",
    ],
    red_flags=[
        "dentingacha chuqurlashishi",
        "sezuvchanlik kuchayishi",
    ],
)

attrition = Disease(
    id="attrition",
    name_uz="Patologik yeyilish (attritsiya)",
    name_ru="Патологическая стираемость (аттриция)",
    name_en="Pathological attrition",
    category="tooth",
    core_features={
        "occlusal_wear": True,
        "bruxism": True,
    },
    optional_features={
        "multiple_teeth_affected": True,
        "cold_sensitivity": True,
    },
    negative_features={
        "cavity_visible": True,
        "acid_exposure": True,
        "since_childhood": True,
    },
    discriminators=[
        "chaynov yuzasi tekislanib yedirilgan",
        "tish g'ichirlatish (bruksizm)",
        "tish-tishga ishqalanishdan",
    ],
    red_flags=[
        "tish bo'yi qisqarishi",
        "pulpaga yaqinlashishi",
    ],
)

abrasion = Disease(
    id="abrasion",
    name_uz="Abrasiya (mexanik yeyilish)",
    name_ru="Абразия (механическое истирание)",
    name_en="Abrasion",
    category="tooth",
    core_features={
        "wedge_defect": True,
        "hard_brushing": True,
    },
    optional_features={
        "cold_sensitivity": True,
        "gum_recession": True,
        "multiple_teeth_affected": True,
    },
    negative_features={
        "cavity_visible": True,
        "bruxism": True,
        "acid_exposure": True,
    },
    discriminators=[
        "tish bo'ynida ponasimon nuqson",
        "qattiq/noto'g'ri cho'tkalash",
        "tashqi mexanik ta'sir",
    ],
    red_flags=[
        "sezuvchanlik kuchayishi",
        "nuqson chuqurlashishi",
    ],
)

abfraction = Disease(
    id="abfraction",
    name_uz="Abfraksiya",
    name_ru="Абфракция",
    name_en="Abfraction",
    category="tooth",
    core_features={
        "wedge_defect": True,
        "bruxism": True,
    },
    optional_features={
        "cold_sensitivity": True,
        "gum_recession": True,
    },
    negative_features={
        "cavity_visible": True,
        "hard_brushing": True,
        "acid_exposure": True,
    },
    discriminators=[
        "bo'yinda V-shaklidagi nuqson",
        "okklyuzion zo'riqish (bruksizm)",
        "cho'tkalashdan emas — egilish kuchlaridan",
    ],
    red_flags=[
        "nuqson chuqurlashishi",
        "tish sinishi xavfi",
    ],
)

hard_tissue_necrosis = Disease(
    id="hard_tissue_necrosis",
    name_uz="Tish qattiq to'qimalari nekrozi",
    name_ru="Некроз твёрдых тканей зуба",
    name_en="Hard tissue necrosis",
    category="tooth",
    core_features={
        "chalky_enamel": True,
        "acid_exposure": True,
    },
    optional_features={
        "multiple_teeth_affected": True,
        "cold_sensitivity": True,
        "tooth_discoloration": True,
    },
    negative_features={
        "since_childhood": True,
        "old_filling": True,
    },
    discriminators=[
        "bo'rsimon, mo'rt, to'kiluvchan emal",
        "kislota/kasbiy yoki kimyoviy ta'sir",
        "tez progressiv yo'qotish",
    ],
    red_flags=[
        "tez yemirilish",
        "pulpa zararlanishi",
    ],
)

dentin_hypersensitivity = Disease(
    id="dentin_hypersensitivity",
    name_uz="Tish gipersensitivligi (sezuvchanlik)",
    name_ru="Гиперестезия (гиперчувствительность) зубов",
    name_en="Dentin hypersensitivity",
    category="tooth",
    core_features={
        "cold_sensitivity": True,
        "cold_short": True,
    },
    optional_features={
        "sweet_sensitivity": True,
        "gum_recession": True,
        "wedge_defect": True,
    },
    negative_features={
        "cavity_visible": True,
        "spontaneous_pain": True,
        "night_pain": True,
    },
    discriminators=[
        "qisqa, o'tkir og'riq (sovuq/shirin/teginish)",
        "ko'rinarli kovak yo'q",
        "ko'pincha ochiq tish bo'yni bilan",
    ],
    red_flags=[
        "og'riqning uzoq davom etishi (pulpitga shubha)",
    ],
)

dentin_dysplasia = Disease(
    id="dentin_dysplasia",
    name_uz="Dentin displaziyasi",
    name_ru="Дисплазия дентина",
    name_en="Dentin dysplasia",
    category="tooth",
    core_features={
        "family_history": True,
        "since_childhood": True,
        "tooth_mobility": True,
    },
    optional_features={
        "multiple_teeth_affected": True,
        "abnormal_tooth_color": True,
    },
    negative_features={
        "cavity_visible": True,
        "acid_exposure": True,
        "occlusal_wear": True,
    },
    discriminators=[
        "nasliy, tug'ma holat",
        "ildizlar kalta — tish harakatchan",
        "erta tish yo'qotish xavfi",
    ],
    red_flags=[
        "tishlarning erta tushishi",
    ],
)

amelogenesis_imperfecta = Disease(
    id="amelogenesis_imperfecta",
    name_uz="Amelogenez imperfecta",
    name_ru="Несовершенный амелогенез",
    name_en="Amelogenesis imperfecta",
    category="tooth",
    core_features={
        "family_history": True,
        "since_childhood": True,
        "enamel_pits": True,
    },
    optional_features={
        "multiple_teeth_affected": True,
        "cold_sensitivity": True,
        "abnormal_tooth_color": True,
    },
    negative_features={
        "cavity_visible": True,
        "acid_exposure": True,
    },
    discriminators=[
        "nasliy emal nuqsoni",
        "emal yupqa/g'adir-budur, barcha tishlarda",
        "tug'ma, oilada uchraydi",
    ],
    red_flags=[
        "emalning ko'chib tushishi",
        "tez yeyilish",
    ],
)

dentinogenesis_imperfecta = Disease(
    id="dentinogenesis_imperfecta",
    name_uz="Dentinogenez imperfecta",
    name_ru="Несовершенный дентиногенез",
    name_en="Dentinogenesis imperfecta",
    category="tooth",
    core_features={
        "family_history": True,
        "since_childhood": True,
        "abnormal_tooth_color": True,
    },
    optional_features={
        "occlusal_wear": True,
        "multiple_teeth_affected": True,
    },
    negative_features={
        "cavity_visible": True,
        "enamel_pits": True,
    },
    discriminators=[
        "nasliy dentin nuqsoni",
        "opal (kulrang-ko'k/jigarrang) shaffof tishlar",
        "emal ko'chadi, tez yeyiladi",
    ],
    red_flags=[
        "tish bo'yi tez yo'qolishi",
        "tish sinishi",
    ],
)

# ═════════════════════════════════════════════════════════════════
#  3. PULPA KASALLIKLARI
# ═════════════════════════════════════════════════════════════════

acute_pulpitis_focal = Disease(
    id="acute_pulpitis_focal",
    name_uz="O'tkir o'choqli pulpit",
    name_ru="Острый очаговый пульпит",
    name_en="Acute focal pulpitis",
    category="pulp",
    core_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "pain_attacks": True,
    },
    optional_features={
        "cold_prolonged": True,
        "localized_pain": True,
        "hot_increases_pain": True,
    },
    negative_features={
        "percussion_pain": True,
        "gum_swelling": True,
        "irradiation": True,
    },
    discriminators=[
        "spontan, qisqa xurujli og'riq",
        "tunda kuchayadi, og'riqsiz oraliqlar uzun",
        "og'riq aniq bir tishda lokal",
    ],
    red_flags=[
        "og'riq xurujlari uzayishi (diffuz pulpitga o'tish)",
        "issiqdan keskin kuchayish",
    ],
)

acute_pulpitis_diffuse = Disease(
    id="acute_pulpitis_diffuse",
    name_uz="O'tkir diffuz pulpit",
    name_ru="Острый диффузный пульпит",
    name_en="Acute diffuse pulpitis",
    category="pulp",
    core_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "irradiation": True,
    },
    optional_features={
        "hot_increases_pain": True,
        "cold_relieves_pain": True,
        "pain_attacks": True,
        "severe_pain": True,
    },
    negative_features={
        "percussion_pain": True,
        "localized_pain": True,
    },
    discriminators=[
        "kuchli, uzluksizga yaqin og'riq",
        "quloq/chakka/bo'yinga tarqaladi",
        "qaysi tish ekanini aniqlash qiyin",
    ],
    red_flags=[
        "yuz shishi",
        "isitma",
        "chidab bo'lmas og'riq",
    ],
)

chronic_pulpitis_fibrous = Disease(
    id="chronic_pulpitis_fibrous",
    name_uz="Surunkali fibroz pulpit",
    name_ru="Хронический фиброзный пульпит",
    name_en="Chronic fibrous pulpitis",
    category="pulp",
    core_features={
        "cold_prolonged": True,
        "cavity_visible": True,
    },
    optional_features={
        "dull_ache": True,
        "pain_triggered": True,
        "bad_smell": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "percussion_pain": True,
    },
    discriminators=[
        "stimuldan keyin og'riq uzoq qoladi",
        "og'riq kuchsiz, bo'g'iq",
        "kuchli spontan og'riq yo'q",
    ],
    red_flags=[
        "spontan og'riq paydo bo'lishi",
        "og'riq kuchayishi",
    ],
)

chronic_pulpitis_hypertrophic = Disease(
    id="chronic_pulpitis_hypertrophic",
    name_uz="Surunkali gipertrofik pulpit",
    name_ru="Хронический гипертрофический пульпит",
    name_en="Chronic hypertrophic pulpitis",
    category="pulp",
    core_features={
        "pulp_polyp": True,
        "bleeding_on_chewing": True,
    },
    optional_features={
        "no_pain": True,
        "cavity_visible": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "percussion_pain": True,
    },
    discriminators=[
        "kavakda pulpa polipi (go'shtsimon o'siq)",
        "chaynaganda qonash",
        "kuchli og'riq yo'q",
    ],
    red_flags=[
        "infeksiya qo'shilishi",
        "og'riq paydo bo'lishi",
    ],
)

chronic_pulpitis_gangrenous = Disease(
    id="chronic_pulpitis_gangrenous",
    name_uz="Surunkali gangrenoz pulpit",
    name_ru="Хронический гангренозный пульпит",
    name_en="Chronic gangrenous pulpitis",
    category="pulp",
    core_features={
        "bad_smell": True,
        "tooth_discoloration": True,
        "hot_increases_pain": True,
    },
    optional_features={
        "cold_prolonged": True,
        "dull_ache": True,
        "cavity_visible": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "percussion_pain": True,
    },
    discriminators=[
        "og'izda yomon hid",
        "issiqdan kuchayuvchi bo'g'iq og'riq",
        "tish rangi qoraygan",
    ],
    red_flags=[
        "periapikal asoratlar",
        "og'riq kuchayishi",
    ],
)

pulp_necrosis = Disease(
    id="pulp_necrosis",
    name_uz="Pulpa nekrozi",
    name_ru="Некроз пульпы",
    name_en="Pulp necrosis",
    category="pulp",
    core_features={
        "no_sensitivity": True,
        "tooth_discoloration": True,
    },
    optional_features={
        "no_pain": True,
        "bad_smell": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "cold_short": True,
        "cold_prolonged": True,
    },
    discriminators=[
        "tish sovuq/issiqqa umuman javob bermaydi",
        "tish rangi o'zgargan (devital)",
        "og'riq odatda yo'q",
    ],
    red_flags=[
        "perkussiya og'rig'i (periodontitga o'tish)",
    ],
)

# ═════════════════════════════════════════════════════════════════
#  PERIAPIKAL KASALLIKLAR (3-kategoriya — keyingi bosqichda qayta tuziladi)
#  Hozircha o'zgarishsiz saqlanadi (regressiyaning oldini olish uchun).
# ═════════════════════════════════════════════════════════════════

acute_apical_periodontitis = Disease(
    id="acute_apical_periodontitis",
    name_uz="O'tkir apikal periodontit",
    name_ru="Острый апикальный периодонтит",
    name_en="Acute apical periodontitis",
    category="periapical",
    core_features={
        "percussion_pain": True,
        "localized_pain": True,
        "pressure_pain": True,
    },
    optional_features={
        "spontaneous_pain": True,
        "gum_swelling": True,
        "bad_smell": True,
    },
    negative_features={
        "cold_short": True,
        "night_pain": True,
    },
    discriminators=[
        "bosimda kuchli og'riq",
        "tishni aniq ko'rsata oladi",
        "perkussiyada keskin og'riq",
    ],
    red_flags=[
        "yuz shishi",
        "isitma",
        "limfa tugunlari kattalashuvi",
    ],
)

chronic_apical_periodontitis_fibrous = Disease(
    id="chronic_apical_periodontitis_fibrous",
    name_uz="Surunkali apikal periodontit – fibroz",
    name_ru="Хронический апикальный периодонтит – фиброзный",
    name_en="Chronic apical periodontitis – fibrous",
    category="periapical",
    core_features={
        "no_pain": True,
        "tooth_discoloration": True,
    },
    optional_features={
        "dull_ache": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "percussion_pain": True,
        "gum_swelling": True,
    },
    discriminators=[
        "deyarli simptomsiz",
        "devital tish",
        "rentgenda o'zgarish",
    ],
    red_flags=[
        "og'riq paydo bo'lishi",
    ],
)

periapical_granuloma = Disease(
    id="periapical_granuloma",
    name_uz="Periapikal granuloma",
    name_ru="Периапикальная гранулёма",
    name_en="Periapical granuloma",
    category="periapical",
    core_features={
        "tooth_discoloration": True,
        "no_pain": True,
    },
    optional_features={
        "dull_ache": True,
        "fistula": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "night_pain": True,
    },
    discriminators=[
        "simptomlar kam",
        "devital tish",
        "periapikal o'choq",
    ],
    red_flags=[
        "abscessga o'tish",
        "fistula paydo bo'lishi",
    ],
)

periapical_abscess = Disease(
    id="periapical_abscess",
    name_uz="Periapikal abscess",
    name_ru="Периапикальный абсцесс",
    name_en="Periapical abscess",
    category="periapical",
    core_features={
        "spontaneous_pain": True,
        "percussion_pain": True,
        "gum_swelling": True,
    },
    optional_features={
        "fever": True,
        "bad_smell": True,
        "fistula": True,
        "irradiation": True,
    },
    negative_features={},
    discriminators=[
        "kuchli doimiy og'riq",
        "shish va yiring",
        "perkussiyada keskin og'riq",
    ],
    red_flags=[
        "yuz shishi",
        "isitma",
        "limfadenit",
        "trizm",
    ],
)

radicular_cyst = Disease(
    id="radicular_cyst",
    name_uz="Radikulyar kista",
    name_ru="Радикулярная киста",
    name_en="Radicular cyst",
    category="periapical",
    core_features={
        "no_pain": True,
        "tooth_discoloration": True,
    },
    optional_features={
        "pressure_sensation": True,
        "gum_swelling": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "percussion_pain": True,
        "fever": True,
    },
    discriminators=[
        "uzoq vaqt simptomsiz",
        "sekin kattalashish",
        "aniq chegaralangan o'choq",
    ],
    red_flags=[
        "infeksiya qo'shilishi",
        "suyak deformatsiyasi",
    ],
)

# ═════════════════════════════════════════════════════════════════
#  EXPORT
# ═════════════════════════════════════════════════════════════════
CARIES_DISEASES = [
    white_spot,
    superficial_caries,
    medium_caries,
    deep_caries,
    secondary_caries,
]

NON_CARIOUS_DISEASES = [
    enamel_hypoplasia,
    enamel_aplasia,
    dental_fluorosis,
    tooth_erosion,
    attrition,
    abrasion,
    abfraction,
    hard_tissue_necrosis,
    dentin_hypersensitivity,
    dentin_dysplasia,
    amelogenesis_imperfecta,
    dentinogenesis_imperfecta,
]

# Hard-tissue (qattiq to'qima) — 1-kategoriya
TOOTH_DISEASES = CARIES_DISEASES + NON_CARIOUS_DISEASES

PULP_DISEASES = [
    acute_pulpitis_focal,
    acute_pulpitis_diffuse,
    chronic_pulpitis_fibrous,
    chronic_pulpitis_hypertrophic,
    chronic_pulpitis_gangrenous,
    pulp_necrosis,
]

# Periapikal kasalliklar (3-kategoriya) — hozircha asl holatida saqlanadi,
# keyingi bosqichda qayta tuziladi.
PERIAPICAL_DISEASES = [
    acute_apical_periodontitis,
    chronic_apical_periodontitis_fibrous,
    periapical_granuloma,
    periapical_abscess,
    radicular_cyst,
]

# Foydalanuvchi "tishda og'riq" deganda barcha tish kasalliklari
# (karies + nokarioz + pulpa + periapikal) bitta guruhda ko'rib chiqiladi.
ALL_TOOTH_DISEASES = TOOTH_DISEASES + PULP_DISEASES + PERIAPICAL_DISEASES
