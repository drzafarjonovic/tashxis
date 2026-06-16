"""
7-kategoriya — Jag' suyaklari kasalliklari.

Yallig'lanish: periostit, osteit, alveolit (quruq katakcha), osteomiyelit
(o'tkir/surunkali). Kistalar: follikulyar (dentigeroz), keratokista.
(Radikulyar kista periapikal guruhda — 3-kategoriya.)
"""

from medical.disease_model import Disease

# ─────────────────────────────────────────────
#  YALLIG'LANISH
# ─────────────────────────────────────────────

periostitis = Disease(
    id="periostitis",
    name_uz="Periostit (fleyus)",
    name_ru="Периостит (флюс)",
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
        "sequestrum": True,
        "jaw_deformity": True,
    },
    discriminators=[
        "lokal subperiostal shish (fleyus)",
        "sababchi tish mavjud",
        "palpatsiyada og'riq",
    ],
    red_flags=[
        "shish tez kattalashmoqda",
        "isitma oshmoqda",
        "og'iz ochish qiyinlashmoqda",
    ],
)

osteitis = Disease(
    id="osteitis",
    name_uz="Osteit",
    name_ru="Остит",
    name_en="Osteitis",
    category="jaw",
    core_features={
        "recent_extraction": True,
        "dull_ache": True,
    },
    optional_features={
        "bad_smell": True,
        "jaw_swelling": True,
        "lymph_nodes": True,
    },
    negative_features={
        "empty_socket_pain": True,
        "high_fever": True,
        "sequestrum": True,
    },
    discriminators=[
        "suyakning lokal yallig'lanishi",
        "ko'pincha ekstraksiya/infeksiyadan keyin",
        "lokal bo'g'iq og'riq, diffuz emas",
    ],
    red_flags=[
        "osteomiyelitga o'tish",
        "isitma qo'shilishi",
    ],
)

alveolitis = Disease(
    id="alveolitis",
    name_uz="Alveolit (quruq katakcha)",
    name_ru="Альвеолит (сухая лунка)",
    name_en="Alveolitis (dry socket)",
    category="jaw",
    core_features={
        "recent_extraction": True,
        "empty_socket_pain": True,
    },
    optional_features={
        "bad_smell": True,
        "dull_ache": True,
        "lymph_nodes": True,
    },
    negative_features={
        "high_fever": True,
        "jaw_deformity": True,
        "sequestrum": True,
    },
    discriminators=[
        "tish olingandan 3-4 kun keyin kuchaygan og'riq",
        "bo'sh katakcha (qon laxtasi yo'q)",
        "yomon hid",
    ],
    red_flags=[
        "og'riqning tarqalishi",
        "isitma va shish qo'shilishi",
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
    negative_features={
        "slow_growth": True,
    },
    discriminators=[
        "yuqori isitma va intoksikatsiya",
        "kuchli chuqur og'riq, diffuz shish",
        "bir necha tishning harakatchanligi",
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
        "severe_pain": True,
    },
    discriminators=[
        "uzoq davom etgan jarayon",
        "fistula va sekvestr (suyak parchalari)",
        "suyak deformatsiyasi",
    ],
    red_flags=[
        "yuzning o'zgarishi",
        "patologik sinish xavfi",
    ],
)

# ─────────────────────────────────────────────
#  KISTALAR
# ─────────────────────────────────────────────

follicular_cyst = Disease(
    id="follicular_cyst",
    name_uz="Follikulyar (dentigeroz) kista",
    name_ru="Фолликулярная (дентигеронная) киста",
    name_en="Follicular (dentigerous) cyst",
    category="jaw",
    core_features={
        "no_pain": True,
        "retained_tooth": True,
        "slow_growth": True,
    },
    optional_features={
        "jaw_swelling": True,
        "pressure_sensation": True,
    },
    negative_features={
        "fever": True,
        "spontaneous_pain": True,
        "recurrence_history": True,
    },
    discriminators=[
        "chiqmagan (retensiyalangan) tish toji atrofida",
        "uzoq vaqt simptomsiz, sekin kattalashish",
        "rentgenda tish toji bilan bog'liq aniq o'choq",
    ],
    red_flags=[
        "infeksiya qo'shilishi",
        "suyak deformatsiyasi/patologik sinish",
    ],
)

odontogenic_keratocyst = Disease(
    id="odontogenic_keratocyst",
    name_uz="Odontogen keratokista",
    name_ru="Одонтогенная кератокиста",
    name_en="Odontogenic keratocyst",
    category="jaw",
    core_features={
        "slow_growth": True,
        "recurrence_history": True,
    },
    optional_features={
        "jaw_swelling": True,
        "pressure_sensation": True,
        "retained_tooth": True,
    },
    negative_features={
        "fever": True,
        "empty_socket_pain": True,
    },
    discriminators=[
        "suyak bo'ylab tarqalib o'sadi (shishsiz ham)",
        "olib tashlangandan keyin tez-tez qaytalanadi",
        "agressivroq kechishi",
    ],
    red_flags=[
        "tez qaytalanish",
        "keng suyak destruksiyasi",
    ],
)

# ─────────────────────────────────────────────
#  EXPORT
# ─────────────────────────────────────────────
JAW_DISEASES = [
    periostitis,
    osteitis,
    alveolitis,
    osteomyelitis_acute,
    osteomyelitis_chronic,
    follicular_cyst,
    odontogenic_keratocyst,
]
