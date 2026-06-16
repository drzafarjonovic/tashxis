from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Disease:
    """
    Stomatologik kasallik modeli.

    Identifikatsiya (Akinator/Bayes uchun):
        id, name_*, category, core/optional/negative_features, discriminators, red_flags

    Tashxis aniqlangandan keyin foydalanuvchiga ko'rsatiladigan boy ma'lumot
    (3 tilda — uz/ru/en; bo'sh bo'lsa, qisqa avtomatik matn ishlatiladi):
        description:  Kasallik haqida to'liq tavsif (klinika, sabab)
        symptoms_text:Asosiy simptomlarning batafsil tavsifi
        differential: Differensial tashxis (qaysi kasalliklardan farqlanadi)
        treatment:    Davolash / "nima qilish kerak" tavsiyasi
    """
    id: str
    name_uz: str
    name_ru: str
    name_en: str
    category: str
    core_features: Dict[str, bool] = field(default_factory=dict)
    optional_features: Dict[str, bool] = field(default_factory=dict)
    negative_features: Dict[str, bool] = field(default_factory=dict)
    discriminators: List[str] = field(default_factory=list)
    red_flags: List[str] = field(default_factory=list)

    # Boy ma'lumot bloklari (til → matn)
    description: Dict[str, str] = field(default_factory=dict)
    symptoms_text: Dict[str, str] = field(default_factory=dict)
    differential: Dict[str, str] = field(default_factory=dict)
    treatment: Dict[str, str] = field(default_factory=dict)

    # ── V2.0: epidemiologik prior va anatomik joylashuv ──────────
    # prevalence: tarqalganlik darajasi (bazaviy prior tier'i)
    #   "very_common" | "common" | "uncommon" | "rare" | "very_rare"
    prevalence: str = "uncommon"
    # location_profile: anatomik joylashuvga bog'liq nisbiy ehtimol (P(L|D))
    #   masalan {"lower": 1.4, "molar": 1.8} — neytral qiymat 1.0
    location_profile: Dict[str, float] = field(default_factory=dict)

    def get_name(self, lang: str) -> str:
        if lang == "ru":
            return self.name_ru
        if lang == "en":
            return self.name_en
        return self.name_uz

    @staticmethod
    def _pick(block: Dict[str, str], lang: str) -> str:
        if not block:
            return ""
        return block.get(lang) or block.get("uz") or block.get("ru") or block.get("en") or ""

    def get_description(self, lang: str) -> str:
        return self._pick(self.description, lang)

    def get_symptoms_text(self, lang: str) -> str:
        return self._pick(self.symptoms_text, lang)

    def get_differential(self, lang: str) -> str:
        return self._pick(self.differential, lang)

    def get_treatment(self, lang: str) -> str:
        return self._pick(self.treatment, lang)
