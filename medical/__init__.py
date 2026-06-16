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
