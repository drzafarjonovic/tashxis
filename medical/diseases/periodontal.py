"""
4-kategoriya — Parodont (milk va tish atrofi to'qimalari) kasalliklari.

Gingival kasalliklar, parodontitlar (lokal/generalizatsiyalashgan/agressiv),
parodontal absess, periimplantit, parodontoz, gingival retsessiya,
furkatsion shikastlanish, perikoronit.
"""

from medical.disease_model import Disease

# ─────────────────────────────────────────────
#  GINGIVAL KASALLIKLAR
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
        "gum_recession": True,
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
        "gum_recession": True,
    },
    discriminators=[
        "milk kattalashgan (tishni qoplay boshlagan)",
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
        "gum_bleeding": True,
    },
    negative_features={
        "tooth_mobility": True,
        "gum_recession": True,
    },
    discriminators=[
        "milkda yara va nekroz",
        "juda yomon hid",
        "kuchli og'riq",
    ],
    red_flags=[
        "isitma",
        "umumiy holsizlik",
        "tez tarqalishi",
    ],
)

gingivitis_desquamative = Disease(
    id="gingivitis_desquamative",
    name_uz="Deskvamativ gingivit",
    name_ru="Десквамативный гингивит",
    name_en="Desquamative gingivitis",
    category="periodontal",
    core_features={
        "gum_desquamation": True,
        "gum_redness": True,
    },
    optional_features={
        "gum_pain": True,
        "bilateral": True,
        "cold_sensitivity": True,
    },
    negative_features={
        "periodontal_pocket": True,
        "tooth_mobility": True,
        "gum_enlargement": True,
    },
    discriminators=[
        "milk yuzasi qizil, yaltiroq va ko'chadi",
        "og'riq/achishish bilan",
        "ko'pincha tizimli dermatoz (lixen) bilan bog'liq",
    ],
    red_flags=[
        "keng tarqalgan eroziyalar",
        "boshqa shilliq qavatlarning zararlanishi",
    ],
)

# ─────────────────────────────────────────────
#  PARODONTITLAR
# ─────────────────────────────────────────────

periodontitis_localized = Disease(
    id="periodontitis_localized",
    name_uz="Lokal parodontit",
    name_ru="Локализованный пародонтит",
    name_en="Localized periodontitis",
    category="periodontal",
    core_features={
        "periodontal_pocket": True,
        "tooth_mobility": True,
    },
    optional_features={
        "bad_smell": True,
        "pressure_pain": True,
        "gum_bleeding": True,
    },
    negative_features={
        "generalized": True,
        "rapid_progression": True,
        "no_bone_loss": True,
    },
    discriminators=[
        "bir yoki bir necha tishda chegaralangan",
        "periodontal cho'ntak va harakatchanlik",
        "mahalliy sabab (plomba, lokma) bilan",
    ],
    red_flags=[
        "tish bo'shashishi",
        "yiring ajralishi",
    ],
)

periodontitis_generalized = Disease(
    id="periodontitis_generalized",
    name_uz="Generalizatsiyalashgan parodontit",
    name_ru="Генерализованный пародонтит",
    name_en="Generalized periodontitis",
    category="periodontal",
    core_features={
        "periodontal_pocket": True,
        "tooth_mobility": True,
        "generalized": True,
    },
    optional_features={
        "gum_bleeding": True,
        "bad_smell": True,
        "pus_discharge": True,
    },
    negative_features={
        "no_bone_loss": True,
        "gum_enlargement": True,
    },
    discriminators=[
        "deyarli barcha tishlar atrofida",
        "chuqur cho'ntaklar va suyak rezorbsiyasi",
        "tishlarning ko'p sonli harakatchanligi",
    ],
    red_flags=[
        "tishlarning tez bo'shashishi",
        "ko'p o'choqli yiring",
    ],
)

periodontitis_aggressive = Disease(
    id="periodontitis_aggressive",
    name_uz="Agressiv parodontit",
    name_ru="Агрессивный пародонтит",
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
        "generalized": True,
    },
    negative_features={
        "no_bone_loss": True,
    },
    discriminators=[
        "yosh bemorlarda",
        "tez (oylar ichida) rivojlanadi",
        "yallig'lanish darajasiga nomutanosib suyak yo'qotilishi",
    ],
    red_flags=[
        "tezkor suyak yo'qotilishi",
        "erta tish yo'qotish",
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
        "pus_discharge": True,
        "bad_smell": True,
    },
    negative_features={
        "no_bone_loss": True,
    },
    discriminators=[
        "cho'ntak sohasida o'tkir abscess",
        "kuchli og'riq va shish",
        "cho'ntakdan yiring",
    ],
    red_flags=[
        "isitma",
        "tez kattalashuvchi shish",
    ],
)

periimplantitis = Disease(
    id="periimplantitis",
    name_uz="Periimplantit",
    name_ru="Периимплантит",
    name_en="Peri-implantitis",
    category="periodontal",
    core_features={
        "has_implant": True,
        "periodontal_pocket": True,
    },
    optional_features={
        "gum_bleeding": True,
        "gum_swelling": True,
        "pus_discharge": True,
        "bad_smell": True,
        "tooth_mobility": True,
    },
    negative_features={
        "no_bone_loss": True,
    },
    discriminators=[
        "implant atrofidagi yallig'lanish",
        "implant atrofida suyak yo'qotilishi va cho'ntak",
        "qonash/yiring va (kech bosqichda) implant bo'shashishi",
    ],
    red_flags=[
        "implantning bo'shashishi",
        "tez suyak yo'qotilishi",
    ],
)

# ─────────────────────────────────────────────
#  DISTROFIK / BOSHQA HOLATLAR
# ─────────────────────────────────────────────

periodontosis = Disease(
    id="periodontosis",
    name_uz="Parodontoz",
    name_ru="Пародонтоз",
    name_en="Periodontosis",
    category="periodontal",
    core_features={
        "gum_recession": True,
        "root_exposure": True,
        "no_inflammation": True,
    },
    optional_features={
        "cold_sensitivity": True,
        "generalized": True,
    },
    negative_features={
        "gum_bleeding": True,
        "gum_swelling": True,
        "periodontal_pocket": True,
    },
    discriminators=[
        "yallig'lanish belgilari yo'q (distrofik)",
        "milk retraksiyasi va ildiz yalang'ochlanishi",
        "tekis suyak atrofiyasi, cho'ntaksiz",
    ],
    red_flags=[
        "tish bo'shashishi (kech bosqich)",
    ],
)

gingival_recession = Disease(
    id="gingival_recession",
    name_uz="Gingival retsessiya (milk chekinishi)",
    name_ru="Рецессия десны",
    name_en="Gingival recession",
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
        "generalized": True,
    },
    discriminators=[
        "mahalliy (ko'pincha bitta tish) milk chekinishi",
        "ildiz ochilishi va sezuvchanlik",
        "yallig'lanishsiz, ko'pincha travma/cho'tkalashdan",
    ],
    red_flags=[
        "ildiz kariesi xavfi",
        "defekt chuqurlashishi",
    ],
)

furcation_involvement = Disease(
    id="furcation_involvement",
    name_uz="Furkatsion shikastlanish",
    name_ru="Поражение фуркации",
    name_en="Furcation involvement",
    category="periodontal",
    core_features={
        "furcation_defect": True,
        "tooth_mobility": True,
    },
    optional_features={
        "periodontal_pocket": True,
        "bad_smell": True,
        "pus_discharge": True,
    },
    negative_features={
        "gum_enlargement": True,
        "no_bone_loss": True,
    },
    discriminators=[
        "ko'p ildizli tishda ildizlararo defekt",
        "furkatsiyaga zond kiradi",
        "harakatchanlik va cho'ntak bilan",
    ],
    red_flags=[
        "tishni saqlash imkoniyatining kamayishi",
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
        "pus_discharge": True,
    },
    negative_features={
        "gum_recession": True,
    },
    discriminators=[
        "aql tishi sohasida",
        "tish ustidagi milk (kapyushon) yallig'langan",
        "og'iz ochish qiyinlashishi",
    ],
    red_flags=[
        "trizm",
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
    gingivitis_desquamative,
    periodontitis_localized,
    periodontitis_generalized,
    periodontitis_aggressive,
    periodontal_abscess,
    periimplantitis,
    periodontosis,
    gingival_recession,
    furcation_involvement,
    pericoronitis,
]
