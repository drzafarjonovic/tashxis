from medical.disease_model import Disease

# ─────────────────────────────────────────────
#  4. PERIODONTAL KASALLIKLAR
# ─────────────────────────────────────────────

gingivitis_catarrhal = Disease(
    id="gingivitis_catarrhal",
    name_uz="Kataral gingivit",
    name_ru="Катаральный гингивит",
    name_en="Catarrhal gingivitis",
    category="periodontal",
    core_features={
        "gum_bleeding": True,
        "gum_swelling": True,
        "gum_redness": True,
    },
    optional_features={
        "bad_smell": True,
        "no_bone_loss": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "tooth_mobility": True,
        "periodontal_pocket": True,
    },
    discriminators=[
        "milkdan qonash",
        "shish va giperemiya",
        "suyak rezorbsiyasi yo'q",
    ],
    red_flags=[
        "qonash kuchayishi",
        "periodontitga o'tish belgilari",
    ],
)

gingivitis_hypertrophic = Disease(
    id="gingivitis_hypertrophic",
    name_uz="Gipertrofik gingivit",
    name_ru="Гипертрофический гингивит",
    name_en="Hypertrophic gingivitis",
    category="periodontal",
    core_features={
        "gum_enlargement": True,
        "gum_bleeding": True,
    },
    optional_features={
        "bad_smell": True,
        "gum_redness": True,
    },
    negative_features={
        "spontaneous_pain": True,
        "tooth_mobility": True,
    },
    discriminators=[
        "milk kattalashgan",
        "qonash",
        "og'riq minimal",
    ],
    red_flags=[
        "kuchli qonash",
        "infeksiya qo'shilishi",
    ],
)

gingivitis_ulcerative = Disease(
    id="gingivitis_ulcerative",
    name_uz="Yarali-nekrotik gingivit (Vinsent)",
    name_ru="Язвенно-некротический гингивит (Венсана)",
    name_en="Ulcerative necrotizing gingivitis (Vincent's)",
    category="periodontal",
    core_features={
        "gum_ulcer": True,
        "bad_smell": True,
        "gum_pain": True,
    },
    optional_features={
        "fever": True,
        "general_weakness": True,
    },
    negative_features={
        "tooth_mobility": True,
    },
    discriminators=[
        "milkda yara",
        "juda yomon hid",
        "kuchli og'riq",
    ],
    red_flags=[
        "isitma",
        "umumiy holsizlik",
        "tez tarqalishi",
    ],
)

periodontitis_chronic = Disease(
    id="periodontitis_chronic",
    name_uz="Surunkali periodontit",
    name_ru="Хронический периодонтит",
    name_en="Chronic periodontitis",
    category="periodontal",
    core_features={
        "periodontal_pocket": True,
        "tooth_mobility": True,
        "gum_bleeding": True,
    },
    optional_features={
        "bad_smell": True,
        "pressure_pain": True,
        "fistula": True,
    },
    negative_features={
        "no_periodontal_pocket": True,
    },
    discriminators=[
        "periodontal cho'ntak mavjud",
        "tish harakatchanligi",
        "alveolyar suyak rezorbsiyasi",
    ],
    red_flags=[
        "tishlarning tez bo'shashishi",
        "yiring ajralishi",
    ],
)

periodontitis_aggressive = Disease(
    id="periodontitis_aggressive",
    name_uz="Agressiv periodontit",
    name_ru="Агрессивный периодонтит",
    name_en="Aggressive periodontitis",
    category="periodontal",
    core_features={
        "periodontal_pocket": True,
        "tooth_mobility": True,
        "rapid_progression": True,
    },
    optional_features={
        "young_patient": True,
        "gum_bleeding": True,
    },
    negative_features={},
    discriminators=[
        "yosh bemorlarda",
        "tez rivojlanadi",
        "chuqur cho'ntaklar",
    ],
    red_flags=[
        "tezkor suyak yo'qotilishi",
    ],
)

periodontosis = Disease(
    id="periodontosis",
    name_uz="Periodontoz",
    name_ru="Пародонтоз",
    name_en="Periodontosis",
    category="periodontal",
    core_features={
        "gum_recession": True,
        "root_exposure": True,
    },
    optional_features={
        "cold_sensitivity": True,
        "no_inflammation": True,
    },
    negative_features={
        "gum_bleeding": True,
        "gum_swelling": True,
        "periodontal_pocket": True,
    },
    discriminators=[
        "yallig'lanish belgilari yo'q",
        "milk retraksiyasi",
        "suyak atrofiyasi",
    ],
    red_flags=[
        "tish bo'shashishi (kech bosqich)",
    ],
)

periodontal_abscess = Disease(
    id="periodontal_abscess",
    name_uz="Parodontal abscess",
    name_ru="Пародонтальный абсцесс",
    name_en="Periodontal abscess",
    category="periodontal",
    core_features={
        "gum_swelling": True,
        "gum_pain": True,
        "periodontal_pocket": True,
    },
    optional_features={
        "fever": True,
        "fistula": True,
        "bad_smell": True,
    },
    negative_features={},
    discriminators=[
        "milkda abscess",
        "kuchli og'riq",
        "cho'ntakdan yiring",
    ],
    red_flags=[
        "isitma",
        "tez kattalashuvchi shish",
    ],
)

pericoronitis = Disease(
    id="pericoronitis",
    name_uz="Perikoronit",
    name_ru="Перикоронит",
    name_en="Pericoronitis",
    category="periodontal",
    core_features={
        "wisdom_tooth_pain": True,
        "gum_swelling": True,
    },
    optional_features={
        "trismus": True,
        "fever": True,
        "bad_smell": True,
    },
    negative_features={},
    discriminators=[
        "aql tishi sohasida",
        "milk ustidan og'riq",
        "og'iz ochish qiyinlashishi",
    ],
    red_flags=[
        "trismus",
        "yuz shishi",
        "yutish qiyinlashishi",
    ],
)

# ─────────────────────────────────────────────
#  EXPORT
# ─────────────────────────────────────────────
PERIODONTAL_DISEASES = [
    gingivitis_catarrhal,
    gingivitis_hypertrophic,
    gingivitis_ulcerative,
    periodontitis_chronic,
    periodontitis_aggressive,
    periodontosis,
    periodontal_abscess,
    pericoronitis,
]
