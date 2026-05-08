from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Disease:
    """
    Stomatologik kasallik modeli.

    Attributes:
        id:               Noyob identifikator (masalan: 'acute_pulpitis')
        name_uz:          O'zbek tilidagi nom
        name_ru:          Rus tilidagi nom
        name_en:          Ingliz tilidagi nom
        category:         Toifa: tooth | mucosa | jaw | periodontal | pulp | periapical
        core_features:    Asosiy belgilar (+3 ball)
        optional_features:Qo'shimcha belgilar (+1 ball)
        negative_features:Qarama-qarshi belgilar (-3 ball)
        discriminators:   Differensial uchun eng muhim belgilar (o'zbek tilida)
        red_flags:        Xavfli belgilar (tezkor murojaat)
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

    def get_name(self, lang: str) -> str:
        if lang == "ru":
            return self.name_ru
        if lang == "en":
            return self.name_en
        return self.name_uz
