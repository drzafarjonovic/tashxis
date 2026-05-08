import os
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or os.getenv("AI_API_KEY")

SYSTEM_PROMPTS = {
    "uz": (
        "Sen stomatologik yordamchi botsan. Faqat berilgan tashxisni oddiy, tushunarli o'zbek tilida "
        "izohla. Yangi tashxis qo'shma. Tibbiy terminlarni oddiy so'zlar bilan tushuntir. "
        "3 qismda yoz: 1) bu nima, 2) sababi, 3) bemor nima qilishi kerak. Juda qisqa (5-7 jumla)."
    ),
    "ru": (
        "Ты стоматологический бот-помощник. Объясни только предоставленный диагноз простым понятным "
        "русским языком. Не добавляй новых диагнозов. Медицинские термины объясняй простыми словами. "
        "Пиши в 3 частях: 1) что это, 2) причина, 3) что делать. Очень кратко (5-7 предложений)."
    ),
    "en": (
        "You are a dental assistant bot. Explain only the given diagnosis in simple, clear English. "
        "Do not add new diagnoses. Explain medical terms in plain words. "
        "Write in 3 parts: 1) what it is, 2) cause, 3) what to do. Very brief (5-7 sentences)."
    ),
}


def explain_diagnosis(
    diagnosis: str,
    symptoms: Dict[str, Any],
    lang: str = "uz",
) -> str:
    fallback = {
        "uz": f"Bu holat bo'yicha batafsil ma'lumot olish uchun stomatologga murojaat qiling.",
        "ru": "Для получения подробной информации обратитесь к стоматологу.",
        "en": "Please see a dentist for more detailed information about this condition.",
    }

    if not GROQ_API_KEY:
        logger.warning("GROQ_API_KEY topilmadi — fallback qaytarilmoqda.")
        return fallback.get(lang, fallback["uz"])

    prompt_map = {
        "uz": f"Tashxis: {diagnosis}\nBelgilar: {symptoms}\n\nIzohla:",
        "ru": f"Диагноз: {diagnosis}\nСимптомы: {symptoms}\n\nОбъясни:",
        "en": f"Diagnosis: {diagnosis}\nSymptoms: {symptoms}\n\nExplain:",
    }

    try:
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPTS.get(lang, SYSTEM_PROMPTS["uz"])},
                {"role": "user",   "content": prompt_map.get(lang, prompt_map["uz"])},
            ],
            max_tokens=300,
            temperature=0.4,
        )
        return response.choices[0].message.content.strip()

    except Exception as exc:
        logger.error(f"Groq API xatoligi: {exc}")
        return fallback.get(lang, fallback["uz"])
