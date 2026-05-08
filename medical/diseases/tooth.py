from medical.disease_model import Disease

# ─────────────────────────────────────────────
#  1. KARIES GURUHI
# ─────────────────────────────────────────────

white_spot = Disease(
    id="white_spot",
    name_uz="Boshlang'ich karies (oq dog')",
    name_ru="Начальный кариес (белое пятно)",
    name_en="Initial caries (white spot)",
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
    },
    discriminators=[
        "og'riq yo'q",
        "emalda oq dog'",
        "kovak hosil bo'lmagan",
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
    },
    discriminators=[
        "faqat emal zararlangan",
        "qisqa og'riq",
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
        "qisqa og'riq",
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
        "qisqa stimul og'rig'i",
        "perkussiyada og'riq yo'q",
    ],
    red_flags=[
        "spontan og'riq paydo bo'lishi",
        "issiqdan kuchayuvchi og'riq",
    ],
)

secondary_caries = Disease(
    id="secondary_caries",
    name_uz="Ikkilamchi (sekundar) karies",
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
        "qisqa stimul og'rig'i",
    ],
    red_flags=[
        "og'riq kuchayishi",
        "spontan og'riq (pulpitga o'tish)",
    ],
)

# ─────────────────────────────────────────────
#  2. PULPIT GURUHI
# ─────────────────────────────────────────────

acute_pulpitis_serous = Disease(
    id="acute_pulpitis_serous",
    name_uz="O'tkir pulpit – seroz",
    name_ru="Острый пульпит – серозный",
    name_en="Acute pulpitis – serous",
    category="pulp",
    core_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "pain_attacks": True,
    },
    optional_features={
        "cold_prolonged": True,
        "hot_pain": True,
        "irradiation": True,
    },
    negative_features={
        "percussion_pain": True,
        "gum_swelling": True,
    },
    discriminators=[
        "spontan, xurujli og'riq",
        "tunda kuchayadi",
        "sovuqqa uzoq javob",
    ],
    red_flags=[
        "og'riq kuchayib borishi",
        "issiqdan keskin kuchayish",
    ],
)

acute_pulpitis_purulent = Disease(
    id="acute_pulpitis_purulent",
    name_uz="O'tkir pulpit – yiringli",
    name_ru="Острый пульпит – гнойный",
    name_en="Acute pulpitis – purulent",
    category="pulp",
    core_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "hot_increases_pain": True,
        "cold_relieves_pain": True,
    },
    optional_features={
        "irradiation": True,
        "pain_attacks": True,
    },
    negative_features={
        "percussion_pain": True,
    },
    discriminators=[
        "issiqdan kuchayadi",
        "sovuqdan yengillashadi",
        "juda kuchli uzluksiz og'riq",
    ],
    red_flags=[
        "yuz shishi",
        "isitma",
        "chidab bo'lmas og'riq",
    ],
)

chronic_pulpitis_fibrous = Disease(
    id="chronic_pulpitis_fibrous",
    name_uz="Surunkali pulpit – fibroz",
    name_ru="Хронический пульпит – фиброзный",
    name_en="Chronic pulpitis – fibrous",
    category="pulp",
    core_features={
        "pain_triggered": True,
        "cold_short": True,
    },
    optional_features={
        "dull_ache": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "night_pain": True,
        "percussion_pain": True,
    },
    discriminators=[
        "og'riq kuchsiz",
        "stimulusga qisqa javob",
        "spontan og'riq yo'q",
    ],
    red_flags=[
        "og'riq kuchayishi",
        "spontan og'riq paydo bo'lishi",
    ],
)

chronic_pulpitis_gangrenous = Disease(
    id="chronic_pulpitis_gangrenous",
    name_uz="Surunkali pulpit – gangrenoz",
    name_ru="Хронический пульпит – гангренозный",
    name_en="Chronic pulpitis – gangrenous",
    category="pulp",
    core_features={
        "bad_smell": True,
        "tooth_discoloration": True,
        "hot_increases_pain": True,
    },
    optional_features={
        "cold_short": True,
        "dull_ache": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "percussion_pain": True,
    },
    discriminators=[
        "og'izda yomon hid",
        "issiqdan kuchayadi",
        "tish rangi qoraygan",
    ],
    red_flags=[
        "og'riq kuchayishi",
        "periapikal asoratlar",
    ],
)

chronic_pulpitis_hypertrophic = Disease(
    id="chronic_pulpitis_hypertrophic",
    name_uz="Surunkali pulpit – gipertrofik",
    name_ru="Хронический пульпит – гипертрофический",
    name_en="Chronic pulpitis – hypertrophic",
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
        "pulpa polipi mavjud",
        "og'riq yo'q",
        "chaynaganda qonash",
    ],
    red_flags=[
        "infeksiya qo'shilishi",
        "og'riq paydo bo'lishi",
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
        "bad_smell": True,
    },
    optional_features={
        "no_pain": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "cold_short": True,
    },
    discriminators=[
        "tish hech narsaga sezuvchan emas",
        "tish rangi o'zgargan",
        "devital tish",
    ],
    red_flags=[
        "perkussiya og'rig'i (periodontitga o'tish)",
    ],
)

# ─────────────────────────────────────────────
#  3. PERIAPIKAL KASALLIKLAR
# ─────────────────────────────────────────────

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

# ─────────────────────────────────────────────
#  EXPORT
# ─────────────────────────────────────────────
TOOTH_DISEASES = [
    white_spot,
    superficial_caries,
    medium_caries,
    deep_caries,
    secondary_caries,
]

PULP_DISEASES = [
    acute_pulpitis_serous,
    acute_pulpitis_purulent,
    chronic_pulpitis_fibrous,
    chronic_pulpitis_gangrenous,
    chronic_pulpitis_hypertrophic,
    pulp_necrosis,
]

PERIAPICAL_DISEASES = [
    acute_apical_periodontitis,
    chronic_apical_periodontitis_fibrous,
    periapical_granuloma,
    periapical_abscess,
    radicular_cyst,
]

ALL_TOOTH_DISEASES = TOOTH_DISEASES + PULP_DISEASES + PERIAPICAL_DISEASES
