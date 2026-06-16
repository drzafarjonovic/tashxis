"""
Kasalliklar bo'yicha to'liq ma'lumot (tashxis aniqlangandan keyin ko'rsatiladi).

Har bir yozuv 4 blokdan iborat, har biri 3 tilda (uz/ru/en):
    description   — kasallik haqida qisqa tavsif (klinika, sabab)
    symptoms_text — asosiy simptomlar
    differential  — differensial tashxis
    treatment     — davolash / "nima qilish kerak"

Bu ma'lumot medical/__init__.py da import paytida Disease obyektlariga biriktiriladi.
Eslatma: tibbiy matn ochiq stomatologiya manbalari asosida tayyorlangan va
faqat ma'lumot xarakteriga ega — aniq tashxis uchun shifokorga murojaat qilinadi.
"""

from typing import Dict

DISEASE_INFO: Dict[str, Dict[str, Dict[str, str]]] = {

    # ═══════════════════════════════════════════════════════════════
    #  1. KARIES GURUHI
    # ═══════════════════════════════════════════════════════════════
    "white_spot": {
        "description": {
            "uz": "Boshlang'ich karies — emalning demineralizatsiyasi natijasida paydo bo'ladigan dastlabki bosqich. Kovak hali yo'q; emalda bo'r rangidagi oq dog' ko'rinadi. Bu bosqich qaytariladigan (remineralizatsiya mumkin).",
            "ru": "Начальный кариес — самая ранняя стадия, вызванная деминерализацией эмали. Полости ещё нет; на эмали видно меловидное белое пятно. Стадия обратима (возможна реминерализация).",
            "en": "Initial caries is the earliest stage caused by enamel demineralization. There is no cavity yet; a chalky white spot is visible on the enamel. This stage is reversible (remineralization is possible).",
        },
        "symptoms_text": {
            "uz": "• Emalda bo'r rangidagi (matlashgan) oq dog'.\n• Og'riq yo'q.\n• Ba'zan shirin narsadan yengil noqulaylik.",
            "ru": "• Меловидное (матовое) белое пятно на эмали.\n• Боли нет.\n• Иногда лёгкий дискомфорт от сладкого.",
            "en": "• Chalky (matte) white spot on the enamel.\n• No pain.\n• Occasionally mild discomfort from sweets.",
        },
        "differential": {
            "uz": "Fluoroz va emal gipoplaziyasidan (ko'p tishda, simmetrik, tug'ma) farqlanadi.",
            "ru": "Дифференцируют с флюорозом и гипоплазией эмали (множественные, симметричные, врождённые).",
            "en": "Differentiated from fluorosis and enamel hypoplasia (multiple, symmetrical, congenital).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga ko'rining. Remineralizatsiya (ftor lak/gel, kalsiy), gigiyena va parhez bilan jarayonni to'xtatish mumkin — burg'ulashsiz.",
            "ru": "Что делать: обратитесь к стоматологу. Процесс можно остановить реминерализацией (фторлак/гель, кальций), гигиеной и диетой — без сверления.",
            "en": "What to do: see a dentist. The process can be halted with remineralization (fluoride varnish/gel, calcium), hygiene and diet — without drilling.",
        },
    },
    "superficial_caries": {
        "description": {
            "uz": "Yuzaki karies — faqat emal qatlamini zararlaydigan bosqich; kichik kovak hosil bo'ladi, lekin dentinga yetmaydi.",
            "ru": "Поверхностный кариес — стадия, поражающая только эмаль; образуется небольшая полость, не достигающая дентина.",
            "en": "Superficial caries affects only the enamel; a small cavity forms but does not reach the dentin.",
        },
        "symptoms_text": {
            "uz": "• Emalda kichik kovak/g'adir-budurlik.\n• Qisqa, tez o'tuvchi og'riq (shirin, nordon, ba'zan sovuqdan).\n• Spontan og'riq yo'q.",
            "ru": "• Небольшая полость/шероховатость в эмали.\n• Кратковременная боль (от сладкого, кислого, иногда холодного).\n• Самопроизвольной боли нет.",
            "en": "• Small cavity/roughness in the enamel.\n• Short, transient pain (from sweet, sour, sometimes cold).\n• No spontaneous pain.",
        },
        "differential": {
            "uz": "O'rta kariesdan (dentin zararlangan) va emal eroziyasi/abraziyasidan farqlanadi.",
            "ru": "Дифференцируют со средним кариесом (поражён дентин) и эрозией/абразией эмали.",
            "en": "Differentiated from medium caries (dentin involved) and enamel erosion/abrasion.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga murojaat qiling — kovak tozalanib, plomba qo'yiladi. Erta davolash chuqurlashishning oldini oladi.",
            "ru": "Что делать: обратитесь к стоматологу — полость очищают и пломбируют. Раннее лечение предотвращает углубление.",
            "en": "What to do: see a dentist — the cavity is cleaned and filled. Early treatment prevents progression.",
        },
    },
    "medium_caries": {
        "description": {
            "uz": "O'rta karies — emaldan o'tib dentinning o'rta qatlamini zararlaydigan bosqich. Kovak aniq ko'rinadi.",
            "ru": "Средний кариес — поражение проходит через эмаль и захватывает средние слои дентина. Полость хорошо видна.",
            "en": "Medium caries extends through the enamel into the middle layers of dentin. The cavity is clearly visible.",
        },
        "symptoms_text": {
            "uz": "• Aniq ko'rinadigan kovak.\n• Sovuq/shirin/nordon ta'sirdan qisqa og'riq.\n• Spontan va tungi og'riq yo'q.",
            "ru": "• Хорошо заметная полость.\n• Кратковременная боль от холодного/сладкого/кислого.\n• Самопроизвольной и ночной боли нет.",
            "en": "• Clearly visible cavity.\n• Short pain from cold/sweet/sour.\n• No spontaneous or night pain.",
        },
        "differential": {
            "uz": "Chuqur kariesdan (pulpa yaqin) va surunkali pulpitdan (stimuldan keyin uzoq og'riq) farqlanadi.",
            "ru": "Дифференцируют с глубоким кариесом (близость пульпы) и хроническим пульпитом (длительная боль после раздражителя).",
            "en": "Differentiated from deep caries (pulp proximity) and chronic pulpitis (lingering pain after stimulus).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog kovakni tozalab, plomba qo'yadi. Kechiktirmang — chuqur kariesga o'tadi.",
            "ru": "Что делать: стоматолог очищает полость и ставит пломбу. Не откладывайте — переходит в глубокий кариес.",
            "en": "What to do: the dentist cleans the cavity and places a filling. Do not delay — it progresses to deep caries.",
        },
    },
    "deep_caries": {
        "description": {
            "uz": "Chuqur karies — kovak dentinning chuqur qatlamiga yetib, pulpaga juda yaqinlashgan bosqich. Pulpit xavfi yuqori.",
            "ru": "Глубокий кариес — полость достигает глубоких слоёв дентина, близко к пульпе. Высокий риск пульпита.",
            "en": "Deep caries reaches the deep layers of dentin, very close to the pulp. High risk of pulpitis.",
        },
        "symptoms_text": {
            "uz": "• Chuqur, keng kovak.\n• Sovuq/issiq/shirindan og'riq, stimul olingach tez o'tadi.\n• Ovqat qoldig'i tushganda og'riq; ba'zan yomon hid.",
            "ru": "• Глубокая, широкая полость.\n• Боль от холодного/горячего/сладкого, быстро проходит после устранения раздражителя.\n• Боль при попадании пищи; иногда неприятный запах.",
            "en": "• Deep, wide cavity.\n• Pain from cold/hot/sweet that quickly subsides after the stimulus is removed.\n• Pain when food enters; sometimes bad odour.",
        },
        "differential": {
            "uz": "Pulpitlardan (spontan/tungi og'riq, stimuldan keyin uzoq og'riq) farqlanadi — bu eng muhim chegara.",
            "ru": "Дифференцируют с пульпитами (самопроизвольная/ночная боль, длительная боль после раздражителя) — ключевая граница.",
            "en": "Differentiated from pulpitis (spontaneous/night pain, lingering pain after stimulus) — the key boundary.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: zudlik bilan stomatologga boring. Davolovchi qatlam + plomba qo'yiladi; ba'zan pulpani saqlash choralari ko'riladi.",
            "ru": "Что делать: срочно к стоматологу. Накладывают лечебную прокладку и пломбу; иногда меры по сохранению пульпы.",
            "en": "What to do: see a dentist promptly. A therapeutic liner and filling are placed; sometimes pulp-preserving measures are taken.",
        },
    },
    "secondary_caries": {
        "description": {
            "uz": "Ikkilamchi (residiv) karies — avval qo'yilgan plomba chetida (marginal bo'shliqda) qaytadan rivojlanadigan karies.",
            "ru": "Вторичный (рецидивный) кариес — кариес, развивающийся повторно по краю ранее поставленной пломбы (в краевой щели).",
            "en": "Secondary (recurrent) caries develops again at the margin of a previously placed filling (marginal gap).",
        },
        "symptoms_text": {
            "uz": "• Eski plomba atrofida qorayish yoki kovak.\n• Sovuq/shirindan qisqa og'riq.\n• Plomba chetining qo'pollashishi, ba'zan yomon hid.",
            "ru": "• Потемнение или полость вокруг старой пломбы.\n• Кратковременная боль от холодного/сладкого.\n• Шероховатость края пломбы, иногда неприятный запах.",
            "en": "• Darkening or cavity around an old filling.\n• Short pain from cold/sweet.\n• Rough filling margin, sometimes bad odour.",
        },
        "differential": {
            "uz": "Plombaning oddiy rang o'zgarishidan va plomba ostidagi pulpitdan farqlanadi.",
            "ru": "Дифференцируют с обычным окрашиванием пломбы и пульпитом под пломбой.",
            "en": "Differentiated from simple staining of the filling and pulpitis beneath the filling.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog eski plombani olib, kovakni qayta tozalab, yangi plomba qo'yadi.",
            "ru": "Что делать: стоматолог удаляет старую пломбу, очищает полость и ставит новую пломбу.",
            "en": "What to do: the dentist removes the old filling, re-cleans the cavity and places a new filling.",
        },
    },

    # ═══════════════════════════════════════════════════════════════
    #  2. NOKARIOZ SHIKASTLANISHLAR
    # ═══════════════════════════════════════════════════════════════
    "enamel_hypoplasia": {
        "description": {
            "uz": "Emal gipoplaziyasi — tish rivojlanishi davrida emalning yetarli shakllanmasligi natijasidagi tug'ma nuqson. Emalda chuqurchalar, egatlar yoki dog'lar bo'ladi.",
            "ru": "Гипоплазия эмали — врождённый дефект из-за недостаточного формирования эмали в период развития зуба. Проявляется ямками, бороздками или пятнами.",
            "en": "Enamel hypoplasia is a developmental defect from insufficient enamel formation during tooth development. It presents as pits, grooves or spots.",
        },
        "symptoms_text": {
            "uz": "• Emalda chuqurcha, egat yoki nuqsonlar (tishlar chiqqanidan beri).\n• Ko'pincha bir necha tishda.\n• Odatda og'riqsiz; estetik muammo.",
            "ru": "• Ямки, бороздки или дефекты эмали (с момента прорезывания).\n• Часто на нескольких зубах.\n• Обычно безболезненно; эстетическая проблема.",
            "en": "• Pits, grooves or defects in the enamel (present since eruption).\n• Often on several teeth.\n• Usually painless; an aesthetic concern.",
        },
        "differential": {
            "uz": "Karies (kovak, og'riq) va fluorozdan (jigarrang chipor dog'lar) farqlanadi.",
            "ru": "Дифференцируют с кариесом (полость, боль) и флюорозом (коричневая крапчатость).",
            "en": "Differentiated from caries (cavity, pain) and fluorosis (brown mottling).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga ko'rining. Remineralizatsiya, kompozit qoplama yoki vinir/koronka bilan tiklash mumkin.",
            "ru": "Что делать: обратитесь к стоматологу. Возможна реминерализация, реставрация композитом или винир/коронка.",
            "en": "What to do: see a dentist. Remineralization, composite restoration or veneers/crowns can be used.",
        },
    },
    "enamel_aplasia": {
        "description": {
            "uz": "Emal aplaziyasi — emalning butunlay yoki deyarli yo'qligi bilan kechadigan og'ir tug'ma nuqson; dentin ochiq qoladi.",
            "ru": "Аплазия эмали — тяжёлый врождённый дефект с полным или почти полным отсутствием эмали; дентин обнажён.",
            "en": "Enamel aplasia is a severe congenital defect with complete or near-complete absence of enamel; the dentin is exposed.",
        },
        "symptoms_text": {
            "uz": "• Emal yo'q, sarg'ish dentin ochiq.\n• Yuqori sezuvchanlik (sovuq, mexanik).\n• Tez yeyilish, estetik nuqson.",
            "ru": "• Эмаль отсутствует, обнажён желтоватый дентин.\n• Высокая чувствительность (холод, механика).\n• Быстрое стирание, эстетический дефект.",
            "en": "• Enamel absent, yellowish dentin exposed.\n• High sensitivity (cold, mechanical).\n• Rapid wear, aesthetic defect.",
        },
        "differential": {
            "uz": "Og'ir gipoplaziya va amelogenez imperfectadan farqlanadi.",
            "ru": "Дифференцируют с тяжёлой гипоплазией и несовершенным амелогенезом.",
            "en": "Differentiated from severe hypoplasia and amelogenesis imperfecta.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga murojaat qiling — tishlarni qoplama/koronka bilan himoya qilish va sezuvchanlikni kamaytirish kerak.",
            "ru": "Что делать: обратитесь к стоматологу — необходима защита зубов коронками/реставрациями и снижение чувствительности.",
            "en": "What to do: see a dentist — teeth need protection with crowns/restorations and sensitivity reduction.",
        },
    },
    "dental_fluorosis": {
        "description": {
            "uz": "Dental fluoroz — tish rivojlanishi davrida ortiqcha ftor (suv, pasta) ta'sirida emalning shikastlanishi. Ko'p tishda simmetrik dog'lar.",
            "ru": "Флюороз зубов — поражение эмали из-за избытка фтора (вода, паста) в период развития зубов. Симметричные пятна на многих зубах.",
            "en": "Dental fluorosis is enamel damage from excess fluoride (water, toothpaste) during tooth development. Symmetrical spots on many teeth.",
        },
        "symptoms_text": {
            "uz": "• Oq-jigarrang chipor (notekis) dog'lar.\n• Ko'p tishda simmetrik joylashgan.\n• Og'irroq shaklda emal yuzasi yemiriladi.",
            "ru": "• Бело-коричневая крапчатость (пятнистость).\n• Симметрично на многих зубах.\n• В тяжёлой форме эмаль разрушается.",
            "en": "• White-brown mottling (speckling).\n• Symmetrical across many teeth.\n• In severe forms the enamel surface breaks down.",
        },
        "differential": {
            "uz": "Gipoplaziya (lokal nuqsonlar) va boshlang'ich kariesdan (bitta tishda) farqlanadi.",
            "ru": "Дифференцируют с гипоплазией (локальные дефекты) и начальным кариесом (на одном зубе).",
            "en": "Differentiated from hypoplasia (local defects) and initial caries (on a single tooth).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ftor manbasini kamaytiring; stomatolog oqartirish, mikroabraziya yoki vinir taklif qilishi mumkin.",
            "ru": "Что делать: уменьшите источник фтора; стоматолог может предложить отбеливание, микроабразию или виниры.",
            "en": "What to do: reduce the fluoride source; the dentist may offer bleaching, microabrasion or veneers.",
        },
    },
    "tooth_erosion": {
        "description": {
            "uz": "Tish eroziyasi — kislota (ovqat, gazli ichimlik, reflyuks, qusish) ta'sirida emalning kimyoviy erishi. Kovaksiz, silliq botiq yuzalar.",
            "ru": "Эрозия зубов — химическое растворение эмали под действием кислот (пища, газировка, рефлюкс, рвота). Гладкие вогнутые поверхности без полости.",
            "en": "Tooth erosion is chemical dissolution of enamel by acids (food, soda, reflux, vomiting). Smooth concave surfaces without a cavity.",
        },
        "symptoms_text": {
            "uz": "• Silliq, yaltiroq, botiq (kosacha) yuzalar.\n• Sovuq/issiqqa sezuvchanlik.\n• Tish bo'yi yupqalashishi, sarg'ish tus.",
            "ru": "• Гладкие, блестящие, вогнутые (чашеобразные) поверхности.\n• Чувствительность к холодному/горячему.\n• Истончение, желтоватый оттенок.",
            "en": "• Smooth, shiny, concave (cupped) surfaces.\n• Sensitivity to cold/hot.\n• Thinning, yellowish hue.",
        },
        "differential": {
            "uz": "Abraziya (mexanik), attritsiya (yeyilish) va kariesdan farqlanadi.",
            "ru": "Дифференцируют с абразией (механической), аттрицией (стиранием) и кариесом.",
            "en": "Differentiated from abrasion (mechanical), attrition (wear) and caries.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: kislota manbasini bartaraf eting (parhez, reflyuks davolash); stomatolog ftor va restavratsiya bilan himoya qiladi.",
            "ru": "Что делать: устраните источник кислоты (диета, лечение рефлюкса); стоматолог защищает фтором и реставрациями.",
            "en": "What to do: remove the acid source (diet, treat reflux); the dentist protects with fluoride and restorations.",
        },
    },
    "attrition": {
        "description": {
            "uz": "Patologik yeyilish (attritsiya) — tish-tishga ishqalanishi (ko'pincha bruksizm) natijasida chaynov yuzasining yedirilishi.",
            "ru": "Патологическая стираемость (аттриция) — стирание жевательных поверхностей от трения зуб-о-зуб (часто бруксизм).",
            "en": "Pathological attrition is wear of the chewing surfaces from tooth-to-tooth friction (often bruxism).",
        },
        "symptoms_text": {
            "uz": "• Chaynov yuzasi/qirralar tekislanib yedirilgan.\n• Tish g'ichirlatish (ko'pincha uyquda).\n• Sezuvchanlik, tish bo'yining qisqarishi.",
            "ru": "• Сточенные, плоские жевательные поверхности/края.\n• Скрежет зубами (часто во сне).\n• Чувствительность, укорочение коронок.",
            "en": "• Flattened, worn chewing surfaces/edges.\n• Teeth grinding (often during sleep).\n• Sensitivity, shortened crowns.",
        },
        "differential": {
            "uz": "Eroziya (kislota) va abraziyadan (cho'tka/tashqi mexanik) farqlanadi.",
            "ru": "Дифференцируют с эрозией (кислота) и абразией (щётка/внешняя механика).",
            "en": "Differentiated from erosion (acid) and abrasion (brush/external mechanical).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga ko'rining — tungi kapa (kappa), bruksizmni nazorat, kerak bo'lsa restavratsiya/balandlikni tiklash.",
            "ru": "Что делать: обратитесь к стоматологу — ночная капа, контроль бруксизма, при необходимости реставрация/восстановление высоты.",
            "en": "What to do: see a dentist — a night guard, bruxism control, and if needed restoration/bite rehabilitation.",
        },
    },
    "abrasion": {
        "description": {
            "uz": "Abrasiya — tashqi mexanik ta'sir (qattiq cho'tkalash, qattiq cho'tka, abraziv pasta) natijasida tish bo'ynida ponasimon nuqson.",
            "ru": "Абразия — клиновидный дефект у шейки зуба от внешнего механического воздействия (жёсткая чистка, абразивная паста).",
            "en": "Abrasion is a wedge-shaped defect at the tooth neck from external mechanical action (hard brushing, abrasive paste).",
        },
        "symptoms_text": {
            "uz": "• Tish bo'ynida ponasimon (V) nuqson.\n• Sovuqqa sezuvchanlik.\n• Ko'pincha milk chekinishi bilan.",
            "ru": "• Клиновидный (V) дефект у шейки зуба.\n• Чувствительность к холодному.\n• Часто с рецессией десны.",
            "en": "• Wedge-shaped (V) defect at the tooth neck.\n• Cold sensitivity.\n• Often with gum recession.",
        },
        "differential": {
            "uz": "Abfraksiya (okklyuzion zo'riqish) va eroziyadan (kislota) farqlanadi.",
            "ru": "Дифференцируют с абфракцией (окклюзионная нагрузка) и эрозией (кислота).",
            "en": "Differentiated from abfraction (occlusal load) and erosion (acid).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: yumshoq cho'tka va to'g'ri texnika; stomatolog nuqsonni plomba bilan tiklaydi.",
            "ru": "Что делать: мягкая щётка и правильная техника; стоматолог восстанавливает дефект пломбой.",
            "en": "What to do: soft brush and correct technique; the dentist restores the defect with a filling.",
        },
    },
    "abfraction": {
        "description": {
            "uz": "Abfraksiya — okklyuzion (chaynash) zo'riqish kuchlari ta'sirida tish bo'ynida egilish natijasidagi ponasimon nuqson.",
            "ru": "Абфракция — клиновидный дефект у шейки зуба из-за изгибающих окклюзионных нагрузок.",
            "en": "Abfraction is a wedge-shaped cervical defect caused by bending from occlusal (biting) stress.",
        },
        "symptoms_text": {
            "uz": "• Bo'ynida aniq qirrali V-nuqson.\n• Ko'pincha bruksizm/noto'g'ri okklyuziya bilan.\n• Sovuqqa sezuvchanlik.",
            "ru": "• Чёткий клиновидный дефект у шейки.\n• Часто с бруксизмом/нарушением окклюзии.\n• Чувствительность к холодному.",
            "en": "• Sharp wedge-shaped defect at the neck.\n• Often with bruxism/occlusal problems.\n• Cold sensitivity.",
        },
        "differential": {
            "uz": "Abraziya (cho'tka) va eroziyadan farqlanadi; ko'pincha birga uchraydi.",
            "ru": "Дифференцируют с абразией (щётка) и эрозией; часто сочетаются.",
            "en": "Differentiated from abrasion (brush) and erosion; they often coexist.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog okklyuziyani tuzatadi (kapa, sayqallash) va nuqsonni plomba bilan tiklaydi.",
            "ru": "Что делать: стоматолог корректирует окклюзию (капа, пришлифовка) и восстанавливает дефект пломбой.",
            "en": "What to do: the dentist corrects the occlusion (guard, adjustment) and restores the defect with a filling.",
        },
    },
    "hard_tissue_necrosis": {
        "description": {
            "uz": "Tish qattiq to'qimalari nekrozi — kislota bug'lari (kasbiy), kimyoviy yoki tizimli ta'sir natijasida emalning bo'rsimon yemirilishi.",
            "ru": "Некроз твёрдых тканей зуба — меловидное разрушение эмали из-за кислотных паров (профессиональных), химических или системных воздействий.",
            "en": "Hard tissue necrosis is chalky destruction of enamel from acid vapours (occupational), chemical or systemic factors.",
        },
        "symptoms_text": {
            "uz": "• Bo'rsimon, mo'rt, to'kiluvchan emal.\n• Ko'p tishda, tez progressiv.\n• Sezuvchanlik, rang o'zgarishi.",
            "ru": "• Меловидная, хрупкая, крошащаяся эмаль.\n• На многих зубах, быстро прогрессирует.\n• Чувствительность, изменение цвета.",
            "en": "• Chalky, brittle, crumbling enamel.\n• On many teeth, rapidly progressive.\n• Sensitivity, discolouration.",
        },
        "differential": {
            "uz": "Eroziya va fluorozdan farqlanadi (sabab va tarqalish bo'yicha).",
            "ru": "Дифференцируют с эрозией и флюорозом (по причине и распространённости).",
            "en": "Differentiated from erosion and fluorosis (by cause and distribution).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: zararli ta'sirni to'xtating (kasbiy himoya); stomatolog remineralizatsiya va restavratsiya qiladi.",
            "ru": "Что делать: устраните вредное воздействие (профзащита); стоматолог проводит реминерализацию и реставрацию.",
            "en": "What to do: stop the harmful exposure (occupational protection); the dentist performs remineralization and restoration.",
        },
    },
    "dentin_hypersensitivity": {
        "description": {
            "uz": "Tish gipersensitivligi — ochilgan dentin (milk chekinishi, yeyilish) tufayli qisqa, o'tkir og'riq. Kasallik emas, balki holat.",
            "ru": "Гиперчувствительность зубов — короткая острая боль из-за обнажённого дентина (рецессия, стирание). Это состояние, а не болезнь.",
            "en": "Dentin hypersensitivity is short, sharp pain due to exposed dentin (recession, wear). It is a condition rather than a disease.",
        },
        "symptoms_text": {
            "uz": "• Sovuq, shirin yoki teginishdan qisqa o'tkir og'riq.\n• Stimul olingach darhol o'tadi.\n• Ko'rinarli kovak yo'q.",
            "ru": "• Короткая острая боль от холодного, сладкого или прикосновения.\n• Сразу проходит после устранения раздражителя.\n• Видимой полости нет.",
            "en": "• Short, sharp pain from cold, sweet or touch.\n• Stops immediately after the stimulus is removed.\n• No visible cavity.",
        },
        "differential": {
            "uz": "Karies va pulpitdan (uzoq/spontan og'riq) farqlanadi.",
            "ru": "Дифференцируют с кариесом и пульпитом (длительная/самопроизвольная боль).",
            "en": "Differentiated from caries and pulpitis (lingering/spontaneous pain).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: desensibilizatsiyalovchi pasta, ftor; stomatolog ochilgan sohani qoplaydi va sababini (milk, yeyilish) davolaydi.",
            "ru": "Что делать: десенсибилизирующая паста, фтор; стоматолог закрывает обнажённый участок и лечит причину (десна, стирание).",
            "en": "What to do: desensitizing paste, fluoride; the dentist seals the exposed area and treats the cause (gum, wear).",
        },
    },
    "dentin_dysplasia": {
        "description": {
            "uz": "Dentin displaziyasi — dentin va ildizlarning nasliy rivojlanish nuqsoni; ildizlar kalta, tishlar harakatchan, erta tushishi mumkin.",
            "ru": "Дисплазия дентина — наследственный дефект развития дентина и корней; корни короткие, зубы подвижны, возможна ранняя потеря.",
            "en": "Dentin dysplasia is a hereditary developmental defect of dentin and roots; roots are short, teeth mobile, early loss possible.",
        },
        "symptoms_text": {
            "uz": "• Tishlar harakatchan (kalta ildiz).\n• Nasliy, tug'ma.\n• Tojlar nisbatan normal ko'rinishi mumkin.",
            "ru": "• Подвижность зубов (короткие корни).\n• Наследственная, врождённая.\n• Коронки могут выглядеть относительно нормально.",
            "en": "• Tooth mobility (short roots).\n• Hereditary, congenital.\n• Crowns may look relatively normal.",
        },
        "differential": {
            "uz": "Dentinogenez imperfecta va parodontitdan (yallig'lanish) farqlanadi.",
            "ru": "Дифференцируют с несовершенным дентиногенезом и пародонтитом (воспаление).",
            "en": "Differentiated from dentinogenesis imperfecta and periodontitis (inflammation).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/ortoped kuzatuvi; tishlarni saqlash, harakatchanlikni nazorat va protezlash rejasi.",
            "ru": "Что делать: наблюдение стоматолога/ортопеда; сохранение зубов, контроль подвижности и план протезирования.",
            "en": "What to do: dental/prosthodontic monitoring; tooth preservation, mobility control and a prosthetic plan.",
        },
    },
    "amelogenesis_imperfecta": {
        "description": {
            "uz": "Amelogenez imperfecta — emalning nasliy shakllanish nuqsoni; barcha tishlarda emal yupqa, g'adir-budur yoki rangi o'zgargan.",
            "ru": "Несовершенный амелогенез — наследственный дефект формирования эмали; на всех зубах эмаль тонкая, шероховатая или изменённого цвета.",
            "en": "Amelogenesis imperfecta is a hereditary defect of enamel formation; on all teeth the enamel is thin, rough or discoloured.",
        },
        "symptoms_text": {
            "uz": "• Barcha tishlarda emal nuqsoni (tug'ma, oilada).\n• Yupqa/g'adir emal, sarg'ish-jigarrang tus.\n• Sezuvchanlik, tez yeyilish.",
            "ru": "• Дефект эмали на всех зубах (врождённый, семейный).\n• Тонкая/шероховатая эмаль, желто-коричневый оттенок.\n• Чувствительность, быстрое стирание.",
            "en": "• Enamel defect on all teeth (congenital, familial).\n• Thin/rough enamel, yellow-brown hue.\n• Sensitivity, rapid wear.",
        },
        "differential": {
            "uz": "Gipoplaziya (lokal), fluoroz va dentinogenez imperfectadan farqlanadi.",
            "ru": "Дифференцируют с гипоплазией (локальной), флюорозом и несовершенным дентиногенезом.",
            "en": "Differentiated from hypoplasia (local), fluorosis and dentinogenesis imperfecta.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga murojaat qiling — koronka/vinir bilan to'liq tiklash va sezuvchanlikni boshqarish.",
            "ru": "Что делать: обратитесь к стоматологу — полная реставрация коронками/винирами и контроль чувствительности.",
            "en": "What to do: see a dentist — full restoration with crowns/veneers and sensitivity management.",
        },
    },
    "dentinogenesis_imperfecta": {
        "description": {
            "uz": "Dentinogenez imperfecta — dentinning nasliy nuqsoni; tishlar opal (kulrang-ko'k/jigarrang), shaffof, emal oson ko'chadi va tez yeyiladi.",
            "ru": "Несовершенный дентиногенез — наследственный дефект дентина; зубы опалесцирующие (серо-синие/коричневые), эмаль легко скалывается и быстро стирается.",
            "en": "Dentinogenesis imperfecta is a hereditary dentin defect; teeth are opalescent (grey-blue/brown), enamel chips easily and wears quickly.",
        },
        "symptoms_text": {
            "uz": "• Opal, shaffof tishlar (tug'ma, oilada).\n• Emal ko'chadi, tez yeyiladi.\n• Ildizlar kalta bo'lishi mumkin.",
            "ru": "• Опалесцирующие, полупрозрачные зубы (врождённые, семейные).\n• Эмаль скалывается, быстро стирается.\n• Корни могут быть короткими.",
            "en": "• Opalescent, translucent teeth (congenital, familial).\n• Enamel chips, wears quickly.\n• Roots may be short.",
        },
        "differential": {
            "uz": "Amelogenez imperfecta (emal nuqsoni) va dentin displaziyasidan farqlanadi.",
            "ru": "Дифференцируют с несовершенным амелогенезом (дефект эмали) и дисплазией дентина.",
            "en": "Differentiated from amelogenesis imperfecta (enamel defect) and dentin dysplasia.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga ko'rining — koronka bilan himoya, estetik tiklash va kuzatuv.",
            "ru": "Что делать: обратитесь к стоматологу — защита коронками, эстетическая реставрация и наблюдение.",
            "en": "What to do: see a dentist — protection with crowns, aesthetic restoration and monitoring.",
        },
    },
}


# ═══════════════════════════════════════════════════════════════
#  PULPA (acute_pulpitis_focal inline namuna sifatida tooth.py da)
# ═══════════════════════════════════════════════════════════════
DISEASE_INFO.update({
    "acute_pulpitis_diffuse": {
        "description": {
            "uz": "O'tkir diffuz pulpit — pulpaning butun bo'ylab tarqalgan o'tkir yallig'lanishi; o'choqli pulpitning keyingi, og'irroq bosqichi.",
            "ru": "Острый диффузный пульпит — острое воспаление, охватывающее всю пульпу; более поздняя и тяжёлая стадия после очагового.",
            "en": "Acute diffuse pulpitis is acute inflammation spread throughout the pulp; a later, more severe stage after focal pulpitis.",
        },
        "symptoms_text": {
            "uz": "• Kuchli, uzoq davom etuvchi (deyarli uzluksiz) og'riq.\n• Og'riq quloq, chakka, bo'yinga tarqaladi — qaysi tish ekanini aniqlash qiyin.\n• Issiq kuchaytiradi, sovuq biroz tinchlantiradi; tunda kuchayadi.",
            "ru": "• Сильная, длительная (почти непрерывная) боль.\n• Боль иррадиирует в ухо, висок, шею — трудно указать зуб.\n• Горячее усиливает, холодное немного успокаивает; усиливается ночью.",
            "en": "• Severe, long-lasting (almost continuous) pain.\n• Pain radiates to ear, temple, neck — hard to localize the tooth.\n• Hot worsens it, cold slightly relieves; worse at night.",
        },
        "differential": {
            "uz": "O'choqli pulpit (qisqa xuruj, lokal), apikal periodontit (perkussiyada og'riq), uchlamchi nerv nevralgiyasi va gaymoritdan farqlanadi.",
            "ru": "Дифференцируют с очаговым пульпитом (короткие приступы, локально), верхушечным периодонтитом (боль при перкуссии), невралгией тройничного нерва и гайморитом.",
            "en": "Differentiated from focal pulpitis (short, localized attacks), apical periodontitis (percussion pain), trigeminal neuralgia and sinusitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: zudlik bilan stomatologga boring — odatda kanal davolash (endodontiya) talab qilinadi. Uyda davolanmang.",
            "ru": "Что делать: срочно к стоматологу — обычно требуется лечение каналов (эндодонтия). Не лечите дома.",
            "en": "What to do: see a dentist urgently — root canal treatment (endodontics) is usually needed. Do not self-treat.",
        },
    },
    "chronic_pulpitis_fibrous": {
        "description": {
            "uz": "Surunkali fibroz pulpit — pulpaning uzoq davom etuvchi, kuchsiz yallig'lanishi; ko'pincha o'tkir pulpit yoki chuqur karies oqibati.",
            "ru": "Хронический фиброзный пульпит — длительное, слабо выраженное воспаление пульпы; часто исход острого пульпита или глубокого кариеса.",
            "en": "Chronic fibrous pulpitis is long-standing, mild pulp inflammation; often the outcome of acute pulpitis or deep caries.",
        },
        "symptoms_text": {
            "uz": "• Stimuldan (ayniqsa sovuq) keyin og'riq uzoq qoladi.\n• Og'riq kuchsiz, bo'g'iq.\n• Chuqur kovak; spontan kuchli og'riq odatda yo'q.",
            "ru": "• После раздражителя (особенно холода) боль долго не проходит.\n• Боль слабая, ноющая.\n• Глубокая полость; сильной самопроизвольной боли обычно нет.",
            "en": "• Pain lingers long after a stimulus (especially cold).\n• Pain is mild, aching.\n• Deep cavity; strong spontaneous pain usually absent.",
        },
        "differential": {
            "uz": "Chuqur karies (stimuldan keyin tez o'tadi) va o'tkir pulpitdan farqlanadi.",
            "ru": "Дифференцируют с глубоким кариесом (боль быстро проходит) и острым пульпитом.",
            "en": "Differentiated from deep caries (pain subsides quickly) and acute pulpitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — kanal davolash (endodontiya) zarur bo'ladi.",
            "ru": "Что делать: обратитесь к стоматологу — потребуется лечение каналов (эндодонтия).",
            "en": "What to do: see a dentist — root canal treatment (endodontics) will be needed.",
        },
    },
    "chronic_pulpitis_hypertrophic": {
        "description": {
            "uz": "Surunkali gipertrofik pulpit — keng ochiq kovakda pulpaning o'sib chiqishi (pulpa polipi). Ko'pincha yosh bemorlarda.",
            "ru": "Хронический гипертрофический пульпит — разрастание пульпы в широкой открытой полости (полип пульпы). Чаще у молодых.",
            "en": "Chronic hypertrophic pulpitis is overgrowth of pulp into a wide open cavity (pulp polyp). More common in young patients.",
        },
        "symptoms_text": {
            "uz": "• Kovakda go'shtsimon o'siq (polip).\n• Chaynaganda qonash va yengil og'riq.\n• Kuchli spontan og'riq odatda yo'q.",
            "ru": "• Мясистое разрастание (полип) в полости.\n• Кровоточивость и лёгкая боль при жевании.\n• Сильной самопроизвольной боли обычно нет.",
            "en": "• Fleshy overgrowth (polyp) in the cavity.\n• Bleeding and mild pain when chewing.\n• Strong spontaneous pain usually absent.",
        },
        "differential": {
            "uz": "Milk so'rg'ichining o'sib kirishidan (giperplaziya) va granulyatsion to'qimadan farqlanadi.",
            "ru": "Дифференцируют с разрастанием десневого сосочка (гиперплазией) и грануляционной тканью.",
            "en": "Differentiated from gingival papilla overgrowth (hyperplasia) and granulation tissue.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — kanal davolash yoki ko'rsatma bo'lsa tishni olib tashlash.",
            "ru": "Что делать: обратитесь к стоматологу — лечение каналов или, по показаниям, удаление зуба.",
            "en": "What to do: see a dentist — root canal treatment or, if indicated, extraction.",
        },
    },
    "chronic_pulpitis_gangrenous": {
        "description": {
            "uz": "Surunkali gangrenoz pulpit — pulpaning qisman parchalanishi (chirishi) bilan kechadigan surunkali yallig'lanish.",
            "ru": "Хронический гангренозный пульпит — хроническое воспаление с частичным распадом (гангреной) пульпы.",
            "en": "Chronic gangrenous pulpitis is chronic inflammation with partial breakdown (gangrene) of the pulp.",
        },
        "symptoms_text": {
            "uz": "• Og'izda yomon hid.\n• Issiqdan kuchayuvchi bo'g'iq og'riq.\n• Tish rangi qoraygan, chuqur kovak.",
            "ru": "• Неприятный запах изо рта.\n• Ноющая боль, усиливающаяся от горячего.\n• Потемнение зуба, глубокая полость.",
            "en": "• Bad mouth odour.\n• Aching pain that worsens with heat.\n• Darkened tooth, deep cavity.",
        },
        "differential": {
            "uz": "Pulpa nekrozi (sezuvchanlik yo'q) va surunkali periodontitdan farqlanadi.",
            "ru": "Дифференцируют с некрозом пульпы (нет чувствительности) и хроническим периодонтитом.",
            "en": "Differentiated from pulp necrosis (no sensitivity) and chronic periodontitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — kanal davolash (endodontiya) shart; aks holda periodontitga o'tadi.",
            "ru": "Что делать: обратитесь к стоматологу — обязательно лечение каналов; иначе перейдёт в периодонтит.",
            "en": "What to do: see a dentist — root canal treatment is essential; otherwise it progresses to periodontitis.",
        },
    },
    "pulp_necrosis": {
        "description": {
            "uz": "Pulpa nekrozi — tish nervining to'liq o'lishi (devital tish). Ko'pincha davolanmagan pulpit yoki travma oqibati.",
            "ru": "Некроз пульпы — полная гибель нерва зуба (девитальный зуб). Часто исход нелеченого пульпита или травмы.",
            "en": "Pulp necrosis is complete death of the tooth nerve (non-vital tooth). Often the result of untreated pulpitis or trauma.",
        },
        "symptoms_text": {
            "uz": "• Tish sovuq/issiqqa umuman javob bermaydi.\n• Tish rangi o'zgargan (kulrang/qoramtir).\n• Og'riq odatda yo'q; ba'zan yomon hid.",
            "ru": "• Зуб не реагирует на холод/тепло.\n• Изменён цвет (серый/тёмный).\n• Боли обычно нет; иногда запах.",
            "en": "• Tooth does not respond to cold/heat.\n• Discoloured (grey/dark).\n• Usually painless; sometimes bad odour.",
        },
        "differential": {
            "uz": "Gangrenoz pulpit (qisman tirik) va apikal periodontitdan (perkussiya og'rig'i) farqlanadi.",
            "ru": "Дифференцируют с гангренозным пульпитом (частично жив) и верхушечным периодонтитом (боль при перкуссии).",
            "en": "Differentiated from gangrenous pulpitis (partly vital) and apical periodontitis (percussion pain).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — kanal davolash (endodontiya) zarur; kechiktirilsa periapikal asoratlar rivojlanadi.",
            "ru": "Что делать: обратитесь к стоматологу — нужно лечение каналов; при промедлении развиваются периапикальные осложнения.",
            "en": "What to do: see a dentist — root canal treatment is needed; delay leads to periapical complications.",
        },
    },
})

# ═══════════════════════════════════════════════════════════════
#  3. PERIAPIKAL KASALLIKLAR
# ═══════════════════════════════════════════════════════════════
DISEASE_INFO.update({
    "acute_apical_periodontitis": {
        "description": {
            "uz": "O'tkir apikal periodontit — tish ildizi uchidagi (apikal) to'qimalarning o'tkir yallig'lanishi; ko'pincha pulpa nekrozi yoki infeksiya tarqalishi oqibati.",
            "ru": "Острый апикальный периодонтит — острое воспаление тканей у верхушки корня; часто следствие некроза пульпы или распространения инфекции.",
            "en": "Acute apical periodontitis is acute inflammation of tissues at the root apex; often a result of pulp necrosis or spreading infection.",
        },
        "symptoms_text": {
            "uz": "• Tishga bosish/chaynash va perkussiyada kuchli og'riq.\n• Bemor og'riyotgan tishni aniq ko'rsatadi.\n• 'Tish o'sib qolgandek' tuyg'usi; ba'zan milk shishi.",
            "ru": "• Сильная боль при накусывании/жевании и перкуссии.\n• Пациент чётко указывает больной зуб.\n• Ощущение «выросшего зуба»; иногда отёк десны.",
            "en": "• Severe pain on biting/chewing and percussion.\n• The patient points clearly to the tooth.\n• Feeling of a 'raised tooth'; sometimes gum swelling.",
        },
        "differential": {
            "uz": "Pulpitlardan (perkussiya og'riqsiz) va periapikal abscessdan (yiring, isitma) farqlanadi.",
            "ru": "Дифференцируют с пульпитами (перкуссия безболезненна) и периапикальным абсцессом (гной, лихорадка).",
            "en": "Differentiated from pulpitis (painless percussion) and periapical abscess (pus, fever).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — kanalni ochish/drenaj va endodontik davolash. Shish/isitma qo'shilsa kechiktirmang.",
            "ru": "Что делать: обратитесь к стоматологу — раскрытие/дренирование канала и эндодонтическое лечение. При отёке/лихорадке не медлите.",
            "en": "What to do: see a dentist — opening/drainage of the canal and endodontic treatment. Do not delay if swelling/fever appears.",
        },
    },
    "chronic_apical_periodontitis_fibrous": {
        "description": {
            "uz": "Surunkali fibroz periodontit — ildiz uchi atrofida fibroz to'qima bilan kechadigan sokin surunkali jarayon; deyarli simptomsiz.",
            "ru": "Хронический фиброзный периодонтит — спокойный хронический процесс с фиброзом у верхушки корня; почти бессимптомный.",
            "en": "Chronic fibrous periodontitis is a quiet chronic process with fibrosis at the root apex; almost asymptomatic.",
        },
        "symptoms_text": {
            "uz": "• Deyarli simptomsiz; tish devital.\n• Ba'zan bosimda yengil noqulaylik.\n• Asosan rentgenda (periodontal yoriq kengayishi) aniqlanadi.",
            "ru": "• Почти бессимптомно; зуб девитальный.\n• Иногда лёгкий дискомфорт при накусывании.\n• Выявляется в основном рентгенологически.",
            "en": "• Almost asymptomatic; the tooth is non-vital.\n• Occasionally mild discomfort on biting.\n• Mainly detected on X-ray.",
        },
        "differential": {
            "uz": "Granullovchi/granulomatoz periodontit va radikulyar kistadan (rentgen bilan) farqlanadi.",
            "ru": "Дифференцируют с гранулирующим/гранулематозным периодонтитом и радикулярной кистой (по рентгену).",
            "en": "Differentiated from granulating/granulomatous periodontitis and radicular cyst (by X-ray).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog rentgen bilan baholaydi; ko'rsatma bo'lsa endodontik davolash.",
            "ru": "Что делать: стоматолог оценивает по рентгену; при показаниях — эндодонтическое лечение.",
            "en": "What to do: the dentist evaluates with an X-ray; endodontic treatment if indicated.",
        },
    },
    "chronic_apical_periodontitis_granulating": {
        "description": {
            "uz": "Surunkali granullovchi periodontit — ildiz uchida faol granulyatsion to'qima o'sadigan, ko'pincha fistula bilan kechadigan shakl.",
            "ru": "Хронический гранулирующий периодонтит — форма с активным разрастанием грануляционной ткани у верхушки, часто со свищом.",
            "en": "Chronic granulating periodontitis features active granulation tissue at the apex, often with a fistula.",
        },
        "symptoms_text": {
            "uz": "• Milkda fistula (yiring chiqaruvchi kanal).\n• Davriy bo'g'iq og'riq, devital tish.\n• Ba'zan yomon hid.",
            "ru": "• Свищ на десне (выделяет гной).\n• Периодическая ноющая боль, девитальный зуб.\n• Иногда неприятный запах.",
            "en": "• Fistula on the gum (draining pus).\n• Periodic aching pain, non-vital tooth.\n• Sometimes bad odour.",
        },
        "differential": {
            "uz": "Fibroz/granulomatoz periodontit va parodontal fisuladan farqlanadi.",
            "ru": "Дифференцируют с фиброзным/гранулематозным периодонтитом и пародонтальным свищом.",
            "en": "Differentiated from fibrous/granulomatous periodontitis and periodontal fistula.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — endodontik davolash; ko'rsatma bo'lsa apikal jarrohlik.",
            "ru": "Что делать: обратитесь к стоматологу — эндодонтическое лечение; при показаниях апикальная хирургия.",
            "en": "What to do: see a dentist — endodontic treatment; apical surgery if indicated.",
        },
    },
    "chronic_apical_periodontitis_granulomatous": {
        "description": {
            "uz": "Surunkali granulomatoz periodontit — ildiz uchida chegaralangan granuloma shakllanadigan shakl; deyarli simptomsiz kechadi.",
            "ru": "Хронический гранулематозный периодонтит — форма с образованием отграниченной гранулёмы у верхушки; протекает почти бессимптомно.",
            "en": "Chronic granulomatous periodontitis forms a circumscribed granuloma at the apex; it is almost asymptomatic.",
        },
        "symptoms_text": {
            "uz": "• Deyarli simptomsiz, devital tish.\n• Rentgenda aniq chegaralangan o'choq.\n• O'tkirlashganda og'riq paydo bo'lishi mumkin.",
            "ru": "• Почти бессимптомно, девитальный зуб.\n• Чётко отграниченный очаг на рентгене.\n• При обострении возможна боль.",
            "en": "• Almost asymptomatic, non-vital tooth.\n• Well-defined focus on X-ray.\n• Pain may appear during exacerbation.",
        },
        "differential": {
            "uz": "Periapikal granuloma, radikulyar kista va granullovchi periodontitdan farqlanadi (rentgen/gistologiya).",
            "ru": "Дифференцируют с периапикальной гранулёмой, радикулярной кистой и гранулирующим периодонтитом (рентген/гистология).",
            "en": "Differentiated from periapical granuloma, radicular cyst and granulating periodontitis (X-ray/histology).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — endodontik davolash; katta o'choqda apikal rezeksiya.",
            "ru": "Что делать: обратитесь к стоматологу — эндодонтическое лечение; при крупном очаге резекция верхушки.",
            "en": "What to do: see a dentist — endodontic treatment; apical resection for a large focus.",
        },
    },
    "periapical_granuloma": {
        "description": {
            "uz": "Periapikal (apikal) granuloma — ildiz uchida surunkali infeksiyaga javoban shakllanadigan granulyatsion to'qima to'plami.",
            "ru": "Периапикальная (апикальная) гранулёма — скопление грануляционной ткани у верхушки корня в ответ на хроническую инфекцию.",
            "en": "Periapical (apical) granuloma is a mass of granulation tissue at the root apex in response to chronic infection.",
        },
        "symptoms_text": {
            "uz": "• Ko'pincha simptomsiz, devital tish.\n• Ba'zan fistula yoki yengil og'riq.\n• Rentgenda yumaloq o'choq.",
            "ru": "• Часто бессимптомно, девитальный зуб.\n• Иногда свищ или лёгкая боль.\n• Округлый очаг на рентгене.",
            "en": "• Often asymptomatic, non-vital tooth.\n• Sometimes a fistula or mild pain.\n• Rounded focus on X-ray.",
        },
        "differential": {
            "uz": "Radikulyar kista (kattaroq) va granulomatoz periodontitdan farqlanadi.",
            "ru": "Дифференцируют с радикулярной кистой (крупнее) и гранулематозным периодонтитом.",
            "en": "Differentiated from radicular cyst (larger) and granulomatous periodontitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — endodontik davolash, ko'pincha o'choq so'riladi; aks holda apikal jarrohlik.",
            "ru": "Что делать: обратитесь к стоматологу — эндодонтическое лечение, очаг часто рассасывается; иначе апикальная хирургия.",
            "en": "What to do: see a dentist — endodontic treatment, the lesion often resolves; otherwise apical surgery.",
        },
    },
    "periapical_abscess": {
        "description": {
            "uz": "Periapikal abscess — ildiz uchida yiring to'planishi bilan kechadigan o'tkir yiringli jarayon. Tez tarqalishi mumkin.",
            "ru": "Периапикальный абсцесс — острый гнойный процесс со скоплением гноя у верхушки корня. Может быстро распространяться.",
            "en": "Periapical abscess is an acute purulent process with pus collecting at the root apex. It can spread quickly.",
        },
        "symptoms_text": {
            "uz": "• Kuchli doimiy og'riq, perkussiyada keskin og'riq.\n• Milk/yuz shishi, ba'zan fistula va yiring.\n• Isitma, limfa tugunlari kattalashishi mumkin.",
            "ru": "• Сильная постоянная боль, резкая при перкуссии.\n• Отёк десны/лица, иногда свищ и гной.\n• Возможны лихорадка и увеличение лимфоузлов.",
            "en": "• Severe constant pain, sharp on percussion.\n• Gum/face swelling, sometimes fistula and pus.\n• Fever and enlarged lymph nodes may occur.",
        },
        "differential": {
            "uz": "O'tkir apikal periodontit (yiringsiz), periostit va parodontal abscessdan farqlanadi.",
            "ru": "Дифференцируют с острым апикальным периодонтитом (без гноя), периоститом и пародонтальным абсцессом.",
            "en": "Differentiated from acute apical periodontitis (no pus), periostitis and periodontal abscess.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: zudlik bilan stomatologga boring — drenaj va endodontik davolash. Yuz shishi + isitma bo'lsa — shoshilinch yordam!",
            "ru": "Что делать: срочно к стоматологу — дренирование и эндодонтическое лечение. При отёке лица и лихорадке — неотложная помощь!",
            "en": "What to do: see a dentist urgently — drainage and endodontic treatment. Facial swelling + fever — seek emergency care!",
        },
    },
    "radicular_cyst": {
        "description": {
            "uz": "Radikulyar kista — devital tish ildizi uchida suyuqlik bilan to'lgan, qobiqli bo'shliq (kista); granulomadan rivojlanadi.",
            "ru": "Радикулярная киста — заполненная жидкостью полость с оболочкой у верхушки девитального зуба; развивается из гранулёмы.",
            "en": "Radicular cyst is a fluid-filled, lined cavity at the apex of a non-vital tooth; develops from a granuloma.",
        },
        "symptoms_text": {
            "uz": "• Uzoq vaqt simptomsiz, sekin kattalashish.\n• Kattalashganda suyak bo'rtishi/bosim hissi.\n• Rentgenda aniq chegaralangan yumaloq o'choq.",
            "ru": "• Долго бессимптомно, медленный рост.\n• При увеличении — выбухание кости/чувство давления.\n• Чётко отграниченный округлый очаг на рентгене.",
            "en": "• Long asymptomatic, slow growth.\n• When enlarged — bone expansion/pressure feeling.\n• Well-defined rounded focus on X-ray.",
        },
        "differential": {
            "uz": "Periapikal granuloma (kichikroq), follikulyar va boshqa jag' kistalaridan farqlanadi.",
            "ru": "Дифференцируют с периапикальной гранулёмой (меньше), фолликулярной и другими кистами челюсти.",
            "en": "Differentiated from periapical granuloma (smaller), follicular and other jaw cysts.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/jarrohga boring — endodontik davolash yoki kistektomiya (jarrohlik olib tashlash).",
            "ru": "Что делать: к стоматологу/хирургу — эндодонтическое лечение или цистэктомия (хирургическое удаление).",
            "en": "What to do: see a dentist/surgeon — endodontic treatment or cystectomy (surgical removal).",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
#  4. PARODONT KASALLIKLARI
# ═══════════════════════════════════════════════════════════════
DISEASE_INFO.update({
    "gingivitis_catarrhal": {
        "description": {
            "uz": "Kataral gingivit — milkning eng keng tarqalgan, yuzaki yallig'lanishi; suyak yo'qotilmaydi. Asosiy sabab — gigiyena yetishmovchiligi (tish karashi).",
            "ru": "Катаральный гингивит — самое частое поверхностное воспаление дёсен без потери кости. Основная причина — недостаток гигиены (зубной налёт).",
            "en": "Catarrhal gingivitis is the most common superficial gum inflammation without bone loss. The main cause is poor hygiene (plaque).",
        },
        "symptoms_text": {
            "uz": "• Tish yuvganda yoki ovqatda milkdan qonash.\n• Milk shishgan, qizargan.\n• Yengil noqulaylik; tish harakatchanligi yo'q.",
            "ru": "• Кровоточивость дёсен при чистке или еде.\n• Дёсны отёчны, покрасневшие.\n• Лёгкий дискомфорт; подвижности зубов нет.",
            "en": "• Gums bleed when brushing or eating.\n• Gums swollen and red.\n• Mild discomfort; no tooth mobility.",
        },
        "differential": {
            "uz": "Parodontitdan (cho'ntak, suyak yo'qotilishi, harakatchanlik) farqlanadi.",
            "ru": "Дифференцируют с пародонтитом (карман, потеря кости, подвижность).",
            "en": "Differentiated from periodontitis (pocket, bone loss, mobility).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologda professional tozalash (tosh olib tashlash) va to'g'ri gigiyena. Erta bartaraf etilsa to'liq tuzaladi.",
            "ru": "Что делать: профессиональная чистка (снятие камня) у стоматолога и правильная гигиена. При раннем устранении полностью обратимо.",
            "en": "What to do: professional cleaning (scaling) at the dentist and proper hygiene. Fully reversible if addressed early.",
        },
    },
    "gingivitis_hypertrophic": {
        "description": {
            "uz": "Gipertrofik gingivit — milkning kattalashishi (giperplaziyasi) bilan kechadigan surunkali yallig'lanish; gormonal o'zgarishlar, dorilar yoki gigiyena bilan bog'liq.",
            "ru": "Гипертрофический гингивит — хроническое воспаление с разрастанием (гиперплазией) дёсен; связано с гормонами, лекарствами или гигиеной.",
            "en": "Hypertrophic gingivitis is chronic inflammation with gum overgrowth (hyperplasia); linked to hormones, medications or hygiene.",
        },
        "symptoms_text": {
            "uz": "• Milk kattalashib, tishni qisman qoplaydi.\n• Qonash, yengil og'riq.\n• Soxta cho'ntaklar (yallig'langan kattalashgan milk).",
            "ru": "• Дёсны разрастаются, частично перекрывают зубы.\n• Кровоточивость, лёгкая боль.\n• Ложные карманы (увеличенная воспалённая десна).",
            "en": "• Gums enlarge, partly covering the teeth.\n• Bleeding, mild pain.\n• False pockets (enlarged inflamed gum).",
        },
        "differential": {
            "uz": "Dori-induktsiyalangan giperplaziya, leykemiya va parodontitdan farqlanadi.",
            "ru": "Дифференцируют с медикаментозной гиперплазией, лейкозом и пародонтитом.",
            "en": "Differentiated from drug-induced hyperplasia, leukaemia and periodontitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: gigiyena va professional tozalash; sababiy omilni (dori/gormon) bartaraf etish; kerak bo'lsa gingivektomiya.",
            "ru": "Что делать: гигиена и профчистка; устранение причины (лекарство/гормон); при необходимости гингивэктомия.",
            "en": "What to do: hygiene and professional cleaning; remove the cause (drug/hormone); gingivectomy if needed.",
        },
    },
    "gingivitis_ulcerative": {
        "description": {
            "uz": "Yarali-nekrotik gingivit (Vinsent) — milkning o'tkir yarali-nekrotik yallig'lanishi; immunitet pasayishi, stress, gigiyena yomonligi bilan bog'liq.",
            "ru": "Язвенно-некротический гингивит (Венсана) — острое язвенно-некротическое воспаление дёсен; связано со снижением иммунитета, стрессом, плохой гигиеной.",
            "en": "Ulcerative necrotizing gingivitis (Vincent's) is acute ulcerative-necrotic gum inflammation; linked to low immunity, stress, poor hygiene.",
        },
        "symptoms_text": {
            "uz": "• Milk so'rg'ichlarida yara va nekroz (kulrang parda).\n• Juda yomon hid, kuchli og'riq.\n• Isitma, holsizlik, limfa tugunlari kattalashishi mumkin.",
            "ru": "• Язвы и некроз десневых сосочков (серый налёт).\n• Очень неприятный запах, сильная боль.\n• Возможны лихорадка, слабость, увеличение лимфоузлов.",
            "en": "• Ulcers and necrosis of gum papillae (grey film).\n• Very bad odour, severe pain.\n• Fever, weakness, enlarged lymph nodes possible.",
        },
        "differential": {
            "uz": "Gerpetik stomatit, qon kasalliklari (leykemiya) va oddiy gingivitdan farqlanadi.",
            "ru": "Дифференцируют с герпетическим стоматитом, болезнями крови (лейкоз) и обычным гингивитом.",
            "en": "Differentiated from herpetic stomatitis, blood disorders (leukaemia) and ordinary gingivitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: tezroq stomatologga boring — nekrozni tozalash, antiseptik, og'riqsizlantirish; shifokor ko'rsatmasi bo'yicha antibiotik.",
            "ru": "Что делать: скорее к стоматологу — очистка некроза, антисептики, обезболивание; антибиотик по назначению врача.",
            "en": "What to do: see a dentist soon — debridement, antiseptics, pain relief; antibiotics if the dentist prescribes.",
        },
    },
    "gingivitis_desquamative": {
        "description": {
            "uz": "Deskvamativ gingivit — milk yuzasining qizarib, yaltirab, po'st tashlashi bilan kechadigan holat; ko'pincha lixen planus yoki pemfigoid kabi dermatozlar belgisi.",
            "ru": "Десквамативный гингивит — состояние с покраснением, блеском и слущиванием поверхности десны; часто проявление дерматозов (плоский лишай, пемфигоид).",
            "en": "Desquamative gingivitis presents with red, shiny, peeling gum surface; often a sign of dermatoses (lichen planus, pemphigoid).",
        },
        "symptoms_text": {
            "uz": "• Milk qizil, yaltiroq, yuzasi ko'chadi.\n• Og'riq/achishish, ovqatdan kuchayadi.\n• Ko'pincha ikki tomonlama; tish toshi bilan bog'liq emas.",
            "ru": "• Десна красная, блестящая, слущивается.\n• Боль/жжение, усиливается от еды.\n• Часто двусторонне; не связано с зубным камнем.",
            "en": "• Gum is red, shiny, the surface sloughs.\n• Pain/burning, worse with food.\n• Often bilateral; not related to calculus.",
        },
        "differential": {
            "uz": "Kataral gingivit (karash bilan) va o'tkir yallig'lanishlardan farqlanadi; asosiy kasallikni aniqlash kerak.",
            "ru": "Дифференцируют с катаральным гингивитом (налёт) и острыми воспалениями; нужно выявить основное заболевание.",
            "en": "Differentiated from catarrhal gingivitis (plaque) and acute inflammations; the underlying disease must be identified.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog (va kerak bo'lsa dermatolog) ko'rigi; asosiy dermatozni davolash, yumshoq gigiyena, mahalliy vositalar.",
            "ru": "Что делать: осмотр стоматолога (и дерматолога при необходимости); лечение основного дерматоза, щадящая гигиена, местные средства.",
            "en": "What to do: see a dentist (and dermatologist if needed); treat the underlying dermatosis, gentle hygiene, topical agents.",
        },
    },
    "periodontitis_localized": {
        "description": {
            "uz": "Lokal parodontit — bir yoki bir necha tish atrofida chegaralangan parodont yallig'lanishi; ko'pincha mahalliy sabab (plomba qirrasi, lokma) bilan.",
            "ru": "Локализованный пародонтит — воспаление пародонта вокруг одного-нескольких зубов; часто из-за местной причины (край пломбы, травма пищей).",
            "en": "Localized periodontitis is periodontal inflammation around one or a few teeth; often due to a local cause (filling overhang, food impaction).",
        },
        "symptoms_text": {
            "uz": "• Aniq sohada periodontal cho'ntak.\n• Tish harakatchanligi, qonash.\n• Yomon hid, ba'zan bosimda og'riq.",
            "ru": "• Пародонтальный карман в определённом участке.\n• Подвижность зуба, кровоточивость.\n• Неприятный запах, иногда боль при накусывании.",
            "en": "• Periodontal pocket in a defined area.\n• Tooth mobility, bleeding.\n• Bad odour, sometimes pain on biting.",
        },
        "differential": {
            "uz": "Generalizatsiyalashgan parodontit (butun og'iz) va gingivitdan (suyaksiz) farqlanadi.",
            "ru": "Дифференцируют с генерализованным пародонтитом (весь рот) и гингивитом (без кости).",
            "en": "Differentiated from generalized periodontitis (whole mouth) and gingivitis (no bone loss).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: parodontologga boring — mahalliy sababni bartaraf etish, cho'ntakni tozalash (kyuretaj), gigiyena.",
            "ru": "Что делать: к пародонтологу — устранение местной причины, чистка кармана (кюретаж), гигиена.",
            "en": "What to do: see a periodontist — remove the local cause, clean the pocket (curettage), hygiene.",
        },
    },
    "periodontitis_generalized": {
        "description": {
            "uz": "Generalizatsiyalashgan parodontit — deyarli barcha tishlar atrofida parodontning surunkali yallig'lanishi; alveolyar suyak rezorbsiyasi va tish yo'qotilishiga olib keladi.",
            "ru": "Генерализованный пародонтит — хроническое воспаление пародонта почти всех зубов; ведёт к резорбции альвеолярной кости и потере зубов.",
            "en": "Generalized periodontitis is chronic periodontal inflammation around almost all teeth; leads to alveolar bone resorption and tooth loss.",
        },
        "symptoms_text": {
            "uz": "• Ko'p tishda chuqur cho'ntaklar va qonash.\n• Tishlarning harakatchanligi va siljishi.\n• Yomon hid, ba'zan yiring; milk chekinishi.",
            "ru": "• Глубокие карманы и кровоточивость на многих зубах.\n• Подвижность и смещение зубов.\n• Неприятный запах, иногда гной; рецессия десны.",
            "en": "• Deep pockets and bleeding on many teeth.\n• Tooth mobility and drifting.\n• Bad odour, sometimes pus; gum recession.",
        },
        "differential": {
            "uz": "Lokal va agressiv parodontit, parodontoz (yallig'lanishsiz) va tizimli kasalliklardan farqlanadi.",
            "ru": "Дифференцируют с локализованным и агрессивным пародонтитом, пародонтозом (без воспаления) и системными болезнями.",
            "en": "Differentiated from localized and aggressive periodontitis, periodontosis (no inflammation) and systemic diseases.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: parodontologga boring — bosqichli davolash (tozalash, kyuretaj, jarrohlik), gigiyena, shinalash; tizimli omillarni nazorat.",
            "ru": "Что делать: к пародонтологу — этапное лечение (чистка, кюретаж, хирургия), гигиена, шинирование; контроль системных факторов.",
            "en": "What to do: see a periodontist — staged treatment (cleaning, curettage, surgery), hygiene, splinting; control systemic factors.",
        },
    },
    "periodontitis_aggressive": {
        "description": {
            "uz": "Agressiv parodontit — yosh, sog'lom bemorlarda tez (oylar ichida) rivojlanadigan, yallig'lanish darajasiga nomutanosib og'ir suyak yo'qotilishi; nasliy moyillik bo'ladi.",
            "ru": "Агрессивный пародонтит — у молодых здоровых людей быстрое (за месяцы) развитие с тяжёлой потерей кости, непропорциональной воспалению; есть наследственная предрасположенность.",
            "en": "Aggressive periodontitis develops rapidly (over months) in young, healthy patients with severe bone loss disproportionate to inflammation; there is hereditary predisposition.",
        },
        "symptoms_text": {
            "uz": "• Yosh bemorda tez chuqurlashuvchi cho'ntaklar.\n• Tishlarning tez bo'shashishi va siljishi.\n• Karash kam bo'lsa-da, suyak yo'qotilishi katta.",
            "ru": "• Быстро углубляющиеся карманы у молодого пациента.\n• Быстрая подвижность и смещение зубов.\n• Несмотря на малый налёт — большая потеря кости.",
            "en": "• Rapidly deepening pockets in a young patient.\n• Rapid tooth mobility and drifting.\n• Despite little plaque, marked bone loss.",
        },
        "differential": {
            "uz": "Surunkali (sekin) parodontit va tizimli kasalliklar fonidagi parodontitdan farqlanadi.",
            "ru": "Дифференцируют с хроническим (медленным) пародонтитом и пародонтитом на фоне системных болезней.",
            "en": "Differentiated from chronic (slow) periodontitis and periodontitis associated with systemic diseases.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: zudlik bilan parodontologga boring — intensiv mexanik davolash + antibiotik (shifokor ko'rsatmasi bo'yicha), doimiy kuzatuv.",
            "ru": "Что делать: срочно к пародонтологу — интенсивное механическое лечение + антибиотики (по назначению), постоянное наблюдение.",
            "en": "What to do: see a periodontist promptly — intensive mechanical therapy + antibiotics (as prescribed), ongoing monitoring.",
        },
    },
    "periodontal_abscess": {
        "description": {
            "uz": "Parodontal abscess — periodontal cho'ntak ichida yiring to'planishi bilan kechadigan o'tkir yiringli jarayon.",
            "ru": "Пародонтальный абсцесс — острый гнойный процесс со скоплением гноя в пародонтальном кармане.",
            "en": "Periodontal abscess is an acute purulent process with pus collecting in a periodontal pocket.",
        },
        "symptoms_text": {
            "uz": "• Milkda og'riqli shish (do'mboq).\n• Cho'ntakdan yiring, yomon hid.\n• Tishni bosishda og'riq; ba'zan isitma.",
            "ru": "• Болезненный отёк (выбухание) десны.\n• Гной из кармана, неприятный запах.\n• Боль при накусывании; иногда лихорадка.",
            "en": "• Painful gum swelling (bulge).\n• Pus from the pocket, bad odour.\n• Pain on biting; sometimes fever.",
        },
        "differential": {
            "uz": "Periapikal abscess (tishdan, devital tish) va perikoronitdan farqlanadi.",
            "ru": "Дифференцируют с периапикальным абсцессом (от зуба, девитальный) и перикоронитом.",
            "en": "Differentiated from periapical abscess (from a non-vital tooth) and pericoronitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — drenaj, cho'ntakni tozalash, antiseptik; shish/isitma kuchaysa kechiktirmang.",
            "ru": "Что делать: к стоматологу — дренирование, очистка кармана, антисептики; при росте отёка/лихорадке не медлите.",
            "en": "What to do: see a dentist — drainage, pocket cleaning, antiseptics; do not delay if swelling/fever worsens.",
        },
    },
    "periimplantitis": {
        "description": {
            "uz": "Periimplantit — dental implant atrofidagi to'qimalarning yallig'lanishi va implantni ushlab turuvchi suyakning yo'qotilishi.",
            "ru": "Периимплантит — воспаление тканей вокруг импланта и потеря удерживающей его кости.",
            "en": "Peri-implantitis is inflammation of tissues around a dental implant with loss of the supporting bone.",
        },
        "symptoms_text": {
            "uz": "• Implant atrofida qonash, shish, cho'ntak.\n• Ba'zan yiring va yomon hid.\n• Kech bosqichda implantning bo'shashishi.",
            "ru": "• Кровоточивость, отёк, карман вокруг импланта.\n• Иногда гной и неприятный запах.\n• На поздней стадии подвижность импланта.",
            "en": "• Bleeding, swelling, pocket around the implant.\n• Sometimes pus and bad odour.\n• Implant mobility at a late stage.",
        },
        "differential": {
            "uz": "Periimplantat mukozitidan (suyak yo'qotilishisiz) farqlanadi.",
            "ru": "Дифференцируют с периимплантатным мукозитом (без потери кости).",
            "en": "Differentiated from peri-implant mucositis (without bone loss).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: implantolog/parodontologga boring — implant yuzasini tozalash, antiseptik, kerak bo'lsa jarrohlik; gigiyena nazorati.",
            "ru": "Что делать: к имплантологу/пародонтологу — очистка поверхности импланта, антисептики, при необходимости хирургия; контроль гигиены.",
            "en": "What to do: see an implantologist/periodontist — implant surface decontamination, antiseptics, surgery if needed; hygiene control.",
        },
    },
    "periodontosis": {
        "description": {
            "uz": "Parodontoz — parodontning yallig'lanishsiz, distrofik kasalligi; milkning tekis chekinishi va suyak atrofiyasi bilan kechadi (kamdan-kam uchraydi).",
            "ru": "Пародонтоз — невоспалительное, дистрофическое заболевание пародонта; равномерная рецессия дёсен и атрофия кости (встречается редко).",
            "en": "Periodontosis is a non-inflammatory, dystrophic periodontal disease; uniform gum recession and bone atrophy (rare).",
        },
        "symptoms_text": {
            "uz": "• Milk tekis chekinadi, ildizlar ochiladi.\n• Yallig'lanish (qonash/shish) yo'q.\n• Sezuvchanlik; cho'ntak yo'q yoki sayoz.",
            "ru": "• Равномерная рецессия дёсен, обнажение корней.\n• Воспаления (кровоточивости/отёка) нет.\n• Чувствительность; карманов нет или мелкие.",
            "en": "• Uniform gum recession, exposed roots.\n• No inflammation (bleeding/swelling).\n• Sensitivity; pockets absent or shallow.",
        },
        "differential": {
            "uz": "Parodontit (yallig'lanish, cho'ntak) va gingival retsessiyadan (lokal) farqlanadi.",
            "ru": "Дифференцируют с пародонтитом (воспаление, карман) и рецессией десны (локальной).",
            "en": "Differentiated from periodontitis (inflammation, pocket) and gingival recession (localized).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: parodontologga boring — sezuvchanlikni davolash, gigiyena, tizimli omillarni nazorat; jarayonni sekinlashtirish.",
            "ru": "Что делать: к пародонтологу — лечение чувствительности, гигиена, контроль системных факторов; замедление процесса.",
            "en": "What to do: see a periodontist — treat sensitivity, hygiene, control systemic factors; slow the process.",
        },
    },
    "gingival_recession": {
        "description": {
            "uz": "Gingival retsessiya — milk chetining apikal tomonga chekinib, ildiz yuzasining ochilishi; ko'pincha qattiq cho'tkalash, travma yoki ingichka biotip bilan.",
            "ru": "Рецессия десны — смещение края десны вниз с обнажением поверхности корня; часто из-за жёсткой чистки, травмы или тонкого биотипа.",
            "en": "Gingival recession is apical migration of the gum margin exposing the root surface; often from hard brushing, trauma or thin biotype.",
        },
        "symptoms_text": {
            "uz": "• Lokal (ko'pincha bitta tish) milk chekinishi.\n• Ildiz ochilishi va sovuqqa sezuvchanlik.\n• Yallig'lanish odatda yo'q.",
            "ru": "• Локальная (часто на одном зубе) рецессия десны.\n• Обнажение корня и чувствительность к холоду.\n• Воспаления обычно нет.",
            "en": "• Localized (often single tooth) gum recession.\n• Root exposure and cold sensitivity.\n• Usually no inflammation.",
        },
        "differential": {
            "uz": "Parodontoz (generalizatsiyalashgan) va parodontitdan farqlanadi.",
            "ru": "Дифференцируют с пародонтозом (генерализованным) и пародонтитом.",
            "en": "Differentiated from periodontosis (generalized) and periodontitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — yumshoq cho'tka/texnika, sezuvchanlikni davolash; ko'rsatma bo'lsa milk transplantatsiyasi.",
            "ru": "Что делать: к стоматологу — мягкая щётка/техника, лечение чувствительности; при показаниях пластика десны (трансплантат).",
            "en": "What to do: see a dentist — soft brush/technique, treat sensitivity; gum grafting if indicated.",
        },
    },
    "furcation_involvement": {
        "description": {
            "uz": "Furkatsion shikastlanish — ko'p ildizli tish ildizlari ajralgan joyda (furkatsiyada) parodontning yo'qotilishi; parodontitning og'irlashgan belgisi.",
            "ru": "Поражение фуркации — потеря пародонта в зоне разделения корней многокорневого зуба; признак тяжёлого пародонтита.",
            "en": "Furcation involvement is periodontal loss in the area where multi-rooted tooth roots divide; a sign of advanced periodontitis.",
        },
        "symptoms_text": {
            "uz": "• Ko'p ildizli tishda harakatchanlik.\n• Furkatsiyaga zond/til kirishi, ovqat tiqilishi.\n• Cho'ntak, yomon hid, ba'zan yiring.",
            "ru": "• Подвижность многокорневого зуба.\n• Зонд/язык заходит в фуркацию, застревание пищи.\n• Карман, неприятный запах, иногда гной.",
            "en": "• Mobility of a multi-rooted tooth.\n• A probe/tongue enters the furcation, food trapping.\n• Pocket, bad odour, sometimes pus.",
        },
        "differential": {
            "uz": "Oddiy parodontal cho'ntak va periapikal jarayondan farqlanadi.",
            "ru": "Дифференцируют с обычным пародонтальным карманом и периапикальным процессом.",
            "en": "Differentiated from a simple periodontal pocket and a periapical process.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: parodontologga boring — chuqur tozalash, furkatsiya davolash (jarrohlik, ba'zan ildizni amputatsiya); gigiyena.",
            "ru": "Что делать: к пародонтологу — глубокая чистка, лечение фуркации (хирургия, иногда ампутация корня); гигиена.",
            "en": "What to do: see a periodontist — deep cleaning, furcation therapy (surgery, sometimes root amputation); hygiene.",
        },
    },
    "pericoronitis": {
        "description": {
            "uz": "Perikoronit — to'liq chiqmagan tish (ko'pincha aql tishi) ustidagi milk kapyushonining yallig'lanishi.",
            "ru": "Перикоронит — воспаление десневого капюшона над не полностью прорезавшимся зубом (часто зубом мудрости).",
            "en": "Pericoronitis is inflammation of the gum flap over a partially erupted tooth (often a wisdom tooth).",
        },
        "symptoms_text": {
            "uz": "• Eng orqa tish sohasida og'riq va shish.\n• Og'iz ochish va yutish qiyinlashishi (trizm).\n• Yomon hid, ba'zan yiring va isitma.",
            "ru": "• Боль и отёк в области самого заднего зуба.\n• Затруднение открывания рта и глотания (тризм).\n• Неприятный запах, иногда гной и лихорадка.",
            "en": "• Pain and swelling at the very back tooth.\n• Difficulty opening the mouth and swallowing (trismus).\n• Bad odour, sometimes pus and fever.",
        },
        "differential": {
            "uz": "Parodontal/periapikal abscess va anginadan farqlanadi.",
            "ru": "Дифференцируют с пародонтальным/периапикальным абсцессом и ангиной.",
            "en": "Differentiated from periodontal/periapical abscess and tonsillitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — kapyushon ostini yuvish/tozalash, antiseptik; ko'rsatma bo'lsa tishni olib tashlash. Trizm/yutish qiyinlashsa kechiktirmang.",
            "ru": "Что делать: к стоматологу — промывание/очистка под капюшоном, антисептики; при показаниях удаление зуба. При тризме/затруднении глотания не медлите.",
            "en": "What to do: see a dentist — irrigation/cleaning under the flap, antiseptics; tooth removal if indicated. Do not delay if trismus/swallowing difficulty.",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
#  5. SHILLIQ QAVAT — stomatitlar, til, lab
# ═══════════════════════════════════════════════════════════════
DISEASE_INFO.update({
    "aphthous_stomatitis": {
        "description": {
            "uz": "Aftoz stomatit — og'iz shilliq qavatida og'riqli yaralar (aftalar) bilan kechadigan, ko'pincha qaytalanuvchi holat; stress, immunitet, ovqat bilan bog'liq.",
            "ru": "Афтозный стоматит — болезненные язвы (афты) на слизистой рта, часто рецидивирующие; связаны со стрессом, иммунитетом, пищей.",
            "en": "Aphthous stomatitis presents with painful ulcers (aphthae) on the oral mucosa, often recurrent; linked to stress, immunity, food.",
        },
        "symptoms_text": {
            "uz": "• Oq/sarg'ish markaz va qizil halqali og'riqli afta.\n• Ovqat va gapirishda og'riq.\n• Isitmasiz; ko'pincha qaytalanadi.",
            "ru": "• Болезненная афта с бело-жёлтым центром и красным ободком.\n• Боль при еде и разговоре.\n• Без лихорадки; часто рецидивирует.",
            "en": "• Painful aphtha with a white-yellow centre and red halo.\n• Pain when eating and speaking.\n• No fever; often recurrent.",
        },
        "differential": {
            "uz": "Gerpetik stomatit (pufakchalar, isitma), travmatik yara va saraton (qattiq, bitmaydigan)dan farqlanadi.",
            "ru": "Дифференцируют с герпетическим стоматитом (пузырьки, лихорадка), травматической язвой и раком (плотная, незаживающая).",
            "en": "Differentiated from herpetic stomatitis (vesicles, fever), traumatic ulcer and cancer (hard, non-healing).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: antiseptik/og'riqsizlantiruvchi gellar, qo'zg'atuvchini chetlash. 2 haftadan ortiq bitmasa — albatta shifokorga.",
            "ru": "Что делать: антисептические/обезболивающие гели, исключение раздражителей. Если не заживает дольше 2 недель — обязательно к врачу.",
            "en": "What to do: antiseptic/analgesic gels, avoid triggers. If it does not heal within 2 weeks — see a doctor.",
        },
    },
    "catarrhal_stomatitis": {
        "description": {
            "uz": "Kataral stomatit — og'iz shilliq qavatining yarasiz, yuzaki yallig'lanishi; gigiyena yomonligi, infeksiya yoki ta'sirlovchi omillar bilan bog'liq.",
            "ru": "Катаральный стоматит — поверхностное воспаление слизистой рта без язв; связано с плохой гигиеной, инфекцией или раздражителями.",
            "en": "Catarrhal stomatitis is superficial inflammation of the oral mucosa without ulcers; linked to poor hygiene, infection or irritants.",
        },
        "symptoms_text": {
            "uz": "• Shilliq qavat umumiy qizargan va shishgan.\n• Og'riq minimal, yara yo'q.\n• Yomon hid, og'iz qurishi mumkin.",
            "ru": "• Слизистая в целом покрасневшая и отёчная.\n• Боль минимальна, язв нет.\n• Возможны неприятный запах и сухость.",
            "en": "• Mucosa generally red and swollen.\n• Minimal pain, no ulcers.\n• Bad odour and dryness possible.",
        },
        "differential": {
            "uz": "Yarali stomatit (yara bor) va kandidozdan (oq qatlam) farqlanadi.",
            "ru": "Дифференцируют с язвенным стоматитом (есть язвы) и кандидозом (белый налёт).",
            "en": "Differentiated from ulcerative stomatitis (ulcers present) and candidiasis (white coating).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: gigiyena, antiseptik chayqashlar, qo'zg'atuvchini bartaraf etish. Odatda tez tuzaladi.",
            "ru": "Что делать: гигиена, антисептические полоскания, устранение раздражителя. Обычно быстро проходит.",
            "en": "What to do: hygiene, antiseptic rinses, remove the irritant. Usually resolves quickly.",
        },
    },
    "ulcerative_stomatitis": {
        "description": {
            "uz": "Yarali stomatit — shilliq qavatning yarali-nekrotik yallig'lanishi; ko'pincha gigiyena yomonligi, immunitet pasayishi yoki kataral stomatitning asorati.",
            "ru": "Язвенный стоматит — язвенно-некротическое воспаление слизистой; часто следствие плохой гигиены, снижения иммунитета или катарального стоматита.",
            "en": "Ulcerative stomatitis is ulcerative-necrotic inflammation of the mucosa; often from poor hygiene, low immunity or progression of catarrhal stomatitis.",
        },
        "symptoms_text": {
            "uz": "• Qizargan shilliq fonida yaralar.\n• Yomon hid, og'riq.\n• Ba'zan isitma, holsizlik, limfa tugunlari.",
            "ru": "• Язвы на фоне покрасневшей слизистой.\n• Неприятный запах, боль.\n• Иногда лихорадка, слабость, лимфоузлы.",
            "en": "• Ulcers on a reddened mucosa.\n• Bad odour, pain.\n• Sometimes fever, weakness, lymph nodes.",
        },
        "differential": {
            "uz": "Aftoz stomatit (qaytalanuvchi afta), yarali gingivit va qon kasalliklaridan farqlanadi.",
            "ru": "Дифференцируют с афтозным стоматитом, язвенным гингивитом и болезнями крови.",
            "en": "Differentiated from aphthous stomatitis, ulcerative gingivitis and blood disorders.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — yaralarni tozalash, antiseptik, og'riqsizlantirish; gigiyena va umumiy holatni yaxshilash.",
            "ru": "Что делать: к стоматологу — очистка язв, антисептики, обезболивание; гигиена и улучшение общего состояния.",
            "en": "What to do: see a dentist — clean the ulcers, antiseptics, pain relief; hygiene and improving general health.",
        },
    },
    "traumatic_stomatitis": {
        "description": {
            "uz": "Travmatik stomatit — mexanik (tish, protez, qattiq ovqat), termik yoki kimyoviy travma natijasida shilliq qavatda paydo bo'lgan yara.",
            "ru": "Травматический стоматит — язва слизистой от механической (зуб, протез, твёрдая пища), термической или химической травмы.",
            "en": "Traumatic stomatitis is a mucosal ulcer caused by mechanical (tooth, denture, hard food), thermal or chemical trauma.",
        },
        "symptoms_text": {
            "uz": "• Aniq travma joyida bitta yara.\n• Og'riq; sabab bartaraf etilsa bitadi.\n• Qaytalanmaydi, ko'p o'choqli emas.",
            "ru": "• Одиночная язва в месте травмы.\n• Боль; заживает после устранения причины.\n• Не рецидивирует, не множественная.",
            "en": "• Single ulcer at the site of trauma.\n• Pain; heals once the cause is removed.\n• Non-recurrent, not multiple.",
        },
        "differential": {
            "uz": "Aftoz stomatit (qaytalanuvchi) va saratondan (qattiq, bitmaydigan) farqlanadi — bu juda muhim.",
            "ru": "Дифференцируют с афтозным стоматитом (рецидивы) и раком (плотная, незаживающая) — это очень важно.",
            "en": "Differentiated from aphthous stomatitis (recurrent) and cancer (hard, non-healing) — this is very important.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: travma sababini bartaraf eting (tishni silliqlash, protezni tuzatish). Sabab yo'qolgach 2 haftada bitmasa — shifokorga.",
            "ru": "Что делать: устраните причину травмы (сошлифовка зуба, коррекция протеза). Если после устранения не заживает за 2 недели — к врачу.",
            "en": "What to do: remove the cause of trauma (smooth the tooth, adjust the denture). If it does not heal within 2 weeks after that — see a doctor.",
        },
    },
    "oral_candidiasis": {
        "description": {
            "uz": "Og'iz kandidiazi (molochnitsa) — Candida zamburug'i keltirib chiqaradigan infeksiya; ko'pincha antibiotik, immunitet pasayishi yoki protez bilan bog'liq.",
            "ru": "Кандидоз полости рта (молочница) — инфекция, вызванная грибком Candida; часто связана с антибиотиками, снижением иммунитета или протезом.",
            "en": "Oral candidiasis (thrush) is an infection caused by Candida fungus; often linked to antibiotics, low immunity or dentures.",
        },
        "symptoms_text": {
            "uz": "• Oq tvorogsimon qatlam, artilganda ko'tariladi.\n• Ostida qizil yuza.\n• Achishish, og'iz qurishi, ta'm o'zgarishi.",
            "ru": "• Белый творожистый налёт, снимается при соскабливании.\n• Под ним красная поверхность.\n• Жжение, сухость, изменение вкуса.",
            "en": "• White curd-like coating that wipes off.\n• Red surface underneath.\n• Burning, dryness, taste change.",
        },
        "differential": {
            "uz": "Leykoplakiya (artilmaydi) va lixen planusdan farqlanadi.",
            "ru": "Дифференцируют с лейкоплакией (не снимается) и плоским лишаём.",
            "en": "Differentiated from leukoplakia (does not wipe off) and lichen planus.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: shifokorga ko'rining — zamburug'ga qarshi vositalar (mahalliy/tizimli), gigiyena, sababiy omilni bartaraf etish.",
            "ru": "Что делать: к врачу — противогрибковые средства (местные/системные), гигиена, устранение причины.",
            "en": "What to do: see a doctor — antifungal agents (topical/systemic), hygiene, address the underlying cause.",
        },
    },
    "geographic_tongue": {
        "description": {
            "uz": "Geografik til (desquamativ glossit) — til yuzasida papillalar vaqtincha yo'qolib, xaritaga o'xshash ko'chib yuruvchi qizil-oq dog'lar hosil bo'lishi. Xavfsiz holat.",
            "ru": "Географический язык (десквамативный глоссит) — временная потеря сосочков с образованием мигрирующих красно-белых пятен в виде карты. Доброкачественное состояние.",
            "en": "Geographic tongue (desquamative glossitis) — temporary loss of papillae forming migrating, map-like red-white patches. A benign condition.",
        },
        "symptoms_text": {
            "uz": "• Tilda xarita kabi qizil-oq dog'lar, joyi o'zgaradi.\n• Ko'pincha simptomsiz; ba'zan achishish.\n• Achchiq/nordon ovqatdan sezuvchanlik.",
            "ru": "• Красно-белые пятна на языке как карта, меняют расположение.\n• Часто бессимптомно; иногда жжение.\n• Чувствительность к острой/кислой пище.",
            "en": "• Map-like red-white patches that change location.\n• Often asymptomatic; sometimes burning.\n• Sensitivity to spicy/sour food.",
        },
        "differential": {
            "uz": "Lixen planus, kandidoz va leykoplakiyadan farqlanadi.",
            "ru": "Дифференцируют с плоским лишаём, кандидозом и лейкоплакией.",
            "en": "Differentiated from lichen planus, candidiasis and leukoplakia.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: davo talab qilmaydi (xavfsiz). Achishsa — qo'zg'atuvchi ovqatlardan saqlaning. Shubha bo'lsa stomatologga ko'rining.",
            "ru": "Что делать: лечения не требует (доброкачественное). При жжении — избегайте раздражающей пищи. При сомнениях покажитесь стоматологу.",
            "en": "What to do: needs no treatment (benign). If it burns — avoid irritating foods. See a dentist if unsure.",
        },
    },
    "hairy_tongue": {
        "description": {
            "uz": "Qora tukli til — til usti papillalarining uzayishi va shoxlanishi natijasida tukli, qora-jigarrang qoplama hosil bo'lishi; chekish, gigiyena, antibiotik bilan bog'liq.",
            "ru": "Чёрный волосатый язык — удлинение и ороговение сосочков с образованием волосистого чёрно-коричневого налёта; связано с курением, гигиеной, антибиотиками.",
            "en": "Black hairy tongue — elongation/keratinization of papillae forming a hairy black-brown coating; linked to smoking, hygiene, antibiotics.",
        },
        "symptoms_text": {
            "uz": "• Til ustida tukli qora/jigarrang qoplama.\n• Yomon hid, ta'm o'zgarishi.\n• Og'riq odatda yo'q.",
            "ru": "• Волосистый чёрно-коричневый налёт на языке.\n• Неприятный запах, изменение вкуса.\n• Боли обычно нет.",
            "en": "• Hairy black/brown coating on the tongue.\n• Bad odour, taste change.\n• Usually no pain.",
        },
        "differential": {
            "uz": "Oziq-ovqatdan bo'yalish va kandidozdan farqlanadi.",
            "ru": "Дифференцируют с пищевым окрашиванием и кандидозом.",
            "en": "Differentiated from food staining and candidiasis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: tilni tozalash (skreper), chekishni kamaytirish, gigiyena. Odatda yaxshilanadi.",
            "ru": "Что делать: чистка языка (скребок), отказ от курения, гигиена. Обычно улучшается.",
            "en": "What to do: tongue cleaning (scraper), reduce smoking, hygiene. Usually improves.",
        },
    },
    "median_rhomboid_glossitis": {
        "description": {
            "uz": "Rombsimon glossit — til o'rtasida (orqaroq) papillasiz, silliq qizil rombsimon dog'; ko'pincha surunkali kandidoz bilan bog'liq.",
            "ru": "Ромбовидный глоссит — гладкое красное ромбовидное пятно без сосочков по средней линии языка; часто связано с хроническим кандидозом.",
            "en": "Median rhomboid glossitis — a smooth, papilla-free, red rhomboid patch in the midline of the tongue; often linked to chronic candidiasis.",
        },
        "symptoms_text": {
            "uz": "• Til o'rtasida silliq qizil romb/oval dog'.\n• Ko'pincha simptomsiz; ba'zan achishish.\n• Doimiy joylashuv (geografik tildan farqli).",
            "ru": "• Гладкое красное ромбовидное пятно по средней линии.\n• Часто бессимптомно; иногда жжение.\n• Постоянная локализация (в отличие от географического).",
            "en": "• Smooth red rhomboid patch in the midline.\n• Often asymptomatic; sometimes burning.\n• Fixed location (unlike geographic tongue).",
        },
        "differential": {
            "uz": "Geografik til (ko'chuvchi) va saratondan farqlanadi.",
            "ru": "Дифференцируют с географическим языком (мигрирующий) и раком.",
            "en": "Differentiated from geographic tongue (migrating) and cancer.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga ko'rining — kandidozni davolash (zamburug'ga qarshi), chekishni kamaytirish.",
            "ru": "Что делать: к стоматологу — лечение кандидоза (противогрибковые), отказ от курения.",
            "en": "What to do: see a dentist — treat candidiasis (antifungals), reduce smoking.",
        },
    },
    "glossitis": {
        "description": {
            "uz": "Glossit — tilning yallig'lanishi; vitamin/temir yetishmovchiligi, infeksiya yoki ta'sirlovchi omillardan kelib chiqishi mumkin.",
            "ru": "Глоссит — воспаление языка; может быть вызвано дефицитом витаминов/железа, инфекцией или раздражителями.",
            "en": "Glossitis is inflammation of the tongue; it can be caused by vitamin/iron deficiency, infection or irritants.",
        },
        "symptoms_text": {
            "uz": "• Til qizargan, shishgan, achishadi.\n• Ta'm o'zgarishi, og'riq.\n• Og'ir holatda papillalar silliqlashadi.",
            "ru": "• Язык покрасневший, отёчный, жжёт.\n• Изменение вкуса, боль.\n• В тяжёлых случаях сглаживание сосочков.",
            "en": "• Tongue red, swollen, burning.\n• Taste change, pain.\n• In severe cases papillae become smooth.",
        },
        "differential": {
            "uz": "Geografik/rombsimon glossit va kandidozdan farqlanadi; tizimli sababni aniqlash kerak.",
            "ru": "Дифференцируют с географическим/ромбовидным глосситом и кандидозом; нужно выявить системную причину.",
            "en": "Differentiated from geographic/rhomboid glossitis and candidiasis; the systemic cause must be found.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: shifokorga ko'rining — sababni davolash (vitamin/temir, infeksiya), qo'zg'atuvchini chetlash, gigiyena.",
            "ru": "Что делать: к врачу — лечение причины (витамины/железо, инфекция), исключение раздражителей, гигиена.",
            "en": "What to do: see a doctor — treat the cause (vitamins/iron, infection), avoid irritants, hygiene.",
        },
    },
    "meteorological_cheilitis": {
        "description": {
            "uz": "Meteorologik xeylit — sovuq, shamol, quyosh yoki quruq havo ta'sirida lab qizil hoshiyasining yallig'lanishi.",
            "ru": "Метеорологический хейлит — воспаление красной каймы губ от холода, ветра, солнца или сухого воздуха.",
            "en": "Meteorological cheilitis is inflammation of the lip vermilion from cold, wind, sun or dry air.",
        },
        "symptoms_text": {
            "uz": "• Lab qaqrab, yorilib, po'st tashlaydi.\n• Quruqlik, taranglik, yengil achishish.\n• Ob-havo o'zgarishi bilan bog'liq.",
            "ru": "• Губы сохнут, трескаются, шелушатся.\n• Сухость, стянутость, лёгкое жжение.\n• Связь с погодными условиями.",
            "en": "• Lips dry, crack and peel.\n• Dryness, tightness, mild burning.\n• Linked to weather conditions.",
        },
        "differential": {
            "uz": "Aktinik (quyosh, prekanseroz) va eksfoliativ xeylitdan farqlanadi.",
            "ru": "Дифференцируют с актиническим (солнце, предрак) и эксфолиативным хейлитом.",
            "en": "Differentiated from actinic (sun, precancerous) and exfoliative cheilitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: himoya balzami/krem, lab namligini saqlash, ob-havodan himoya. Odatda yaxshilanadi.",
            "ru": "Что делать: защитный бальзам/крем, увлажнение губ, защита от погоды. Обычно улучшается.",
            "en": "What to do: protective balm/cream, keep lips moisturized, protect from weather. Usually improves.",
        },
    },
    "exfoliative_cheilitis": {
        "description": {
            "uz": "Eksfoliativ xeylit — lab qizil hoshiyasining doimiy po'st tashlashi va qatlamlanishi bilan kechadigan surunkali holat; ko'pincha psixogen omillar bilan.",
            "ru": "Эксфолиативный хейлит — хроническое состояние с постоянным шелушением и образованием чешуек на красной кайме губ; часто с психогенными факторами.",
            "en": "Exfoliative cheilitis is a chronic condition with persistent peeling and scaling of the lip vermilion; often with psychogenic factors.",
        },
        "symptoms_text": {
            "uz": "• Lab doimiy po'st tashlaydi, qoraqo'ng'ir qatlamlar.\n• Quruqlik, achishish.\n• Surunkali, qaytalanuvchi kechish.",
            "ru": "• Постоянное шелушение губ, чешуйки-корки.\n• Сухость, жжение.\n• Хроническое, рецидивирующее течение.",
            "en": "• Persistent lip peeling, scaly crusts.\n• Dryness, burning.\n• Chronic, recurrent course.",
        },
        "differential": {
            "uz": "Meteorologik va aktinik xeylit, kontakt allergiyasidan farqlanadi.",
            "ru": "Дифференцируют с метеорологическим и актиническим хейлитом, контактной аллергией.",
            "en": "Differentiated from meteorological and actinic cheilitis, and contact allergy.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: lab namligi, qatlamni kovlamaslik; stomatolog/dermatolog ko'rigi, kerak bo'lsa psixoemotsional omilni bartaraf etish.",
            "ru": "Что делать: увлажнение губ, не сдирать чешуйки; осмотр стоматолога/дерматолога, при необходимости коррекция психоэмоциональных факторов.",
            "en": "What to do: moisturize lips, do not pick scales; see a dentist/dermatologist, address psychoemotional factors if needed.",
        },
    },
    "actinic_cheilitis": {
        "description": {
            "uz": "Aktinik xeylit — uzoq quyosh (ultrabinafsha) ta'siridan pastki labning surunkali shikastlanishi; prekanseroz holat hisoblanadi.",
            "ru": "Актинический хейлит — хроническое поражение нижней губы от длительного солнца (УФ); считается предраковым состоянием.",
            "en": "Actinic cheilitis is chronic damage to the lower lip from prolonged sun (UV); it is a precancerous condition.",
        },
        "symptoms_text": {
            "uz": "• Pastki lab qo'pol, quruq, oq-qizil dog'li.\n• Hoshiya chegarasi xiralashishi.\n• Yara/qattiqlashish — xavfli belgi.",
            "ru": "• Нижняя губа шершавая, сухая, с бело-красными участками.\n• Размытость границы каймы.\n• Язва/уплотнение — тревожный признак.",
            "en": "• Lower lip rough, dry, with white-red areas.\n• Blurring of the vermilion border.\n• Ulcer/induration — a warning sign.",
        },
        "differential": {
            "uz": "Meteorologik xeylit, leykoplakiya va lab saratonidan farqlanadi.",
            "ru": "Дифференцируют с метеорологическим хейлитом, лейкоплакией и раком губы.",
            "en": "Differentiated from meteorological cheilitis, leukoplakia and lip cancer.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: quyoshdan himoya (SPF balzam); stomatolog/onkologga ko'rining — prekanseroz sifatida kuzatuv va kerak bo'lsa davolash.",
            "ru": "Что делать: защита от солнца (бальзам с SPF); к стоматологу/онкологу — наблюдение как за предраком и лечение при необходимости.",
            "en": "What to do: sun protection (SPF balm); see a dentist/oncologist — monitor as a precancer and treat if needed.",
        },
    },
    "angular_cheilitis": {
        "description": {
            "uz": "Angular xeylit (zaeda) — lab burchaklarining yallig'lanishi va yorilishi; ko'pincha kandida/bakteriya, temir-vitamin yetishmovchiligi yoki tishlash balandligi pasayishi bilan.",
            "ru": "Ангулярный хейлит (заеды) — воспаление и трещины в углах рта; часто кандида/бактерии, дефицит железа-витаминов или снижение высоты прикуса.",
            "en": "Angular cheilitis — inflammation and cracks at the corners of the mouth; often candida/bacteria, iron-vitamin deficiency or reduced bite height.",
        },
        "symptoms_text": {
            "uz": "• Lab burchaklarida yoriq, yara, qotgan qatlam.\n• Achishish, og'riq, ba'zan namlanish.\n• Og'iz ochishda yorilish.",
            "ru": "• Трещины, ранки, корки в углах рта.\n• Жжение, боль, иногда мокнутие.\n• Растрескивание при открывании рта.",
            "en": "• Cracks, sores, crusts at the corners of the mouth.\n• Burning, pain, sometimes oozing.\n• Splitting when opening the mouth.",
        },
        "differential": {
            "uz": "Herpes (pufakchalar) va boshqa xeylitlardan farqlanadi.",
            "ru": "Дифференцируют с герпесом (пузырьки) и другими хейлитами.",
            "en": "Differentiated from herpes (vesicles) and other cheilitis types.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: sababni davolash (zamburug'/temir-vitamin), namlik; tishlash balandligini tiklash. Shifokorga ko'rining.",
            "ru": "Что делать: лечение причины (грибок/железо-витамины), увлажнение; восстановление высоты прикуса. Покажитесь врачу.",
            "en": "What to do: treat the cause (fungus/iron-vitamins), moisturize; restore bite height. See a doctor.",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
#  6. INFEKSION + 12. O'SMA / PREKANSEROZ (shilliq qavat)
# ═══════════════════════════════════════════════════════════════
DISEASE_INFO.update({
    "herpetic_stomatitis": {
        "description": {
            "uz": "O'tkir gerpetik stomatit — Herpes simplex virusining birlamchi infeksiyasi; ko'pincha bolalarda isitma bilan boshlanadi va og'izda ko'plab pufakcha-eroziyalar beradi.",
            "ru": "Острый герпетический стоматит — первичная инфекция вируса простого герпеса; часто у детей, начинается с лихорадки, даёт множественные пузырьки-эрозии во рту.",
            "en": "Acute herpetic stomatitis is a primary herpes simplex infection; often in children, starts with fever and causes multiple vesicles/erosions in the mouth.",
        },
        "symptoms_text": {
            "uz": "• Ko'p sonli mayda pufakchalar va eroziyalar.\n• Isitma bilan boshlanadi, limfa tugunlari kattalashishi.\n• Og'riq, ovqat yeyish qiyinlashishi.",
            "ru": "• Множественные мелкие пузырьки и эрозии.\n• Начинается с лихорадки, увеличение лимфоузлов.\n• Боль, затруднение приёма пищи.",
            "en": "• Multiple small vesicles and erosions.\n• Starts with fever, enlarged lymph nodes.\n• Pain, difficulty eating.",
        },
        "differential": {
            "uz": "Aftoz stomatit (isitmasiz, kam afta) va qo'l-oyoq-og'iz kasalligidan farqlanadi.",
            "ru": "Дифференцируют с афтозным стоматитом (без лихорадки) и синдромом рука-нога-рот.",
            "en": "Differentiated from aphthous stomatitis (no fever) and hand-foot-mouth disease.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: shifokorga ko'rining — antiviral (erta boshlansa), og'riqsizlantirish, suyuqlik. Bolada suvsizlanishdan ehtiyot bo'ling.",
            "ru": "Что делать: к врачу — противовирусные (при раннем начале), обезболивание, питьё. У детей следите за обезвоживанием.",
            "en": "What to do: see a doctor — antivirals (if started early), pain relief, fluids. Watch for dehydration in children.",
        },
    },
    "herpes_simplex_labialis": {
        "description": {
            "uz": "Herpes simplex (labial uchuq) — Herpes simplex virusining qaytalanuvchi reaktivatsiyasi; lab/burun atrofida guruh pufakchalar.",
            "ru": "Простой герпес (герпес губ) — рецидивирующая реактивация вируса простого герпеса; сгруппированные пузырьки на губах/у носа.",
            "en": "Herpes simplex labialis is a recurrent reactivation of herpes simplex virus; grouped blisters on the lips/around the nose.",
        },
        "symptoms_text": {
            "uz": "• Oldindan achishish/qichishish, so'ng guruh pufakchalar.\n• Pufakchalar yorilib, qotadi (po'st).\n• Qaytalanuvchi (stress, isitma, quyosh).",
            "ru": "• Предшествующее жжение/зуд, затем сгруппированные пузырьки.\n• Пузырьки вскрываются и покрываются коркой.\n• Рецидивирует (стресс, лихорадка, солнце).",
            "en": "• Preceding tingling/itching, then grouped blisters.\n• Blisters rupture and crust over.\n• Recurrent (stress, fever, sun).",
        },
        "differential": {
            "uz": "Herpes zoster (bir tomonlama, og'riqli) va impetigodan farqlanadi.",
            "ru": "Дифференцируют с опоясывающим герпесом (односторонний, болезненный) и импетиго.",
            "en": "Differentiated from herpes zoster (unilateral, painful) and impetigo.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: erta bosqichda antiviral krem/tabletka; quyoshdan himoya. Tez-tez qaytalansa shifokorga ko'rining.",
            "ru": "Что делать: на ранней стадии противовирусный крем/таблетки; защита от солнца. При частых рецидивах — к врачу.",
            "en": "What to do: antiviral cream/tablets at the early stage; sun protection. See a doctor if it recurs often.",
        },
    },
    "herpes_zoster": {
        "description": {
            "uz": "Herpes zoster (belbog' temiratkisi) — suvchechak virusining reaktivatsiyasi; nerv bo'ylab, yuzning bir tomonida og'riqli toshma.",
            "ru": "Опоясывающий герпес — реактивация вируса ветряной оспы; болезненная сыпь по ходу нерва, на одной стороне лица.",
            "en": "Herpes zoster is reactivation of the varicella virus; a painful rash along a nerve, on one side of the face.",
        },
        "symptoms_text": {
            "uz": "• Toshma faqat bir tomonda, chiziq bo'ylab (chegarani kesmaydi).\n• Kuchli og'riq/achishish (ko'pincha toshmagacha).\n• Pufakchalar, keyin po'stloq.",
            "ru": "• Сыпь только с одной стороны, по ходу нерва (не пересекает среднюю линию).\n• Сильная боль/жжение (часто до сыпи).\n• Пузырьки, затем корки.",
            "en": "• Rash only on one side, along the nerve (does not cross the midline).\n• Severe pain/burning (often before the rash).\n• Vesicles, then crusts.",
        },
        "differential": {
            "uz": "Herpes simplex (ikki tomonlama bo'lishi, qaytalanuvchi) va pulpit/periodontitdan farqlanadi.",
            "ru": "Дифференцируют с простым герпесом (может быть двусторонним, рецидивы) и пульпитом/периодонтитом.",
            "en": "Differentiated from herpes simplex (can be bilateral, recurrent) and pulpitis/periodontitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: tezroq shifokorga boring — antiviral erta boshlanishi muhim; og'riqni davolash. Ko'z sohasi jalb etilsa shoshilinch.",
            "ru": "Что делать: скорее к врачу — важно раннее начало противовирусных; обезболивание. При вовлечении глаза — срочно.",
            "en": "What to do: see a doctor promptly — early antivirals matter; pain control. Urgent if the eye is involved.",
        },
    },
    "hpv_papilloma": {
        "description": {
            "uz": "HPV bilan bog'liq papilloma — odam papillomavirusi keltirib chiqaradigan yaxshi sifatli, so'galsimon o'simta.",
            "ru": "ВПЧ-ассоциированная папиллома — доброкачественное бородавчатое разрастание, вызванное вирусом папилломы человека.",
            "en": "HPV-associated papilloma is a benign wart-like growth caused by the human papillomavirus.",
        },
        "symptoms_text": {
            "uz": "• Gulkaram/so'galsimon mayda o'simta.\n• Og'riqsiz, sekin o'sadi.\n• Til, lab, tanglayda joylashishi mumkin.",
            "ru": "• Мелкое бородавчатое/цветной капусты разрастание.\n• Безболезненно, растёт медленно.\n• Может быть на языке, губе, нёбе.",
            "en": "• Small wart-like/cauliflower growth.\n• Painless, slow-growing.\n• May be on tongue, lip, palate.",
        },
        "differential": {
            "uz": "Fibroma, kondiloma va yomon sifatli o'smadan farqlanadi.",
            "ru": "Дифференцируют с фибромой, кондиломой и злокачественной опухолью.",
            "en": "Differentiated from fibroma, condyloma and malignant tumour.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/jarrohga boring — jarrohlik olib tashlash va gistologiya. Tez o'ssa kechiktirmang.",
            "ru": "Что делать: к стоматологу/хирургу — хирургическое удаление и гистология. При быстром росте не медлите.",
            "en": "What to do: see a dentist/surgeon — surgical removal and histology. Do not delay if it grows fast.",
        },
    },
    "hand_foot_mouth": {
        "description": {
            "uz": "Qo'l-oyoq-og'iz kasalligi — enterovirus (Coxsackie) infeksiyasi; og'iz bilan birga qo'l va oyoqlarda toshma. Ko'pincha bolalarda.",
            "ru": "Синдром рука-нога-рот — энтеровирусная (Коксаки) инфекция; сыпь во рту вместе с кистями и стопами. Чаще у детей.",
            "en": "Hand-foot-mouth disease is an enterovirus (Coxsackie) infection; a rash in the mouth together with hands and feet. Mostly in children.",
        },
        "symptoms_text": {
            "uz": "• Og'izda yaralar/pufakchalar + qo'l-oyoqda toshma.\n• Isitma, holsizlik.\n• Yutishda og'riq (bolada).",
            "ru": "• Язвочки/пузырьки во рту + сыпь на кистях и стопах.\n• Лихорадка, слабость.\n• Боль при глотании (у ребёнка).",
            "en": "• Sores/vesicles in the mouth + rash on hands and feet.\n• Fever, malaise.\n• Painful swallowing (in a child).",
        },
        "differential": {
            "uz": "Gerpetik stomatit (faqat og'iz) va suvchechakdan farqlanadi.",
            "ru": "Дифференцируют с герпетическим стоматитом (только рот) и ветрянкой.",
            "en": "Differentiated from herpetic stomatitis (mouth only) and chickenpox.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: simptomatik (suyuqlik, og'riqsizlantirish), o'z-o'zidan o'tadi. Suvsizlanish belgilarida shifokorga.",
            "ru": "Что делать: симптоматически (питьё, обезболивание), проходит само. При признаках обезвоживания — к врачу.",
            "en": "What to do: symptomatic care (fluids, pain relief), it self-resolves. See a doctor if dehydration signs appear.",
        },
    },
    "oral_syphilis": {
        "description": {
            "uz": "Sifilisning og'izdagi ko'rinishi — Treponema pallidum infeksiyasi; bosqichga qarab og'riqsiz qattiq yara (shankr), toshma yoki gumma beradi.",
            "ru": "Проявления сифилиса в полости рта — инфекция Treponema pallidum; в зависимости от стадии даёт безболезненный твёрдый шанкр, высыпания или гумму.",
            "en": "Oral syphilis — infection with Treponema pallidum; depending on the stage it causes a painless firm chancre, mucous patches or a gumma.",
        },
        "symptoms_text": {
            "uz": "• Qattiq qirrali, og'riqsiz yara (shankr).\n• Regionar limfa tugunlari kattalashishi.\n• Keyingi bosqichda oq dog'lar/toshma.",
            "ru": "• Твёрдая, безболезненная язва (шанкр).\n• Увеличение регионарных лимфоузлов.\n• На поздних стадиях белые пятна/высыпания.",
            "en": "• Firm, painless ulcer (chancre).\n• Enlarged regional lymph nodes.\n• White patches/rash at later stages.",
        },
        "differential": {
            "uz": "Travmatik yara, aftoz stomatit va saratondan farqlanadi; serologik tasdiq zarur.",
            "ru": "Дифференцируют с травматической язвой, афтозным стоматитом и раком; нужна серологическая верификация.",
            "en": "Differentiated from traumatic ulcer, aphthous stomatitis and cancer; serological confirmation is needed.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: zudlik bilan shifokorga (dermatovenerolog) — tizimli antibiotik (penitsillin). Bu yuqumli kasallik.",
            "ru": "Что делать: срочно к врачу (дерматовенеролог) — системные антибиотики (пенициллин). Это заразное заболевание.",
            "en": "What to do: see a doctor (dermatovenereologist) promptly — systemic antibiotics (penicillin). It is a contagious disease.",
        },
    },
    "oral_tuberculosis": {
        "description": {
            "uz": "Tuberkulyozning og'izdagi ko'rinishi — Mycobacterium tuberculosis tomonidan; ko'pincha o'pka silining ikkilamchi belgisi, uzoq bitmaydigan yara.",
            "ru": "Проявления туберкулёза в полости рта — Mycobacterium tuberculosis; чаще вторичный признак лёгочного туберкулёза, длительно незаживающая язва.",
            "en": "Oral tuberculosis — caused by Mycobacterium tuberculosis; often secondary to pulmonary TB, a long non-healing ulcer.",
        },
        "symptoms_text": {
            "uz": "• Uzoq bitmaydigan og'riqli yara (ko'pincha til orqasida).\n• Yumshoq, qirrasi o'yilgan yara.\n• Umumiy belgilar: vazn yo'qotish, kechki terlash.",
            "ru": "• Длительно незаживающая болезненная язва (часто на спинке языка).\n• Мягкая, с подрытыми краями.\n• Общие симптомы: потеря веса, ночная потливость.",
            "en": "• Long non-healing painful ulcer (often on the tongue dorsum).\n• Soft, with undermined edges.\n• Systemic signs: weight loss, night sweats.",
        },
        "differential": {
            "uz": "Saraton (qattiq, indurativ), sifilis (og'riqsiz) va travmatik yaradan farqlanadi.",
            "ru": "Дифференцируют с раком (плотный, индуративный), сифилисом (безболезненный) и травматической язвой.",
            "en": "Differentiated from cancer (hard, indurated), syphilis (painless) and traumatic ulcer.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: shifokorga (ftiziatr) — tizimli silga qarshi davolash. Og'iz o'chog'i o'pka tekshiruvini talab qiladi.",
            "ru": "Что делать: к врачу (фтизиатр) — системное противотуберкулёзное лечение. Очаг во рту требует обследования лёгких.",
            "en": "What to do: see a doctor (TB specialist) — systemic anti-TB therapy. An oral focus warrants lung evaluation.",
        },
    },
    "actinomycosis": {
        "description": {
            "uz": "Aktinomikoz — Actinomyces bakteriyalari keltirib chiqaradigan surunkali yiringli infeksiya; qattiq yog'ochsimon shish va ko'p fistula.",
            "ru": "Актиномикоз — хроническая гнойная инфекция, вызванная бактериями Actinomyces; плотная деревянистая припухлость с множественными свищами.",
            "en": "Actinomycosis is a chronic suppurative infection caused by Actinomyces bacteria; a hard, woody swelling with multiple fistulas.",
        },
        "symptoms_text": {
            "uz": "• Qattiq, yog'ochsimon shish.\n• Ko'p fistula, ulardan sarg'ish donachalar (oltingugurt donalari).\n• Sekin, surunkali kechish.",
            "ru": "• Плотная, деревянистая припухлость.\n• Множественные свищи с желтоватыми зёрнами (серные гранулы).\n• Медленное, хроническое течение.",
            "en": "• Hard, woody swelling.\n• Multiple fistulas draining yellowish granules (sulphur granules).\n• Slow, chronic course.",
        },
        "differential": {
            "uz": "Surunkali osteomiyelit, o'sma va boshqa infeksiyalardan farqlanadi.",
            "ru": "Дифференцируют с хроническим остеомиелитом, опухолью и другими инфекциями.",
            "en": "Differentiated from chronic osteomyelitis, tumour and other infections.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: shifokorga boring — uzoq muddatli antibiotik (penitsillin) va kerak bo'lsa jarrohlik drenaj.",
            "ru": "Что делать: к врачу — длительная антибиотикотерапия (пенициллин) и при необходимости хирургическое дренирование.",
            "en": "What to do: see a doctor — prolonged antibiotics (penicillin) and surgical drainage if needed.",
        },
    },
    "leukoplakia": {
        "description": {
            "uz": "Leykoplakiya — shilliq qavatda artilmaydigan oq dog'; tamaki/surunkali ta'sir bilan bog'liq prekanseroz holat.",
            "ru": "Лейкоплакия — несоскабливаемое белое пятно на слизистой; предраковое состояние, связанное с табаком/хроническим раздражением.",
            "en": "Leukoplakia is a non-scrapable white patch on the mucosa; a precancerous condition linked to tobacco/chronic irritation.",
        },
        "symptoms_text": {
            "uz": "• Artilmaydigan oq dog' (chegaralangan).\n• Odatda og'riqsiz.\n• Tamaki/surunkali ta'sir bilan bog'liq.",
            "ru": "• Несоскабливаемое белое пятно (отграниченное).\n• Обычно безболезненно.\n• Связь с табаком/хроническим раздражением.",
            "en": "• Non-scrapable white patch (well-defined).\n• Usually painless.\n• Linked to tobacco/chronic irritation.",
        },
        "differential": {
            "uz": "Kandidoz (artiladi), lixen planus va eritroplakiyadan farqlanadi.",
            "ru": "Дифференцируют с кандидозом (снимается), плоским лишаём и эритроплакией.",
            "en": "Differentiated from candidiasis (wipes off), lichen planus and erythroplakia.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/onkologga ko'rining — qo'zg'atuvchini (tamaki) chetlash, biopsiya va kuzatuv; ko'rsatma bo'lsa olib tashlash.",
            "ru": "Что делать: к стоматологу/онкологу — устранение раздражителя (табак), биопсия и наблюдение; при показаниях удаление.",
            "en": "What to do: see a dentist/oncologist — remove the irritant (tobacco), biopsy and monitoring; removal if indicated.",
        },
    },
    "erythroplakia": {
        "description": {
            "uz": "Eritroplakiya — artilmaydigan qizil, baxmaldek dog'; leykoplakiyaga qaraganda saratonga aylanish xavfi ancha yuqori prekanseroz.",
            "ru": "Эритроплакия — несоскабливаемое красное бархатистое пятно; предрак с гораздо более высоким риском озлокачествления, чем лейкоплакия.",
            "en": "Erythroplakia is a non-scrapable red, velvety patch; a precancer with a much higher malignant risk than leukoplakia.",
        },
        "symptoms_text": {
            "uz": "• Qizil, baxmaldek, silliq dog' (artilmaydi).\n• Odatda og'riqsiz.\n• Ko'pincha tamaki/alkogol bilan.",
            "ru": "• Красное, бархатистое, гладкое пятно (не снимается).\n• Обычно безболезненно.\n• Часто с табаком/алкоголем.",
            "en": "• Red, velvety, smooth patch (non-scrapable).\n• Usually painless.\n• Often with tobacco/alcohol.",
        },
        "differential": {
            "uz": "Yallig'lanish, kandidoz va boshlang'ich saratondan farqlanadi.",
            "ru": "Дифференцируют с воспалением, кандидозом и ранним раком.",
            "en": "Differentiated from inflammation, candidiasis and early cancer.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: zudlik bilan onkolog/jarrohga — biopsiya shart (saraton xavfi yuqori), olib tashlash va kuzatuv.",
            "ru": "Что делать: срочно к онкологу/хирургу — обязательна биопсия (высокий риск рака), удаление и наблюдение.",
            "en": "What to do: see an oncologist/surgeon promptly — biopsy is essential (high cancer risk), removal and monitoring.",
        },
    },
    "oral_submucous_fibrosis": {
        "description": {
            "uz": "Oral submukoz fibroz — shilliq qavat ostida fibroz tortmalar hosil bo'lishi; betel/nos iste'moli bilan bog'liq prekanseroz holat.",
            "ru": "Подслизистый фиброз полости рта — образование фиброзных тяжей под слизистой; предрак, связанный с употреблением бетеля/наса.",
            "en": "Oral submucous fibrosis — fibrous bands forming under the mucosa; a precancer linked to betel/areca/nas use.",
        },
        "symptoms_text": {
            "uz": "• Og'iz ochilishining asta-sekin cheklanishi.\n• Shilliq oqarib, qotadi (fibroz tortmalar).\n• Achchiq ovqatdan achishish.",
            "ru": "• Постепенное ограничение открывания рта.\n• Слизистая бледнеет и уплотняется (фиброзные тяжи).\n• Жжение от острой пищи.",
            "en": "• Gradually limited mouth opening.\n• Mucosa pales and stiffens (fibrous bands).\n• Burning from spicy food.",
        },
        "differential": {
            "uz": "Lixen planus, sklerodermiya va TMJ kasalliklaridan farqlanadi.",
            "ru": "Дифференцируют с плоским лишаём, склеродермией и заболеваниями ВНЧС.",
            "en": "Differentiated from lichen planus, scleroderma and TMJ disorders.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: betel/nosni butunlay tashlang; stomatolog/onkologga boring — kuzatuv, fizioterapiya, kerak bo'lsa jarrohlik.",
            "ru": "Что делать: полностью откажитесь от бетеля/наса; к стоматологу/онкологу — наблюдение, физиотерапия, при необходимости хирургия.",
            "en": "What to do: completely stop betel/areca/nas; see a dentist/oncologist — monitoring, physiotherapy, surgery if needed.",
        },
    },
    "oral_lichen_planus": {
        "description": {
            "uz": "Og'iz lixen planusi — surunkali immun-vositali kasallik; ko'pincha yonoq ichida to'r shaklidagi oq chiziqlar (Wickham), ba'zan eroziv shakl.",
            "ru": "Красный плоский лишай полости рта — хроническое иммунно-опосредованное заболевание; кружевные белые линии (Уикхема), иногда эрозивная форма.",
            "en": "Oral lichen planus is a chronic immune-mediated disease; lacy white lines (Wickham's striae), sometimes an erosive form.",
        },
        "symptoms_text": {
            "uz": "• To'r/chiziq shaklidagi oq naqsh, ikki tomonlama.\n• Ko'pincha yonoq ichida; ba'zan eroziya va og'riq.\n• Surunkali, qaytalanuvchi.",
            "ru": "• Кружевной/линейный белый узор, двусторонне.\n• Чаще на слизистой щёк; иногда эрозии и боль.\n• Хроническое, рецидивирующее.",
            "en": "• Lacy/linear white pattern, bilateral.\n• Often on the cheeks; sometimes erosion and pain.\n• Chronic, recurrent.",
        },
        "differential": {
            "uz": "Leykoplakiya (bir tomonlama dog'), kandidoz va lupusdan farqlanadi.",
            "ru": "Дифференцируют с лейкоплакией, кандидозом и красной волчанкой.",
            "en": "Differentiated from leukoplakia, candidiasis and lupus.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/dermatologga boring — mahalliy kortikosteroidlar, qo'zg'atuvchini chetlash; eroziv shaklni kuzatish (saraton xavfi).",
            "ru": "Что делать: к стоматологу/дерматологу — местные кортикостероиды, исключение раздражителей; наблюдение эрозивной формы (риск рака).",
            "en": "What to do: see a dentist/dermatologist — topical corticosteroids, avoid irritants; monitor the erosive form (cancer risk).",
        },
    },
    "fibroma": {
        "description": {
            "uz": "Fibroma — biriktiruvchi to'qimadan iborat yaxshi sifatli o'sma; ko'pincha surunkali ishqalanish/tishlab olish joyida.",
            "ru": "Фиброма — доброкачественная опухоль из соединительной ткани; часто в месте хронического трения/прикусывания.",
            "en": "Fibroma is a benign connective tissue tumour; often at a site of chronic friction/biting.",
        },
        "symptoms_text": {
            "uz": "• Qattiqroq, silliq, og'riqsiz tugun.\n• Sekin o'sadi, barqaror.\n• Ko'pincha yonoq/lab/til chetida.",
            "ru": "• Плотноватый, гладкий, безболезненный узел.\n• Растёт медленно, стабилен.\n• Часто на щеке/губе/крае языка.",
            "en": "• Firm, smooth, painless nodule.\n• Slow-growing, stable.\n• Often on the cheek/lip/tongue edge.",
        },
        "differential": {
            "uz": "Papilloma, lipoma va yomon sifatli o'smadan farqlanadi.",
            "ru": "Дифференцируют с папилломой, липомой и злокачественной опухолью.",
            "en": "Differentiated from papilloma, lipoma and malignant tumour.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/jarrohga boring — ishqalanish sababini bartaraf etish, jarrohlik olib tashlash va gistologiya.",
            "ru": "Что делать: к стоматологу/хирургу — устранение причины трения, хирургическое удаление и гистология.",
            "en": "What to do: see a dentist/surgeon — remove the friction cause, surgical excision and histology.",
        },
    },
    "hemangioma": {
        "description": {
            "uz": "Gemangioma — qon tomirlaridan iborat yaxshi sifatli o'sma; ko'pincha tug'ma yoki erta yoshda paydo bo'ladi.",
            "ru": "Гемангиома — доброкачественная опухоль из кровеносных сосудов; часто врождённая или появляется в раннем возрасте.",
            "en": "Hemangioma is a benign tumour of blood vessels; often congenital or appearing early in life.",
        },
        "symptoms_text": {
            "uz": "• Qizil-ko'kimtir o'simta.\n• Bosganda rangi oqaradi (blanching).\n• Og'riqsiz; travmadan qonashi mumkin.",
            "ru": "• Красно-синюшное образование.\n• Бледнеет при надавливании (blanching).\n• Безболезненно; может кровоточить от травмы.",
            "en": "• Red-bluish lesion.\n• Blanches (pales) when pressed.\n• Painless; may bleed if traumatized.",
        },
        "differential": {
            "uz": "Varikoz, pigmentli o'smalar va Kaposi sarkomasidan farqlanadi.",
            "ru": "Дифференцируют с варикозом, пигментными образованиями и саркомой Капоши.",
            "en": "Differentiated from varix, pigmented lesions and Kaposi's sarcoma.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/jarrohga ko'rining — kuzatuv yoki davolash (sklerozlash, lazer, jarrohlik). Qonashda shoshilinch yordam.",
            "ru": "Что делать: к стоматологу/хирургу — наблюдение или лечение (склерозирование, лазер, хирургия). При кровотечении — неотложно.",
            "en": "What to do: see a dentist/surgeon — observation or treatment (sclerotherapy, laser, surgery). Bleeding needs urgent care.",
        },
    },
    "lipoma": {
        "description": {
            "uz": "Lipoma — yog' to'qimasidan iborat yaxshi sifatli o'sma; yumshoq, sekin o'suvchi tugun.",
            "ru": "Липома — доброкачественная опухоль из жировой ткани; мягкий, медленно растущий узел.",
            "en": "Lipoma is a benign tumour of fatty tissue; a soft, slowly growing nodule.",
        },
        "symptoms_text": {
            "uz": "• Yumshoq, sarg'ish, og'riqsiz tugun.\n• Juda sekin o'sadi.\n• Ko'pincha yonoq/og'iz tubida.",
            "ru": "• Мягкий, желтоватый, безболезненный узел.\n• Растёт очень медленно.\n• Часто на щеке/дне рта.",
            "en": "• Soft, yellowish, painless nodule.\n• Very slow-growing.\n• Often on the cheek/floor of mouth.",
        },
        "differential": {
            "uz": "Fibroma, kista va mukoseledan farqlanadi.",
            "ru": "Дифференцируют с фибромой, кистой и мукоцеле.",
            "en": "Differentiated from fibroma, cyst and mucocele.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/jarrohga boring — jarrohlik olib tashlash (kerak bo'lsa) va gistologiya.",
            "ru": "Что делать: к стоматологу/хирургу — хирургическое удаление (при необходимости) и гистология.",
            "en": "What to do: see a dentist/surgeon — surgical removal (if needed) and histology.",
        },
    },
    "oral_scc": {
        "description": {
            "uz": "Og'iz bo'shlig'i yassi hujayrali karsinomasi — og'izning eng keng tarqalgan yomon sifatli o'smasi; tamaki, alkogol va surunkali ta'sir bilan bog'liq.",
            "ru": "Плоскоклеточный рак полости рта — самая частая злокачественная опухоль рта; связан с табаком, алкоголем и хроническим раздражением.",
            "en": "Oral squamous cell carcinoma is the most common malignant oral tumour; linked to tobacco, alcohol and chronic irritation.",
        },
        "symptoms_text": {
            "uz": "• Qattiq, o'rnashgan (indurativ) yara/o'simta, 3 haftadan ortiq bitmaydi.\n• Oson qonaydi; ba'zan uvishish/karaxtlik.\n• Bo'yin limfa tugunlari kattalashishi.",
            "ru": "• Плотная, фиксированная (индуративная) язва/образование, не заживает >3 недель.\n• Легко кровоточит; иногда онемение.\n• Увеличение шейных лимфоузлов.",
            "en": "• Hard, fixed (indurated) ulcer/growth not healing for >3 weeks.\n• Bleeds easily; sometimes numbness.\n• Enlarged neck lymph nodes.",
        },
        "differential": {
            "uz": "Travmatik yara, sil, sifilis va prekanseroz holatlardan farqlanadi; biopsiya hal qiluvchi.",
            "ru": "Дифференцируют с травматической язвой, туберкулёзом, сифилисом и предраком; решающа биопсия.",
            "en": "Differentiated from traumatic ulcer, TB, syphilis and precancers; biopsy is decisive.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ZUDLIK bilan onkolog/yuz-jag' jarrohiga boring — biopsiya va kompleks davolash (jarrohlik, nur, kimyo). Erta tashxis hayotiy muhim.",
            "ru": "Что делать: СРОЧНО к онкологу/челюстно-лицевому хирургу — биопсия и комплексное лечение (хирургия, лучевая, химия). Ранняя диагностика критична.",
            "en": "What to do: see an oncologist/maxillofacial surgeon URGENTLY — biopsy and combined treatment (surgery, radiation, chemo). Early diagnosis is critical.",
        },
    },
    "tongue_cancer": {
        "description": {
            "uz": "Til saratoni — ko'pincha tilning yon yuzasida yassi hujayrali karsinoma; tamaki/alkogol bilan bog'liq, erta metastaz beradi.",
            "ru": "Рак языка — чаще плоскоклеточный рак на боковой поверхности языка; связан с табаком/алкоголем, рано метастазирует.",
            "en": "Tongue cancer — usually squamous cell carcinoma on the lateral tongue; linked to tobacco/alcohol, metastasizes early.",
        },
        "symptoms_text": {
            "uz": "• Tilda qattiq, bitmaydigan yara/o'simta.\n• Og'riq, uvishish, til harakatining cheklanishi.\n• Bo'yin limfa tugunlari kattalashishi.",
            "ru": "• Плотная, незаживающая язва/образование на языке.\n• Боль, онемение, ограничение подвижности языка.\n• Увеличение шейных лимфоузлов.",
            "en": "• Hard, non-healing ulcer/growth on the tongue.\n• Pain, numbness, limited tongue movement.\n• Enlarged neck lymph nodes.",
        },
        "differential": {
            "uz": "Travmatik yara, sil yarasi va rombsimon glossitdan farqlanadi.",
            "ru": "Дифференцируют с травматической язвой, туберкулёзной язвой и ромбовидным глосситом.",
            "en": "Differentiated from traumatic ulcer, TB ulcer and rhomboid glossitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ZUDLIK bilan onkologga — biopsiya va kompleks davolash. Til chetidagi bitmaydigan yarani e'tiborsiz qoldirmang.",
            "ru": "Что делать: СРОЧНО к онкологу — биопсия и комплексное лечение. Не игнорируйте незаживающую язву на крае языка.",
            "en": "What to do: see an oncologist URGENTLY — biopsy and combined treatment. Do not ignore a non-healing ulcer on the tongue edge.",
        },
    },
    "lip_cancer": {
        "description": {
            "uz": "Lab saratoni — ko'pincha pastki labda yassi hujayrali karsinoma; uzoq quyosh ta'siri va chekish bilan bog'liq.",
            "ru": "Рак губы — чаще плоскоклеточный рак на нижней губе; связан с длительным солнцем и курением.",
            "en": "Lip cancer — usually squamous cell carcinoma on the lower lip; linked to chronic sun exposure and smoking.",
        },
        "symptoms_text": {
            "uz": "• Pastki labda qattiq, bitmaydigan yara/qadoq.\n• Sekin kattalashish, oson qonash.\n• Ba'zan aktinik xeylit fonida.",
            "ru": "• Плотная, незаживающая язва/корка на нижней губе.\n• Медленный рост, лёгкая кровоточивость.\n• Иногда на фоне актинического хейлита.",
            "en": "• Hard, non-healing ulcer/crust on the lower lip.\n• Slow growth, easy bleeding.\n• Sometimes on a background of actinic cheilitis.",
        },
        "differential": {
            "uz": "Aktinik xeylit, herpes va travmatik yaradan farqlanadi.",
            "ru": "Дифференцируют с актиническим хейлитом, герпесом и травматической язвой.",
            "en": "Differentiated from actinic cheilitis, herpes and traumatic ulcer.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ZUDLIK bilan onkolog/jarrohga — biopsiya va davolash. Quyoshdan himoyalaning. Prognoz erta tashxisda yaxshi.",
            "ru": "Что делать: СРОЧНО к онкологу/хирургу — биопсия и лечение. Защищайтесь от солнца. Прогноз хороший при раннем выявлении.",
            "en": "What to do: see an oncologist/surgeon URGENTLY — biopsy and treatment. Protect from the sun. Prognosis is good with early detection.",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
#  7. JAG' SUYAGI
# ═══════════════════════════════════════════════════════════════
DISEASE_INFO.update({
    "periostitis": {
        "description": {
            "uz": "Periostit (fleyus) — jag' suyagi pardasining (periost) yiringli yallig'lanishi; ko'pincha sababchi tishdan infeksiya tarqalishi natijasida.",
            "ru": "Периостит (флюс) — гнойное воспаление надкостницы челюсти; чаще из-за распространения инфекции от причинного зуба.",
            "en": "Periostitis (gumboil) is purulent inflammation of the jaw periosteum; usually from infection spreading from a causative tooth.",
        },
        "symptoms_text": {
            "uz": "• Milk/yuzda lokal shish (fleyus).\n• Sababchi tishda og'riq, palpatsiyada og'riq.\n• Ba'zan isitma va limfa tugunlari.",
            "ru": "• Локальный отёк десны/лица (флюс).\n• Боль в причинном зубе, болезненность при пальпации.\n• Иногда лихорадка и лимфоузлы.",
            "en": "• Localized gum/face swelling (gumboil).\n• Pain in the causative tooth, tender on palpation.\n• Sometimes fever and lymph nodes.",
        },
        "differential": {
            "uz": "Periapikal/parodontal abscess va osteomiyelitdan farqlanadi.",
            "ru": "Дифференцируют с периапикальным/пародонтальным абсцессом и остеомиелитом.",
            "en": "Differentiated from periapical/periodontal abscess and osteomyelitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: tezroq stomatologga boring — drenaj (kesib bo'shatish) va sababchi tishni davolash. Shish tez kattalashsa kechiktirmang.",
            "ru": "Что делать: скорее к стоматологу — дренирование (вскрытие) и лечение причинного зуба. При быстром росте отёка не медлите.",
            "en": "What to do: see a dentist soon — drainage (incision) and treatment of the causative tooth. Do not delay if swelling grows fast.",
        },
    },
    "osteitis": {
        "description": {
            "uz": "Osteit — jag' suyagining lokal yallig'lanishi; ko'pincha ekstraksiya yoki infeksiyadan keyin, osteomiyelitdan oldingi bosqich bo'lishi mumkin.",
            "ru": "Остит — локальное воспаление кости челюсти; часто после удаления или инфекции, может предшествовать остеомиелиту.",
            "en": "Osteitis is localized inflammation of the jawbone; often after extraction or infection, may precede osteomyelitis.",
        },
        "symptoms_text": {
            "uz": "• Lokal bo'g'iq og'riq (ekstraksiya/infeksiyadan keyin).\n• Ba'zan yengil shish, yomon hid.\n• Diffuz emas, isitma yuqori emas.",
            "ru": "• Локальная ноющая боль (после удаления/инфекции).\n• Иногда лёгкий отёк, неприятный запах.\n• Не диффузный, температура невысокая.",
            "en": "• Localized aching pain (after extraction/infection).\n• Sometimes mild swelling, bad odour.\n• Not diffuse, no high fever.",
        },
        "differential": {
            "uz": "Alveolit (bo'sh katakcha) va osteomiyelitdan (diffuz, sekvestr) farqlanadi.",
            "ru": "Дифференцируют с альвеолитом (пустая лунка) и остеомиелитом (диффузный, секвестр).",
            "en": "Differentiated from alveolitis (empty socket) and osteomyelitis (diffuse, sequestrum).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — o'choqni tozalash, antiseptik/antibiotik (ko'rsatma bo'yicha), kuzatuv.",
            "ru": "Что делать: к стоматологу — санация очага, антисептики/антибиотики (по показаниям), наблюдение.",
            "en": "What to do: see a dentist — debridement of the focus, antiseptics/antibiotics (as indicated), monitoring.",
        },
    },
    "alveolitis": {
        "description": {
            "uz": "Alveolit (quruq katakcha) — tish olingandan keyin katakchadagi qon laxtasining yo'qolishi va yallig'lanishi; kuchli og'riq bilan kechadi.",
            "ru": "Альвеолит (сухая лунка) — потеря кровяного сгустка и воспаление лунки после удаления зуба; сопровождается сильной болью.",
            "en": "Alveolitis (dry socket) is loss of the blood clot and inflammation of the socket after tooth extraction; with severe pain.",
        },
        "symptoms_text": {
            "uz": "• Tish olingandan 3-4 kun keyin kuchaygan og'riq.\n• Bo'sh katakcha (laxta yo'q), yomon hid.\n• Og'riq quloq/chakkaga tarqalishi mumkin.",
            "ru": "• Усилившаяся боль через 3-4 дня после удаления.\n• Пустая лунка (нет сгустка), неприятный запах.\n• Боль может отдавать в ухо/висок.",
            "en": "• Pain intensifying 3-4 days after extraction.\n• Empty socket (no clot), bad odour.\n• Pain may radiate to ear/temple.",
        },
        "differential": {
            "uz": "Osteit/osteomiyelit va katakchada qolgan ildiz parchasidan farqlanadi.",
            "ru": "Дифференцируют с оститом/остеомиелитом и оставшимся осколком корня в лунке.",
            "en": "Differentiated from osteitis/osteomyelitis and a retained root fragment in the socket.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga boring — katakchani yuvish va davolovchi tampon qo'yish, og'riqsizlantirish. O'zingiz kavlamang.",
            "ru": "Что делать: к стоматологу — промывание лунки и лечебная повязка, обезболивание. Не выскабливайте сами.",
            "en": "What to do: see a dentist — socket irrigation and a medicated dressing, pain relief. Do not scrape it yourself.",
        },
    },
    "osteomyelitis_acute": {
        "description": {
            "uz": "O'tkir osteomiyelit — jag' suyagi va ko'migining o'tkir yiringli yallig'lanishi; og'ir, tez tarqaladigan, umumiy intoksikatsiya bilan kechadigan holat.",
            "ru": "Острый остеомиелит — острое гнойное воспаление кости и костного мозга челюсти; тяжёлое, быстро распространяющееся состояние с интоксикацией.",
            "en": "Acute osteomyelitis is acute purulent inflammation of the jawbone and marrow; a severe, rapidly spreading condition with intoxication.",
        },
        "symptoms_text": {
            "uz": "• Yuqori isitma, kuchli chuqur og'riq, diffuz shish.\n• Bir necha tishning harakatchanligi.\n• Og'iz ochish qiyinlashishi, holsizlik.",
            "ru": "• Высокая температура, сильная глубокая боль, диффузный отёк.\n• Подвижность нескольких зубов.\n• Затруднение открывания рта, слабость.",
            "en": "• High fever, severe deep pain, diffuse swelling.\n• Mobility of several teeth.\n• Difficulty opening the mouth, weakness.",
        },
        "differential": {
            "uz": "Periostit (lokal), o'tkir periodontit va o'smadan farqlanadi.",
            "ru": "Дифференцируют с периоститом (локальным), острым периодонтитом и опухолью.",
            "en": "Differentiated from periostitis (localized), acute periodontitis and tumour.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: SHOSHILINCH yuz-jag' jarrohiga/shifoxonaga — drenaj, tizimli antibiotik, sababchi tishni olib tashlash. Bu jiddiy holat!",
            "ru": "Что делать: НЕОТЛОЖНО к челюстно-лицевому хирургу/в стационар — дренирование, системные антибиотики, удаление причинного зуба. Это серьёзно!",
            "en": "What to do: seek a maxillofacial surgeon/hospital URGENTLY — drainage, systemic antibiotics, removal of the causative tooth. This is serious!",
        },
    },
    "osteomyelitis_chronic": {
        "description": {
            "uz": "Surunkali osteomiyelit — jag' suyagining uzoq davom etuvchi yallig'lanishi; o'lik suyak (sekvestr) va fistula bilan kechadi.",
            "ru": "Хронический остеомиелит — длительное воспаление кости челюсти; с образованием мёртвой кости (секвестра) и свищей.",
            "en": "Chronic osteomyelitis is long-standing inflammation of the jawbone; with dead bone (sequestrum) and fistulas.",
        },
        "symptoms_text": {
            "uz": "• Fistula(lar)dan yiring, ba'zan suyak parchalari (sekvestr) chiqishi.\n• Suyak deformatsiyasi, bo'g'iq og'riq.\n• Davriy o'tkirlashish.",
            "ru": "• Гной из свища, иногда выходят костные фрагменты (секвестры).\n• Деформация кости, ноющая боль.\n• Периодические обострения.",
            "en": "• Pus from fistula(s), sometimes bone fragments (sequestra) extrude.\n• Bone deformity, aching pain.\n• Periodic exacerbations.",
        },
        "differential": {
            "uz": "Aktinomikoz, suyak o'smasi va o'tkir osteomiyelitdan farqlanadi.",
            "ru": "Дифференцируют с актиномикозом, опухолью кости и острым остеомиелитом.",
            "en": "Differentiated from actinomycosis, bone tumour and acute osteomyelitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: yuz-jag' jarrohiga boring — sekvestrektomiya (o'lik suyakni olib tashlash), antibiotik, kuzatuv.",
            "ru": "Что делать: к челюстно-лицевому хирургу — секвестрэктомия (удаление мёртвой кости), антибиотики, наблюдение.",
            "en": "What to do: see a maxillofacial surgeon — sequestrectomy (removal of dead bone), antibiotics, monitoring.",
        },
    },
    "follicular_cyst": {
        "description": {
            "uz": "Follikulyar (dentigeroz) kista — chiqmagan tish toji atrofida shakllanadigan, suyuqlik bilan to'lgan kista; sekin kattalashadi.",
            "ru": "Фолликулярная (дентигеронная) киста — заполненная жидкостью киста вокруг коронки непрорезавшегося зуба; растёт медленно.",
            "en": "Follicular (dentigerous) cyst forms around the crown of an unerupted tooth; fluid-filled and slow-growing.",
        },
        "symptoms_text": {
            "uz": "• Uzoq vaqt simptomsiz.\n• Chiqmagan tish + sekin kattalashuvchi shish/bosim.\n• Rentgenda tish toji bilan bog'liq aniq o'choq.",
            "ru": "• Долго бессимптомно.\n• Непрорезавшийся зуб + медленно растущий отёк/давление.\n• Чёткий очаг, связанный с коронкой зуба, на рентгене.",
            "en": "• Asymptomatic for a long time.\n• Unerupted tooth + slowly growing swelling/pressure.\n• Well-defined focus linked to the tooth crown on X-ray.",
        },
        "differential": {
            "uz": "Radikulyar kista, keratokista va o'smadan farqlanadi.",
            "ru": "Дифференцируют с радикулярной кистой, кератокистой и опухолью.",
            "en": "Differentiated from radicular cyst, keratocyst and tumour.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: yuz-jag' jarrohiga boring — kistani jarrohlik olib tashlash (kistektomiya), ko'pincha tish bilan birga; gistologiya.",
            "ru": "Что делать: к челюстно-лицевому хирургу — хирургическое удаление кисты (цистэктомия), часто вместе с зубом; гистология.",
            "en": "What to do: see a maxillofacial surgeon — surgical removal of the cyst (cystectomy), often with the tooth; histology.",
        },
    },
    "odontogenic_keratocyst": {
        "description": {
            "uz": "Odontogen keratokista — suyak bo'ylab agressiv tarqalib o'sadigan, olib tashlangach tez-tez qaytalanadigan kista.",
            "ru": "Одонтогенная кератокиста — киста, агрессивно растущая вдоль кости и часто рецидивирующая после удаления.",
            "en": "Odontogenic keratocyst grows aggressively along the bone and frequently recurs after removal.",
        },
        "symptoms_text": {
            "uz": "• Suyak bo'ylab o'sadi (ko'pincha shishsiz).\n• Olib tashlangach qaytalanish tarixi.\n• Rentgenda keng, ko'p kamerali o'choq bo'lishi mumkin.",
            "ru": "• Растёт вдоль кости (часто без отёка).\n• Рецидивы после удаления в анамнезе.\n• На рентгене обширный, иногда многокамерный очаг.",
            "en": "• Grows along the bone (often without swelling).\n• History of recurrence after removal.\n• Extensive, sometimes multilocular focus on X-ray.",
        },
        "differential": {
            "uz": "Follikulyar/radikulyar kista va ameloblastomadan farqlanadi.",
            "ru": "Дифференцируют с фолликулярной/радикулярной кистой и амелобластомой.",
            "en": "Differentiated from follicular/radicular cyst and ameloblastoma.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: yuz-jag' jarrohiga boring — to'liq jarrohlik olib tashlash va uzoq muddatli kuzatuv (qaytalanish xavfi yuqori).",
            "ru": "Что делать: к челюстно-лицевому хирургу — полное хирургическое удаление и длительное наблюдение (высокий риск рецидива).",
            "en": "What to do: see a maxillofacial surgeon — complete surgical removal and long-term follow-up (high recurrence risk).",
        },
    },
})

# ═══════════════════════════════════════════════════════════════
#  8. TMJ (chakka-pastki jag' bo'g'imi)
# ═══════════════════════════════════════════════════════════════
DISEASE_INFO.update({
    "tmj_dysfunction": {
        "description": {
            "uz": "TMJ disfunksiyasi (mio-fassial sindrom) — chaynov mushaklari va bo'g'im ishining buzilishi; ko'pincha bruksizm, stress va okklyuziya nuqsonlari bilan.",
            "ru": "Дисфункция ВНЧС (миофасциальный синдром) — нарушение работы жевательных мышц и сустава; часто из-за бруксизма, стресса и дефектов окклюзии.",
            "en": "TMJ dysfunction (myofascial syndrome) is disordered function of the chewing muscles and joint; often from bruxism, stress and occlusal problems.",
        },
        "symptoms_text": {
            "uz": "• Og'iz ochib-yopganda bo'g'imda shiqillash.\n• Bo'g'im/mushaklarda og'riq, quloqqa tarqalishi.\n• Ertalabki qotishish, jag' charchashi.",
            "ru": "• Щелчки в суставе при открывании/закрывании.\n• Боль в суставе/мышцах, отдаёт в ухо.\n• Утренняя скованность, усталость челюсти.",
            "en": "• Clicking in the joint when opening/closing.\n• Pain in the joint/muscles, radiating to the ear.\n• Morning stiffness, jaw fatigue.",
        },
        "differential": {
            "uz": "Disk dislokatsiyasi (qulflanish), artroz (krepitatsiya) va tish og'riqlaridan farqlanadi.",
            "ru": "Дифференцируют со смещением диска (блок), артрозом (крепитация) и зубной болью.",
            "en": "Differentiated from disc dislocation (locking), arthrosis (crepitus) and dental pain.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: gnatolog/stomatologga boring — tungi kapa, bruksizm/stressni kamaytirish, mashqlar, okklyuziyani tuzatish.",
            "ru": "Что делать: к гнатологу/стоматологу — ночная капа, снижение бруксизма/стресса, упражнения, коррекция окклюзии.",
            "en": "What to do: see a TMJ specialist/dentist — a night guard, reduce bruxism/stress, exercises, occlusal correction.",
        },
    },
    "tmj_arthritis": {
        "description": {
            "uz": "TMJ artriti — bo'g'imning yallig'lanishli kasalligi (infeksion, travmatik yoki revmatoid); og'riq va harakat cheklanishi bilan.",
            "ru": "Артрит ВНЧС — воспалительное заболевание сустава (инфекционное, травматическое или ревматоидное); с болью и ограничением движения.",
            "en": "TMJ arthritis is inflammatory joint disease (infectious, traumatic or rheumatoid); with pain and limited movement.",
        },
        "symptoms_text": {
            "uz": "• Bo'g'imda yallig'lanishli og'riq.\n• Ertalabki qotishish, harakatda og'riq.\n• Ba'zan isitma yoki tizimli kasallik (revmatoid).",
            "ru": "• Воспалительная боль в суставе.\n• Утренняя скованность, боль при движении.\n• Иногда лихорадка или системная болезнь (ревматоид).",
            "en": "• Inflammatory joint pain.\n• Morning stiffness, pain on movement.\n• Sometimes fever or systemic disease (rheumatoid).",
        },
        "differential": {
            "uz": "Artroz (krepitatsiya, degenerativ) va disfunksiyadan farqlanadi.",
            "ru": "Дифференцируют с артрозом (крепитация, дегенеративный) и дисфункцией.",
            "en": "Differentiated from arthrosis (crepitus, degenerative) and dysfunction.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: shifokorga boring — yallig'lanishga qarshi davolash, bo'g'imni tinchlantirish; tizimli sabab bo'lsa revmatologga.",
            "ru": "Что делать: к врачу — противовоспалительное лечение, разгрузка сустава; при системной причине — к ревматологу.",
            "en": "What to do: see a doctor — anti-inflammatory treatment, joint rest; if systemic, see a rheumatologist.",
        },
    },
    "tmj_arthrosis": {
        "description": {
            "uz": "TMJ artrozi (osteoartroz) — bo'g'imning degenerativ-distrofik kasalligi; tog'ay va suyakning yemirilishi bilan.",
            "ru": "Артроз ВНЧС (остеоартроз) — дегенеративно-дистрофическое заболевание сустава; с разрушением хряща и кости.",
            "en": "TMJ arthrosis (osteoarthrosis) is a degenerative-dystrophic joint disease; with cartilage and bone breakdown.",
        },
        "symptoms_text": {
            "uz": "• Bo'g'imda krepitatsiya (qum g'ichirlashi).\n• Uzoq davom etgan, kuchsiz og'riq.\n• Harakat hajmining asta-sekin kamayishi.",
            "ru": "• Крепитация в суставе (скрип песка).\n• Длительная, слабая боль.\n• Постепенное уменьшение объёма движений.",
            "en": "• Crepitus in the joint (sand-like grating).\n• Long-standing, mild pain.\n• Gradual reduction in range of motion.",
        },
        "differential": {
            "uz": "Artrit (yallig'lanish), disfunksiya (shiqillash) va ankilozdan farqlanadi.",
            "ru": "Дифференцируют с артритом (воспаление), дисфункцией (щелчки) и анкилозом.",
            "en": "Differentiated from arthritis (inflammation), dysfunction (clicking) and ankylosis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: gnatolog/jarrohga boring — bo'g'imni yuklamani kamaytirish, fizioterapiya, kapa; og'ir holatda jarrohlik.",
            "ru": "Что делать: к гнатологу/хирургу — снижение нагрузки на сустав, физиотерапия, капа; в тяжёлых случаях хирургия.",
            "en": "What to do: see a TMJ specialist/surgeon — reduce joint load, physiotherapy, a splint; surgery in severe cases.",
        },
    },
    "tmj_disc_dislocation": {
        "description": {
            "uz": "Disk dislokatsiyasi — bo'g'im diskining siljishi; shiqillash va jag'ning qulflanishi (ochilmaslik yoki yopilmaslik) bilan.",
            "ru": "Смещение диска ВНЧС — смещение суставного диска; со щелчками и блокировкой челюсти.",
            "en": "TMJ disc dislocation — displacement of the joint disc; with clicking and jaw locking.",
        },
        "symptoms_text": {
            "uz": "• Shiqillash + jag'ning qulflanishi.\n• Og'iz ochishda blok hissi.\n• Jag'ning bir tomonga og'ishi.",
            "ru": "• Щелчки + блокировка челюсти.\n• Ощущение блока при открывании.\n• Смещение челюсти в сторону.",
            "en": "• Clicking + jaw locking.\n• A blocked feeling when opening.\n• Jaw deviating to one side.",
        },
        "differential": {
            "uz": "Disfunksiya (qulflanishsiz), artroz va ankilozdan farqlanadi.",
            "ru": "Дифференцируют с дисфункцией (без блока), артрозом и анкилозом.",
            "en": "Differentiated from dysfunction (no locking), arthrosis and ankylosis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: gnatolog/jarrohga boring — kapa, repozitsiya, fizioterapiya; doimiy qulflanishda jarrohlik.",
            "ru": "Что делать: к гнатологу/хирургу — капа, вправление, физиотерапия; при постоянной блокировке хирургия.",
            "en": "What to do: see a TMJ specialist/surgeon — splint, repositioning, physiotherapy; surgery for persistent locking.",
        },
    },
    "tmj_ankylosis": {
        "description": {
            "uz": "TMJ ankilozi — bo'g'imning fibroz yoki suyak bilan birikib qolishi natijasida og'iz ochilishining doimiy cheklanishi; ko'pincha travma/infeksiya oqibati.",
            "ru": "Анкилоз ВНЧС — стойкое ограничение открывания рта из-за фиброзного или костного сращения сустава; часто следствие травмы/инфекции.",
            "en": "TMJ ankylosis is permanent restriction of mouth opening due to fibrous or bony fusion of the joint; often after trauma/infection.",
        },
        "symptoms_text": {
            "uz": "• Og'iz ochilishining doimiy (progressiv) cheklanishi.\n• Shiqillash/og'riq odatda yo'q.\n• Bolalarda yuz assimetriyasi rivojlanishi.",
            "ru": "• Стойкое (прогрессирующее) ограничение открывания рта.\n• Щелчков/боли обычно нет.\n• У детей — развитие асимметрии лица.",
            "en": "• Permanent (progressive) restriction of mouth opening.\n• Usually no clicking/pain.\n• Facial asymmetry develops in children.",
        },
        "differential": {
            "uz": "Trizm (mushak), submukoz fibroz va disk dislokatsiyasidan farqlanadi.",
            "ru": "Дифференцируют с тризмом (мышечным), подслизистым фиброзом и смещением диска.",
            "en": "Differentiated from trismus (muscular), submucous fibrosis and disc dislocation.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: yuz-jag' jarrohiga boring — jarrohlik davolash (artroplastika) va reabilitatsiya. Bolalarda erta murojaat muhim.",
            "ru": "Что делать: к челюстно-лицевому хирургу — хирургическое лечение (артропластика) и реабилитация. У детей важно раннее обращение.",
            "en": "What to do: see a maxillofacial surgeon — surgical treatment (arthroplasty) and rehabilitation. Early care matters in children.",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
#  11. TRAVMATIK SHIKASTLANISHLAR
# ═══════════════════════════════════════════════════════════════
DISEASE_INFO.update({
    "enamel_fracture": {
        "description": {
            "uz": "Emal sinishi — zarbadan tish toji emalining kichik bo'lagi uchishi; dentin ochilmaydi, asoratsiz shikast.",
            "ru": "Перелом эмали — откол небольшого фрагмента эмали коронки от удара; дентин не обнажён, неосложнённая травма.",
            "en": "Enamel fracture — a small chip of crown enamel breaks off after a blow; dentin is not exposed, an uncomplicated injury.",
        },
        "symptoms_text": {
            "uz": "• Tishning kichik chekkasi uchgan.\n• Og'riq yo'q, dentin ochilmagan.\n• Tish qimirlamaydi.",
            "ru": "• Откол небольшого края зуба.\n• Боли нет, дентин не обнажён.\n• Зуб неподвижен.",
            "en": "• Small edge of the tooth chipped.\n• No pain, dentin not exposed.\n• Tooth is not mobile.",
        },
        "differential": {
            "uz": "Emal-dentin sinishi (dentin ochiq) va eski yeyilishdan farqlanadi.",
            "ru": "Дифференцируют с перелом эмали-дентина (обнажён дентин) и старым сколом/стиранием.",
            "en": "Differentiated from enamel-dentin fracture (exposed dentin) and old wear/chipping.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga ko'rining — qirralarni silliqlash yoki kompozit bilan tiklash. Tishning hayotiyligini kuzatish.",
            "ru": "Что делать: к стоматологу — сошлифовка краёв или реставрация композитом. Наблюдение за жизнеспособностью зуба.",
            "en": "What to do: see a dentist — smoothing the edges or composite restoration. Monitor tooth vitality.",
        },
    },
    "enamel_dentin_fracture": {
        "description": {
            "uz": "Emal-dentin sinishi (asoratsiz) — toj sinishida emal va dentin zararlanadi, lekin pulpa (nerv) ochilmaydi.",
            "ru": "Перелом эмали и дентина (без вскрытия пульпы) — при сколе коронки повреждаются эмаль и дентин, но пульпа не обнажена.",
            "en": "Enamel-dentin fracture (uncomplicated) — the crown fracture involves enamel and dentin, but the pulp is not exposed.",
        },
        "symptoms_text": {
            "uz": "• Siniqda sarg'ish dentin ochiq.\n• Sovuq/havoga sezuvchanlik.\n• Qizil nuqta (nerv) ko'rinmaydi.",
            "ru": "• В сколе обнажён желтоватый дентин.\n• Чувствительность к холоду/воздуху.\n• Красной точки (нерва) не видно.",
            "en": "• Yellowish dentin exposed in the fracture.\n• Sensitivity to cold/air.\n• No red dot (nerve) visible.",
        },
        "differential": {
            "uz": "Emal sinishi (dentinsiz) va pulpa ochilishi bilan sinishdan farqlanadi.",
            "ru": "Дифференцируют с переломом эмали (без дентина) и переломом со вскрытием пульпы.",
            "en": "Differentiated from enamel fracture (no dentin) and fracture with pulp exposure.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: tezroq stomatologga boring — ochilgan dentinni qoplash va kompozit bilan tiklash; hayotiylikni kuzatish.",
            "ru": "Что делать: скорее к стоматологу — закрытие обнажённого дентина и реставрация композитом; наблюдение за пульпой.",
            "en": "What to do: see a dentist soon — cover the exposed dentin and restore with composite; monitor vitality.",
        },
    },
    "crown_fracture_pulp": {
        "description": {
            "uz": "Pulpa ochilishi bilan toj sinishi (asoratli) — siniqda nerv (pulpa) ochiq qoladi; tezkor endodontik yordam talab qiladi.",
            "ru": "Перелом коронки со вскрытием пульпы (осложнённый) — в сколе обнажён нерв (пульпа); требует срочной эндодонтической помощи.",
            "en": "Crown fracture with pulp exposure (complicated) — the nerve (pulp) is exposed in the fracture; requires urgent endodontic care.",
        },
        "symptoms_text": {
            "uz": "• Siniq markazida qizil nuqta yoki qon (nerv ochiq).\n• Kuchli og'riq, sezuvchanlik.\n• Yaqinda zarba bo'lgan.",
            "ru": "• В центре скола красная точка или кровь (нерв обнажён).\n• Сильная боль, чувствительность.\n• Недавняя травма.",
            "en": "• Red dot or bleeding in the centre of the fracture (pulp exposed).\n• Severe pain, sensitivity.\n• Recent trauma.",
        },
        "differential": {
            "uz": "Emal-dentin sinishidan (nerv yopiq) farqlanadi — bu hal qiluvchi farq.",
            "ru": "Дифференцируют с перелом эмали-дентина (пульпа закрыта) — это решающее отличие.",
            "en": "Differentiated from enamel-dentin fracture (pulp closed) — this is the key difference.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ZUDLIK bilan stomatologga boring — pulpani qoplash yoki kanal davolash. Vaqt muhim (nervni saqlash uchun).",
            "ru": "Что делать: СРОЧНО к стоматологу — покрытие пульпы или лечение каналов. Время важно (для сохранения нерва).",
            "en": "What to do: see a dentist URGENTLY — pulp capping or root canal treatment. Time matters (to save the nerve).",
        },
    },
    "root_fracture": {
        "description": {
            "uz": "Ildiz sinishi — tish ildizining sinishi; toj butun bo'lishi mumkin, lekin tish harakatchan/og'riqli. Rentgensiz aniqlash qiyin.",
            "ru": "Перелом корня — перелом корня зуба; коронка может быть цела, но зуб подвижен/болезнен. Без рентгена трудно выявить.",
            "en": "Root fracture — fracture of the tooth root; the crown may be intact, but the tooth is mobile/tender. Hard to detect without X-ray.",
        },
        "symptoms_text": {
            "uz": "• Zarbadan keyin tish harakatchan va og'riqli.\n• Toj ko'pincha butun.\n• Ba'zan tish biroz siljigan.",
            "ru": "• После травмы зуб подвижен и болезнен.\n• Коронка часто цела.\n• Иногда зуб слегка смещён.",
            "en": "• After trauma the tooth is mobile and tender.\n• The crown is often intact.\n• Sometimes the tooth is slightly displaced.",
        },
        "differential": {
            "uz": "Subluksatsiya, ekstruziya va alveolyar suyak sinishidan farqlanadi (rentgen zarur).",
            "ru": "Дифференцируют с подвывихом, экструзией и переломом альвеолярной кости (нужен рентген).",
            "en": "Differentiated from subluxation, extrusion and alveolar bone fracture (X-ray needed).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: tezroq stomatologga boring — rentgen, tishni shinalash (qotirish) va kuzatuv; joylashuviga qarab davolash.",
            "ru": "Что делать: скорее к стоматологу — рентген, шинирование зуба и наблюдение; лечение зависит от уровня перелома.",
            "en": "What to do: see a dentist soon — X-ray, splinting the tooth and monitoring; treatment depends on the fracture level.",
        },
    },
    "concussion": {
        "description": {
            "uz": "Konkussiya — tishni ushlab turuvchi to'qimalarning yengil shikastlanishi; tish qimirlamaydi va siljimaydi, lekin perkussiyaga sezgir.",
            "ru": "Ушиб зуба (сотрясение) — лёгкое повреждение удерживающих тканей; зуб не подвижен и не смещён, но чувствителен к перкуссии.",
            "en": "Concussion — minor injury to the supporting tissues; the tooth is not mobile or displaced but tender to percussion.",
        },
        "symptoms_text": {
            "uz": "• Zarbadan keyin tish og'riydi (bosish/chaynashda).\n• Qimirlamaydi va siljimagan.\n• Siniq yo'q.",
            "ru": "• После удара зуб болит (при накусывании).\n• Не подвижен и не смещён.\n• Перелома нет.",
            "en": "• Tooth hurts after the blow (on biting).\n• Not mobile or displaced.\n• No fracture.",
        },
        "differential": {
            "uz": "Subluksatsiya (harakatchan) va ildiz sinishidan farqlanadi.",
            "ru": "Дифференцируют с подвывихом (подвижен) и переломом корня.",
            "en": "Differentiated from subluxation (mobile) and root fracture.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatologga ko'rining — yumshoq parhez, tishni tinchlantirish va hayotiylik kuzatuvi. Keyinchalik rang o'zgarishini kuzating.",
            "ru": "Что делать: к стоматологу — щадящая диета, покой зуба и наблюдение за жизнеспособностью. Следите за изменением цвета.",
            "en": "What to do: see a dentist — soft diet, rest the tooth and monitor vitality. Watch for later discolouration.",
        },
    },
    "subluxation": {
        "description": {
            "uz": "Subluksatsiya — tishni ushlab turuvchi to'qimalarning shikastlanishi natijasida tishning bo'shashishi (harakatchanligi), lekin siljimasligi.",
            "ru": "Подвывих — расшатывание (подвижность) зуба из-за повреждения удерживающих тканей, но без смещения.",
            "en": "Subluxation — loosening (mobility) of the tooth from injury to the supporting tissues, but without displacement.",
        },
        "symptoms_text": {
            "uz": "• Zarbadan keyin tish bo'shashgan (harakatchan).\n• Milk yorig'idan qon kelishi mumkin.\n• Tish o'z o'rnida (siljimagan), siniq yo'q.",
            "ru": "• После травмы зуб расшатан (подвижен).\n• Возможна кровь из десневой борозды.\n• Зуб на месте (не смещён), перелома нет.",
            "en": "• Tooth loosened (mobile) after trauma.\n• Possible bleeding from the gingival sulcus.\n• Tooth in place (not displaced), no fracture.",
        },
        "differential": {
            "uz": "Konkussiya (harakatsiz), ekstruziya (siljigan) va ildiz sinishidan farqlanadi.",
            "ru": "Дифференцируют с ушибом (без подвижности), экструзией (смещён) и переломом корня.",
            "en": "Differentiated from concussion (no mobility), extrusion (displaced) and root fracture.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: tezroq stomatologga boring — kerak bo'lsa shinalash, yumshoq parhez, hayotiylik kuzatuvi.",
            "ru": "Что делать: скорее к стоматологу — при необходимости шинирование, щадящая диета, наблюдение за жизнеспособностью.",
            "en": "What to do: see a dentist soon — splinting if needed, soft diet, vitality monitoring.",
        },
    },
    "extrusion": {
        "description": {
            "uz": "Ekstruziya — tishning katakchadan qisman chiqib (uzunroq ko'rinib) siljishi; tezkor repozitsiya talab qiladi.",
            "ru": "Экструзия — частичное смещение зуба из лунки (выглядит длиннее); требует срочного вправления.",
            "en": "Extrusion — partial displacement of the tooth out of the socket (looks longer); requires prompt repositioning.",
        },
        "symptoms_text": {
            "uz": "• Tish katakchadan chiqib, uzunroq ko'rinadi.\n• Harakatchan, og'riqli.\n• Yaqinda zarba bo'lgan.",
            "ru": "• Зуб выдвинут из лунки, выглядит длиннее.\n• Подвижен, болезнен.\n• Недавняя травма.",
            "en": "• Tooth pushed out of the socket, looks longer.\n• Mobile, painful.\n• Recent trauma.",
        },
        "differential": {
            "uz": "Subluksatsiya (siljimagan), intruziya (ichkariga) va avulsiyadan farqlanadi.",
            "ru": "Дифференцируют с подвывихом (без смещения), интрузией (внутрь) и авульсией.",
            "en": "Differentiated from subluxation (not displaced), intrusion (inward) and avulsion.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ZUDLIK bilan stomatologga boring — tishni joyiga qaytarish (repozitsiya) va shinalash; hayotiylik kuzatuvi.",
            "ru": "Что делать: СРОЧНО к стоматологу — вправление зуба (репозиция) и шинирование; наблюдение за жизнеспособностью.",
            "en": "What to do: see a dentist URGENTLY — repositioning the tooth and splinting; vitality monitoring.",
        },
    },
    "intrusion": {
        "description": {
            "uz": "Intruziya — tishning zarba ta'sirida suyak ichiga kirib ketishi (kaltaroq ko'rinishi); og'ir dislokatsiya turi.",
            "ru": "Интрузия — вколачивание зуба в кость от удара (выглядит короче); тяжёлый тип вывиха.",
            "en": "Intrusion — the tooth is driven into the bone by the blow (looks shorter); a severe dislocation type.",
        },
        "symptoms_text": {
            "uz": "• Tish ichkariga kirib, kaltaroq ko'rinadi.\n• Qimirlamaydi (qotgan).\n• Yaqinda kuchli zarba bo'lgan.",
            "ru": "• Зуб вдавлен внутрь, выглядит короче.\n• Неподвижен (как вколочен).\n• Недавняя сильная травма.",
            "en": "• Tooth pushed inward, looks shorter.\n• Immobile (locked in).\n• Recent strong trauma.",
        },
        "differential": {
            "uz": "Ekstruziya (chiqqan) va alveolyar suyak sinishidan farqlanadi.",
            "ru": "Дифференцируют с экструзией (выдвинут) и переломом альвеолярной кости.",
            "en": "Differentiated from extrusion (pushed out) and alveolar bone fracture.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ZUDLIK bilan stomatologga boring — rentgen, repozitsiya (jarrohlik/ortodontik) va kuzatuv. Bolalarda doimiy tish kurtagi xavf ostida.",
            "ru": "Что делать: СРОЧНО к стоматологу — рентген, репозиция (хирургическая/ортодонтическая) и наблюдение. У детей под угрозой зачаток постоянного зуба.",
            "en": "What to do: see a dentist URGENTLY — X-ray, repositioning (surgical/orthodontic) and monitoring. In children the permanent tooth bud is at risk.",
        },
    },
    "avulsion": {
        "description": {
            "uz": "Avulsiya — tishning katakchadan butunlay chiqib (tushib) ketishi; tezkor reimplantatsiya talab qiladigan dental favqulodda holat.",
            "ru": "Авульсия — полное выпадение зуба из лунки; неотложная стоматологическая ситуация, требующая срочной реплантации.",
            "en": "Avulsion — complete loss of the tooth from the socket; a dental emergency requiring urgent replantation.",
        },
        "symptoms_text": {
            "uz": "• Tish butunlay o'rnidan chiqib tushgan.\n• Katakcha bo'sh, qon ketishi.\n• Yaqinda zarba.",
            "ru": "• Зуб полностью выбит из лунки.\n• Лунка пуста, кровотечение.\n• Недавний удар.",
            "en": "• Tooth completely knocked out of the socket.\n• Empty socket, bleeding.\n• Recent blow.",
        },
        "differential": {
            "uz": "Intruziya (suyakka kirgan, ko'rinmasligi mumkin) dan farqlash uchun rentgen kerak.",
            "ru": "Для отличия от интрузии (вколочен, может быть не виден) нужен рентген.",
            "en": "An X-ray is needed to distinguish from intrusion (driven in, may be invisible).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: DARHOL! Tishni tojidan ushlang (ildizga tegmang), sutda yoki so'lakda saqlang va 30 daqiqa ichida stomatologga yeting — bu tishni saqlash imkonini beradi.",
            "ru": "Что делать: НЕМЕДЛЕННО! Держите зуб за коронку (не трогая корень), храните в молоке или слюне и доберитесь к стоматологу в течение 30 минут — это шанс сохранить зуб.",
            "en": "What to do: IMMEDIATELY! Hold the tooth by the crown (do not touch the root), store it in milk or saliva, and reach a dentist within 30 minutes — this gives a chance to save the tooth.",
        },
    },
})

# ═══════════════════════════════════════════════════════════════
#  13. SO'LAK BEZLARI
# ═══════════════════════════════════════════════════════════════
DISEASE_INFO.update({
    "sialadenitis": {
        "description": {
            "uz": "Sialadenit — so'lak bezining yallig'lanishi (ko'pincha infeksion); bez shishi, og'riq va yo'lidan yiring chiqishi bilan.",
            "ru": "Сиаладенит — воспаление слюнной железы (часто инфекционное); с припухлостью, болью и выделением гноя из протока.",
            "en": "Sialadenitis is inflammation of a salivary gland (often infectious); with gland swelling, pain and pus from the duct.",
        },
        "symptoms_text": {
            "uz": "• Bez sohasida og'riqli shish.\n• Yo'lidan yiring/bulutli so'lak.\n• Ba'zan isitma, limfa tugunlari.",
            "ru": "• Болезненная припухлость в области железы.\n• Гной/мутная слюна из протока.\n• Иногда лихорадка, лимфоузлы.",
            "en": "• Painful swelling in the gland area.\n• Pus/cloudy saliva from the duct.\n• Sometimes fever, lymph nodes.",
        },
        "differential": {
            "uz": "Sialolitiaz (ovqatga bog'liq shish), bez o'smasi va limfadenitdan farqlanadi.",
            "ru": "Дифференцируют с сиалолитиазом (отёк, связанный с едой), опухолью железы и лимфаденитом.",
            "en": "Differentiated from sialolithiasis (meal-related swelling), gland tumour and lymphadenitis.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: shifokorga boring — antibiotik (ko'rsatma bo'yicha), so'lak ajralishini rag'batlantirish (suyuqlik, nordon), gigiyena; abscessda drenaj.",
            "ru": "Что делать: к врачу — антибиотики (по показаниям), стимуляция слюноотделения (питьё, кислое), гигиена; при абсцессе дренирование.",
            "en": "What to do: see a doctor — antibiotics (as indicated), stimulate salivation (fluids, sour foods), hygiene; drainage if abscess.",
        },
    },
    "sialolithiasis": {
        "description": {
            "uz": "Sialolitiaz (so'lak toshi kasalligi) — so'lak bezi yo'lida tosh (konkrement) hosil bo'lib, so'lak oqimini to'sib qo'yishi.",
            "ru": "Сиалолитиаз (слюннокаменная болезнь) — образование камня (конкремента) в протоке слюнной железы с нарушением оттока слюны.",
            "en": "Sialolithiasis (salivary stone disease) — a stone (calculus) forms in the gland duct, obstructing saliva flow.",
        },
        "symptoms_text": {
            "uz": "• Shish ovqatdan oldin/paytida kattalashadi, keyin kichrayadi.\n• Ovqatda og'riq (kolika).\n• Ko'pincha jag' osti bezida.",
            "ru": "• Отёк увеличивается перед/во время еды, затем спадает.\n• Боль при еде (колика).\n• Чаще в поднижнечелюстной железе.",
            "en": "• Swelling enlarges before/during meals, then subsides.\n• Pain when eating (colic).\n• Most often in the submandibular gland.",
        },
        "differential": {
            "uz": "Sialadenit (doimiy shish) va bez o'smasidan farqlanadi.",
            "ru": "Дифференцируют с сиаладенитом (постоянный отёк) и опухолью железы.",
            "en": "Differentiated from sialadenitis (constant swelling) and gland tumour.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: shifokorga boring — kichik tosh so'lak ajralishi/massaj bilan chiqishi mumkin; kattasida jarrohlik yoki sialendoskopiya.",
            "ru": "Что делать: к врачу — небольшой камень может выйти при стимуляции/массаже; при крупном — хирургия или сиалендоскопия.",
            "en": "What to do: see a doctor — a small stone may pass with stimulation/massage; a large one needs surgery or sialendoscopy.",
        },
    },
    "xerostomia": {
        "description": {
            "uz": "Kserostomiya — so'lak ajralishining kamayishi natijasida og'iz qurishi; dorilar, nurlanish, yosh yoki tizimli kasalliklar bilan bog'liq.",
            "ru": "Ксеростомия — сухость рта из-за снижения слюноотделения; связана с лекарствами, облучением, возрастом или системными болезнями.",
            "en": "Xerostomia is dry mouth from reduced saliva; linked to medications, radiation, age or systemic diseases.",
        },
        "symptoms_text": {
            "uz": "• Doimiy og'iz qurishi, yutish/gapirish qiyinlashishi.\n• Yomon hid, tez karies, shilliq achishishi.\n• Bez shishi yo'q.",
            "ru": "• Постоянная сухость, затруднение глотания/речи.\n• Неприятный запах, быстрый кариес, жжение слизистой.\n• Припухлости железы нет.",
            "en": "• Persistent dryness, difficulty swallowing/speaking.\n• Bad odour, rapid caries, mucosal burning.\n• No gland swelling.",
        },
        "differential": {
            "uz": "Sjögren sindromi (ko'z ham quruq) va dehidratatsiyadan farqlanadi.",
            "ru": "Дифференцируют с синдромом Шёгрена (сухость глаз) и обезвоживанием.",
            "en": "Differentiated from Sjögren's syndrome (dry eyes too) and dehydration.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: shifokorga boring — sababni aniqlash (dori/kasallik), ko'p suv, so'lak o'rnini bosuvchilar, kuchli karies profilaktikasi.",
            "ru": "Что делать: к врачу — выявление причины (лекарство/болезнь), много воды, заменители слюны, усиленная профилактика кариеса.",
            "en": "What to do: see a doctor — identify the cause (drug/disease), plenty of water, saliva substitutes, intensive caries prevention.",
        },
    },
    "sjogren_syndrome": {
        "description": {
            "uz": "Sjögren sindromi — autoimmun kasallik; so'lak va ko'z yosh bezlari zararlanib, og'iz va ko'zlarning surunkali quruqligiga olib keladi.",
            "ru": "Синдром Шёгрена — аутоиммунное заболевание; поражаются слюнные и слёзные железы, вызывая хроническую сухость рта и глаз.",
            "en": "Sjögren's syndrome is an autoimmune disease; salivary and lacrimal glands are affected, causing chronic dry mouth and eyes.",
        },
        "symptoms_text": {
            "uz": "• Og'iz va ko'zlarning doimiy quruqligi.\n• Bezlarning simmetrik kattalashishi.\n• Tez karies, umumiy charchoq.",
            "ru": "• Постоянная сухость рта и глаз.\n• Симметричное увеличение желёз.\n• Быстрый кариес, общая усталость.",
            "en": "• Persistent dry mouth and eyes.\n• Symmetrical gland enlargement.\n• Rapid caries, general fatigue.",
        },
        "differential": {
            "uz": "Oddiy kserostomiya (ko'z normal) va boshqa autoimmun kasalliklardan farqlanadi.",
            "ru": "Дифференцируют с обычной ксеростомией (глаза в норме) и другими аутоиммунными болезнями.",
            "en": "Differentiated from simple xerostomia (normal eyes) and other autoimmune diseases.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: revmatolog + stomatologga boring — tizimli davolash, namlovchilar, karies profilaktikasi va kuzatuv (limfoma xavfi).",
            "ru": "Что делать: к ревматологу + стоматологу — системное лечение, увлажнители, профилактика кариеса и наблюдение (риск лимфомы).",
            "en": "What to do: see a rheumatologist + dentist — systemic treatment, moisturizers, caries prevention and monitoring (lymphoma risk).",
        },
    },
    "mucocele": {
        "description": {
            "uz": "Mukosele — so'lak bezchasi yo'lining shikastlanishi (ko'pincha tishlab olish) natijasida hosil bo'ladigan shilliq kista; ko'pincha pastki labda.",
            "ru": "Мукоцеле — слизистая киста из-за повреждения протока мелкой слюнной железы (часто прикусывание); чаще на нижней губе.",
            "en": "Mucocele is a mucous cyst from injury to a minor salivary gland duct (often biting); usually on the lower lip.",
        },
        "symptoms_text": {
            "uz": "• Ko'kimtir, yumshoq, suvli pufak.\n• Og'riqsiz; yorilib qaytalanishi mumkin.\n• Ko'pincha pastki lab/yonoq ichida.",
            "ru": "• Синеватый, мягкий, наполненный жидкостью пузырь.\n• Безболезненный; может вскрываться и рецидивировать.\n• Чаще на нижней губе/щеке.",
            "en": "• Bluish, soft, fluid-filled bump.\n• Painless; may rupture and recur.\n• Usually on the lower lip/cheek.",
        },
        "differential": {
            "uz": "Ranula (til ostida katta), lipoma va gemangiomadan farqlanadi.",
            "ru": "Дифференцируют с ранулой (крупная, под языком), липомой и гемангиомой.",
            "en": "Differentiated from ranula (large, under the tongue), lipoma and hemangioma.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/jarrohga boring — jarrohlik olib tashlash (bezcha bilan), aks holda qaytalanadi.",
            "ru": "Что делать: к стоматологу/хирургу — хирургическое удаление (вместе с железкой), иначе рецидивирует.",
            "en": "What to do: see a dentist/surgeon — surgical removal (with the gland), otherwise it recurs.",
        },
    },
    "ranula": {
        "description": {
            "uz": "Ranula — til osti so'lak bezi bilan bog'liq, og'iz tubida joylashgan katta shilliq kista; qurbaqa qornini eslatadi.",
            "ru": "Ранула — крупная слизистая киста на дне рта, связанная с подъязычной железой; напоминает брюшко лягушки.",
            "en": "Ranula is a large mucous cyst on the floor of the mouth associated with the sublingual gland; resembles a frog's belly.",
        },
        "symptoms_text": {
            "uz": "• Til ostida katta ko'kimtir, yumshoq shish.\n• Og'riqsiz; kattalashsa yutish/gapirishga xalal.\n• Bir tomonda.",
            "ru": "• Крупная синеватая мягкая припухлость под языком.\n• Безболезненна; при росте мешает глотанию/речи.\n• Односторонняя.",
            "en": "• Large bluish soft swelling under the tongue.\n• Painless; if large, interferes with swallowing/speech.\n• Unilateral.",
        },
        "differential": {
            "uz": "Mukosele (kichik), dermoid kista va abssessdan farqlanadi.",
            "ru": "Дифференцируют с мукоцеле (мелкое), дермоидной кистой и абсцессом.",
            "en": "Differentiated from mucocele (small), dermoid cyst and abscess.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: yuz-jag' jarrohiga boring — jarrohlik olib tashlash (ba'zan bez bilan), gistologiya.",
            "ru": "Что делать: к челюстно-лицевому хирургу — хирургическое удаление (иногда с железой), гистология.",
            "en": "What to do: see a maxillofacial surgeon — surgical removal (sometimes with the gland), histology.",
        },
    },
    "salivary_tumor": {
        "description": {
            "uz": "So'lak bezi o'smasi — bezda sekin o'sadigan tugun (ko'pincha yaxshi sifatli pleomorf adenoma, ammo yomon sifatli ham bo'lishi mumkin).",
            "ru": "Опухоль слюнной железы — медленно растущий узел в железе (часто доброкачественная плеоморфная аденома, но может быть и злокачественной).",
            "en": "Salivary gland tumour — a slowly growing nodule in the gland (often benign pleomorphic adenoma, but can be malignant).",
        },
        "symptoms_text": {
            "uz": "• Bezda (ko'pincha quloqoldi) sekin o'sgan og'riqsiz tugun.\n• Yomon sifatda: tez o'sish, og'riq, uvishish, yuz nervi falaji.\n• Yo'lidan yiring chiqmaydi.",
            "ru": "• Медленно растущий безболезненный узел в железе (часто околоушной).\n• При злокачественности: быстрый рост, боль, онемение, парез лицевого нерва.\n• Гноя из протока нет.",
            "en": "• Slowly growing painless nodule in the gland (often parotid).\n• If malignant: rapid growth, pain, numbness, facial nerve palsy.\n• No pus from the duct.",
        },
        "differential": {
            "uz": "Sialadenit (og'riqli, isitma), sialolitiaz (ovqatga bog'liq) va limfa tugunidan farqlanadi.",
            "ru": "Дифференцируют с сиаладенитом (боль, лихорадка), сиалолитиазом (связь с едой) и лимфоузлом.",
            "en": "Differentiated from sialadenitis (painful, fever), sialolithiasis (meal-related) and lymph node.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: yuz-jag' jarrohi/onkologga boring — tekshiruv (UTT/biopsiya) va jarrohlik olib tashlash. Tez o'sish/og'riq/falajda kechiktirmang.",
            "ru": "Что делать: к челюстно-лицевому хирургу/онкологу — обследование (УЗИ/биопсия) и хирургическое удаление. При быстром росте/боли/парезе не медлите.",
            "en": "What to do: see a maxillofacial surgeon/oncologist — workup (ultrasound/biopsy) and surgical removal. Do not delay if rapid growth/pain/palsy.",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
#  9 + 10. RIVOJLANISH ANOMALIYALARI + ORTODONTIK
# ═══════════════════════════════════════════════════════════════
DISEASE_INFO.update({
    "adentia_complete": {
        "description": {
            "uz": "Adentiya — tishlarning tug'ma to'liq yo'qligi (juda kam uchraydi); ko'pincha ektodermal displaziya kabi sindromlar bilan.",
            "ru": "Адентия — врождённое полное отсутствие зубов (очень редко); часто при синдромах (эктодермальная дисплазия).",
            "en": "Complete adentia — congenital total absence of teeth (very rare); often with syndromes (ectodermal dysplasia).",
        },
        "symptoms_text": {
            "uz": "• Tishlar umuman chiqmagan (tug'ma).\n• Chaynash, nutq va estetikaning og'ir buzilishi.\n• Boshqa ektodermal belgilar bo'lishi mumkin.",
            "ru": "• Зубы полностью отсутствуют (врождённо).\n• Тяжёлое нарушение жевания, речи и эстетики.\n• Возможны другие эктодермальные признаки.",
            "en": "• Teeth completely absent (congenital).\n• Severe impairment of chewing, speech and aesthetics.\n• Other ectodermal signs may be present.",
        },
        "differential": {
            "uz": "Oligodontiya (ko'p, lekin to'liq emas) va kechikkan chiqishdan farqlanadi.",
            "ru": "Дифференцируют с олигодонтией (много, но не полностью) и задержкой прорезывания.",
            "en": "Differentiated from oligodontia (many but not complete) and delayed eruption.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortoped-stomatolog/ortodontga boring — protezlash (ba'zan implantlar), kompleks reabilitatsiya.",
            "ru": "Что делать: к ортопеду-стоматологу/ортодонту — протезирование (иногда импланты), комплексная реабилитация.",
            "en": "What to do: see a prosthodontist/orthodontist — prosthetics (sometimes implants), comprehensive rehabilitation.",
        },
    },
    "oligodontia": {
        "description": {
            "uz": "Oligodontiya — oltidan ortiq tishning tug'ma yo'qligi; ko'pincha nasliy yoki sindromlar bilan bog'liq.",
            "ru": "Олигодонтия — врождённое отсутствие более шести зубов; часто наследственная или связана с синдромами.",
            "en": "Oligodontia — congenital absence of more than six teeth; often hereditary or syndrome-associated.",
        },
        "symptoms_text": {
            "uz": "• Ko'p (6+) tishning yo'qligi.\n• Tish qatorida bo'shliqlar, chaynash buzilishi.\n• Ko'pincha nasliy.",
            "ru": "• Отсутствие многих (6+) зубов.\n• Промежутки в ряду, нарушение жевания.\n• Часто наследственная.",
            "en": "• Many (6+) missing teeth.\n• Gaps in the arch, impaired chewing.\n• Often hereditary.",
        },
        "differential": {
            "uz": "Gipodontiya (kamroq tish) va adentiyadan farqlanadi.",
            "ru": "Дифференцируют с гиподонтией (меньше зубов) и адентией.",
            "en": "Differentiated from hypodontia (fewer teeth) and adentia.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodont/ortopedga boring — protezlash, implant, ortodontik tartibga solish.",
            "ru": "Что делать: к ортодонту/ортопеду — протезирование, импланты, ортодонтическое упорядочивание.",
            "en": "What to do: see an orthodontist/prosthodontist — prosthetics, implants, orthodontic management.",
        },
    },
    "hypodontia": {
        "description": {
            "uz": "Gipodontiya — bir nechta (1-5) tishning tug'ma yo'qligi; eng ko'p uchraydigan tish soni anomaliyasi (ko'pincha lateral kesuv yoki premolyar).",
            "ru": "Гиподонтия — врождённое отсутствие нескольких (1-5) зубов; самая частая аномалия числа зубов (чаще боковой резец или премоляр).",
            "en": "Hypodontia — congenital absence of a few (1-5) teeth; the most common tooth-number anomaly (often lateral incisor or premolar).",
        },
        "symptoms_text": {
            "uz": "• 1-5 ta tishning yo'qligi.\n• Bo'shliqlar yoki sut tish saqlanib qolishi.\n• Estetik/funksional muammo.",
            "ru": "• Отсутствие 1-5 зубов.\n• Промежутки или сохранение молочного зуба.\n• Эстетическая/функциональная проблема.",
            "en": "• Absence of 1-5 teeth.\n• Gaps or a retained baby tooth.\n• Aesthetic/functional issue.",
        },
        "differential": {
            "uz": "Oligodontiya (ko'proq) va chiqmagan (retensiyalangan) tishdan farqlanadi.",
            "ru": "Дифференцируют с олигодонтией (больше) и ретенированным (непрорезавшимся) зубом.",
            "en": "Differentiated from oligodontia (more teeth) and an unerupted (retained) tooth.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — bo'shliqni yopish yoki protez/implant bilan tiklash rejasi.",
            "ru": "Что делать: к ортодонту — план закрытия промежутка или восстановления протезом/имплантом.",
            "en": "What to do: see an orthodontist — plan to close the gap or restore with a prosthesis/implant.",
        },
    },
    "hyperdontia": {
        "description": {
            "uz": "Giperodontiya — ortiqcha (sverkomplekt) tishlarning mavjudligi; ko'pincha old qismda (meziodens).",
            "ru": "Гипердонтия — наличие сверхкомплектных зубов; чаще в переднем отделе (мезиоденс).",
            "en": "Hyperdontia — presence of supernumerary (extra) teeth; often in the anterior region (mesiodens).",
        },
        "symptoms_text": {
            "uz": "• Ortiqcha tish(lar).\n• Qo'shni tishlar chiqishiga to'sqinlik, siljish.\n• Zichlik yoki noto'g'ri joylashuv.",
            "ru": "• Лишний зуб(ы).\n• Помеха прорезыванию соседних зубов, смещение.\n• Скученность или неправильное положение.",
            "en": "• Extra tooth/teeth.\n• Obstruct eruption of adjacent teeth, displacement.\n• Crowding or malposition.",
        },
        "differential": {
            "uz": "Geminatsiyadan (bitta tish ikkiga o'xshaydi) farqlanadi.",
            "ru": "Дифференцируют с геминацией (один зуб выглядит как два).",
            "en": "Differentiated from gemination (one tooth looks like two).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodont/jarrohga boring — rentgen, ortiqcha tishni olib tashlash, ortodontik tartibga solish.",
            "ru": "Что делать: к ортодонту/хирургу — рентген, удаление лишнего зуба, ортодонтическое лечение.",
            "en": "What to do: see an orthodontist/surgeon — X-ray, removal of the extra tooth, orthodontic treatment.",
        },
    },
    "gemination": {
        "description": {
            "uz": "Geminatsiya — bitta tish kurtagining qisman bo'linishi natijasida ikki tojga o'xshash, lekin bitta ildizli tish; tishlar soni normal qoladi.",
            "ru": "Геминация — частичное раздвоение одного зачатка: зуб с двумя коронками, но одним корнем; число зубов в норме.",
            "en": "Gemination — partial splitting of one tooth bud: a tooth with two crowns but one root; tooth count remains normal.",
        },
        "symptoms_text": {
            "uz": "• Kattalashgan yoki ikkiga bo'lingan ko'rinishdagi tish.\n• Tishlar soni normal.\n• Estetik/gigiyenik muammo.",
            "ru": "• Увеличенный или раздвоенный с виду зуб.\n• Число зубов нормальное.\n• Эстетическая/гигиеническая проблема.",
            "en": "• An enlarged or two-lobed-looking tooth.\n• Normal tooth count.\n• Aesthetic/hygiene issue.",
        },
        "differential": {
            "uz": "Fuziya (ikki tish qo'shilgan, soni kamayadi) — rentgen bilan farqlanadi.",
            "ru": "Дифференцируют с фузией (слияние двух зубов, число уменьшается) — по рентгену.",
            "en": "Differentiated from fusion (two teeth joined, count reduced) — by X-ray.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/ortodontga boring — rentgen baholash, estetik/gigiyenik korreksiya, kerak bo'lsa restavratsiya.",
            "ru": "Что делать: к стоматологу/ортодонту — оценка по рентгену, эстетическая/гигиеническая коррекция, при необходимости реставрация.",
            "en": "What to do: see a dentist/orthodontist — X-ray assessment, aesthetic/hygiene correction, restoration if needed.",
        },
    },
    "fusion": {
        "description": {
            "uz": "Fuziya — ikki alohida tish kurtagining qo'shilib, bitta katta tish hosil qilishi; tish qatorida soni kamayganga o'xshaydi.",
            "ru": "Фузия (слияние) — соединение двух отдельных зачатков в один крупный зуб; число зубов в ряду кажется уменьшенным.",
            "en": "Fusion — union of two separate tooth buds into one large tooth; the tooth count in the arch appears reduced.",
        },
        "symptoms_text": {
            "uz": "• Ikki tish qo'shilgan katta tish.\n• Tishlar soni kamayganga o'xshaydi.\n• Botiq chiziq bo'ylab karies xavfi.",
            "ru": "• Крупный зуб из двух сросшихся.\n• Число зубов кажется уменьшенным.\n• Риск кариеса по линии борозды.",
            "en": "• A large tooth from two joined teeth.\n• Tooth count appears reduced.\n• Caries risk along the groove.",
        },
        "differential": {
            "uz": "Geminatsiya (soni normal) va konkressensiyadan farqlanadi.",
            "ru": "Дифференцируют с геминацией (число в норме) и конкресценцией.",
            "en": "Differentiated from gemination (normal count) and concrescence.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: stomatolog/ortodontga boring — rentgen, gigiyena, ortodontik/estetik korreksiya.",
            "ru": "Что делать: к стоматологу/ортодонту — рентген, гигиена, ортодонтическая/эстетическая коррекция.",
            "en": "What to do: see a dentist/orthodontist — X-ray, hygiene, orthodontic/aesthetic correction.",
        },
    },
    "concrescence": {
        "description": {
            "uz": "Konkressensiya — ikki tishning tojlari alohida, lekin ildizlari sement orqali qo'shilib qolishi; asosan rentgenda aniqlanadi.",
            "ru": "Конкресценция — коронки двух зубов раздельны, но корни соединены цементом; выявляется в основном на рентгене.",
            "en": "Concrescence — two teeth have separate crowns but roots joined by cementum; detected mainly on X-ray.",
        },
        "symptoms_text": {
            "uz": "• Tojlar alohida, ildizlar qo'shilgan.\n• Odatda simptomsiz.\n• Tish olishda ahamiyatli (birga chiqishi mumkin).",
            "ru": "• Коронки раздельны, корни сращены.\n• Обычно бессимптомно.\n• Важно при удалении (могут выйти вместе).",
            "en": "• Separate crowns, joined roots.\n• Usually asymptomatic.\n• Important for extraction (may come out together).",
        },
        "differential": {
            "uz": "Fuziya va geminatsiyadan (tojlar ham qo'shilgan) farqlanadi.",
            "ru": "Дифференцируют с фузией и геминацией (сросшиеся коронки).",
            "en": "Differentiated from fusion and gemination (joined crowns).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: odatda davo shart emas; tish olish rejalashtirilsa rentgen bilan baholash zarur.",
            "ru": "Что делать: обычно лечение не требуется; при планировании удаления нужна оценка по рентгену.",
            "en": "What to do: usually no treatment needed; X-ray assessment is required if extraction is planned.",
        },
    },
    "taurodontism": {
        "description": {
            "uz": "Taurodontizm — tishning pulpa kamerasi kattalashib, ildizlar kalta bo'lishi; rivojlanish varianti, faqat rentgenda ko'rinadi.",
            "ru": "Тауродонтизм — увеличенная пульпарная камера и короткие корни; вариант развития, виден только на рентгене.",
            "en": "Taurodontism — an enlarged pulp chamber with short roots; a developmental variant, visible only on X-ray.",
        },
        "symptoms_text": {
            "uz": "• Tashqaridan ko'rinmaydi (rentgen belgisi).\n• Odatda simptomsiz.\n• Endodontik davolashda ahamiyatli.",
            "ru": "• Внешне не виден (рентген-признак).\n• Обычно бессимптомно.\n• Важно при эндодонтическом лечении.",
            "en": "• Not visible externally (an X-ray sign).\n• Usually asymptomatic.\n• Relevant for endodontic treatment.",
        },
        "differential": {
            "uz": "Boshqa shakl anomaliyalaridan rentgen bilan farqlanadi.",
            "ru": "Дифференцируют с другими аномалиями формы по рентгену.",
            "en": "Differentiated from other shape anomalies by X-ray.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: davo talab qilmaydi; faqat davolash (kanal) rejalashtirilsa hisobga olinadi.",
            "ru": "Что делать: лечения не требует; учитывается лишь при планировании лечения каналов.",
            "en": "What to do: no treatment needed; only considered when planning root canal treatment.",
        },
    },
    "distopia": {
        "description": {
            "uz": "Distopiya — tishning noto'g'ri joyda yoki noto'g'ri burchakda joylashishi; ko'pincha joy yetishmovchiligi natijasida.",
            "ru": "Дистопия — расположение зуба не на своём месте или под неправильным углом; часто из-за нехватки места.",
            "en": "Distopia — a tooth positioned in the wrong place or at the wrong angle; often due to lack of space.",
        },
        "symptoms_text": {
            "uz": "• Tish noto'g'ri joyda/burchakda.\n• Zichlik, qo'shni tishlarga bosim.\n• Estetik/funksional muammo.",
            "ru": "• Зуб в неправильном месте/под углом.\n• Скученность, давление на соседние зубы.\n• Эстетическая/функциональная проблема.",
            "en": "• Tooth in the wrong place/angle.\n• Crowding, pressure on adjacent teeth.\n• Aesthetic/functional issue.",
        },
        "differential": {
            "uz": "Ektopik chiqish (chiqish yo'li noto'g'ri) va retensiyadan farqlanadi.",
            "ru": "Дифференцируют с эктопическим прорезыванием (неправильный путь) и ретенцией.",
            "en": "Differentiated from ectopic eruption (wrong path) and retention.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — joy ochish va tishni to'g'rilash; ba'zan jarrohlik.",
            "ru": "Что делать: к ортодонту — создание места и выравнивание зуба; иногда хирургия.",
            "en": "What to do: see an orthodontist — create space and align the tooth; sometimes surgery.",
        },
    },
    "tooth_retention": {
        "description": {
            "uz": "Retensiya — to'liq shakllangan tishning suyak/milk ichida qolib, o'z vaqtida chiqmasligi; ko'pincha aql tishi yoki qoziq tish.",
            "ru": "Ретенция — полностью сформированный зуб остаётся в кости/десне и не прорезается; чаще зуб мудрости или клык.",
            "en": "Retention — a fully formed tooth remains in the bone/gum and does not erupt; often a wisdom tooth or canine.",
        },
        "symptoms_text": {
            "uz": "• Tish chiqmagan (suyak/milk ichida).\n• Ko'pincha og'riqsiz; ba'zan bosim/shish.\n• Sut tish saqlanib qolishi mumkin.",
            "ru": "• Зуб не прорезался (в кости/десне).\n• Часто безболезненно; иногда давление/отёк.\n• Может сохраняться молочный зуб.",
            "en": "• Tooth unerupted (in bone/gum).\n• Often painless; sometimes pressure/swelling.\n• A baby tooth may persist.",
        },
        "differential": {
            "uz": "Adentiya (tish umuman yo'q) va follikulyar kistadan farqlanadi.",
            "ru": "Дифференцируют с адентией (зуба нет вовсе) и фолликулярной кистой.",
            "en": "Differentiated from adentia (no tooth at all) and follicular cyst.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodont/jarrohga boring — rentgen; kuzatuv, ortodontik chiqarish yoki jarrohlik olib tashlash.",
            "ru": "Что делать: к ортодонту/хирургу — рентген; наблюдение, ортодонтическое вытяжение или удаление.",
            "en": "What to do: see an orthodontist/surgeon — X-ray; monitoring, orthodontic traction or surgical removal.",
        },
    },
    "ectopic_eruption": {
        "description": {
            "uz": "Ektopik chiqish — tishning odatdagi yo'ldan tashqarida chiqib kelishi; qo'shni tish ildiziga zarar berishi mumkin.",
            "ru": "Эктопическое прорезывание — прорезывание зуба вне обычного пути; может повреждать корень соседнего зуба.",
            "en": "Ectopic eruption — a tooth erupting outside its normal path; may damage the adjacent tooth's root.",
        },
        "symptoms_text": {
            "uz": "• Tish noto'g'ri yo'nalishda chiqyapti.\n• Qo'shni tishga bosim/rezorbsiya.\n• Ko'pincha birinchi molyar/qoziq tishda.",
            "ru": "• Зуб прорезывается в неправильном направлении.\n• Давление/резорбция соседнего зуба.\n• Чаще первый моляр/клык.",
            "en": "• Tooth erupting in the wrong direction.\n• Pressure/resorption of the adjacent tooth.\n• Often first molar/canine.",
        },
        "differential": {
            "uz": "Distopiya (joylashuv) va zichlikdan farqlanadi.",
            "ru": "Дифференцируют с дистопией (положение) и скученностью.",
            "en": "Differentiated from distopia (position) and crowding.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — erta aralashuv, yo'naltirish; qo'shni tishni himoya qilish.",
            "ru": "Что делать: к ортодонту — раннее вмешательство, направление прорезывания; защита соседнего зуба.",
            "en": "What to do: see an orthodontist — early intervention, guiding eruption; protect the adjacent tooth.",
        },
    },
    "distal_occlusion": {
        "description": {
            "uz": "Distal okklyuziya (II klass) — yuqori tishlar/jag' oldinga chiqqan, pastki jag' orqaroqda joylashgan tishlash anomaliyasi.",
            "ru": "Дистальная окклюзия (II класс) — верхние зубы/челюсть выдвинуты вперёд, нижняя челюсть позади.",
            "en": "Distal occlusion (Class II) — upper teeth/jaw protrude, the lower jaw is positioned back.",
        },
        "symptoms_text": {
            "uz": "• Yuqori old tishlar oldinga chiqqan.\n• 'Qush yuzi' profili, lab yopilmasligi.\n• Chuqur tishlash bilan birga kelishi mumkin.",
            "ru": "• Верхние передние зубы выступают вперёд.\n• Профиль 'птичье лицо', несмыкание губ.\n• Может сочетаться с глубоким прикусом.",
            "en": "• Upper front teeth protrude.\n• 'Bird-face' profile, lips do not close.\n• May coexist with deep bite.",
        },
        "differential": {
            "uz": "Mezial okklyuziya (pastki oldinga) va chuqur tishlashdan farqlanadi.",
            "ru": "Дифференцируют с мезиальной окклюзией (нижняя вперёд) и глубоким прикусом.",
            "en": "Differentiated from mesial occlusion (lower forward) and deep bite.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — breket/plastinka bilan tuzatish (erta yoshda samaraliroq).",
            "ru": "Что делать: к ортодонту — исправление брекетами/пластинкой (эффективнее в раннем возрасте).",
            "en": "What to do: see an orthodontist — correction with braces/appliances (more effective at an early age).",
        },
    },
    "mesial_occlusion": {
        "description": {
            "uz": "Mezial okklyuziya (III klass) — pastki jag'/tishlar yuqori tishlardan oldinga chiqqan; teskari old tishlash.",
            "ru": "Мезиальная окклюзия (III класс) — нижняя челюсть/зубы выдвинуты вперёд за верхние; обратное резцовое перекрытие.",
            "en": "Mesial occlusion (Class III) — lower jaw/teeth protrude ahead of the upper teeth; reverse incisor relationship.",
        },
        "symptoms_text": {
            "uz": "• Pastki jag' oldinga chiqqan.\n• Teskari tishlash, chaynash buzilishi.\n• Ko'pincha skelet (suyak) komponenti bilan.",
            "ru": "• Нижняя челюсть выдвинута вперёд.\n• Обратный прикус, нарушение жевания.\n• Часто со скелетным компонентом.",
            "en": "• Lower jaw juts forward.\n• Reverse bite, impaired chewing.\n• Often with a skeletal component.",
        },
        "differential": {
            "uz": "Distal okklyuziya va kross-baytdan farqlanadi.",
            "ru": "Дифференцируют с дистальной окклюзией и перекрёстным прикусом.",
            "en": "Differentiated from distal occlusion and crossbite.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — erta davolash muhim; og'ir skelet shaklida ortognatik jarrohlik.",
            "ru": "Что делать: к ортодонту — важно раннее лечение; при тяжёлой скелетной форме ортогнатическая хирургия.",
            "en": "What to do: see an orthodontist — early treatment matters; orthognathic surgery for severe skeletal forms.",
        },
    },
    "deep_bite": {
        "description": {
            "uz": "Chuqur tishlash — yuqori old tishlar pastki old tishlarni haddan tashqari (deyarli to'liq) qoplashi.",
            "ru": "Глубокий прикус — верхние передние зубы чрезмерно (почти полностью) перекрывают нижние.",
            "en": "Deep bite — the upper front teeth overlap the lower ones excessively (almost completely).",
        },
        "symptoms_text": {
            "uz": "• Yuqori tishlar pastkilarni ko'p qoplaydi.\n• Pastki tishlar tanglay milkini jaroxatlashi mumkin.\n• Yeyilish va TMJ zo'riqishi.",
            "ru": "• Верхние зубы сильно перекрывают нижние.\n• Нижние зубы могут травмировать нёбную десну.\n• Стираемость и нагрузка на ВНЧС.",
            "en": "• Upper teeth heavily overlap the lower ones.\n• Lower teeth may traumatize the palatal gum.\n• Wear and TMJ strain.",
        },
        "differential": {
            "uz": "Ochiq tishlash (teskari) va distal okklyuziyadan farqlanadi.",
            "ru": "Дифференцируют с открытым прикусом (противоположность) и дистальной окклюзией.",
            "en": "Differentiated from open bite (opposite) and distal occlusion.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — breket/plastinka bilan balandlikni tuzatish.",
            "ru": "Что делать: к ортодонту — коррекция брекетами/пластинкой.",
            "en": "What to do: see an orthodontist — correction with braces/appliances.",
        },
    },
    "open_bite": {
        "description": {
            "uz": "Ochiq tishlash — tishlar yopilganda old (yoki yon) qismda tishlar tegmay, ochiq oraliq qolishi; ko'pincha til/barmoq so'rish odati bilan.",
            "ru": "Открытый прикус — при смыкании в переднем (или боковом) отделе остаётся щель; часто из-за привычки сосания языка/пальца.",
            "en": "Open bite — when teeth close, a gap remains in the front (or side); often from tongue/finger sucking habits.",
        },
        "symptoms_text": {
            "uz": "• Old tishlar yopilmaydi (ochiq oraliq).\n• Tishlab uzish va nutq qiyinlashishi.\n• Til so'rish/og'iz orqali nafas olish bilan bog'liq.",
            "ru": "• Передние зубы не смыкаются (щель).\n• Затруднение откусывания и речи.\n• Связь с сосанием языка/ротовым дыханием.",
            "en": "• Front teeth do not meet (gap).\n• Difficulty biting and speaking.\n• Linked to tongue sucking/mouth breathing.",
        },
        "differential": {
            "uz": "Chuqur tishlash (teskari) va skelet anomaliyalaridan farqlanadi.",
            "ru": "Дифференцируют с глубоким прикусом и скелетными аномалиями.",
            "en": "Differentiated from deep bite and skeletal anomalies.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — odatni to'xtatish, breket; og'ir holatda jarrohlik.",
            "ru": "Что делать: к ортодонту — устранение привычки, брекеты; в тяжёлых случаях хирургия.",
            "en": "What to do: see an orthodontist — stop the habit, braces; surgery in severe cases.",
        },
    },
    "crossbite": {
        "description": {
            "uz": "Kross-bayt (kesishgan tishlash) — tishlashda ba'zi pastki tishlar yuqori tishlardan tashqarida yopilishi; bir yoki ikki tomonlama.",
            "ru": "Перекрёстный прикус — при смыкании некоторые нижние зубы оказываются снаружи верхних; одно- или двусторонний.",
            "en": "Crossbite — when biting, some lower teeth close outside the upper teeth; unilateral or bilateral.",
        },
        "symptoms_text": {
            "uz": "• Pastki tishlar yuqoridan tashqarida yopiladi.\n• Yuz assimetriyasi, notekis yeyilish.\n• Chaynash va TMJ muammolari.",
            "ru": "• Нижние зубы смыкаются снаружи верхних.\n• Асимметрия лица, неравномерное стирание.\n• Проблемы жевания и ВНЧС.",
            "en": "• Lower teeth close outside the upper ones.\n• Facial asymmetry, uneven wear.\n• Chewing and TMJ problems.",
        },
        "differential": {
            "uz": "Mezial okklyuziya va alohida tish distopiyasidan farqlanadi.",
            "ru": "Дифференцируют с мезиальной окклюзией и дистопией отдельного зуба.",
            "en": "Differentiated from mesial occlusion and individual tooth distopia.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — erta tuzatish (kengaytirgich, breket) muhim; assimetriyaning oldini oladi.",
            "ru": "Что делать: к ортодонту — важно раннее лечение (расширитель, брекеты); предотвращает асимметрию.",
            "en": "What to do: see an orthodontist — early correction (expander, braces) matters; prevents asymmetry.",
        },
    },
    "dental_crowding": {
        "description": {
            "uz": "Tish qatori torayishi (skuchennost) — jag'da joy yetishmasligi natijasida tishlarning qiyshiq, zich joylashishi.",
            "ru": "Скученность зубов — тесное, кривое расположение зубов из-за нехватки места в челюсти.",
            "en": "Dental crowding — crooked, tightly packed teeth due to insufficient space in the jaw.",
        },
        "symptoms_text": {
            "uz": "• Tishlar qiyshiq, bir-birining ustiga chiqqan.\n• Gigiyena qiyin, karies/gingivit xavfi.\n• Estetik muammo.",
            "ru": "• Зубы кривые, налегают друг на друга.\n• Затруднена гигиена, риск кариеса/гингивита.\n• Эстетическая проблема.",
            "en": "• Teeth crooked, overlapping.\n• Hygiene is hard, caries/gingivitis risk.\n• Aesthetic concern.",
        },
        "differential": {
            "uz": "Tremalar/diastema (bo'shliqlar — teskari holat) dan farqlanadi.",
            "ru": "Дифференцируют с тремами/диастемой (промежутки — противоположное).",
            "en": "Differentiated from tremas/diastema (spacing — the opposite).",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — breket/elaynerlar bilan tekislash; ba'zan joy uchun tish olish.",
            "ru": "Что делать: к ортодонту — выравнивание брекетами/элайнерами; иногда удаление зуба для места.",
            "en": "What to do: see an orthodontist — alignment with braces/aligners; sometimes extraction for space.",
        },
    },
    "diastema": {
        "description": {
            "uz": "Diastema — markaziy old tishlar orasidagi bo'shliq; frenulum yoki tish o'lchami bilan bog'liq.",
            "ru": "Диастема — промежуток между центральными передними зубами; связана с уздечкой или размером зубов.",
            "en": "Diastema — a gap between the central front teeth; related to the frenulum or tooth size.",
        },
        "symptoms_text": {
            "uz": "• Old (markaziy) tishlar orasidagi bo'shliq.\n• Estetik muammo.\n• Pastga tushgan frenulum bilan bog'liq bo'lishi mumkin.",
            "ru": "• Промежуток между центральными передними зубами.\n• Эстетическая проблема.\n• Может быть связана с низкой уздечкой.",
            "en": "• Gap between the central front teeth.\n• Aesthetic concern.\n• May be related to a low frenulum.",
        },
        "differential": {
            "uz": "Tremalar (ko'p bo'shliqlar) va tish yo'qligidan farqlanadi.",
            "ru": "Дифференцируют с тремами (множественные промежутки) и отсутствием зуба.",
            "en": "Differentiated from tremas (multiple spaces) and a missing tooth.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — breket bilan yopish, frenulum plastikasi yoki estetik restavratsiya.",
            "ru": "Что делать: к ортодонту — закрытие брекетами, пластика уздечки или эстетическая реставрация.",
            "en": "What to do: see an orthodontist — closure with braces, frenuloplasty or aesthetic restoration.",
        },
    },
    "tremas": {
        "description": {
            "uz": "Tremalar — bir nechta tishlar orasidagi bo'shliqlar; ko'pincha tish-jag' o'lchami nomutanosibligi yoki tish yo'qligi bilan.",
            "ru": "Тремы — промежутки между несколькими зубами; часто из-за несоответствия размеров зубов и челюсти или отсутствия зубов.",
            "en": "Tremas — spaces between several teeth; often from tooth-jaw size mismatch or missing teeth.",
        },
        "symptoms_text": {
            "uz": "• Bir nechta tishlar orasida bo'shliqlar.\n• Ovqat tiqilishi, estetik muammo.\n• Ko'pincha bolalik almashinuv davrida (fiziologik).",
            "ru": "• Промежутки между несколькими зубами.\n• Застревание пищи, эстетика.\n• Часто в период сменного прикуса (физиологические).",
            "en": "• Spaces between several teeth.\n• Food trapping, aesthetics.\n• Often physiological in the mixed dentition stage.",
        },
        "differential": {
            "uz": "Diastema (faqat old) va skuchennostdan farqlanadi.",
            "ru": "Дифференцируют с диастемой (только передние) и скученностью.",
            "en": "Differentiated from diastema (front only) and crowding.",
        },
        "treatment": {
            "uz": "Nima qilish kerak: ortodontga boring — sababga qarab kuzatuv yoki breket bilan bo'shliqlarni yopish.",
            "ru": "Что делать: к ортодонту — наблюдение или закрытие промежутков брекетами в зависимости от причины.",
            "en": "What to do: see an orthodontist — monitoring or closing spaces with braces depending on the cause.",
        },
    },
})
