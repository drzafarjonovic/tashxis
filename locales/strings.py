"""
Barcha UI matnlari uchun tarjimalar (uz / ru / en).

Telegram'ga HTML parse rejimida yuboriladi: <b>...</b>, <i>...</i>.
Dinamik (foydalanuvchi yoki kasallikdan kelgan) matnlar handlers'da
html.escape() bilan ekranlanadi.
"""

STRINGS = {
    # ── START ────────────────────────────────────────────────────
    "welcome": {
        "uz": (
            "👋 Assalomu alaykum!\n\n"
            "Men stomatologik yordamchi botman.\n"
            "Savollar orqali sizning shikoyatingizga mos tashxis topishga harakat qilaman.\n\n"
            "⚠️ Bu bot tibbiy maslahat emas. Aniq tashxis uchun shifokorga murojaat qiling.\n\n"
            "Tilni tanlang 👇"
        ),
        "ru": (
            "👋 Здравствуйте!\n\n"
            "Я стоматологический бот-помощник.\n"
            "Задавая вопросы, постараюсь подобрать диагноз под ваши жалобы.\n\n"
            "⚠️ Это не медицинская консультация. Для точного диагноза обратитесь к врачу.\n\n"
            "Выберите язык 👇"
        ),
        "en": (
            "👋 Hello!\n\n"
            "I am a dental assistant bot.\n"
            "I will ask questions to help find a diagnosis that matches your complaint.\n\n"
            "⚠️ This is not medical advice. See a dentist for an accurate diagnosis.\n\n"
            "Choose your language 👇"
        ),
    },
    "menu_hint": {
        "uz": "Boshlash uchun pastdagi tugmani bosing 👇",
        "ru": "Нажмите кнопку ниже, чтобы начать 👇",
        "en": "Press the button below to start 👇",
    },
    "lang_set": {
        "uz": "✅ Til: O'zbek",
        "ru": "✅ Язык: Русский",
        "en": "✅ Language: English",
    },
    "start_btn": {
        "uz": "🦷 Tashxisni boshlash",
        "ru": "🦷 Начать диагностику",
        "en": "🦷 Start diagnosis",
    },
    "help_btn": {
        "uz": "❓ Yordam",
        "ru": "❓ Помощь",
        "en": "❓ Help",
    },
    "help_text": {
        "uz": (
            "ℹ️ <b>Qanday ishlaydi?</b>\n\n"
            "1. «Tashxisni boshlash»ni bosing\n"
            "2. Har bir savolga «Ha» yoki «Yo'q» deb javob bering\n"
            "3. Bot belgilaringizga mos tashxisni taklif qiladi\n\n"
            "Qayta boshlash uchun /start buyrug'ini yuboring."
        ),
        "ru": (
            "ℹ️ <b>Как это работает?</b>\n\n"
            "1. Нажмите «Начать диагностику»\n"
            "2. Отвечайте «Да» или «Нет» на каждый вопрос\n"
            "3. Бот предложит диагноз, подходящий под ваши симптомы\n\n"
            "Для перезапуска отправьте /start."
        ),
        "en": (
            "ℹ️ <b>How does it work?</b>\n\n"
            "1. Press 'Start diagnosis'\n"
            "2. Answer 'Yes' or 'No' to each question\n"
            "3. The bot suggests a diagnosis matching your symptoms\n\n"
            "Send /start to restart."
        ),
    },

    # ── TRIAGE ───────────────────────────────────────────────────
    "choose_location": {
        "uz": "1️⃣ Muammo qayerda?\n\nQuyidagi variantlardan birini tanlang:",
        "ru": "1️⃣ Где находится проблема?\n\nВыберите один из вариантов:",
        "en": "1️⃣ Where is the problem?\n\nChoose one of the options:",
    },
    "loc_tooth": {
        "uz": "🦷 Tishda",
        "ru": "🦷 В зубе",
        "en": "🦷 In the tooth",
    },
    "loc_gum": {
        "uz": "🩸 Milkda",
        "ru": "🩸 В дёсне",
        "en": "🩸 In the gum",
    },
    "loc_mucosa": {
        "uz": "👄 Og'iz ichida (yara/oq qatlam/pufakcha)",
        "ru": "👄 В полости рта (язва/налёт/пузырьки)",
        "en": "👄 Inside the mouth (ulcer/patch/blisters)",
    },
    "loc_jaw": {
        "uz": "🦴 Jag' yoki yuzda",
        "ru": "🦴 В челюсти или лице",
        "en": "🦴 In the jaw or face",
    },
    "loc_tmj": {
        "uz": "😬 Jag' bo'g'imi (chaynashda og'riq/shiqillash)",
        "ru": "😬 Челюстной сустав (боль/щелчки при жевании)",
        "en": "😬 Jaw joint (pain/clicking when chewing)",
    },
    "loc_trauma": {
        "uz": "🤕 Jarohat (tish sindi, qimirladi, tushdi)",
        "ru": "🤕 Травма (зуб сломан, подвижен, выбит)",
        "en": "🤕 Injury (tooth broken, loose, knocked out)",
    },
    "loc_dentition": {
        "uz": "🦷 Tish soni/shakli/joylashuvi yoki tishlash",
        "ru": "🦷 Число/форма/положение зубов или прикус",
        "en": "🦷 Tooth count/shape/position or bite",
    },
    "loc_salivary": {
        "uz": "💧 So'lak bezi / og'iz qurishi / bez shishi",
        "ru": "💧 Слюнная железа / сухость рта / припухлость",
        "en": "💧 Salivary gland / dry mouth / gland swelling",
    },

    # ── SAVOL / JAVOB ─────────────────────────────────────────────
    "yes_btn": {
        "uz": "✅ Ha",
        "ru": "✅ Да",
        "en": "✅ Yes",
    },
    "no_btn": {
        "uz": "❌ Yo'q",
        "ru": "❌ Нет",
        "en": "❌ No",
    },
    "analyzing": {
        "uz": "⏳ Tahlil qilinmoqda...",
        "ru": "⏳ Анализируется...",
        "en": "⏳ Analysing...",
    },
    "question_prefix": {
        "uz": "Savol",
        "ru": "Вопрос",
        "en": "Question",
    },

    # ── NATIJA ────────────────────────────────────────────────────
    "result_header": {
        "uz": "🩺 <b>Tashxis natijasi</b>",
        "ru": "🩺 <b>Результат диагностики</b>",
        "en": "🩺 <b>Diagnosis result</b>",
    },
    "top_diagnosis": {
        "uz": "Asosiy tashxis ehtimoli",
        "ru": "Наиболее вероятный диагноз",
        "en": "Most likely diagnosis",
    },
    "confidence_label": {
        "uz": "Ehtimollik",
        "ru": "Вероятность",
        "en": "Confidence",
    },
    "alternatives_label": {
        "uz": "Muqobil variantlar",
        "ru": "Альтернативные варианты",
        "en": "Alternative possibilities",
    },
    "uncertain_result": {
        "uz": (
            "🤔 <b>Aniq tashxis qo'yib bo'lmadi.</b>\n\n"
            "Belgilaringiz bir nechta holatga to'g'ri kelishi mumkin. "
            "Eng ehtimolli variant quyida, ammo ishonchlilik past."
        ),
        "ru": (
            "🤔 <b>Не удалось поставить точный диагноз.</b>\n\n"
            "Ваши симптомы могут соответствовать нескольким состояниям. "
            "Ниже наиболее вероятный вариант, но уверенность низкая."
        ),
        "en": (
            "🤔 <b>Could not determine a clear diagnosis.</b>\n\n"
            "Your symptoms may match several conditions. "
            "The most likely option is shown below, but confidence is low."
        ),
    },
    "red_flags_label": {
        "uz": "⚠️ Zudlik bilan shifokorga:",
        "ru": "⚠️ Срочно к врачу при:",
        "en": "⚠️ See a doctor urgently if:",
    },
    "ai_explanation_label": {
        "uz": "💡 Tushuntirish:",
        "ru": "💡 Объяснение:",
        "en": "💡 Explanation:",
    },
    "about_disease_label": {
        "uz": "Kasallik haqida",
        "ru": "О заболевании",
        "en": "About the condition",
    },
    "symptoms_label": {
        "uz": "Asosiy belgilar",
        "ru": "Основные симптомы",
        "en": "Key symptoms",
    },
    "differential_label": {
        "uz": "Farqlash (differensial tashxis)",
        "ru": "Дифференциальная диагностика",
        "en": "Differential diagnosis",
    },
    "treatment_label": {
        "uz": "Davolash / nima qilish kerak",
        "ru": "Лечение / что делать",
        "en": "Treatment / what to do",
    },
    "disclaimer": {
        "uz": "<i>(Bu natija tibbiy xulosa emas. Aniq tashxis uchun stomatologga murojaat qiling.)</i>",
        "ru": "<i>(Этот результат не является медицинским заключением. Обратитесь к стоматологу.)</i>",
        "en": "<i>(This result is not a medical conclusion. Please see a dentist for an accurate diagnosis.)</i>",
    },
    "restart_hint": {
        "uz": "Qayta tekshirish uchun /start yuboring.",
        "ru": "Для повторной диагностики отправьте /start.",
        "en": "Send /start to run a new check.",
    },

    # ── RED FLAG ──────────────────────────────────────────────────
    "red_flag_alert": {
        "uz": (
            "🚨 <b>DIQQAT — XAVFLI BELGILAR ANIQLANDI!</b>\n\n"
            "Yuqori isitma va yuz/jag'dagi shish bir vaqtda mavjud.\n"
            "Bu <b>yiringli jarayon</b> bo'lishi mumkin.\n\n"
            "⛑ <b>Zudlik bilan yuz-jag' xirurgiga yoki shoshilinch yordamga murojaat qiling!</b>\n\n"
            "Kechikish hayot uchun xavfli bo'lishi mumkin."
        ),
        "ru": (
            "🚨 <b>ВНИМАНИЕ — ОБНАРУЖЕНЫ ОПАСНЫЕ ПРИЗНАКИ!</b>\n\n"
            "Высокая температура и отёк лица/челюсти одновременно.\n"
            "Это может быть <b>гнойный процесс</b>.\n\n"
            "⛑ <b>Немедленно обратитесь к челюстно-лицевому хирургу или в скорую!</b>\n\n"
            "Промедление может быть опасно для жизни."
        ),
        "en": (
            "🚨 <b>WARNING — DANGEROUS SIGNS DETECTED!</b>\n\n"
            "High fever and facial/jaw swelling are present at the same time.\n"
            "This could be a <b>purulent (abscess) process</b>.\n\n"
            "⛑ <b>Seek a maxillofacial surgeon or emergency services immediately!</b>\n\n"
            "Delay may be life-threatening."
        ),
    },

    # ── XATO / HOLAT ──────────────────────────────────────────────
    "unknown_command": {
        "uz": "Tushunmadim. /start buyrug'ini yuboring.",
        "ru": "Не понял. Отправьте /start.",
        "en": "Didn't understand. Please send /start.",
    },
    "session_expired": {
        "uz": "Seans tugagan. Iltimos, /start buyrug'ini yuboring.",
        "ru": "Сессия истекла. Пожалуйста, отправьте /start.",
        "en": "Session expired. Please send /start.",
    },

    # ── JOYLASHUVNI ANIQLASH (tish) ───────────────────────────────
    "loc_step_prefix": {
        "uz": "📍 Joylashuvni aniqlaymiz",
        "ru": "📍 Уточним расположение",
        "en": "📍 Let's pinpoint the location",
    },
    "loc_q_jaw": {
        "uz": "Muammo qaysi jag'da?",
        "ru": "На какой челюсти проблема?",
        "en": "Which jaw is affected?",
    },
    "loc_q_side": {
        "uz": "Qaysi tomonda?",
        "ru": "С какой стороны?",
        "en": "Which side?",
    },
    "loc_q_type": {
        "uz": "Qaysi tish (turi)?",
        "ru": "Какой зуб (тип)?",
        "en": "Which tooth (type)?",
    },
    "loc_opt_upper": {"uz": "⬆️ Yuqori jag'", "ru": "⬆️ Верхняя", "en": "⬆️ Upper"},
    "loc_opt_lower": {"uz": "⬇️ Pastki jag'", "ru": "⬇️ Нижняя", "en": "⬇️ Lower"},
    "loc_opt_right": {"uz": "➡️ O'ng tomon", "ru": "➡️ Правая", "en": "➡️ Right"},
    "loc_opt_left": {"uz": "⬅️ Chap tomon", "ru": "⬅️ Левая", "en": "⬅️ Left"},
    "loc_opt_incisor": {"uz": "Kurak tish", "ru": "Резец", "en": "Incisor"},
    "loc_opt_canine": {"uz": "Qoziq tish", "ru": "Клык", "en": "Canine"},
    "loc_opt_premolar": {"uz": "Kichik oziq (premolyar)", "ru": "Малый коренной (премоляр)", "en": "Premolar"},
    "loc_opt_molar": {"uz": "Katta oziq (molyar)", "ru": "Большой коренной (моляр)", "en": "Molar"},
    "loc_opt_unknown": {"uz": "🤷 Bilmayman / aniq emas", "ru": "🤷 Не знаю / не уверен", "en": "🤷 Not sure"},
    "loc_area_label": {
        "uz": "Ko'rsatilgan soha",
        "ru": "Указанная область",
        "en": "Indicated area",
    },

    # ── KASALLIKLAR MA'LUMOTNOMASI ────────────────────────────────
    "reference_btn": {
        "uz": "📚 Kasalliklar ma'lumotnomasi",
        "ru": "📚 Справочник заболеваний",
        "en": "📚 Disease reference",
    },
    "ref_choose_category": {
        "uz": "📚 <b>Kasalliklar ma'lumotnomasi</b>\n\nBo'limni tanlang:",
        "ru": "📚 <b>Справочник заболеваний</b>\n\nВыберите раздел:",
        "en": "📚 <b>Disease reference</b>\n\nChoose a section:",
    },
    "ref_choose_disease": {
        "uz": "Kasallikni tanlang:",
        "ru": "Выберите заболевание:",
        "en": "Choose a condition:",
    },
    "ref_back_to_categories": {
        "uz": "⬅️ Bo'limlarga qaytish",
        "ru": "⬅️ К разделам",
        "en": "⬅️ Back to sections",
    },
    "ref_back_to_list": {
        "uz": "⬅️ Ro'yxatga qaytish",
        "ru": "⬅️ К списку",
        "en": "⬅️ Back to list",
    },
    "ref_prev": {"uz": "◀️ Oldingi", "ru": "◀️ Назад", "en": "◀️ Prev"},
    "ref_next": {"uz": "Keyingi ▶️", "ru": "Далее ▶️", "en": "Next ▶️"},
    "ref_cat_tooth": {"uz": "🦷 Tish qattiq to'qimalari", "ru": "🦷 Твёрдые ткани зуба", "en": "🦷 Hard dental tissues"},
    "ref_cat_pulp": {"uz": "🔴 Pulpa kasalliklari", "ru": "🔴 Заболевания пульпы", "en": "🔴 Pulp diseases"},
    "ref_cat_periapical": {"uz": "🦷 Periapikal kasalliklar", "ru": "🦷 Периапикальные заболевания", "en": "🦷 Periapical diseases"},
    "ref_cat_periodontal": {"uz": "🩸 Parodont kasalliklari", "ru": "🩸 Заболевания пародонта", "en": "🩸 Periodontal diseases"},
    "ref_cat_mucosa": {"uz": "👄 Shilliq qavat, til, lab", "ru": "👄 Слизистая, язык, губы", "en": "👄 Mucosa, tongue, lips"},
    "ref_cat_jaw": {"uz": "🦴 Jag' suyaklari", "ru": "🦴 Челюстные кости", "en": "🦴 Jaw bones"},
    "ref_cat_tmj": {"uz": "😬 Jag' bo'g'imi (TMJ)", "ru": "😬 Сустав (ВНЧС)", "en": "😬 Jaw joint (TMJ)"},
    "ref_cat_trauma": {"uz": "🤕 Travmatik shikastlanishlar", "ru": "🤕 Травматические повреждения", "en": "🤕 Traumatic injuries"},
    "ref_cat_dentition": {"uz": "🦷 Rivojlanish va ortodontik", "ru": "🦷 Развитие и ортодонтия", "en": "🦷 Development & orthodontics"},
    "ref_cat_salivary": {"uz": "💧 So'lak bezlari", "ru": "💧 Слюнные железы", "en": "💧 Salivary glands"},
}


def t(key: str, lang: str = "uz") -> str:
    """Qisqa tarjima funksiyasi."""
    block = STRINGS.get(key, {})
    return block.get(lang, block.get("uz", key))
