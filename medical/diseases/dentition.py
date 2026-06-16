"""
9 va 10-kategoriya — Tish chiqishi/rivojlanish anomaliyalari va
ortodontik kasalliklar (malokluziyalar).

Eslatma: shakl anomaliyalari (geminatsiya/fuziya/konkressensiya/taurodontizm)
va ba'zi joylashish/oraliq holatlari klinik jihatdan deyarli bir xil ko'rinadi
va aniq farqlash uchun rentgen talab qiladi — bot ularni muqobil variant
sifatida ko'rsatishi mumkin.
"""

from medical.disease_model import Disease

# ─────────────────────────────────────────────
#  SON ANOMALIYALARI
# ─────────────────────────────────────────────

adentia_complete = Disease(
    id="adentia_complete",
    name_uz="Adentiya (to'liq tishsizlik)",
    name_ru="Адентия (полное отсутствие зубов)",
    name_en="Complete adentia",
    category="dentition",
    core_features={
        "all_teeth_missing": True,
        "teeth_missing_congenital": True,
    },
    optional_features={
        "family_history": True,
        "since_childhood": True,
    },
    negative_features={
        "extra_teeth": True,
    },
    discriminators=[
        "tishlarning tug'ma to'liq yo'qligi",
        "ko'pincha tizimli sindromlar bilan",
    ],
    red_flags=[
        "boshqa ektodermal nuqsonlar bilan birga kelishi",
    ],
)

oligodontia = Disease(
    id="oligodontia",
    name_uz="Oligodontiya",
    name_ru="Олигодонтия",
    name_en="Oligodontia",
    category="dentition",
    core_features={
        "teeth_missing_congenital": True,
        "many_teeth_missing": True,
    },
    optional_features={
        "family_history": True,
        "since_childhood": True,
    },
    negative_features={
        "all_teeth_missing": True,
        "extra_teeth": True,
    },
    discriminators=[
        "oltidan ortiq tishning tug'ma yo'qligi",
        "ko'pincha nasliy",
    ],
    red_flags=[
        "chaynash va nutq buzilishi",
    ],
)

hypodontia = Disease(
    id="hypodontia",
    name_uz="Gipodontiya",
    name_ru="Гиподонтия",
    name_en="Hypodontia",
    category="dentition",
    core_features={
        "teeth_missing_congenital": True,
    },
    optional_features={
        "family_history": True,
        "spacing_gaps": True,
    },
    negative_features={
        "many_teeth_missing": True,
        "all_teeth_missing": True,
        "extra_teeth": True,
    },
    discriminators=[
        "bir nechta (1-5) tishning tug'ma yo'qligi",
        "ko'pincha lateral kesuv yoki premolyar",
    ],
    red_flags=[
        "tish qatorida bo'shliqlar",
    ],
)

hyperdontia = Disease(
    id="hyperdontia",
    name_uz="Giperodontiya (ortiqcha tishlar)",
    name_ru="Гипердонтия (сверхкомплектные зубы)",
    name_en="Hyperdontia (supernumerary teeth)",
    category="dentition",
    core_features={
        "extra_teeth": True,
    },
    optional_features={
        "teeth_crowded": True,
        "tooth_wrong_position": True,
    },
    negative_features={
        "teeth_missing_congenital": True,
        "all_teeth_missing": True,
    },
    discriminators=[
        "ortiqcha (sverkomplekt) tishlar",
        "ko'pincha old qism (meziodens)",
    ],
    red_flags=[
        "qo'shni tishlar chiqishiga to'sqinlik",
    ],
)

# ─────────────────────────────────────────────
#  SHAKL ANOMALIYALARI (rentgen bilan farqlanadi)
# ─────────────────────────────────────────────

gemination = Disease(
    id="gemination",
    name_uz="Geminatsiya",
    name_ru="Геминация",
    name_en="Gemination",
    category="dentition",
    core_features={
        "abnormal_tooth_shape": True,
        "since_childhood": True,
    },
    optional_features={
        "family_history": True,
    },
    negative_features={
        "extra_teeth": True,
        "teeth_missing_congenital": True,
        "spacing_gaps": True,
    },
    discriminators=[
        "bitta kurtak bo'linib, ikki tojga o'xshash tish",
        "tishlar soni normal qoladi",
    ],
    red_flags=[],
)

fusion = Disease(
    id="fusion",
    name_uz="Fuziya (tishlar qo'shilishi)",
    name_ru="Слияние зубов (фузия)",
    name_en="Fusion",
    category="dentition",
    core_features={
        "abnormal_tooth_shape": True,
        "teeth_missing_congenital": True,
    },
    optional_features={
        "since_childhood": True,
    },
    negative_features={
        "extra_teeth": True,
    },
    discriminators=[
        "ikki tish bitta bo'lib qo'shilgan",
        "tishlar soni kamayganga o'xshaydi",
    ],
    red_flags=[],
)

concrescence = Disease(
    id="concrescence",
    name_uz="Konkressensiya",
    name_ru="Конкресценция",
    name_en="Concrescence",
    category="dentition",
    core_features={
        "abnormal_tooth_shape": True,
    },
    optional_features={
        "since_childhood": True,
    },
    negative_features={
        "extra_teeth": True,
        "teeth_missing_congenital": True,
        "spacing_gaps": True,
        "family_history": True,
    },
    discriminators=[
        "tojlar alohida, lekin ildizlar sement bilan qo'shilgan",
        "asosan rentgenda aniqlanadi",
    ],
    red_flags=[],
)

taurodontism = Disease(
    id="taurodontism",
    name_uz="Taurodontizm",
    name_ru="Тауродонтизм",
    name_en="Taurodontism",
    category="dentition",
    core_features={
        "abnormal_tooth_shape": True,
        "family_history": True,
    },
    optional_features={
        "since_childhood": True,
    },
    negative_features={
        "extra_teeth": True,
        "teeth_missing_congenital": True,
        "spacing_gaps": True,
    },
    discriminators=[
        "kattalashgan pulpa kamerasi, kalta ildizlar",
        "faqat rentgenda ko'rinadi",
    ],
    red_flags=[],
)

# ─────────────────────────────────────────────
#  JOYLASHISH ANOMALIYALARI
# ─────────────────────────────────────────────

distopia = Disease(
    id="distopia",
    name_uz="Distopiya (noto'g'ri joylashuv)",
    name_ru="Дистопия",
    name_en="Distopia",
    category="dentition",
    core_features={
        "tooth_wrong_position": True,
        "teeth_crowded": True,
    },
    optional_features={
        "since_childhood": True,
    },
    negative_features={
        "extra_teeth": True,
        "retained_tooth": True,
        "all_teeth_missing": True,
    },
    discriminators=[
        "tish noto'g'ri joyda/burchakda joylashgan",
        "ko'pincha joy yetishmovchiligi bilan",
    ],
    red_flags=[
        "qo'shni tishlarga bosim",
    ],
)

tooth_retention = Disease(
    id="tooth_retention",
    name_uz="Retensiya (chiqmagan tish)",
    name_ru="Ретенция зуба",
    name_en="Tooth retention",
    category="dentition",
    core_features={
        "retained_tooth": True,
        "no_pain": True,
    },
    optional_features={
        "pressure_sensation": True,
    },
    negative_features={
        "tooth_wrong_position": True,
        "extra_teeth": True,
        "spacing_gaps": True,
    },
    discriminators=[
        "tish suyak/milk ichida qolib, chiqmagan",
        "ko'pincha aql tishi yoki qoziq tish",
    ],
    red_flags=[
        "follikulyar kista shakllanishi",
        "qo'shni ildiz rezorbsiyasi",
    ],
)

ectopic_eruption = Disease(
    id="ectopic_eruption",
    name_uz="Ektopik chiqish",
    name_ru="Эктопическое прорезывание",
    name_en="Ectopic eruption",
    category="dentition",
    core_features={
        "tooth_wrong_position": True,
    },
    optional_features={
        "since_childhood": True,
    },
    negative_features={
        "teeth_crowded": True,
        "extra_teeth": True,
        "retained_tooth": True,
    },
    discriminators=[
        "tish odatdagi yo'ldan tashqarida chiqib kelyapti",
        "qo'shni tish ildiziga zarar berishi mumkin",
    ],
    red_flags=[
        "qo'shni tish ildizining rezorbsiyasi",
    ],
)

# ─────────────────────────────────────────────
#  ORTODONTIK (MALOKLUZIYALAR)
# ─────────────────────────────────────────────

distal_occlusion = Disease(
    id="distal_occlusion",
    name_uz="Distal okklyuziya (II klass)",
    name_ru="Дистальная окклюзия (II класс)",
    name_en="Distal occlusion (Class II)",
    category="dentition",
    core_features={
        "upper_teeth_protrude": True,
    },
    optional_features={
        "deep_overbite": True,
        "since_childhood": True,
    },
    negative_features={
        "lower_jaw_protrudes": True,
        "front_teeth_no_contact": True,
    },
    discriminators=[
        "yuqori tishlar/jag' oldinga chiqqan",
        "pastki jag' orqaroqda",
    ],
    red_flags=[],
)

mesial_occlusion = Disease(
    id="mesial_occlusion",
    name_uz="Mezial okklyuziya (III klass)",
    name_ru="Мезиальная окклюзия (III класс)",
    name_en="Mesial occlusion (Class III)",
    category="dentition",
    core_features={
        "lower_jaw_protrudes": True,
    },
    optional_features={
        "crossbite": True,
        "since_childhood": True,
    },
    negative_features={
        "upper_teeth_protrude": True,
        "deep_overbite": True,
    },
    discriminators=[
        "pastki jag'/tishlar oldinga chiqqan",
        "teskari old tishlash",
    ],
    red_flags=[],
)

deep_bite = Disease(
    id="deep_bite",
    name_uz="Chuqur tishlash",
    name_ru="Глубокий прикус",
    name_en="Deep bite",
    category="dentition",
    core_features={
        "deep_overbite": True,
    },
    optional_features={
        "upper_teeth_protrude": True,
    },
    negative_features={
        "front_teeth_no_contact": True,
        "lower_jaw_protrudes": True,
    },
    discriminators=[
        "yuqori old tishlar pastkilarini ortiqcha qoplaydi",
    ],
    red_flags=[
        "milk travmasi (pastki tishlardan)",
    ],
)

open_bite = Disease(
    id="open_bite",
    name_uz="Ochiq tishlash",
    name_ru="Открытый прикус",
    name_en="Open bite",
    category="dentition",
    core_features={
        "front_teeth_no_contact": True,
    },
    optional_features={
        "since_childhood": True,
    },
    negative_features={
        "deep_overbite": True,
    },
    discriminators=[
        "tishlar yopilganda old qismda ochiq oraliq",
        "ko'pincha til/barmoq so'rish odati bilan",
    ],
    red_flags=[
        "chaynash va nutq buzilishi",
    ],
)

crossbite = Disease(
    id="crossbite",
    name_uz="Kross-bayt (kesishgan tishlash)",
    name_ru="Перекрёстный прикус",
    name_en="Crossbite",
    category="dentition",
    core_features={
        "crossbite": True,
    },
    optional_features={
        "since_childhood": True,
    },
    negative_features={
        "deep_overbite": True,
        "front_teeth_no_contact": True,
        "upper_teeth_protrude": True,
    },
    discriminators=[
        "pastki tishlar yuqori tishlardan tashqarida yopiladi",
        "bir yoki ikki tomonlama bo'lishi mumkin",
    ],
    red_flags=[
        "yuz assimetriyasi",
    ],
)

dental_crowding = Disease(
    id="dental_crowding",
    name_uz="Tish qatori torayishi (skuchennost)",
    name_ru="Скученность зубов (сужение ряда)",
    name_en="Dental crowding",
    category="dentition",
    core_features={
        "teeth_crowded": True,
    },
    optional_features={
        "tooth_wrong_position": True,
    },
    negative_features={
        "spacing_gaps": True,
        "extra_teeth": True,
    },
    discriminators=[
        "tishlarga joy yetishmaydi — qiyshiq, zich",
        "tish qatorining torayishi",
    ],
    red_flags=[
        "gigiyena qiyinlashishi va karies xavfi",
    ],
)

diastema = Disease(
    id="diastema",
    name_uz="Diastema (old tishlar orasidagi yoriq)",
    name_ru="Диастема",
    name_en="Diastema",
    category="dentition",
    core_features={
        "spacing_gaps": True,
    },
    optional_features={
        "teeth_missing_congenital": True,
    },
    negative_features={
        "teeth_crowded": True,
        "upper_teeth_protrude": True,
    },
    discriminators=[
        "old (markaziy) tishlar orasidagi bo'shliq",
        "frenulum yoki tish o'lchami bilan bog'liq",
    ],
    red_flags=[],
)

tremas = Disease(
    id="tremas",
    name_uz="Tremalar (tishlar orasidagi bo'shliqlar)",
    name_ru="Тремы",
    name_en="Tremas (spacing)",
    category="dentition",
    core_features={
        "spacing_gaps": True,
        "since_childhood": True,
    },
    optional_features={
        "teeth_missing_congenital": True,
    },
    negative_features={
        "teeth_crowded": True,
        "upper_teeth_protrude": True,
    },
    discriminators=[
        "bir nechta tishlar orasidagi bo'shliqlar",
        "ko'pincha tish-jag' o'lchami nomutanosibligi",
    ],
    red_flags=[],
)

# ─────────────────────────────────────────────
#  EXPORT
# ─────────────────────────────────────────────
DENTITION_DISEASES = [
    adentia_complete,
    oligodontia,
    hypodontia,
    hyperdontia,
    gemination,
    fusion,
    concrescence,
    taurodontism,
    distopia,
    tooth_retention,
    ectopic_eruption,
    distal_occlusion,
    mesial_occlusion,
    deep_bite,
    open_bite,
    crossbite,
    dental_crowding,
    diastema,
    tremas,
]
