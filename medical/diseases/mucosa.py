"""
5, 6 (shilliq infeksiyalar) va 12-kategoriya (o'smalar/prekanseroz) —
Og'iz shilliq qavati, til va lab kasalliklari.

Bloklar:
  - Stomatitlar (aftoz, kataral, yarali, travmatik, kandidoz)
  - Til kasalliklari (geografik, qora tukli, rombsimon glossit, glossit)
  - Lab kasalliklari (meteorologik, eksfoliativ, aktinik, angular xeylit)
  - Infeksion (gerpes, herpes zoster, HPV, qo'l-oyoq-og'iz, sifilis, sil, aktinomikoz)
  - Prekanseroz (leykoplakiya, eritroplakiya, submukoz fibroz, lixen planus)
  - Yaxshi sifatli o'smalar (fibroma, gemangioma, lipoma)
  - Yomon sifatli (yassi hujayrali karsinoma, til/lab saratoni)
"""

from medical.disease_model import Disease

# ─────────────────────────────────────────────
#  STOMATITLAR
# ─────────────────────────────────────────────

aphthous_stomatitis = Disease(
    id="aphthous_stomatitis",
    name_uz="Aftoz stomatit",
    name_ru="Афтозный стоматит",
    name_en="Aphthous stomatitis",
    category="mucosa",
    core_features={
        "ulcer": True,
        "pain": True,
        "white_center_red_halo": True,
    },
    optional_features={
        "recurrent": True,
        "stress_trigger": True,
    },
    negative_features={
        "fever": True,
        "blisters": True,
        "white_patch": True,
        "indurated_lesion": True,
    },
    discriminators=[
        "og'riqli afta (oq markaz + qizil halqa)",
        "qaytalanuvchi, isitmasiz",
        "ko'pincha stress bilan bog'liq",
    ],
    red_flags=[
        "2 haftadan ortiq bitmaydi",
        "qattiqlashib/kattalashib boryapti",
    ],
)

catarrhal_stomatitis = Disease(
    id="catarrhal_stomatitis",
    name_uz="Kataral stomatit",
    name_ru="Катаральный стоматит",
    name_en="Catarrhal stomatitis",
    category="mucosa",
    core_features={
        "redness": True,
        "swelling_mucosa": True,
    },
    optional_features={
        "pain": True,
        "bad_smell": True,
        "dry_mouth": True,
    },
    negative_features={
        "ulcer": True,
        "blisters": True,
        "white_patch": True,
    },
    discriminators=[
        "shilliq qavat umumiy qizargan va shishgan",
        "og'riq minimal, yara yo'q",
        "ko'pincha gigiyena/qo'zg'atuvchi bilan",
    ],
    red_flags=[
        "yara paydo bo'lishi",
        "isitma",
    ],
)

ulcerative_stomatitis = Disease(
    id="ulcerative_stomatitis",
    name_uz="Yarali stomatit",
    name_ru="Язвенный стоматит",
    name_en="Ulcerative stomatitis",
    category="mucosa",
    core_features={
        "ulcer": True,
        "redness": True,
        "bad_smell": True,
    },
    optional_features={
        "pain": True,
        "fever": True,
        "lymph_nodes": True,
        "general_weakness": True,
    },
    negative_features={
        "white_center_red_halo": True,
        "recurrent": True,
        "blisters": True,
    },
    discriminators=[
        "kengroq yarali-nekrotik zararlanish",
        "yomon hid va umumiy belgilar",
        "ko'pincha gigiyena yomon/immunitet past",
    ],
    red_flags=[
        "isitma va holsizlik",
        "tez tarqalishi",
    ],
)

traumatic_stomatitis = Disease(
    id="traumatic_stomatitis",
    name_uz="Travmatik stomatit",
    name_ru="Травматический стоматит",
    name_en="Traumatic stomatitis",
    category="mucosa",
    core_features={
        "ulcer": True,
        "trauma_history": True,
        "localized": True,
    },
    optional_features={
        "pain": True,
    },
    negative_features={
        "fever": True,
        "multiple_lesions": True,
        "recurrent": True,
        "indurated_lesion": True,
    },
    discriminators=[
        "travmadan keyin paydo bo'lgan bitta yara",
        "aniq sabab bor (tish, protez, tishlab olish)",
        "sabab bartaraf etilsa bitadi",
    ],
    red_flags=[
        "sabab yo'q qilingach 2 haftada bitmasligi",
        "qattiq qirralarning paydo bo'lishi",
    ],
)

oral_candidiasis = Disease(
    id="oral_candidiasis",
    name_uz="Og'iz kandidiazi (molochnitsa)",
    name_ru="Кандидоз полости рта (молочница)",
    name_en="Oral candidiasis",
    category="mucosa",
    core_features={
        "white_patch": True,
        "removable_patch": True,
    },
    optional_features={
        "burning": True,
        "dry_mouth": True,
        "antibiotic_history": True,
    },
    negative_features={
        "fever": True,
        "blisters": True,
        "ulcer": True,
        "non_removable": True,
    },
    discriminators=[
        "oq qatlam artilganda ko'tariladi",
        "ostida qizil yuza",
        "ko'pincha antibiotik/immunitet pasayishidan keyin",
    ],
    red_flags=[
        "keng tarqalishi (qizilo'ngachga)",
        "davoga javob bermaslik",
    ],
)

# ─────────────────────────────────────────────
#  TIL KASALLIKLARI
# ─────────────────────────────────────────────

geographic_tongue = Disease(
    id="geographic_tongue",
    name_uz="Geografik til (desquamativ glossit)",
    name_ru="Географический язык (десквамативный глоссит)",
    name_en="Geographic tongue",
    category="mucosa",
    core_features={
        "tongue_lesion": True,
        "map_like_patches": True,
    },
    optional_features={
        "burning": True,
        "recurrent": True,
    },
    negative_features={
        "ulcer": True,
        "white_patch": True,
        "indurated_lesion": True,
    },
    discriminators=[
        "tilda xarita kabi ko'chib yuruvchi qizil-oq dog'lar",
        "joyi vaqt o'tib o'zgaradi",
        "ko'pincha simptomsiz yoki yengil achishish",
    ],
    red_flags=[],
)

hairy_tongue = Disease(
    id="hairy_tongue",
    name_uz="Qora tukli til",
    name_ru="Чёрный волосатый язык",
    name_en="Black hairy tongue",
    category="mucosa",
    core_features={
        "tongue_lesion": True,
        "hairy_coating": True,
    },
    optional_features={
        "bad_smell": True,
        "antibiotic_history": True,
    },
    negative_features={
        "ulcer": True,
        "pain": True,
        "indurated_lesion": True,
    },
    discriminators=[
        "til usti tukli, qora-jigarrang qoplama",
        "papillalarning uzayishi",
        "chekish/antibiotik/gigiyena bilan bog'liq",
    ],
    red_flags=[],
)

median_rhomboid_glossitis = Disease(
    id="median_rhomboid_glossitis",
    name_uz="Rombsimon glossit",
    name_ru="Ромбовидный глоссит",
    name_en="Median rhomboid glossitis",
    category="mucosa",
    core_features={
        "tongue_lesion": True,
        "smooth_red_patch_tongue": True,
    },
    optional_features={
        "burning": True,
    },
    negative_features={
        "ulcer": True,
        "map_like_patches": True,
        "hairy_coating": True,
    },
    discriminators=[
        "til o'rtasida silliq qizil rombsimon dog'",
        "papillalar yo'q",
        "ko'pincha kandidoz bilan bog'liq",
    ],
    red_flags=[],
)

glossitis = Disease(
    id="glossitis",
    name_uz="Glossit (til yallig'lanishi)",
    name_ru="Глоссит",
    name_en="Glossitis",
    category="mucosa",
    core_features={
        "tongue_lesion": True,
        "redness": True,
        "burning": True,
    },
    optional_features={
        "pain": True,
        "swelling_mucosa": True,
    },
    negative_features={
        "map_like_patches": True,
        "hairy_coating": True,
        "smooth_red_patch_tongue": True,
        "ulcer": True,
    },
    discriminators=[
        "til qizargan, achishadi va shishgan",
        "ko'pincha vitamin/temir yetishmovchiligi yoki ta'sirlovchi",
    ],
    red_flags=[
        "uzoq davom etishi (tizimli sabab)",
    ],
)

# ─────────────────────────────────────────────
#  LAB KASALLIKLARI (XEYLIT)
# ─────────────────────────────────────────────

meteorological_cheilitis = Disease(
    id="meteorological_cheilitis",
    name_uz="Meteorologik xeylit",
    name_ru="Метеорологический хейлит",
    name_en="Meteorological cheilitis",
    category="mucosa",
    core_features={
        "lip_lesion": True,
        "lip_cracking_weather": True,
    },
    optional_features={
        "burning": True,
    },
    negative_features={
        "lip_sun_damage": True,
        "lip_persistent_scaling": True,
        "angular_cracks": True,
    },
    discriminators=[
        "sovuq/shamol/quruqlikdan lab yorilishi",
        "qaqrash va yengil po'st tashlash",
    ],
    red_flags=[],
)

exfoliative_cheilitis = Disease(
    id="exfoliative_cheilitis",
    name_uz="Eksfoliativ xeylit",
    name_ru="Эксфолиативный хейлит",
    name_en="Exfoliative cheilitis",
    category="mucosa",
    core_features={
        "lip_lesion": True,
        "lip_persistent_scaling": True,
    },
    optional_features={
        "burning": True,
        "stress_trigger": True,
    },
    negative_features={
        "lip_cracking_weather": True,
        "lip_sun_damage": True,
    },
    discriminators=[
        "labning doimiy po'st tashlashi va qoraqo'ng'ir qatlamlar",
        "ko'pincha surunkali, psixogen omil bilan",
    ],
    red_flags=[],
)

actinic_cheilitis = Disease(
    id="actinic_cheilitis",
    name_uz="Aktinik xeylit (prekanseroz)",
    name_ru="Актинический хейлит (предрак)",
    name_en="Actinic cheilitis (precancerous)",
    category="mucosa",
    core_features={
        "lip_lesion": True,
        "lip_sun_damage": True,
    },
    optional_features={
        "non_removable": True,
        "smoking_history": True,
        "tobacco_risk": True,
    },
    negative_features={
        "lip_cracking_weather": True,
    },
    discriminators=[
        "pastki labning uzoq quyoshdan qo'pol, dog'li o'zgarishi",
        "prekanseroz holat — kuzatuv talab qiladi",
    ],
    red_flags=[
        "yara yoki qattiqlashish (saratonga aylanish)",
    ],
)

angular_cheilitis = Disease(
    id="angular_cheilitis",
    name_uz="Angular xeylit (zaeda)",
    name_ru="Ангулярный хейлит (заеды)",
    name_en="Angular cheilitis",
    category="mucosa",
    core_features={
        "angular_cracks": True,
    },
    optional_features={
        "burning": True,
        "removable_patch": True,
        "dry_mouth": True,
    },
    negative_features={
        "lip_sun_damage": True,
        "lip_cracking_weather": True,
    },
    discriminators=[
        "lab burchaklarida yoriq/yara (zaeda)",
        "ko'pincha kandida/temir-vitamin yetishmovchiligi",
    ],
    red_flags=[
        "uzoq bitmasligi",
    ],
)

# ─────────────────────────────────────────────
#  INFEKSION (virusli / bakterial)
# ─────────────────────────────────────────────

herpetic_stomatitis = Disease(
    id="herpetic_stomatitis",
    name_uz="O'tkir gerpetik stomatit (birlamchi)",
    name_ru="Острый герпетический стоматит (первичный)",
    name_en="Acute herpetic stomatitis (primary)",
    category="mucosa",
    core_features={
        "blisters": True,
        "fever": True,
        "multiple_lesions": True,
    },
    optional_features={
        "lymph_nodes": True,
        "general_weakness": True,
        "pain": True,
    },
    negative_features={
        "white_patch": True,
        "wart_like_growth": True,
        "unilateral_rash": True,
    },
    discriminators=[
        "ko'p sonli pufakcha va eroziyalar",
        "isitma bilan boshlanadi (ko'pincha bolalarda)",
        "diffuz zararlanish, limfa tugunlari",
    ],
    red_flags=[
        "yuqori isitma, ovqat yeyolmaslik",
        "suvsizlanish",
    ],
)

herpes_simplex_labialis = Disease(
    id="herpes_simplex_labialis",
    name_uz="Herpes simplex (labial uchuq)",
    name_ru="Простой герпес (герпес губ)",
    name_en="Herpes simplex (labial)",
    category="mucosa",
    core_features={
        "grouped_vesicles": True,
        "lip_lesion": True,
    },
    optional_features={
        "recurrent": True,
        "burning": True,
    },
    negative_features={
        "unilateral_rash": True,
        "white_patch": True,
        "fever": True,
    },
    discriminators=[
        "lab/burun atrofida guruh pufakchalar",
        "oldindan achishish/qichishish",
        "qaytalanuvchi (HSV reaktivatsiyasi)",
    ],
    red_flags=[
        "keng tarqalish (immunitet pasayganda)",
    ],
)

herpes_zoster = Disease(
    id="herpes_zoster",
    name_uz="Herpes zoster (belbog' temiratkisi)",
    name_ru="Опоясывающий герпес (herpes zoster)",
    name_en="Herpes zoster",
    category="mucosa",
    core_features={
        "unilateral_rash": True,
        "blisters": True,
    },
    optional_features={
        "pain": True,
        "lymph_nodes": True,
        "general_weakness": True,
    },
    negative_features={
        "bilateral": True,
        "recurrent": True,
        "white_patch": True,
    },
    discriminators=[
        "toshma yuzning faqat bir tomonida, nerv bo'ylab",
        "kuchli og'riq (nevralgiya)",
        "chegarani kesib o'tmaydi",
    ],
    red_flags=[
        "ko'z sohasi jalb etilishi",
        "post-gerpetik nevralgiya",
    ],
)

hpv_papilloma = Disease(
    id="hpv_papilloma",
    name_uz="HPV bilan bog'liq papilloma",
    name_ru="ВПЧ-ассоциированная папиллома",
    name_en="HPV-associated papilloma",
    category="mucosa",
    core_features={
        "wart_like_growth": True,
    },
    optional_features={
        "no_pain": True,
        "soft_painless_lump": True,
    },
    negative_features={
        "ulcer": True,
        "blisters": True,
        "indurated_lesion": True,
    },
    discriminators=[
        "gulkaram/so'galsimon mayda o'simta",
        "og'riqsiz, sekin o'sadi",
        "HPV bilan bog'liq",
    ],
    red_flags=[
        "tez o'sish yoki qattiqlashish",
    ],
)

hand_foot_mouth = Disease(
    id="hand_foot_mouth",
    name_uz="Qo'l-oyoq-og'iz kasalligi",
    name_ru="Синдром рука-нога-рот",
    name_en="Hand-foot-mouth disease",
    category="mucosa",
    core_features={
        "hand_foot_rash": True,
        "blisters": True,
    },
    optional_features={
        "fever": True,
        "multiple_lesions": True,
        "pain": True,
    },
    negative_features={
        "recurrent": True,
        "white_patch": True,
        "unilateral_rash": True,
    },
    discriminators=[
        "og'iz bilan birga qo'l va oyoqda toshma",
        "ko'pincha bolada, isitma bilan",
        "enterovirus (Coxsackie) infeksiyasi",
    ],
    red_flags=[
        "suvsizlanish (ovqat/suv yeyolmaslik)",
    ],
)

oral_syphilis = Disease(
    id="oral_syphilis",
    name_uz="Sifilisning og'izdagi ko'rinishi",
    name_ru="Проявления сифилиса в полости рта",
    name_en="Oral syphilis",
    category="mucosa",
    core_features={
        "painless_firm_ulcer": True,
    },
    optional_features={
        "lymph_nodes": True,
        "white_patch": True,
    },
    negative_features={
        "pain": True,
        "recurrent": True,
        "blisters": True,
    },
    discriminators=[
        "qattiq qirrali og'riqsiz yara (shankr)",
        "regionar limfa tugunlari kattalashishi",
        "bosqichlarga qarab har xil ko'rinish",
    ],
    red_flags=[
        "tizimli tarqalish",
        "tasdiqlash uchun serologik tekshiruv",
    ],
)

oral_tuberculosis = Disease(
    id="oral_tuberculosis",
    name_uz="Tuberkulyozning og'izdagi ko'rinishi",
    name_ru="Проявления туберкулёза в полости рта",
    name_en="Oral tuberculosis",
    category="mucosa",
    core_features={
        "chronic_nonhealing_ulcer": True,
        "pain": True,
    },
    optional_features={
        "general_weakness": True,
        "lymph_nodes": True,
    },
    negative_features={
        "recurrent": True,
        "white_center_red_halo": True,
        "painless_firm_ulcer": True,
    },
    discriminators=[
        "uzoq bitmaydigan og'riqli yara (ko'pincha til orqasida)",
        "yumshoq, qirrasi o'yilgan yara",
        "o'pka tuberkulyozi bilan bog'liq",
    ],
    red_flags=[
        "umumiy belgilar (vazn yo'qotish, kechki terlash)",
    ],
)

actinomycosis = Disease(
    id="actinomycosis",
    name_uz="Aktinomikoz",
    name_ru="Актиномикоз",
    name_en="Actinomycosis",
    category="mucosa",
    core_features={
        "woody_swelling": True,
    },
    optional_features={
        "bad_smell": True,
        "lymph_nodes": True,
    },
    negative_features={
        "blisters": True,
        "recurrent": True,
    },
    discriminators=[
        "qattiq yog'ochsimon shish va ko'p fistula",
        "sarg'ish donachalar (oltingugurt donalari) chiqishi",
        "sekin, surunkali kechishi",
    ],
    red_flags=[
        "qo'shni to'qima/suyakka tarqalishi",
    ],
)

# ─────────────────────────────────────────────
#  PREKANSEROZ
# ─────────────────────────────────────────────

leukoplakia = Disease(
    id="leukoplakia",
    name_uz="Leykoplakiya (prekanseroz)",
    name_ru="Лейкоплакия (предрак)",
    name_en="Leukoplakia (precancerous)",
    category="mucosa",
    core_features={
        "white_patch": True,
        "non_removable": True,
    },
    optional_features={
        "smoking_history": True,
        "tobacco_risk": True,
        "no_pain": True,
    },
    negative_features={
        "removable_patch": True,
        "fever": True,
        "blisters": True,
    },
    discriminators=[
        "artib tushmaydigan oq dog'",
        "chegaralangan o'choq, og'riqsiz",
        "tamaki bilan bog'liq, prekanseroz",
    ],
    red_flags=[
        "qizarish qo'shilishi (eritroplakiya)",
        "yara/qattiqlashish (saratonga aylanish)",
    ],
)

erythroplakia = Disease(
    id="erythroplakia",
    name_uz="Eritroplakiya (prekanseroz)",
    name_ru="Эритроплакия (предрак)",
    name_en="Erythroplakia (precancerous)",
    category="mucosa",
    core_features={
        "red_velvety_patch": True,
        "non_removable": True,
    },
    optional_features={
        "tobacco_risk": True,
        "burning": True,
    },
    negative_features={
        "white_patch": True,
        "removable_patch": True,
        "ulcer": True,
    },
    discriminators=[
        "artilmaydigan qizil baxmaldek dog'",
        "leykoplakiyaga qaraganda yuqori xavf",
        "yuqori malignizatsiya ehtimoli",
    ],
    red_flags=[
        "biopsiya zarur (saraton xavfi yuqori)",
    ],
)

oral_submucous_fibrosis = Disease(
    id="oral_submucous_fibrosis",
    name_uz="Oral submukoz fibroz (prekanseroz)",
    name_ru="Подслизистый фиброз полости рта (предрак)",
    name_en="Oral submucous fibrosis (precancerous)",
    category="mucosa",
    core_features={
        "progressive_trismus_fibrosis": True,
    },
    optional_features={
        "tobacco_risk": True,
        "burning": True,
    },
    negative_features={
        "ulcer": True,
        "blisters": True,
    },
    discriminators=[
        "og'iz ochilishining asta-sekin cheklanishi",
        "shilliq qavatning oqarib qotishi (fibroz tortmalar)",
        "betel/nos iste'moli bilan bog'liq",
    ],
    red_flags=[
        "saratonga aylanish xavfi",
    ],
)

oral_lichen_planus = Disease(
    id="oral_lichen_planus",
    name_uz="Og'iz lixen planusi (qizil yassi temiratki)",
    name_ru="Красный плоский лишай полости рта",
    name_en="Oral lichen planus",
    category="mucosa",
    core_features={
        "white_lacy_pattern": True,
        "bilateral": True,
    },
    optional_features={
        "pain": True,
        "burning": True,
        "erosion": True,
    },
    negative_features={
        "removable_patch": True,
        "fever": True,
        "blisters": True,
    },
    discriminators=[
        "to'r shaklidagi oq chiziqlar (Wickham)",
        "ikki tomonlama, ko'pincha yonoq ichida",
        "eroziv shakli og'riqli bo'lishi mumkin",
    ],
    red_flags=[
        "eroziv shakl (saraton kuzatuvi)",
    ],
)

# ─────────────────────────────────────────────
#  YAXSHI SIFATLI O'SMALAR
# ─────────────────────────────────────────────

fibroma = Disease(
    id="fibroma",
    name_uz="Fibroma",
    name_ru="Фиброма",
    name_en="Fibroma",
    category="mucosa",
    core_features={
        "soft_painless_lump": True,
        "trauma_history": True,
    },
    optional_features={
        "no_pain": True,
        "localized": True,
    },
    negative_features={
        "red_blue_blanching_lesion": True,
        "indurated_lesion": True,
        "ulcer": True,
    },
    discriminators=[
        "qattiqroq, og'riqsiz, silliq tugun",
        "ko'pincha surunkali ishqalanish/tishlab olishdan",
    ],
    red_flags=[
        "tez o'sish yoki yaralanish",
    ],
)

hemangioma = Disease(
    id="hemangioma",
    name_uz="Gemangioma",
    name_ru="Гемангиома",
    name_en="Hemangioma",
    category="mucosa",
    core_features={
        "red_blue_blanching_lesion": True,
    },
    optional_features={
        "soft_painless_lump": True,
        "no_pain": True,
    },
    negative_features={
        "indurated_lesion": True,
        "ulcer": True,
        "white_patch": True,
    },
    discriminators=[
        "qizil-ko'kimtir qon tomir o'simtasi",
        "bosganda oqaradi (blanching)",
        "tug'ma yoki erta paydo bo'lishi",
    ],
    red_flags=[
        "travmadan kuchli qonash",
    ],
)

lipoma = Disease(
    id="lipoma",
    name_uz="Lipoma",
    name_ru="Липома",
    name_en="Lipoma",
    category="mucosa",
    core_features={
        "soft_painless_lump": True,
        "slow_growth": True,
    },
    optional_features={
        "no_pain": True,
    },
    negative_features={
        "red_blue_blanching_lesion": True,
        "indurated_lesion": True,
        "trauma_history": True,
        "ulcer": True,
    },
    discriminators=[
        "yumshoq, sarg'ish, og'riqsiz tugun",
        "juda sekin o'sadi",
        "yog' to'qimasidan",
    ],
    red_flags=[],
)

# ─────────────────────────────────────────────
#  YOMON SIFATLI O'SMALAR
# ─────────────────────────────────────────────

oral_scc = Disease(
    id="oral_scc",
    name_uz="Og'iz bo'shlig'i yassi hujayrali karsinomasi",
    name_ru="Плоскоклеточный рак полости рта",
    name_en="Oral squamous cell carcinoma",
    category="mucosa",
    core_features={
        "indurated_lesion": True,
        "chronic_nonhealing_ulcer": True,
    },
    optional_features={
        "tobacco_risk": True,
        "easy_bleeding_growth": True,
        "numbness": True,
        "lymph_nodes": True,
    },
    negative_features={
        "recurrent": True,
        "white_center_red_halo": True,
        "tongue_lesion": True,
        "lip_lesion": True,
    },
    discriminators=[
        "qattiq, o'rnashgan (indurativ) yara/o'simta",
        "3 haftadan ortiq bitmaydi, oson qonaydi",
        "tamaki/alkogol bilan bog'liq",
    ],
    red_flags=[
        "qattiq, harakatsiz limfa tugunlari",
        "uvishish/karaxtlik — zudlik bilan onkolog",
    ],
)

tongue_cancer = Disease(
    id="tongue_cancer",
    name_uz="Til saratoni",
    name_ru="Рак языка",
    name_en="Tongue cancer",
    category="mucosa",
    core_features={
        "tongue_lesion": True,
        "indurated_lesion": True,
        "chronic_nonhealing_ulcer": True,
    },
    optional_features={
        "tobacco_risk": True,
        "numbness": True,
        "pain": True,
        "lymph_nodes": True,
    },
    negative_features={
        "recurrent": True,
        "map_like_patches": True,
    },
    discriminators=[
        "tilning qattiq, bitmaydigan yarasi",
        "ko'pincha tilning yon yuzasida",
        "og'riq/uvishish va harakat cheklanishi",
    ],
    red_flags=[
        "bo'yin limfa tugunlari kattalashishi",
        "zudlik bilan onkolog ko'rigi",
    ],
)

lip_cancer = Disease(
    id="lip_cancer",
    name_uz="Lab saratoni",
    name_ru="Рак губы",
    name_en="Lip cancer",
    category="mucosa",
    core_features={
        "lip_lesion": True,
        "indurated_lesion": True,
        "chronic_nonhealing_ulcer": True,
    },
    optional_features={
        "lip_sun_damage": True,
        "tobacco_risk": True,
        "easy_bleeding_growth": True,
    },
    negative_features={
        "recurrent": True,
        "lip_cracking_weather": True,
    },
    discriminators=[
        "pastki labda qattiq, bitmaydigan yara",
        "ko'pincha quyosh ta'siri/chekish bilan",
        "asta-sekin kattalashish",
    ],
    red_flags=[
        "limfa tugunlari jalb etilishi",
        "zudlik bilan onkolog ko'rigi",
    ],
)

# ─────────────────────────────────────────────
#  EXPORT
# ─────────────────────────────────────────────
MUCOSA_DISEASES = [
    aphthous_stomatitis,
    catarrhal_stomatitis,
    ulcerative_stomatitis,
    traumatic_stomatitis,
    oral_candidiasis,
    geographic_tongue,
    hairy_tongue,
    median_rhomboid_glossitis,
    glossitis,
    meteorological_cheilitis,
    exfoliative_cheilitis,
    actinic_cheilitis,
    angular_cheilitis,
    herpetic_stomatitis,
    herpes_simplex_labialis,
    herpes_zoster,
    hpv_papilloma,
    hand_foot_mouth,
    oral_syphilis,
    oral_tuberculosis,
    actinomycosis,
    leukoplakia,
    erythroplakia,
    oral_submucous_fibrosis,
    oral_lichen_planus,
    fibroma,
    hemangioma,
    lipoma,
    oral_scc,
    tongue_cancer,
    lip_cancer,
]
