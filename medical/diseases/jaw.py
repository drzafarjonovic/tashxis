from medical.disease_model import Disease

# ─────────────────────────────────────────────
#  6. JAG' SUYAKLARI KASALLIKLARI
# ─────────────────────────────────────────────

periostitis = Disease(
    id="periostitis",
    name_uz="Periostit",
    name_ru="Периостит",
    name_en="Periostitis",
    category="jaw",
    core_features={
        "jaw_swelling": True,
        "spontaneous_pain": True,
        "causative_tooth": True,
    },
    optional_features={
        "fever": True,
        "lymph_nodes": True,
        "trismus": True,
    },
    negative_features={
        "high_fever": True,
        "diffuse_swelling": True,
    },
    discriminators=[
        "lokal shish",
        "sababchi tish mavjud",
        "palpatsiyada og'riq",
    ],
    red_flags=[
        "shish tez kattalashmoqda",
        "isitma oshmoqda",
        "og'iz ochish qiyinlashmoqda",
    ],
)

osteomyelitis_acute = Disease(
    id="osteomyelitis_acute",
    name_uz="O'tkir osteomiyelit",
    name_ru="Острый остеомиелит",
    name_en="Acute osteomyelitis",
    category="jaw",
    core_features={
        "jaw_swelling": True,
        "high_fever": True,
        "severe_pain": True,
        "trismus": True,
    },
    optional_features={
        "lymph_nodes": True,
        "general_weakness": True,
        "pus_discharge": True,
    },
    negative_features={},
    discriminators=[
        "yuqori isitma",
        "kuchli chuqur og'riq",
        "diffuz shish",
    ],
    red_flags=[
        "yuz shishi tez kattalashmoqda",
        "isitma yuqori",
        "og'iz ochilmayapti",
        "yutish qiyin",
    ],
)

osteomyelitis_chronic = Disease(
    id="osteomyelitis_chronic",
    name_uz="Surunkali osteomiyelit",
    name_ru="Хронический остеомиелит",
    name_en="Chronic osteomyelitis",
    category="jaw",
    core_features={
        "fistula": True,
        "jaw_deformity": True,
    },
    optional_features={
        "dull_ache": True,
        "pus_discharge": True,
        "sequestrum": True,
    },
    negative_features={
        "high_fever": True,
        "acute_pain": True,
    },
    discriminators=[
        "uzoq vaqt davom etgan",
        "fistula mavjud",
        "suyak deformatsiyasi",
    ],
    red_flags=[
        "yuzning o'zgarishi",
        "tishlar tushishi",
    ],
)

follicular_cyst = Disease(
    id="follicular_cyst",
    name_uz="Follikulyar kista",
    name_ru="Фолликулярная киста",
    name_en="Follicular cyst",
    category="jaw",
    core_features={
        "no_pain": True,
        "retained_tooth": True,
    },
    optional_features={
        "jaw_swelling": True,
        "pressure_sensation": True,
    },
    negative_features={
        "fever": True,
        "spontaneous_pain": True,
    },
    discriminators=[
        "retensiyalangan tish atrofida",
        "simptomsiz kechishi",
        "sekin kattalashish",
    ],
    red_flags=[
        "infeksiya qo'shilishi",
        "suyak deformatsiyasi",
    ],
)

# ─────────────────────────────────────────────
#  EXPORT
# ─────────────────────────────────────────────
JAW_DISEASES = [
    periostitis,
    osteomyelitis_acute,
    osteomyelitis_chronic,
    follicular_cyst,
]
