from medical.diseases.tooth import (
    TOOTH_DISEASES, PULP_DISEASES, PERIAPICAL_DISEASES, ALL_TOOTH_DISEASES
)
from medical.diseases.periodontal import PERIODONTAL_DISEASES
from medical.diseases.mucosa import MUCOSA_DISEASES
from medical.diseases.jaw import JAW_DISEASES

ALL_DISEASES = ALL_TOOTH_DISEASES + PERIODONTAL_DISEASES + MUCOSA_DISEASES + JAW_DISEASES

DISEASES_BY_CATEGORY = {
    "tooth":       TOOTH_DISEASES,
    "pulp":        PULP_DISEASES,
    "periapical":  PERIAPICAL_DISEASES,
    "periodontal": PERIODONTAL_DISEASES,
    "mucosa":      MUCOSA_DISEASES,
    "jaw":         JAW_DISEASES,
}
