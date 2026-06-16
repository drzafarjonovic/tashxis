# Changelog

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
