"""
13-kategoriya — So'lak bezlari kasalliklari.

Sialadenit, sialolitiaz, kserostomiya, mukosele, ranula, Sjögren sindromi,
so'lak bezi o'smasi.
"""

from medical.disease_model import Disease

sialadenitis = Disease(
    id="sialadenitis",
    name_uz="Sialadenit (so'lak bezi yallig'lanishi)",
    name_ru="Сиаладенит",
    name_en="Sialadenitis",
    category="salivary",
    core_features={
        "gland_swelling": True,
        "gland_pain": True,
    },
    optional_features={
        "pus_from_duct": True,
        "fever": True,
        "lymph_nodes": True,
        "bad_smell": True,
    },
    negative_features={
        "swelling_with_meals": True,
        "dry_eyes": True,
        "slow_growth": True,
    },
    discriminators=[
        "bezning o'tkir og'riqli shishi",
        "yo'lidan yiring/bulutli so'lak",
        "ko'pincha isitma bilan",
    ],
    red_flags=[
        "abscess shakllanishi",
        "tez tarqaluvchi shish",
    ],
)

sialolithiasis = Disease(
    id="sialolithiasis",
    name_uz="Sialolitiaz (so'lak toshi)",
    name_ru="Сиалолитиаз (слюннокаменная болезнь)",
    name_en="Sialolithiasis",
    category="salivary",
    core_features={
        "gland_swelling": True,
        "swelling_with_meals": True,
    },
    optional_features={
        "gland_pain": True,
        "pus_from_duct": True,
    },
    negative_features={
        "dry_eyes": True,
        "slow_growth": True,
    },
    discriminators=[
        "shish ovqatdan oldin/paytida kattalashadi",
        "keyin asta-sekin kichrayadi",
        "yo'lda tosh (konkrement) bilan to'silish",
    ],
    red_flags=[
        "to'liq tiqilish va o'tkir yallig'lanish",
    ],
)

xerostomia = Disease(
    id="xerostomia",
    name_uz="Kserostomiya (og'iz qurishi)",
    name_ru="Ксеростомия (сухость рта)",
    name_en="Xerostomia",
    category="salivary",
    core_features={
        "dry_mouth": True,
    },
    optional_features={
        "bad_smell": True,
    },
    negative_features={
        "dry_eyes": True,
        "gland_swelling": True,
        "swelling_with_meals": True,
        "gland_pain": True,
    },
    discriminators=[
        "so'lak kamayishi natijasida og'iz qurishi",
        "ko'pincha dorilar/nurlanish/yoshga bog'liq",
        "bez shishi yo'q",
    ],
    red_flags=[
        "tez rivojlanuvchi karies",
        "shilliq qavat infeksiyalari",
    ],
)

sjogren_syndrome = Disease(
    id="sjogren_syndrome",
    name_uz="Sjögren sindromi (og'izdagi ko'rinishi)",
    name_ru="Синдром Шёгрена (проявления в полости рта)",
    name_en="Sjögren's syndrome (oral)",
    category="salivary",
    core_features={
        "dry_mouth": True,
        "dry_eyes": True,
    },
    optional_features={
        "gland_swelling": True,
        "general_weakness": True,
    },
    negative_features={
        "swelling_with_meals": True,
        "pus_from_duct": True,
    },
    discriminators=[
        "og'iz va ko'z birga quruq (autoimmun)",
        "bezlarning simmetrik kattalashishi",
        "tizimli kasallik bilan bog'liq",
    ],
    red_flags=[
        "limfoma rivojlanishi xavfi",
    ],
)

mucocele = Disease(
    id="mucocele",
    name_uz="Mukosele (shilliq kista)",
    name_ru="Мукоцеле (слизистая киста)",
    name_en="Mucocele",
    category="salivary",
    core_features={
        "bluish_soft_swelling": True,
    },
    optional_features={
        "recurrence_history": True,
    },
    negative_features={
        "gland_swelling": True,
        "dry_mouth": True,
        "gland_pain": True,
        "floor_of_mouth_swelling": True,
    },
    discriminators=[
        "labda/yonoqda ko'kimtir yumshoq pufak",
        "ko'pincha tishlab olish/travmadan keyin",
        "yorilib, qayta paydo bo'lishi mumkin",
    ],
    red_flags=[
        "qayta-qayta paydo bo'lishi",
    ],
)

ranula = Disease(
    id="ranula",
    name_uz="Ranula (til osti kistasi)",
    name_ru="Ранула (подъязычная киста)",
    name_en="Ranula",
    category="salivary",
    core_features={
        "floor_of_mouth_swelling": True,
    },
    optional_features={
        "bluish_soft_swelling": True,
    },
    negative_features={
        "dry_mouth": True,
        "gland_pain": True,
        "swelling_with_meals": True,
    },
    discriminators=[
        "til ostida katta ko'kimtir shish",
        "til osti so'lak bezi bilan bog'liq",
        "qurbaqa qornini eslatadi",
    ],
    red_flags=[
        "katta o'lcham — yutish/nutqqa xalal",
    ],
)

salivary_tumor = Disease(
    id="salivary_tumor",
    name_uz="So'lak bezi o'smasi",
    name_ru="Опухоль слюнной железы",
    name_en="Salivary gland tumour",
    category="salivary",
    core_features={
        "gland_swelling": True,
        "slow_growth": True,
        "soft_painless_lump": True,
    },
    optional_features={
        "indurated_lesion": True,
        "numbness": True,
    },
    negative_features={
        "swelling_with_meals": True,
        "gland_pain": True,
        "fever": True,
        "pus_from_duct": True,
    },
    discriminators=[
        "bezda sekin o'sgan og'riqsiz tugun",
        "ko'pincha quloqoldi bezida",
        "og'riq/uvishish — yomon sifat belgisi",
    ],
    red_flags=[
        "tez o'sish, og'riq yoki yuz nervi falaji",
        "qattiq, harakatsiz tugun",
    ],
)

# ─────────────────────────────────────────────
#  EXPORT
# ─────────────────────────────────────────────
SALIVARY_DISEASES = [
    sialadenitis,
    sialolithiasis,
    xerostomia,
    sjogren_syndrome,
    mucocele,
    ranula,
    salivary_tumor,
]
