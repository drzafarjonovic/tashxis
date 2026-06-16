"""
Avtomatik tavsiya matni — AI o'chirilgan (v1.1) bo'lganda ishlatiladi.

Tushuntirish kasallik ma'lumotlaridan (belgilar va red-flag'lardan) tuziladi,
shuningdek kategoriya bo'yicha umumiy "keyingi qadam" tavsiyasi qo'shiladi.
AI v2.0 da yoqilganda bu matn o'rniga jonli izoh ishlatiladi.
"""

from __future__ import annotations

from medical.disease_model import Disease

# Kategoriya bo'yicha umumiy tavsiya (3 tilda)
_NEXT_STEPS = {
    "tooth": {
        "uz": "Tishni tekshirtirish va davolash uchun stomatolog-terapevtga murojaat qiling.",
        "ru": "Обратитесь к стоматологу-терапевту для осмотра и лечения зуба.",
        "en": "See a general dentist to examine and treat the tooth.",
    },
    "pulp": {
        "uz": "Bu pulpa (tish nervi) bilan bog'liq bo'lishi mumkin — tezroq stomatologga boring, "
              "kanal davolash kerak bo'lishi mumkin.",
        "ru": "Это может быть связано с пульпой (нервом зуба) — обратитесь к стоматологу скорее, "
              "возможно потребуется лечение каналов.",
        "en": "This may involve the pulp (tooth nerve) — see a dentist soon; root canal treatment may be needed.",
    },
    "periapical": {
        "uz": "Tish ildizi atrofidagi jarayonga shubha — rentgen va stomatolog ko'rigi zarur.",
        "ru": "Подозрение на процесс вокруг корня зуба — нужен рентген и осмотр стоматолога.",
        "en": "A process around the tooth root is suspected — an X-ray and dentist exam are needed.",
    },
    "periodontal": {
        "uz": "Milk va tish atrofi to'qimalari bilan bog'liq — parodontolog ko'rigidan o'ting.",
        "ru": "Связано с дёснами и тканями вокруг зуба — пройдите осмотр у пародонтолога.",
        "en": "This involves the gums and tissues around the tooth — see a periodontist.",
    },
    "mucosa": {
        "uz": "Og'iz shilliq qavati bilan bog'liq. Agar belgilar 2 haftadan ortiq saqlansa, "
              "albatta mutaxassisga ko'rining.",
        "ru": "Связано со слизистой полости рта. Если симптомы держатся дольше 2 недель, "
              "обязательно обратитесь к специалисту.",
        "en": "This involves the oral mucosa. If symptoms last more than 2 weeks, see a specialist.",
    },
    "jaw": {
        "uz": "Jag' suyagi bilan bog'liq jiddiy holat bo'lishi mumkin — yuz-jag' jarrohiga murojaat qiling.",
        "ru": "Может быть серьёзным состоянием челюстной кости — обратитесь к челюстно-лицевому хирургу.",
        "en": "This may be a serious jawbone condition — see a maxillofacial surgeon.",
    },
    "tmj": {
        "uz": "Chakka-pastki jag' bo'g'imi (TMJ) bilan bog'liq — gnatolog yoki yuz-jag' mutaxassisiga "
              "murojaat qiling; tungi kapa va stress/bruksizmni kamaytirish yordam berishi mumkin.",
        "ru": "Связано с височно-нижнечелюстным суставом (ВНЧС) — обратитесь к гнатологу или "
              "челюстно-лицевому специалисту; помогает ночная капа и снижение нагрузки/бруксизма.",
        "en": "This involves the temporomandibular joint (TMJ) — see a TMJ specialist; a night guard "
              "and reducing clenching/bruxism may help.",
    },
    "trauma": {
        "uz": "Tish/jag' jarohati — iloji boricha tezroq stomatologga boring. Tish tushib qolgan bo'lsa, "
              "uni ildizidan ushlamasdan sutda yoki so'lakda saqlab, 30 daqiqa ichida murojaat qiling.",
        "ru": "Травма зуба/челюсти — обратитесь к стоматологу как можно скорее. Если зуб выбит, храните "
              "его в молоке или слюне (не трогая корень) и обратитесь в течение 30 минут.",
        "en": "Dental/jaw injury — see a dentist as soon as possible. If a tooth was knocked out, store it "
              "in milk or saliva (do not touch the root) and seek care within 30 minutes.",
    },
    "dentition": {
        "uz": "Tish chiqishi/joylashuvi yoki tishlash anomaliyasi — ortodont (va kerak bo'lsa "
              "yuz-jag' jarrohi) ko'rigidan o'ting; rentgen tashxisni aniqlashtiradi.",
        "ru": "Аномалия прорезывания/положения зубов или прикуса — пройдите осмотр ортодонта "
              "(при необходимости — хирурга); рентген уточнит диагноз.",
        "en": "An anomaly of tooth eruption/position or bite — see an orthodontist (and a surgeon if "
              "needed); an X-ray will clarify the diagnosis.",
    },
    "salivary": {
        "uz": "So'lak bezlari bilan bog'liq — stomatolog yoki yuz-jag' jarrohiga murojaat qiling. "
              "Og'iz qurishida ko'p suv iching; bez shishi uzoq davom etsa, albatta tekshiruvdan o'ting.",
        "ru": "Связано со слюнными железами — обратитесь к стоматологу или челюстно-лицевому хирургу. "
              "При сухости рта пейте больше воды; при длительной припухлости обязательно обследуйтесь.",
        "en": "This involves the salivary glands — see a dentist or maxillofacial surgeon. For dry mouth, "
              "drink more water; if gland swelling persists, get it examined.",
    },
}

_SIGNS_LABEL = {
    "uz": "Asosiy belgilar",
    "ru": "Основные признаки",
    "en": "Key signs",
}

_RECOMMEND_LABEL = {
    "uz": "Tavsiya",
    "ru": "Рекомендация",
    "en": "Recommendation",
}


def build_explanation(disease: Disease, category: str, lang: str = "uz") -> str:
    """Kasallik uchun avtomatik (AI'siz) tushuntirish matnini tuzadi."""
    parts: list[str] = []

    signs = disease.discriminators[:3]
    if signs:
        label = _SIGNS_LABEL.get(lang, _SIGNS_LABEL["uz"])
        parts.append(f"{label}: " + "; ".join(signs) + ".")

    steps = _NEXT_STEPS.get(category, {})
    step_text = steps.get(lang, steps.get("uz"))
    if step_text:
        label = _RECOMMEND_LABEL.get(lang, _RECOMMEND_LABEL["uz"])
        parts.append(f"{label}: {step_text}")

    return "\n".join(parts)
