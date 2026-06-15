"""
Simptom registri validatsiyasi.

Har bir kasallik faqat domain/symptoms.py da e'lon qilingan simptom
kalitlaridan foydalanishi kerak. Bu test kelajakdagi xatolarni
(masalan, 'hot_pain' kabi mavjud bo'lmagan kalitlar) avtomatik ushlaydi.
"""

from domain.symptoms import all_symptom_keys
from medical import ALL_DISEASES

# Hozircha registrda yo'q, ammo kasalliklarda uchraydigan kalitlar.
# Bular kasalliklarni qayta tuzish bosqichida tozalanadi/qo'shiladi.
# Yangi qarz qo'shilsa, bu test xato beradi.
KNOWN_MISSING = {
    "acute_pain",
    "diffuse_swelling",
    "hot_pain",
    "no_fever",
    "no_periodontal_pocket",
    "root_exposure",
}


def _collect_unknown_keys() -> set[str]:
    registry = all_symptom_keys()
    unknown: set[str] = set()
    for disease in ALL_DISEASES:
        for feats in (
            disease.core_features,
            disease.optional_features,
            disease.negative_features,
        ):
            for key in feats:
                if key not in registry:
                    unknown.add(key)
    return unknown


def test_no_new_unknown_symptom_keys():
    unknown = _collect_unknown_keys()
    new_debt = unknown - KNOWN_MISSING
    assert not new_debt, f"Registrda yo'q yangi simptom kalitlari: {sorted(new_debt)}"


def test_every_disease_has_an_id_and_names():
    for d in ALL_DISEASES:
        assert d.id, "Kasallik id'siz"
        assert d.name_uz and d.name_ru and d.name_en, f"{d.id}: nom to'liq emas"
