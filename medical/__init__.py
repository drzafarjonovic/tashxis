from medical.diseases.tooth import (
    TOOTH_DISEASES, PULP_DISEASES, PERIAPICAL_DISEASES, ALL_TOOTH_DISEASES
)
from medical.diseases.periodontal import PERIODONTAL_DISEASES
from medical.diseases.mucosa import MUCOSA_DISEASES
from medical.diseases.jaw import JAW_DISEASES
from medical.diseases.tmj import TMJ_DISEASES
from medical.diseases.trauma import TRAUMA_DISEASES
from medical.diseases.dentition import DENTITION_DISEASES
from medical.diseases.salivary import SALIVARY_DISEASES
from medical.info import DISEASE_INFO
from medical.epidemiology import PREVALENCE, LOCATION_PROFILES

ALL_DISEASES = (
    ALL_TOOTH_DISEASES
    + PERIODONTAL_DISEASES
    + MUCOSA_DISEASES
    + JAW_DISEASES
    + TMJ_DISEASES
    + TRAUMA_DISEASES
    + DENTITION_DISEASES
    + SALIVARY_DISEASES
)

# Boy ma'lumot bloklarini (info.py) Disease obyektlariga biriktirish.
# Inline ma'lumotga ega kasalliklar (masalan namuna sifatidagi o'choqli pulpit)
# ustiga yozilmaydi.
for _d in ALL_DISEASES:
    _info = DISEASE_INFO.get(_d.id)
    if not _info:
        continue
    if not _d.description:
        _d.description = _info.get("description", {})
    if not _d.symptoms_text:
        _d.symptoms_text = _info.get("symptoms_text", {})
    if not _d.differential:
        _d.differential = _info.get("differential", {})
    if not _d.treatment:
        _d.treatment = _info.get("treatment", {})

# Epidemiologik prior (tarqalganlik) va anatomik joylashuv profilini biriktirish.
for _d in ALL_DISEASES:
    _tier = PREVALENCE.get(_d.id)
    if _tier:
        _d.prevalence = _tier
    _profile = LOCATION_PROFILES.get(_d.id)
    if _profile and not _d.location_profile:
        _d.location_profile = dict(_profile)

# Diagnostik guruhlar — engine foydalanuvchi tanlagan kategoriya bo'yicha ishlaydi.
# "tooth" guruhiga barcha tish kasalliklari (karies + nokarioz + pulpit + periapikal)
# kiradi: shunda Akinator info-gain orqali ajratuvchi savollarni tabiiy tartibda beradi.
DIAGNOSTIC_GROUPS = {
    "tooth":       ALL_TOOTH_DISEASES,
    "periodontal": PERIODONTAL_DISEASES,
    "mucosa":      MUCOSA_DISEASES,
    "jaw":         JAW_DISEASES,
    "tmj":         TMJ_DISEASES,
    "trauma":      TRAUMA_DISEASES,
    "dentition":   DENTITION_DISEASES,
    "salivary":    SALIVARY_DISEASES,
}

# Batafsil ko'rinish (testlar / kelajakdagi tahlil uchun)
DISEASES_BY_CATEGORY = {
    "tooth":       TOOTH_DISEASES,
    "pulp":        PULP_DISEASES,
    "periapical":  PERIAPICAL_DISEASES,
    "periodontal": PERIODONTAL_DISEASES,
    "mucosa":      MUCOSA_DISEASES,
    "jaw":         JAW_DISEASES,
    "tmj":         TMJ_DISEASES,
    "trauma":      TRAUMA_DISEASES,
    "dentition":   DENTITION_DISEASES,
    "salivary":    SALIVARY_DISEASES,
}
