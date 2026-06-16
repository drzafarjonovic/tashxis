"""
11-kategoriya — Travmatik shikastlanishlar.

Tish sinishlari (emal / emal-dentin / pulpa ochilishi / ildiz) va
dislokatsiyalar (konkussiya, subluksatsiya, ekstruziya, intruziya, avulsiya).
"""

from medical.disease_model import Disease

# ─────────────────────────────────────────────
#  TISH SINISHLARI
# ─────────────────────────────────────────────

enamel_fracture = Disease(
    id="enamel_fracture",
    name_uz="Emal sinishi",
    name_ru="Перелом эмали",
    name_en="Enamel fracture",
    category="trauma",
    core_features={
        "recent_injury": True,
        "tooth_fractured": True,
        "fracture_enamel_only": True,
    },
    optional_features={
        "no_pain": True,
    },
    negative_features={
        "fracture_dentin": True,
        "pulp_exposed_bleeding": True,
        "tooth_displaced": True,
        "tooth_mobility": True,
    },
    discriminators=[
        "faqat emalning kichik bo'lagi uchgan",
        "og'riq yo'q, dentin ochilmagan",
        "tish qimirlamaydi",
    ],
    red_flags=[
        "keyinchalik rangining o'zgarishi",
    ],
)

enamel_dentin_fracture = Disease(
    id="enamel_dentin_fracture",
    name_uz="Emal-dentin sinishi (asoratsiz)",
    name_ru="Перелом эмали и дентина (без вскрытия пульпы)",
    name_en="Enamel-dentin fracture (uncomplicated)",
    category="trauma",
    core_features={
        "recent_injury": True,
        "tooth_fractured": True,
        "fracture_dentin": True,
    },
    optional_features={
        "cold_sensitivity": True,
    },
    negative_features={
        "pulp_exposed_bleeding": True,
        "fracture_enamel_only": True,
        "tooth_displaced": True,
    },
    discriminators=[
        "siniqda sarg'ish dentin ochilgan",
        "sovuq/havoga sezuvchanlik",
        "nerv (pulpa) ochilmagan",
    ],
    red_flags=[
        "og'riq kuchayishi (pulpa zararlanishi)",
    ],
)

crown_fracture_pulp = Disease(
    id="crown_fracture_pulp",
    name_uz="Pulpa ochilishi bilan toj sinishi (asoratli)",
    name_ru="Перелом коронки со вскрытием пульпы (осложнённый)",
    name_en="Crown fracture with pulp exposure (complicated)",
    category="trauma",
    core_features={
        "recent_injury": True,
        "tooth_fractured": True,
        "pulp_exposed_bleeding": True,
    },
    optional_features={
        "cold_sensitivity": True,
    },
    negative_features={
        "fracture_enamel_only": True,
        "tooth_displaced": True,
    },
    discriminators=[
        "siniqda qizil nuqta/qon (nerv ochiq)",
        "kuchli og'riq",
        "tezkor endodontik yordam zarur",
    ],
    red_flags=[
        "pulpa infeksiyasi/nekrozi xavfi",
        "tezkor stomatolog yordami zarur",
    ],
)

root_fracture = Disease(
    id="root_fracture",
    name_uz="Ildiz sinishi",
    name_ru="Перелом корня",
    name_en="Root fracture",
    category="trauma",
    core_features={
        "recent_injury": True,
        "tooth_mobility": True,
        "tooth_tender_after_injury": True,
    },
    optional_features={
        "tooth_displaced": True,
        "gum_bleeding": True,
    },
    negative_features={
        "tooth_fractured": True,
        "fracture_enamel_only": True,
        "fracture_dentin": True,
        "tooth_avulsed": True,
    },
    discriminators=[
        "toj butun, lekin tish harakatchan/og'riqli",
        "zarbadan keyin yumshoq harakatchanlik",
        "tashxis uchun rentgen zarur",
    ],
    red_flags=[
        "tojning siljishi",
        "tish bo'shashishi",
    ],
)

# ─────────────────────────────────────────────
#  DISLOKATSIYALAR
# ─────────────────────────────────────────────

concussion = Disease(
    id="concussion",
    name_uz="Konkussiya (chayqalish)",
    name_ru="Ушиб зуба (сотрясение)",
    name_en="Concussion",
    category="trauma",
    core_features={
        "recent_injury": True,
        "tooth_tender_after_injury": True,
    },
    optional_features={},
    negative_features={
        "tooth_mobility": True,
        "tooth_displaced": True,
        "tooth_fractured": True,
        "tooth_avulsed": True,
        "tooth_intruded": True,
    },
    discriminators=[
        "zarbadan keyin og'riq (perkussiyaga sezgir)",
        "tish qimirlamaydi va siljimagan",
        "siniq yo'q",
    ],
    red_flags=[
        "keyinchalik rang o'zgarishi (pulpa nekrozi)",
    ],
)

subluxation = Disease(
    id="subluxation",
    name_uz="Subluksatsiya",
    name_ru="Подвывих (сублюксация)",
    name_en="Subluxation",
    category="trauma",
    core_features={
        "recent_injury": True,
        "tooth_mobility": True,
    },
    optional_features={
        "gum_bleeding": True,
        "tooth_tender_after_injury": True,
    },
    negative_features={
        "tooth_displaced": True,
        "tooth_intruded": True,
        "tooth_avulsed": True,
        "tooth_fractured": True,
    },
    discriminators=[
        "tish bo'shashgan, lekin siljimagan",
        "milk yorig'idan qon kelishi mumkin",
        "siniq yo'q",
    ],
    red_flags=[
        "harakatchanlik ortishi",
    ],
)

extrusion = Disease(
    id="extrusion",
    name_uz="Ekstruziya (qisman chiqish)",
    name_ru="Экструзия (частичный вывих)",
    name_en="Extrusion",
    category="trauma",
    core_features={
        "recent_injury": True,
        "tooth_displaced": True,
    },
    optional_features={
        "tooth_mobility": True,
        "gum_bleeding": True,
    },
    negative_features={
        "tooth_intruded": True,
        "tooth_avulsed": True,
        "fracture_enamel_only": True,
    },
    discriminators=[
        "tish katakchadan qisman chiqib, uzunroq ko'rinadi",
        "harakatchan va siljigan",
        "tezkor repozitsiya zarur",
    ],
    red_flags=[
        "pulpa zararlanishi",
        "tezkor stomatolog yordami",
    ],
)

intrusion = Disease(
    id="intrusion",
    name_uz="Intruziya (ichkariga kirish)",
    name_ru="Интрузия (вколоченный вывих)",
    name_en="Intrusion",
    category="trauma",
    core_features={
        "recent_injury": True,
        "tooth_intruded": True,
    },
    optional_features={
        "no_pain": True,
    },
    negative_features={
        "tooth_avulsed": True,
        "tooth_displaced": True,
        "tooth_mobility": True,
    },
    discriminators=[
        "tish suyak ichiga kirib, kaltaroq ko'rinadi",
        "qimirlamaydi (qotgan)",
        "tezkor mutaxassis yordami zarur",
    ],
    red_flags=[
        "doimiy tish kurtagiga zarar (bolalarda)",
        "pulpa nekrozi xavfi",
    ],
)

avulsion = Disease(
    id="avulsion",
    name_uz="Avulsiya (tishning to'liq chiqishi)",
    name_ru="Авульсия (полный вывих зуба)",
    name_en="Avulsion",
    category="trauma",
    core_features={
        "recent_injury": True,
        "tooth_avulsed": True,
    },
    optional_features={
        "gum_bleeding": True,
    },
    negative_features={
        "tooth_fractured": True,
        "tooth_intruded": True,
    },
    discriminators=[
        "tish butunlay o'rnidan chiqib tushgan",
        "katakcha bo'sh",
        "DARHOL reimplantatsiya — vaqt hal qiluvchi",
    ],
    red_flags=[
        "30 daqiqa ichida tishni joyiga qaytarish kerak",
        "tishni sutda/so'lakda saqlab, zudlik bilan stomatologga boring",
    ],
)

# ─────────────────────────────────────────────
#  EXPORT
# ─────────────────────────────────────────────
TRAUMA_DISEASES = [
    enamel_fracture,
    enamel_dentin_fracture,
    crown_fracture_pulp,
    root_fracture,
    concussion,
    subluxation,
    extrusion,
    intrusion,
    avulsion,
]
