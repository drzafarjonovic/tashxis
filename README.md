<!-- Tillar / Языки / Languages -->
**🇺🇿 [O'zbekcha](#-oral-detect--ozbekcha) · 🇷🇺 [Русский](#-oral-detect--русский) · 🇬🇧 [English](#-oral-detect--english)**

---

# 🦷 Oral Detect — O'zbekcha

**Oral Detect** — og'iz bo'shlig'i, tish, milk va jag' kasalliklari bo'yicha
dastlabki (triage) baholash beruvchi aqlli Telegram-bot. Savol-javob orqali eng
ehtimolli tashxisni topadi, kasallik haqida to'liq ma'lumot beradi va keyingi
qadam bo'yicha tavsiya qiladi.

> ⚠️ **Ogohlantirish:** Bu bot tibbiy maslahat yoki shifokor o'rnini bosmaydi.
> Natija dastlabki yo'naltirish xarakteriga ega. Aniq tashxis va davolash uchun
> stomatologga murojaat qiling.

## ✨ Asosiy imkoniyatlar
- **121 ta kasallik** — 13 klinik toifa (tish to'qimalari, pulpa, periapikal,
  parodont, shilliq qavat/til/lab, jag', TMJ, travma, rivojlanish/ortodontik,
  so'lak bezlari va boshqalar).
- **Aqlli tashxis yadrosi** — Bayes ehtimollik + information-gain. Har savol
  yetakchi kasalliklarni eng yaxshi ajratadiganidan tanlanadi (o'rtacha ~7 savol).
- **Klinik priorlar + demografiya** — yosh va jins tashxis ehtimolligiga ta'sir
  qiladi (epidemiologik prior: tarqalganlik × yosh × jins).
- **Anatomik joylashuv** — qaysi jag'/tomon/tish turi matematik modelga kiradi
  (`P(D | S, L)`).
- **Kasalliklar ma'lumotnomasi** — istalgan kasallikni qidirib, tavsif, simptomlar,
  differensial tashxis va davolash haqida o'qish.
- **3 til** — o'zbek, rus, ingliz.
- **Admin bilan aloqa** — bot ichida xabar yuborish va javob olish.
- **Admin audit/hisobotlar** — kunlik/haftalik/oylik/interval va individual
  hisobotlar (Excel + PDF + grafik).

## 🔄 Qanday ishlaydi (foydalanuvchi uchun)
1. `/start` — til tanlash (3 tilda yo'riqnoma chiqadi)
2. «Tashxisni boshlash» → yosh va jins
3. Muammo joyini tanlash (tish, milk, shilliq, jag' va h.k.)
4. Tish bo'lsa — qaysi jag'/tomon/tish turi
5. «Ha/Yo'q» savollarga javob berish
6. Natija: ehtimolli tashxis + kasallik haqida ma'lumot + tavsiya

## 🛠 Texnologiyalar
- Python 3.12 · [aiogram 3](https://docs.aiogram.dev/) (Telegram)
- PostgreSQL (Supabase) — `asyncpg` (ixtiyoriy)
- openpyxl · reportlab · matplotlib — hisobotlar
- Deploy: Railway (NIXPACKS) + health-check web server

## ⚙️ O'rnatish va sozlash
```bash
git clone https://github.com/drzafarjonovic/tashxis.git
cd tashxis
pip install -r requirements.txt
cp .env.example .env   # qiymatlarni to'ldiring
python main.py
```

### Muhit o'zgaruvchilari (env)
| O'zgaruvchi | Majburiy | Tavsif |
|---|---|---|
| `BOT_TOKEN` | ✅ | BotFather'dan olingan token |
| `DATABASE_URL` | ❌ | Postgres ulanishi (hisobotlar uchun zarur) |
| `ADMIN_ID` | ❌ | Admin Telegram ID si (audit/aloqa uchun) |
| `ADMIN_USERNAME` | ❌ | To'g'ridan-to'g'ri havola uchun |
| `AI_ENABLED` | ❌ | AI izohlar (hozircha `false`) |
| `GROQ_API_KEY` | ❌ | AI yoqilganda kerak |
| `PORT` | ❌ | Health-check porti (Railway avtomatik beradi) |

> ID ni bilish uchun botga `/myid` yuboring. Admin akkaunti botga avval
> `/start` bosishi shart (Telegram boti suhbatni o'zi boshlay olmaydi).

## 👮 Admin imkoniyatlari
- `/admin` — hisobotlar paneli (kunlik/haftalik/oylik/umumiy/interval, individual,
  obunachilar ro'yxati) — har biri Excel + PDF + grafik.
- `/reply <user_id> matn` — foydalanuvchiga javob berish.
- `/myid` — o'z ID ingizni va admin holatini tekshirish.

## 📜 Litsenziya / Mualliflik
Tibbiy ma'lumot ochiq stomatologiya manbalari asosida, faqat ma'lumot maqsadida.

---

# 🦷 Oral Detect — Русский

**Oral Detect** — умный Telegram-бот для предварительной (триаж) оценки
заболеваний полости рта, зубов, дёсен и челюсти. С помощью вопросов подбирает
наиболее вероятный диагноз, даёт полную информацию о заболевании и рекомендацию
по дальнейшим действиям.

> ⚠️ **Внимание:** Бот не заменяет медицинскую консультацию или врача. Результат
> носит ориентировочный характер. Для точного диагноза и лечения обратитесь к
> стоматологу.

## ✨ Возможности
- **121 заболевание** — 13 клинических разделов (твёрдые ткани зуба, пульпа,
  периапикальные, пародонт, слизистая/язык/губы, челюсть, ВНЧС, травмы,
  развитие/ортодонтия, слюнные железы и др.).
- **Умное ядро диагностики** — байесовская вероятность + information-gain.
  Каждый вопрос лучше всего разделяет ведущие диагнозы (в среднем ~7 вопросов).
- **Клинические приоры + демография** — возраст и пол влияют на вероятность
  диагноза (эпидемиологический приор: распространённость × возраст × пол).
- **Анатомическая локализация** — какая челюсть/сторона/тип зуба входит в
  математическую модель (`P(D | S, L)`).
- **Справочник заболеваний** — поиск любого заболевания: описание, симптомы,
  дифференциальная диагностика, лечение.
- **3 языка** — узбекский, русский, английский.
- **Связь с админом** — отправка сообщения в боте и получение ответа.
- **Аудит/отчёты для админа** — дневные/недельные/месячные/интервальные и
  индивидуальные отчёты (Excel + PDF + график).

## 🔄 Как это работает
1. `/start` — выбор языка (инструкция на 3 языках)
2. «Начать диагностику» → возраст и пол
3. Выбор места проблемы (зуб, десна, слизистая, челюсть и т.д.)
4. Если зуб — челюсть/сторона/тип зуба
5. Ответы «Да/Нет» на вопросы
6. Результат: вероятный диагноз + информация + рекомендация

## 🛠 Технологии
- Python 3.12 · aiogram 3 (Telegram)
- PostgreSQL (Supabase) — `asyncpg` (опционально)
- openpyxl · reportlab · matplotlib — отчёты
- Деплой: Railway (NIXPACKS) + health-check сервер

## ⚙️ Установка
```bash
git clone https://github.com/drzafarjonovic/tashxis.git
cd tashxis
pip install -r requirements.txt
cp .env.example .env   # заполните значения
python main.py
```

### Переменные окружения
| Переменная | Обязательна | Описание |
|---|---|---|
| `BOT_TOKEN` | ✅ | Токен от BotFather |
| `DATABASE_URL` | ❌ | Подключение Postgres (нужно для отчётов) |
| `ADMIN_ID` | ❌ | Telegram ID админа (аудит/связь) |
| `ADMIN_USERNAME` | ❌ | Для прямой ссылки |
| `AI_ENABLED` | ❌ | AI-пояснения (пока `false`) |
| `GROQ_API_KEY` | ❌ | Нужен при включённом AI |
| `PORT` | ❌ | Порт health-check (Railway задаёт сам) |

> Чтобы узнать ID, отправьте боту `/myid`. Аккаунт админа должен сначала нажать
> `/start` в боте (бот не может начать диалог первым).

## 👮 Возможности админа
- `/admin` — панель отчётов (день/неделя/месяц/всё/интервал, индивидуальный,
  список подписчиков) — каждый в Excel + PDF + график.
- `/reply <user_id> текст` — ответить пользователю.
- `/myid` — проверить свой ID и статус админа.

## 📜 Лицензия / Авторство
Медицинская информация основана на открытых стоматологических источниках и носит
исключительно информационный характер.

---

# 🦷 Oral Detect — English

**Oral Detect** is a smart Telegram bot for preliminary (triage) assessment of
oral, dental, gum and jaw conditions. Through a question-and-answer flow it finds
the most likely diagnosis, provides full information about the condition and
recommends next steps.

> ⚠️ **Disclaimer:** This bot does not replace medical advice or a dentist. The
> result is for orientation only. See a dentist for an accurate diagnosis and
> treatment.

## ✨ Features
- **121 conditions** across 13 clinical categories (hard dental tissues, pulp,
  periapical, periodontal, mucosa/tongue/lips, jaw, TMJ, trauma,
  development/orthodontics, salivary glands, and more).
- **Smart diagnostic core** — Bayesian probability + information gain. Each
  question best separates the leading diagnoses (~7 questions on average).
- **Clinical priors + demographics** — age and sex influence diagnosis
  probability (epidemiological prior: prevalence × age × sex).
- **Anatomical location** — which jaw/side/tooth type enters the math model
  (`P(D | S, L)`).
- **Disease reference** — look up any condition: description, symptoms,
  differential diagnosis, treatment.
- **3 languages** — Uzbek, Russian, English.
- **Admin contact** — send a message in-bot and receive a reply.
- **Admin audit/reports** — daily/weekly/monthly/custom-interval and per-user
  reports (Excel + PDF + chart).

## 🔄 How it works
1. `/start` — choose language (instructions in 3 languages)
2. "Start diagnosis" → age and sex
3. Choose the problem area (tooth, gum, mucosa, jaw, etc.)
4. For a tooth — jaw/side/tooth type
5. Answer "Yes/No" questions
6. Result: likely diagnosis + condition info + recommendation

## 🛠 Tech stack
- Python 3.12 · aiogram 3 (Telegram)
- PostgreSQL (Supabase) — `asyncpg` (optional)
- openpyxl · reportlab · matplotlib — reports
- Deploy: Railway (NIXPACKS) + health-check web server

## ⚙️ Setup
```bash
git clone https://github.com/drzafarjonovic/tashxis.git
cd tashxis
pip install -r requirements.txt
cp .env.example .env   # fill in values
python main.py
```

### Environment variables
| Variable | Required | Description |
|---|---|---|
| `BOT_TOKEN` | ✅ | Token from BotFather |
| `DATABASE_URL` | ❌ | Postgres connection (needed for reports) |
| `ADMIN_ID` | ❌ | Admin Telegram ID (audit/contact) |
| `ADMIN_USERNAME` | ❌ | For a direct link |
| `AI_ENABLED` | ❌ | AI explanations (currently `false`) |
| `GROQ_API_KEY` | ❌ | Needed when AI is enabled |
| `PORT` | ❌ | Health-check port (Railway sets it) |

> To find your ID, send `/myid` to the bot. The admin account must press `/start`
> in the bot first (a bot cannot initiate a conversation).

## 👮 Admin features
- `/admin` — reports panel (daily/weekly/monthly/all/interval, per-user,
  subscriber list) — each as Excel + PDF + chart.
- `/reply <user_id> text` — reply to a user.
- `/myid` — check your ID and admin status.

## 📜 License / Attribution
Medical content is based on open stomatology sources and is for informational
purposes only.

---

<sub>Oral Detect · v1.7.0 · Made with 🦷 by drzafarjonovic</sub>
