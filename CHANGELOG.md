# Changelog

## [1.7.4] - 2026-06 — /dbtest qotib qolishi tuzatildi

- `/dbtest` natijasi endi **oddiy matn** sifatida yuboriladi (HTML parse'siz) —
  asyncpg xatosidagi `< > &` belgilari xabarni buzmaydi (avval "tekshirilmoqda"da
  qotib qolardi).
- Ulanish diagnostikasiga **qat'iy timeout** (`asyncio.wait_for`, 15s) qo'shildi —
  endi har doim natija qaytaradi.

## [1.7.3] - 2026-06 — DB diagnostikasi (/dbtest) va mustahkam ulanish

- Yangi **`/dbtest`** admin buyrug'i: jonli ulanishni sinaydi va **aniq xato
  matnini** to'g'ridan-to'g'ri Telegram'da ko'rsatadi (Railway loglarisiz tashxis).
- `init_db` da ulanish va sxema ajratildi: sxema xatosi endi DB'ni o'chirmaydi
  (jadvallar mavjud bo'lsa hisobotlar ishlaydi).
- Sxema bayonotlari bittalab qo'llanadi (Supabase pooler uchun xavfsizroq).

## [1.7.2] - 2026-06 — /admin va DB diagnostikasi

- `/admin` endi jim qolmaydi: admin emas yoki ADMIN_ID sozlanmagan bo'lsa aniq
  sabab va yo'riqnoma beradi; DB ulanmagan bo'lsa pooler/loglarni tekshirishni
  taklif qiladi.
- `/myid` ga **DB holati** qo'shildi (✅ ulangan / ❌ ulanmagan) — bir buyruqда
  admin va baza holatini tekshirish.

## [1.7.1] - 2026-06 — DB ulanishini mustahkamlash (Supabase/Railway)

- `asyncpg` ulanishiga **SSL** (Supabase talabi), **`statement_cache_size=0`**
  (Supabase pooler transaction-mode mosligi) va ulanish **timeout** qo'shildi.
- Ulanish xatosi loglari aniqroq: xato turi/matni + Railway IPv6 eslatmasi.
- `.env.example`: Railway uchun **Connection Pooler (IPv4)** URL'ini ishlatish
  bo'yicha ko'rsatma (direct `db.xxx.supabase.co` IPv6-only — Railway'da ishlamaydi).

## [1.7.0] - 2026-06 — Admin audit va hisobotlar

### Yangi: Admin paneli (`/admin`, faqat ADMIN_ID egasi uchun)
Bot obunachilari bo'yicha to'liq audit va hisobot:
- **Davr hisobotlari:** kunlik / haftalik (7 kun) / oylik (30 kun) / umumiy
  (barcha vaqt) / **ixtiyoriy interval** (sana oralig'i: `YYYY-MM-DD YYYY-MM-DD`).
- **Har bir hisobot 3 formatda:** 📈 grafik (PNG — kunlik faollik + top tashxislar),
  📄 PDF (sammari + top tashxislar jadvali + grafik), 📋 Excel (to'liq audit).
- **Excel audit varaqlari:** Summary, Sessions (har sessiya: sana, user_id, ism,
  username, til, kategoriya, yosh, jins, joylashuv, savollar soni, tashxis,
  ishonch), Answers (har bir savol-javob), Users (obunachilar).
- **👤 Individual hisobot** — obunachi Telegram ID si bo'yicha: profil + barcha
  sessiyalari + har bir sessiyadagi savol-javoblar va tashxis (PDF + Excel).
- **👥 Obunachilar ro'yxati** — Excel + qisqa matnli ro'yxat.
- Hisobotda obunachi ismi, ID si va username i ko'rsatiladi.

### Ma'lumot to'liqligi
- `bot_users` ga `first_name`, `last_name`, `username` ustunlari qo'shildi va
  til tanlashda saqlanadi (hisobotlarda ism/username ko'rsatish uchun).

### Texnik
- Yangi modullar: `db/reports.py` (audit so'rovlari), `reporting/exporters.py`
  (Excel/PDF/grafik), `bot/admin.py` (admin router).
- Yangi kutubxonalar: `openpyxl`, `reportlab`, `matplotlib`.
- Fayl generatsiyasi alohida threadда (`asyncio.to_thread`) — botni bloklamaydi.
- DB sozlanmagan bo'lsa yoki kutubxona yo'q bo'lsa — graceful (matnli hisobot/ogohlantirish).
- Admin uchun `/admin`, `/reply` buyruqlari faqat admin chatida ko'rinadi.

## [1.6.3] - 2026-06 — Admin contact diagnostics

- Yangi **`/myid`** buyrug'i: foydalanuvchining Telegram ID si va bot uni admin
  deb taniyaptimi yo'qmi ko'rsatadi (admin aloqani sozlashni osonlashtiradi).
- Startup logida `ADMIN_ID` qiymati ko'rsatiladi (Railway loglaridan tekshirish uchun).
- Eslatma: admin aloqa ishlashi uchun admin akkaunti botga avval `/start` bosishi
  shart (Telegram boti suhbatni o'zi boshlay olmaydi) va `ADMIN_ID` to'g'ri raqam
  bo'lishi kerak (`/myid` orqali tekshiriladi).

## [1.6.2] - 2026-06 — Trilingual start fix

- `/start` endi **3 tilda** (o'zbek/rus/ingliz) qisqacha yo'riqnoma va til tanlash
  tugmalarini ko'rsatadi (avval faqat o'zbekcha chiqardi). Til tanlangach, qolgan
  oqim tanlangan tilda davom etadi.
- Yangi `WELCOME_MULTI` matni (732 belgi — logo caption limitiga mos).

## [1.6.1] - 2026-06 — Oral Detect (rebrand + admin contact)

### Brending
- Bot nomi **Oral Detect** deb belgilandi (welcome, /about, health-check, loglar).
- `/start` da kengaytirilgan kirish: bot haqida qisqacha + tilni tanlash.
  Agar `assets/logo.png` mavjud bo'lsa, u rasm sifatida yuboriladi (ixtiyoriy).
- **ℹ️ Bot haqida** — to'liq ishlatish qo'llanmasi (6 qadamli), ma'lumotnoma va
  aloqa haqida; `/about` buyrug'i orqali ham ochiladi.

### Yangi funksiya — Admin bilan aloqa
- Menyuda **✉️ Admin bilan aloqa** tugmasi.
- Ishlash tartibi (relay): foydalanuvchi bot ichida xabar yozadi → xabar
  administratorга (`ADMIN_ID`) foydalanuvchi ismi/ID si bilan yetkaziladi →
  admin **`/reply <user_id> matn`** orqali javob beradi → bot foydalanuvchiga
  yetkazadi.
- `ADMIN_ID` o'rnatilmagan bo'lsa: `ADMIN_USERNAME` havolasi yoki "sozlanmagan"
  xabari ko'rsatiladi (bot baribir ishlaydi).
- Yangi env: `ADMIN_ID`, `ADMIN_USERNAME` (`.env.example`da).

### Versiyalash
- Avvalgi reliz "2.0.0" emas, **1.5.1** deb qayta belgilandi (quyida); joriy
  reliz **1.6.1**. (ML/kalibrlash/AI hali dormant — to'liq v2.0 emas.)

## [1.5.1] - 2026-06 — Bayesian Clinical Core

V2.0 loyihani oddiy Bayes-botdan **klinik qaror qabul qilish platformasi**ga
yo'naltiradi. Bu relizda **deterministik yadro to'liq faol**; ma'lumot/internet
talab qiladigan qatlamlar (ML, kalibrlash fit, self-learning, AI) **interfeys
sifatida ulanган va xavfsiz fallback bilan dormant** turadi.

### Faol (bu relizda ishlaydi)
- **Clinical Prior System** — har kasallikka epidemiologik prior:
  `effective_prior = base(prevalence) × age_factor × sex_factor`.
  121 kasallik 5 tarqalganlik tier'iga ajratildi (`medical/epidemiology.py`).
- **Demographic Engine** — sessiya boshida yosh (5 guruh) va jins yig'iladi
  (`DemographicContext`) va prior orqali Bayes'ga ta'sir qiladi. Misol: agressiv
  parodontit 13-18 yoshda 0.38 → 0.64; og'iz saratoni keksa erkakda ko'tariladi.
- **Anatomical Location Intelligence** — joylashuv endi matematikaga kiradi:
  `P(D|S,L) ∝ P(D)·P(S|D)·P(L|D)`. Misol: pastki jag' belgilanса perikoronit
  0.48 → 0.59 ko'tariladi.
- **Adaptive Question Engine** — Expected Diagnostic Gain; o'rtacha savol soni
  ~10-12 dan **~7.5 ga** tushdi (erta to'xtash + priorlar).
- **Clinical Data Collection Platform** — yangi DB jadvallari:
  diagnosis_sessions, session_answers, doctor_feedback, disease_statistics,
  priors, model_versions. Har sessiya (demografiya, joylashuv, javoblar, natija)
  saqlanadi (DB ixtiyoriy — o'chiq bo'lsa bot baribir ishlaydi).

### Dormant (interfeys tayyor, ma'lumot/internet kelganda yoqiladi)
- **ML Layer** (`engine/ml.py`) — Bayes+ML gibrid (0.6/0.4). Model yo'q →
  sof Bayes'ga fallback. CatBoost real dataset va internet talab qiladi.
- **Confidence Calibration** (`engine/calibration.py`) — Isotonic (PAV)
  interfeysi; hozir identity (labeled outcome yo'q).
- **Self-Learning Prior Update** — `priors` jadvalidan o'rganilgan
  multiplikatorlar startda yuklanadi; tasdiqlangan tashxislar to'planganda ishlaydi.
- **AI Clinical Explainer** — Groq interfeysi (`AI_ENABLED=false`).

### Validatsiya
- 121/121 kasallik o'z belgilaridan to'g'ri aniqlanadi (priorlar bilan ham).
- Demografiya va joylashuv rankingni kutilgan yo'nalishda o'zgartiradi.
- Barcha modullar `py_compile`dan o'tdi.

### Eslatma
- Prior tier'lari ataylab YUMSHOQ (nudge) — mos belgili kam uchraydigan kasallik
  baribir yetib boriladi. Real ma'lumot to'planganda kalibrlanadi.
- Sandbox internetsiz: ML/AI o'rnatib/sinab bo'lmadi (interfeys + fallback bilan).

## [1.5.0] - 2026-06

### Tashxis aniqligi — joylashuvni belgilash
Tish bilan bog'liq kategoriyalarda (tish, travma, parodont, jag') tashxisdan
oldin zararlangan sohani aniqlashtiruvchi qadamlar qo'shildi:
- **Qaysi jag'?** (yuqori/pastki)
- **Qaysi tomon?** (o'ng/chap)
- **Qaysi tish?** (kurak / qoziq / kichik oziq / katta oziq) — faqat tish/travma uchun
- Har bir savolda "Bilmayman" varianti bor; tanlangan soha natijada
  "🦷 Ko'rsatilgan soha: pastki o'ng katta oziq tish" ko'rinishida chiqadi.
- Joylashuv tasniflovchi (diagnostik) emas — u tashxisni tavsiflaydi, Bayes
  mexanizmiga ta'sir qilmaydi (savollar soni chegarasiga ham kirmaydi).

### Yangi bo'lim — Kasalliklar ma'lumotnomasi
Asosiy menyuga **📚 Kasalliklar ma'lumotnomasi** tugmasi qo'shildi:
- 10 ta bo'lim (tish/pulpa/periapikal/parodont/shilliq/jag'/TMJ/travma/
  rivojlanish/so'lak bezlari) → kasallik tanlash (uzun ro'yxatlar sahifalanadi)
  → tanlangan kasallik haqida **to'liq ma'lumot** (tavsif, simptomlar,
  differensial, davolash, xavfli belgilar).
- Orqaga qaytish tugmalari bilan qulay navigatsiya; barcha 121 kasallik mavjud.
- Ma'lumot rendering kodi tashxis natijasi bilan umumiy funksiyaga birlashtirildi.

### Texnik
- Yangi FSM holati `localizing`; `loc_*` va `rc_/rd_/rhome` callback'lari.
- `bot/keyboards.py` ga katalog va joylashuv klaviaturalari qo'shildi.

## [1.4.0] - 2026-06

### Har bir kasallik uchun to'liq ma'lumot (tashxisdan keyin)
Tashxis aniqlangandan so'ng foydalanuvchiga kasallik bo'yicha to'liq ma'lumot
va aniq tavsiya beriladi. `Disease` modeli 4 ta yangi maydon bilan kengaytirildi
(har biri 3 tilda — uz/ru/en):
- **description** — kasallik haqida tavsif (klinika, sabab)
- **symptoms_text** — asosiy simptomlar
- **differential** — differensial tashxis (qaysi kasalliklardan farqlanadi)
- **treatment** — davolash / "nima qilish kerak"

Barcha **121 kasallik** uchun ushbu 4 blok to'ldirildi (`medical/info.py` da
markazlashtirilgan va import paytida biriktiriladi). Natija xabari endi
"Kasallik haqida → Asosiy belgilar → Farqlash → Davolash/nima qilish kerak →
Xavfli belgilar" tartibida ko'rsatiladi.

### Aniqlashtirilgan tashxis
- `O'tkir o'choqli pulpit` namuna sifatida to'liq ishlab chiqildi (foydalanuvchi
  tasdiqlagan format asosida).
- Yangi farqlovchi savol: "Og'riq xurujlari qisqami (10-30 daqiqa), oraliqlari
  uzoqmi?" — o'choqli pulpitni diffuz pulpitdan aniq ajratadi.

### Eslatma
- Tibbiy matn ochiq stomatologiya manbalari asosida, faqat ma'lumot maqsadida
  tayyorlangan — aniq tashxis uchun shifokorga murojaat qilinadi.

## [1.3.0] - 2026-06

### To'liq tibbiy taksonomiya (qolgan barcha kategoriyalar)
13 toifa bo'yicha kasalliklar bazasi yakunlandi. Jami kasalliklar **47 → 121**,
savollar **88 → 157**, diagnostik guruhlar **4 → 8**.

- **3-kategoriya — Periapikal:** granullovchi va granulomatoz surunkali
  periodontit qo'shildi (o'tkir/fibroz, granuloma, radikulyar kista, abscess bilan).
- **4-kategoriya — Parodont (13):** deskvamativ gingivit, lokal va
  generalizatsiyalashgan parodontit (avvalgi "surunkali" o'rniga), periimplantit,
  gingival retsessiya, furkatsion shikastlanish qo'shildi.
- **5/6/12-kategoriya — Shilliq qavat (31):** yarali stomatit; til kasalliklari
  (geografik, qora tukli, rombsimon glossit, glossit); xeylitlar (meteorologik,
  eksfoliativ, aktinik, angular); infeksion (gerpes simplex, herpes zoster, HPV
  papilloma, qo'l-oyoq-og'iz, sifilis, sil, aktinomikoz); prekanseroz (eritroplakiya,
  submukoz fibroz); o'smalar (fibroma, gemangioma, lipoma) va yomon sifatli
  (yassi hujayrali karsinoma, til/lab saratoni) qo'shildi.
- **7-kategoriya — Jag' suyagi:** osteit, alveolit (quruq katakcha), odontogen
  keratokista qo'shildi.
- **8-kategoriya — TMJ (yangi):** disfunksiya, artrit, artroz, disk dislokatsiyasi, ankiloz.
- **9/10-kategoriya — Rivojlanish + ortodontik (yangi, 19):** adentiya/gipo/oligo/
  giperodontiya, geminatsiya/fuziya/konkressensiya/taurodontizm, distopiya/retensiya/
  ektopik chiqish, distal/mezial okklyuziya, chuqur/ochiq tishlash, kross-bayt,
  skuchennost, diastema, tremalar.
- **11-kategoriya — Travma (yangi, 9):** emal / emal-dentin / pulpa ochilishi /
  ildiz sinishi, konkussiya, subluksatsiya, ekstruziya, intruziya, avulsiya.
- **13-kategoriya — So'lak bezlari (yangi, 7):** sialadenit, sialolitiaz,
  kserostomiya, Sjögren sindromi, mukosele, ranula, so'lak bezi o'smasi.

### Engine va UI
- **4 ta yangi triage tugmasi:** Jag' bo'g'imi (TMJ), Jarohat (travma),
  Tish soni/shakli/tishlash (rivojlanish/ortodontik), So'lak bezlari.
- **Favqulodda aniqlash kengaytirildi:** o'tkir osteomiyelitga o'xshash holat
  (yuqori isitma + kuchli og'riq + trizm) va yiringli sialadenit (yuqori isitma +
  bez shishi) ham aniqlanadi.
- `MAX_QUESTIONS` 12 → 14 (katta shilliq qavat guruhida noyob kasalliklarni
  ajratish uchun; erta to'xtash aksariyat sessiyani baribir 4-6 savolda tugatadi).

### Tuzatishlar
- Qolgan barcha "o'lik" simptom kalitlari tozalandi: `root_exposure`,
  `no_periodontal_pocket`, `diffuse_swelling`, `acute_pain`, `no_fever` —
  endi `KNOWN_MISSING` bo'sh.

### Validatsiya
- 121/121 kasallik o'z belgilaridan to'g'ri yetib boriladi (rentgensiz klinik
  jihatdan ajralmas egizaklar — masalan geminatsiya/fuziya — sinonim guruh
  sifatida hisobga olingan). 71 ta engine test holati va registr/favqulodda
  testlari muvaffaqiyatli.

### Eslatma
- Sandbox internetsiz bo'lgani uchun `ctoma.ru` ochib bo'lmadi; tibbiy ma'lumot
  ochiq stomatologiya manbalari tuzilishiga mos ravishda tayyorlandi.
- Ba'zi holatlar (shakl anomaliyalari, ba'zi periapikal/oraliq holatlar) aniq
  farqlash uchun rentgen talab qiladi — bot ularni muqobil variant sifatida ko'rsatadi.

## [1.2.0] - 2026-06

### Tibbiy baza kengaytirildi (1 va 2-kategoriya — namuna bosqichi)
- **1-kategoriya — Tish qattiq to'qimalari:** karies bosqichlari (oq dog',
  yuzaki, o'rta, chuqur, ikkilamchi) saqlandi va aniqlashtirildi. **12 ta yangi
  nokarioz shikastlanish** qo'shildi: emal gipoplaziyasi, emal aplaziyasi,
  dental fluoroz, tish eroziyasi, attritsiya, abrasiya, abfraksiya, qattiq
  to'qima nekrozi, gipersensitivlik, dentin displaziyasi, amelogenez imperfecta,
  dentinogenez imperfecta.
- **2-kategoriya — Pulpa:** klassifikatsiya foydalanuvchi taksonomiyasiga
  moslandi — *o'tkir o'choqli* va *o'tkir diffuz* pulpit (avvalgi seroz/yiringli
  o'rniga), surunkali fibroz/gipertrofik/gangrenoz pulpit, pulpa nekrozi.
- **14 ta yangi simptom/savol** (3 tilda) qo'shildi: ko'p tish zararlanishi,
  bolalikdan mavjudligi, nasliylik, jigarrang/chipor dog'lar, emal chuqurchalari,
  emal yo'qligi, ponasimon nuqson, chaynov yuzasi yeyilishi, bruksizm, qattiq
  cho'tkalash, kislota ta'siri, silliq-yaltiroq yuza, bo'rsimon emal, tug'ma rang.
- Jami kasalliklar soni **35 → 47** ga yetdi.

### Tuzatilgan xatolar
- `hot_pain` "o'lik" kaliti tuzatildi (`hot_increases_pain` ga moslandi) va
  `KNOWN_MISSING` ro'yxatidan olib tashlandi.

### Eslatma
- Periapikal (3), parodont (4), shilliq qavat (5), jag' (7) va boshqa
  kategoriyalar hozircha asl holatida — keyingi bosqichlarda qayta tuziladi.
- Tibbiy ma'lumot ochiq stomatologiya manbalariga (jumladan ctoma.ru tuzilishiga)
  mos ravishda tayyorlandi.

## [1.1.0] - 2026-06

### O'zgarishlar
- **Engine to'liq qayta yozildi:** haqiqiy Akinator mexanizmi (information-gain
  asosida savol tanlash) va aniq triage daraxti (decision tree).
- **Bayes/og'irlikli ballash:** so'ralmagan belgilar neytral hisoblanadi,
  ishonchlilik (confidence) to'g'ri normalizatsiya qilinadi, yetarli dalil
  bo'lmasa "aniq emas" natijasi qaytariladi.
- **Simptom registri (`domain/symptoms.py`):** savol va simptom kalitlari uchun
  yagona manba. Kasallik mavjud bo'lmagan simptomga murojaat qilsa, test xato beradi.
- **AI vaqtincha o'chirildi** (`AI_ENABLED=false`). Uning o'rniga har kasallik uchun
  kodda tayyor tavsiya matni ko'rsatiladi. AI v2.0 da qaytariladi.
- **Supabase integratsiyasi:** foydalanuvchi, sessiya va tashxis tarixi saqlanadi
  (asyncpg). DB ishlamasa ham bot ishlashda davom etadi.
- **Telegram xabarlari HTML rejimida** (Markdown parse xatolari yo'q qilindi).
- **Railway deploy** uchun nixpacks konfiguratsiyasi qo'shildi.
- Markaziy `Settings` konfiguratsiyasi, qoldiq kod tozalandi, `/start` va `/help`
  komandalar menyusi qo'shildi, eskirgan tugma bosilganda xabar beriladi.

### Tuzatilgan xatolar
- `hot_pain` → mavjud bo'lmagan simptom kaliti (registr orqali oldini olinadi).
- `root_exposure`, `no_periodontal_pocket`, `diffuse_swelling`, `acute_pain`,
  `no_fever` kabi savolsiz ("o'lik") kalitlar aniqlandi (kasalliklar bosqichida tozalanadi).
