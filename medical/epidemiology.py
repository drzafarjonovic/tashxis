"""
Epidemiologik ma'lumotlar (V2.0 Clinical Prior System uchun).

3 qatlamli prior:
    effective_prior = base_prior(prevalence) × age_factor × sex_factor

Bu yerda statik (boshlang'ich) qiymatlar saqlanadi. Kelajakda tasdiqlangan
tashxislar (doctor_feedback) asosida `priors` jadvali orqali yangilanishi mumkin
(Self-Learning Prior Update) — o'sha qiymatlar shu standart qiymatlarning
ustidan qo'llaniladi.

Eslatma: qiymatlar ochiq stomatologik epidemiologiya bilimiga asoslangan
taxminiy bo'lib, real ma'lumot to'planganda kalibrlanishi kerak.
"""

from typing import Dict

AGE_GROUPS = ["5-12", "13-18", "19-40", "41-65", "65+"]
SEXES = ["male", "female"]

# ─────────────────────────────────────────────────────────────────
#  1-QATLAM: TARQALGANLIK (base prior tier'i)
# ─────────────────────────────────────────────────────────────────
TIER_WEIGHTS: Dict[str, float] = {
    # Diagnostik yordamchi uchun prior NUDGE qiladi (dominatsiya qilmaydi):
    # mos belgilari bo'lgan kam uchraydigan kasallik baribir yetib boriladi.
    # Real ma'lumot to'planganda bu qiymatlar kalibrlanadi.
    "very_common": 1.0,
    "common": 0.70,
    "uncommon": 0.50,
    "rare": 0.34,
    "very_rare": 0.24,
}

# id → tier. Ro'yxatda yo'q kasallik uchun "uncommon" (default).
PREVALENCE: Dict[str, str] = {
    # tish to'qimalari / pulpa / periapikal
    "white_spot": "very_common",
    "superficial_caries": "very_common",
    "medium_caries": "very_common",
    "deep_caries": "very_common",
    "secondary_caries": "common",
    "dentin_hypersensitivity": "very_common",
    "tooth_erosion": "common",
    "attrition": "common",
    "abrasion": "common",
    "dental_fluorosis": "common",
    "enamel_hypoplasia": "uncommon",
    "abfraction": "uncommon",
    "hard_tissue_necrosis": "rare",
    "enamel_aplasia": "very_rare",
    "dentin_dysplasia": "very_rare",
    "amelogenesis_imperfecta": "very_rare",
    "dentinogenesis_imperfecta": "very_rare",
    "acute_pulpitis_focal": "very_common",
    "acute_pulpitis_diffuse": "very_common",
    "chronic_pulpitis_fibrous": "common",
    "chronic_pulpitis_gangrenous": "common",
    "chronic_pulpitis_hypertrophic": "uncommon",
    "pulp_necrosis": "common",
    "acute_apical_periodontitis": "very_common",
    "chronic_apical_periodontitis_fibrous": "common",
    "chronic_apical_periodontitis_granulating": "common",
    "chronic_apical_periodontitis_granulomatous": "common",
    "periapical_granuloma": "common",
    "periapical_abscess": "common",
    "radicular_cyst": "uncommon",
    # parodont
    "gingivitis_catarrhal": "very_common",
    "gingivitis_hypertrophic": "common",
    "gingivitis_ulcerative": "uncommon",
    "gingivitis_desquamative": "rare",
    "periodontitis_localized": "common",
    "periodontitis_generalized": "very_common",
    "periodontitis_aggressive": "rare",
    "periodontal_abscess": "common",
    "periimplantitis": "uncommon",
    "periodontosis": "rare",
    "gingival_recession": "common",
    "furcation_involvement": "uncommon",
    "pericoronitis": "common",
    # shilliq qavat / til / lab / infeksion / o'sma
    "aphthous_stomatitis": "very_common",
    "catarrhal_stomatitis": "common",
    "ulcerative_stomatitis": "uncommon",
    "traumatic_stomatitis": "common",
    "oral_candidiasis": "common",
    "geographic_tongue": "common",
    "hairy_tongue": "uncommon",
    "median_rhomboid_glossitis": "uncommon",
    "glossitis": "uncommon",
    "meteorological_cheilitis": "common",
    "exfoliative_cheilitis": "uncommon",
    "actinic_cheilitis": "rare",
    "angular_cheilitis": "common",
    "herpetic_stomatitis": "common",
    "herpes_simplex_labialis": "very_common",
    "herpes_zoster": "uncommon",
    "hpv_papilloma": "uncommon",
    "hand_foot_mouth": "uncommon",
    "oral_syphilis": "rare",
    "oral_tuberculosis": "rare",
    "actinomycosis": "very_rare",
    "leukoplakia": "uncommon",
    "erythroplakia": "rare",
    "oral_submucous_fibrosis": "rare",
    "oral_lichen_planus": "uncommon",
    "fibroma": "common",
    "hemangioma": "rare",
    "lipoma": "rare",
    "oral_scc": "rare",
    "tongue_cancer": "rare",
    "lip_cancer": "rare",
    # jag'
    "periostitis": "common",
    "osteitis": "uncommon",
    "alveolitis": "common",
    "osteomyelitis_acute": "rare",
    "osteomyelitis_chronic": "rare",
    "follicular_cyst": "uncommon",
    "odontogenic_keratocyst": "rare",
    # TMJ
    "tmj_dysfunction": "common",
    "tmj_arthritis": "uncommon",
    "tmj_arthrosis": "uncommon",
    "tmj_disc_dislocation": "uncommon",
    "tmj_ankylosis": "very_rare",
    # travma
    "enamel_fracture": "common",
    "enamel_dentin_fracture": "common",
    "crown_fracture_pulp": "uncommon",
    "root_fracture": "uncommon",
    "concussion": "common",
    "subluxation": "common",
    "extrusion": "uncommon",
    "intrusion": "uncommon",
    "avulsion": "uncommon",
    # rivojlanish / ortodontik
    "adentia_complete": "very_rare",
    "oligodontia": "rare",
    "hypodontia": "common",
    "hyperdontia": "uncommon",
    "gemination": "rare",
    "fusion": "rare",
    "concrescence": "very_rare",
    "taurodontism": "rare",
    "distopia": "common",
    "tooth_retention": "common",
    "ectopic_eruption": "uncommon",
    "distal_occlusion": "very_common",
    "mesial_occlusion": "common",
    "deep_bite": "common",
    "open_bite": "common",
    "crossbite": "common",
    "dental_crowding": "very_common",
    "diastema": "common",
    "tremas": "common",
    # so'lak bezlari
    "sialadenitis": "uncommon",
    "sialolithiasis": "common",
    "xerostomia": "common",
    "sjogren_syndrome": "rare",
    "mucocele": "common",
    "ranula": "uncommon",
    "salivary_tumor": "rare",
}

# ─────────────────────────────────────────────────────────────────
#  2-QATLAM: YOSH BO'YICHA (id → {age_group: factor}); default 1.0
# ─────────────────────────────────────────────────────────────────
AGE_PRIORS: Dict[str, Dict[str, float]] = {
    "pericoronitis": {"13-18": 1.6, "19-40": 1.8, "41-65": 0.6, "65+": 0.3, "5-12": 0.2},
    "periodontitis_aggressive": {"13-18": 2.2, "19-40": 1.8, "41-65": 0.5, "65+": 0.3},
    "periodontitis_generalized": {"41-65": 1.6, "65+": 1.8, "13-18": 0.4, "5-12": 0.1},
    "periodontosis": {"41-65": 1.6, "65+": 1.9, "5-12": 0.1, "13-18": 0.3},
    "gingival_recession": {"41-65": 1.5, "65+": 1.7},
    "xerostomia": {"65+": 2.0, "41-65": 1.4, "5-12": 0.4},
    "sjogren_syndrome": {"41-65": 1.8, "65+": 1.8, "5-12": 0.1, "13-18": 0.3},
    "salivary_tumor": {"41-65": 1.5, "65+": 1.7},
    "oral_scc": {"41-65": 1.8, "65+": 2.0, "5-12": 0.05, "13-18": 0.1},
    "tongue_cancer": {"41-65": 1.8, "65+": 2.0, "5-12": 0.05, "13-18": 0.1},
    "lip_cancer": {"41-65": 1.7, "65+": 2.0, "5-12": 0.05},
    "leukoplakia": {"41-65": 1.5, "65+": 1.6, "5-12": 0.1},
    "actinic_cheilitis": {"41-65": 1.6, "65+": 1.8},
    "hand_foot_mouth": {"5-12": 2.5, "13-18": 0.8, "41-65": 0.3, "65+": 0.2},
    "herpetic_stomatitis": {"5-12": 2.2, "13-18": 1.2, "65+": 0.5},
    "aphthous_stomatitis": {"13-18": 1.4, "19-40": 1.3, "65+": 0.7},
    "geographic_tongue": {"5-12": 1.3, "19-40": 1.1},
    # rivojlanish anomaliyalari — asosan bolalik/o'smirlik
    "amelogenesis_imperfecta": {"5-12": 2.0, "13-18": 1.6, "41-65": 0.4, "65+": 0.2},
    "dentinogenesis_imperfecta": {"5-12": 2.0, "13-18": 1.6, "41-65": 0.4, "65+": 0.2},
    "enamel_hypoplasia": {"5-12": 1.8, "13-18": 1.4},
    "enamel_aplasia": {"5-12": 2.0, "13-18": 1.4},
    "dental_fluorosis": {"5-12": 1.6, "13-18": 1.4},
    "adentia_complete": {"5-12": 2.0, "13-18": 1.4},
    "oligodontia": {"5-12": 1.8, "13-18": 1.5},
    "hypodontia": {"5-12": 1.6, "13-18": 1.5},
    "hyperdontia": {"5-12": 1.7, "13-18": 1.4},
    "ectopic_eruption": {"5-12": 2.0, "13-18": 1.3},
    "tooth_retention": {"13-18": 1.5, "19-40": 1.4},
    "distal_occlusion": {"5-12": 1.5, "13-18": 1.6},
    "mesial_occlusion": {"5-12": 1.5, "13-18": 1.5},
    "open_bite": {"5-12": 1.6, "13-18": 1.3},
    "crossbite": {"5-12": 1.6, "13-18": 1.3},
    "dental_crowding": {"13-18": 1.5, "19-40": 1.2},
    "osteomyelitis_chronic": {"41-65": 1.3, "65+": 1.4},
    "tmj_arthrosis": {"41-65": 1.5, "65+": 1.8, "5-12": 0.1},
    "tmj_dysfunction": {"13-18": 1.3, "19-40": 1.5, "65+": 0.7},
}

# ─────────────────────────────────────────────────────────────────
#  3-QATLAM: JINS BO'YICHA (id → {sex: factor}); default 1.0
# ─────────────────────────────────────────────────────────────────
SEX_PRIORS: Dict[str, Dict[str, float]] = {
    "gingivitis_desquamative": {"female": 1.6, "male": 0.6},
    "oral_lichen_planus": {"female": 1.4, "male": 0.7},
    "sjogren_syndrome": {"female": 2.0, "male": 0.4},
    "tmj_dysfunction": {"female": 1.5, "male": 0.7},
    "tmj_arthritis": {"female": 1.3, "male": 0.8},
    "gingivitis_hypertrophic": {"female": 1.3, "male": 0.8},  # gormonal/homiladorlik
    "leukoplakia": {"male": 1.4, "female": 0.7},
    "oral_scc": {"male": 1.5, "female": 0.7},
    "tongue_cancer": {"male": 1.4, "female": 0.8},
    "lip_cancer": {"male": 1.6, "female": 0.6},
    "actinic_cheilitis": {"male": 1.4, "female": 0.7},
    "oral_submucous_fibrosis": {"male": 1.4, "female": 0.7},
    "hairy_tongue": {"male": 1.3, "female": 0.8},
}

# ─────────────────────────────────────────────────────────────────
#  ANATOMIK JOYLASHUV PROFILLARI (id → {location_token: weight}); 1.0 neytral
#  Tokenlar: jaw=upper/lower, side=right/left, type=incisor/canine/premolar/molar
# ─────────────────────────────────────────────────────────────────
LOCATION_PROFILES: Dict[str, Dict[str, float]] = {
    # Perikoronit — deyarli har doim pastki aql tishi (oxirgi molyar) sohasida
    "pericoronitis": {"lower": 1.6, "molar": 1.8},
    # Follikulyar kista va retensiya — ko'pincha aql tishi/qoziq (molyar/qoziq)
    "follicular_cyst": {"molar": 1.3},
    "tooth_retention": {"molar": 1.3, "canine": 1.2},
    "ectopic_eruption": {"molar": 1.2, "canine": 1.3},
    # Diastema — markaziy kurak tishlar orasida
    "diastema": {"incisor": 1.5},
    # Lab saratoni / aktinik xeylit — old (kurak) soha bilan bog'liq emas, lekin
    # pastki labda; tish-tipi bu yerda kuchsiz signal — neytral qoldiramiz.
}
