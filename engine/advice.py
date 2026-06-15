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
