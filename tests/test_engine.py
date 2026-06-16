"""
Engine (Akinator + Bayes) xatti-harakat testlari.

Bemorning haqiqiy belgilari berilganda, simulyatsiya qilingan sessiya
to'g'ri tashxis (disease_id) bilan yakunlanishini tekshiradi.
"""

from typing import Dict

import pytest

from engine import diagnose, get_next_question, is_emergency, should_stop


def _simulate(category: str, truth: Dict[str, bool], max_q: int = 14) -> Dict:
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
        ("periodontal", {"periodontal_pocket": True, "tooth_mobility": True, "generalized": True, "gum_bleeding": True}, "periodontitis_generalized"),
        ("periodontal", {"gum_desquamation": True, "gum_redness": True, "gum_pain": True}, "gingivitis_desquamative"),
        ("periodontal", {"has_implant": True, "periodontal_pocket": True, "gum_bleeding": True}, "periimplantitis"),
        ("periodontal", {"gum_recession": True, "root_exposure": True, "cold_sensitivity": True}, "gingival_recession"),
        ("periodontal", {"furcation_defect": True, "tooth_mobility": True, "periodontal_pocket": True}, "furcation_involvement"),
        # shilliq qavat / til / lab / infeksion / o'sma
        ("mucosa", {"ulcer": True, "pain": True, "white_center_red_halo": True, "recurrent": True}, "aphthous_stomatitis"),
        ("mucosa", {"white_patch": True, "removable_patch": True, "burning": True}, "oral_candidiasis"),
        ("mucosa", {"tongue_lesion": True, "map_like_patches": True}, "geographic_tongue"),
        ("mucosa", {"tongue_lesion": True, "hairy_coating": True, "bad_smell": True}, "hairy_tongue"),
        ("mucosa", {"lip_lesion": True, "lip_sun_damage": True}, "actinic_cheilitis"),
        ("mucosa", {"angular_cracks": True, "burning": True}, "angular_cheilitis"),
        ("mucosa", {"grouped_vesicles": True, "lip_lesion": True, "recurrent": True}, "herpes_simplex_labialis"),
        ("mucosa", {"unilateral_rash": True, "blisters": True, "pain": True}, "herpes_zoster"),
        ("mucosa", {"wart_like_growth": True, "no_pain": True}, "hpv_papilloma"),
        ("mucosa", {"hand_foot_rash": True, "blisters": True, "fever": True}, "hand_foot_mouth"),
        ("mucosa", {"woody_swelling": True, "bad_smell": True}, "actinomycosis"),
        ("mucosa", {"white_patch": True, "non_removable": True, "smoking_history": True}, "leukoplakia"),
        ("mucosa", {"red_velvety_patch": True, "non_removable": True}, "erythroplakia"),
        ("mucosa", {"progressive_trismus_fibrosis": True, "tobacco_risk": True}, "oral_submucous_fibrosis"),
        ("mucosa", {"red_blue_blanching_lesion": True}, "hemangioma"),
        ("mucosa", {"indurated_lesion": True, "chronic_nonhealing_ulcer": True, "tobacco_risk": True}, "oral_scc"),
        ("mucosa", {"tongue_lesion": True, "indurated_lesion": True, "chronic_nonhealing_ulcer": True}, "tongue_cancer"),
        # jag' suyagi
        ("jaw", {"jaw_swelling": True, "spontaneous_pain": True, "causative_tooth": True}, "periostitis"),
        ("jaw", {"recent_extraction": True, "empty_socket_pain": True, "bad_smell": True}, "alveolitis"),
        ("jaw", {"jaw_swelling": True, "high_fever": True, "severe_pain": True, "trismus": True}, "osteomyelitis_acute"),
        ("jaw", {"no_pain": True, "retained_tooth": True, "slow_growth": True}, "follicular_cyst"),
        ("jaw", {"slow_growth": True, "recurrence_history": True}, "odontogenic_keratocyst"),
        # TMJ
        ("tmj", {"jaw_clicking": True, "joint_pain": True, "bruxism": True}, "tmj_dysfunction"),
        ("tmj", {"joint_crepitus": True, "joint_pain": True}, "tmj_arthrosis"),
        ("tmj", {"jaw_clicking": True, "jaw_locking": True}, "tmj_disc_dislocation"),
        ("tmj", {"cannot_open_progressive": True, "trismus": True}, "tmj_ankylosis"),
        # travma
        ("trauma", {"recent_injury": True, "tooth_fractured": True, "fracture_enamel_only": True}, "enamel_fracture"),
        ("trauma", {"recent_injury": True, "tooth_fractured": True, "fracture_dentin": True}, "enamel_dentin_fracture"),
        ("trauma", {"recent_injury": True, "tooth_fractured": True, "pulp_exposed_bleeding": True}, "crown_fracture_pulp"),
        ("trauma", {"recent_injury": True, "tooth_intruded": True}, "intrusion"),
        ("trauma", {"recent_injury": True, "tooth_avulsed": True}, "avulsion"),
        ("trauma", {"recent_injury": True, "tooth_tender_after_injury": True}, "concussion"),
        # rivojlanish / ortodontik
        ("dentition", {"extra_teeth": True}, "hyperdontia"),
        ("dentition", {"all_teeth_missing": True, "teeth_missing_congenital": True}, "adentia_complete"),
        ("dentition", {"teeth_missing_congenital": True, "many_teeth_missing": True}, "oligodontia"),
        ("dentition", {"upper_teeth_protrude": True}, "distal_occlusion"),
        ("dentition", {"lower_jaw_protrudes": True}, "mesial_occlusion"),
        ("dentition", {"front_teeth_no_contact": True}, "open_bite"),
        ("dentition", {"deep_overbite": True}, "deep_bite"),
        ("dentition", {"crossbite": True}, "crossbite"),
        ("dentition", {"teeth_crowded": True}, "dental_crowding"),
        # so'lak bezlari
        ("salivary", {"gland_swelling": True, "swelling_with_meals": True}, "sialolithiasis"),
        ("salivary", {"gland_swelling": True, "gland_pain": True, "pus_from_duct": True}, "sialadenitis"),
        ("salivary", {"dry_mouth": True, "dry_eyes": True}, "sjogren_syndrome"),
        ("salivary", {"bluish_soft_swelling": True}, "mucocele"),
        ("salivary", {"floor_of_mouth_swelling": True}, "ranula"),
        ("salivary", {"gland_swelling": True, "slow_growth": True, "soft_painless_lump": True}, "salivary_tumor"),
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
