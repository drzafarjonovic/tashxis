# Changelog

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
