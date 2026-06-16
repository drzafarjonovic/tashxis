"""
Engine (Akinator + Bayes) xatti-harakat testlari.

Bemorning haqiqiy belgilari berilganda, simulyatsiya qilingan sessiya
to'g'ri tashxis (disease_id) bilan yakunlanishini tekshiradi.
"""

from typing import Dict

import pytest

from engine import diagnose, get_next_question, is_emergency, should_stop


def _simulate(category: str, truth: Dict[str, bool], max_q: int = 12) -> Dict:
    """Berilgan 'haqiqat' bo'yicha avtomatik javob beruvchi sessiya."""
    obs: Dict[str, bool] = {}
    asked: list[str] = []
    for _ in range(max_q):
        qid = get_next_question(category, obs, asked)
        if qid is None:
            break
        obs[qid] = truth.get(qid, False)
        asked.append(qid)
        if should_stop(category, obs, len(asked)):
            break
    return diagnose(category, obs, "uz")


@pytest.mark.parametrize(
    "category,truth,expected_id",
    [
        ("tooth", {"spontaneous_pain": True, "night_pain": True, "pain_attacks": True, "cold_prolonged": True, "localized_pain": True}, "acute_pulpitis_focal"),
        ("tooth", {"spontaneous_pain": True, "night_pain": True, "irradiation": True, "hot_increases_pain": True, "cold_relieves_pain": True, "severe_pain": True}, "acute_pulpitis_diffuse"),
        ("tooth", {"no_pain": True, "visible_white_spot": True}, "white_spot"),
        ("tooth", {"cavity_visible": True, "pain_triggered": True, "cold_short": True, "sweet_sensitivity": True, "bad_smell": True}, "deep_caries"),
        # nokarioz shikastlanishlar (1-kategoriya)
        ("tooth", {"brown_stains": True, "multiple_teeth_affected": True, "since_childhood": True, "no_pain": True}, "dental_fluorosis"),
        ("tooth", {"enamel_pits": True, "since_childhood": True, "multiple_teeth_affected": True}, "enamel_hypoplasia"),
        ("tooth", {"enamel_missing": True, "since_childhood": True, "cold_sensitivity": True}, "enamel_aplasia"),
        ("tooth", {"acid_exposure": True, "smooth_shiny_surface": True, "cold_sensitivity": True, "multiple_teeth_affected": True}, "tooth_erosion"),
        ("tooth", {"occlusal_wear": True, "bruxism": True, "multiple_teeth_affected": True}, "attrition"),
        ("tooth", {"wedge_defect": True, "hard_brushing": True, "cold_sensitivity": True}, "abrasion"),
        ("tooth", {"wedge_defect": True, "bruxism": True, "cold_sensitivity": True}, "abfraction"),
        ("tooth", {"chalky_enamel": True, "acid_exposure": True, "multiple_teeth_affected": True}, "hard_tissue_necrosis"),
        ("tooth", {"cold_sensitivity": True, "cold_short": True, "sweet_sensitivity": True, "gum_recession": True}, "dentin_hypersensitivity"),
        ("tooth", {"family_history": True, "since_childhood": True, "tooth_mobility": True}, "dentin_dysplasia"),
        ("tooth", {"family_history": True, "since_childhood": True, "enamel_pits": True}, "amelogenesis_imperfecta"),
        ("tooth", {"family_history": True, "since_childhood": True, "abnormal_tooth_color": True, "occlusal_wear": True}, "dentinogenesis_imperfecta"),
        ("tooth", {"percussion_pain": True, "localized_pain": True, "pressure_pain": True, "spontaneous_pain": True, "gum_swelling": True}, "acute_apical_periodontitis"),
        ("tooth", {"no_sensitivity": True, "tooth_discoloration": True, "bad_smell": True}, "pulp_necrosis"),
        ("periodontal", {"gum_bleeding": True, "gum_swelling": True, "gum_redness": True}, "gingivitis_catarrhal"),
        ("periodontal", {"periodontal_pocket": True, "tooth_mobility": True, "gum_bleeding": True, "bad_smell": True}, "periodontitis_chronic"),
        ("mucosa", {"ulcer": True, "pain": True, "white_center_red_halo": True, "recurrent": True}, "aphthous_stomatitis"),
        ("mucosa", {"white_patch": True, "removable_patch": True, "burning": True}, "oral_candidiasis"),
        ("jaw", {"jaw_swelling": True, "spontaneous_pain": True, "causative_tooth": True}, "periostitis"),
    ],
)
def test_diagnosis_reaches_expected_disease(category, truth, expected_id):
    result = _simulate(category, truth)
    assert result["disease_id"] == expected_id, (
        f"Kutilgan {expected_id}, olingan {result['disease_id']} (conf={result['confidence']})"
    )


def test_first_tooth_question_is_discriminating():
    # Bo'sh holatda eng informativ savol so'ralishi kerak (oqim qotib qolmasligi)
    qid = get_next_question("tooth", {}, [])
    assert qid is not None


def test_emergency_detection():
    assert is_emergency({"high_fever": True, "jaw_swelling": True})
    assert is_emergency({"fever": True, "trismus": True, "jaw_swelling": True})
    assert not is_emergency({"jaw_swelling": True})
    assert not is_emergency({})


def test_diagnose_empty_observations_is_uncertain_but_safe():
    result = diagnose("tooth", {}, "uz")
    assert result["diagnosis"] is not None
    assert 0.0 <= result["confidence"] <= 1.0
