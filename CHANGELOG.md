# Changelog

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
