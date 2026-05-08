from medical.disease_model import Disease

# ─────────────────────────────────────────────
#  5. OG'IZ SHILLIQ QAVATI KASALLIKLARI
# ─────────────────────────────────────────────

aphthous_stomatitis = Disease(
    id="aphthous_stomatitis",
    name_uz="Aftoz stomatit",
    name_ru="Афтозный стоматит",
    name_en="Aphthous stomatitis",
    category="mucosa",
    core_features={
        "ulcer": True,
        "pain": True,
        "white_center_red_halo": True,
    },
    optional_features={
        "recurrent": True,
        "stress_trigger": True,
    },
    negative_features={
        "fever": True,
        "blisters": True,
        "white_patch": True,
    },
    discriminators=[
        "og'riqli afta",
        "oq markaz + qizil halqa",
        "isitmasiz kechadi",
    ],
    red_flags=[
        "2 haftadan ortiq bitmaydi",
        "kattalashib boryapti",
    ],
)

herpetic_stomatitis = Disease(
    id="herpetic_stomatitis",
    name_uz="Gerpetik stomatit",
    name_ru="Герпетический стоматит",
    name_en="Herpetic stomatitis",
    category="mucosa",
    core_features={
        "blisters": True,
        "fever": True,
        "multiple_lesions": True,
    },
    optional_features={
        "lymph_nodes": True,
        "general_weakness": True,
        "recurrent": True,
    },
    negative_features={
        "white_patch": True,
        "no_fever": True,
    },
    discriminators=[
        "ko'p pufakchalar",
        "isitma bilan boshlanadi",
        "diffuz zararlanish",
    ],
    red_flags=[
        "yuqori isitma",
        "ovqat yeyolmaslik",
        "suvsizlanish",
    ],
)

oral_candidiasis = Disease(
    id="oral_candidiasis",
    name_uz="Oral kandidiaz",
    name_ru="Оральный кандидоз",
    name_en="Oral candidiasis",
    category="mucosa",
    core_features={
        "white_patch": True,
        "removable_patch": True,
    },
    optional_features={
        "burning": True,
        "dry_mouth": True,
        "antibiotic_history": True,
    },
    negative_features={
        "fever": True,
        "blisters": True,
        "ulcer": True,
    },
    discriminators=[
        "oq qatlam artib tushadi",
        "ostida qizil yuzasi",
        "achishish hissi",
    ],
    red_flags=[
        "keng tarqalishi",
        "davoga javob bermaslik",
    ],
)

catarrhal_stomatitis = Disease(
    id="catarrhal_stomatitis",
    name_uz="Kataral stomatit",
    name_ru="Катаральный стоматит",
    name_en="Catarrhal stomatitis",
    category="mucosa",
    core_features={
        "redness": True,
        "swelling_mucosa": True,
    },
    optional_features={
        "pain": True,
        "bad_smell": True,
        "dry_mouth": True,
    },
    negative_features={
        "ulcer": True,
        "blisters": True,
        "white_patch": True,
    },
    discriminators=[
        "shilliq qavat qizargan",
        "og'riq minimal",
        "yara yo'q",
    ],
    red_flags=[
        "yara paydo bo'lishi",
        "isitma",
    ],
)

traumatic_stomatitis = Disease(
    id="traumatic_stomatitis",
    name_uz="Travmatik stomatit",
    name_ru="Травматический стоматит",
    name_en="Traumatic stomatitis",
    category="mucosa",
    core_features={
        "ulcer": True,
        "trauma_history": True,
    },
    optional_features={
        "pain": True,
        "localized": True,
    },
    negative_features={
        "fever": True,
        "multiple_lesions": True,
        "recurrent": True,
    },
    discriminators=[
        "travma keyin paydo bo'lgan",
        "bitta yara",
        "aniq sabab bor",
    ],
    red_flags=[
        "yara bitmayapti",
        "kattalashib boryapti",
    ],
)

leukoplakia = Disease(
    id="leukoplakia",
    name_uz="Leykoplakiya",
    name_ru="Лейкоплакия",
    name_en="Leukoplakia",
    category="mucosa",
    core_features={
        "white_patch": True,
        "non_removable": True,
    },
    optional_features={
        "smoking_history": True,
        "no_pain": True,
    },
    negative_features={
        "removable_patch": True,
        "fever": True,
        "blisters": True,
    },
    discriminators=[
        "oq dog' artib tushmaydigan",
        "chegaralangan o'choq",
        "og'riq odatda yo'q",
    ],
    red_flags=[
        "tezkor o'sish",
        "qizarish qo'shilishi (eritroplakiya)",
        "yara paydo bo'lishi",
    ],
)

oral_lichen_planus = Disease(
    id="oral_lichen_planus",
    name_uz="Oral lixen planus",
    name_ru="Красный плоский лишай полости рта",
    name_en="Oral lichen planus",
    category="mucosa",
    core_features={
        "white_lacy_pattern": True,
        "bilateral": True,
    },
    optional_features={
        "pain": True,
        "burning": True,
        "erosion": True,
    },
    negative_features={
        "removable_patch": True,
        "fever": True,
        "blisters": True,
    },
    discriminators=[
        "to'r shaklidagi oq chiziqlar",
        "ikki tomonlama",
        "yonoq ichida ko'proq",
    ],
    red_flags=[
        "eroziv shakl",
        "tez o'zgarish",
    ],
)

# ─────────────────────────────────────────────
#  EXPORT
# ─────────────────────────────────────────────
MUCOSA_DISEASES = [
    aphthous_stomatitis,
    herpetic_stomatitis,
    oral_candidiasis,
    catarrhal_stomatitis,
    traumatic_stomatitis,
    leukoplakia,
    oral_lichen_planus,
]
