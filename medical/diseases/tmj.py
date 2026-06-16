"""
8-kategoriya — Temporomandibulyar bo'g'im (TMJ) kasalliklari.

TMJ disfunksiyasi, artrit, artroz, disk dislokatsiyasi, ankiloz.
"""

from medical.disease_model import Disease

tmj_dysfunction = Disease(
    id="tmj_dysfunction",
    name_uz="TMJ disfunksiyasi (mio-fassial sindrom)",
    name_ru="Дисфункция ВНЧС (миофасциальный синдром)",
    name_en="TMJ dysfunction (myofascial)",
    category="tmj",
    core_features={
        "jaw_clicking": True,
        "joint_pain": True,
    },
    optional_features={
        "bruxism": True,
        "morning_stiffness": True,
        "jaw_deviation": True,
        "irradiation": True,
    },
    negative_features={
        "joint_crepitus": True,
        "cannot_open_progressive": True,
        "jaw_locking": True,
    },
    discriminators=[
        "ochib-yopganda shiqillash",
        "bo'g'im/chaynov mushaklarida og'riq",
        "ko'pincha bruksizm/stress bilan",
    ],
    red_flags=[
        "og'riqning kuchayishi",
        "harakat cheklanishining ortishi",
    ],
)

tmj_arthritis = Disease(
    id="tmj_arthritis",
    name_uz="TMJ artriti",
    name_ru="Артрит ВНЧС",
    name_en="TMJ arthritis",
    category="tmj",
    core_features={
        "joint_pain": True,
        "morning_stiffness": True,
    },
    optional_features={
        "fever": True,
        "trismus": True,
        "irradiation": True,
    },
    negative_features={
        "joint_crepitus": True,
        "jaw_clicking": True,
        "cannot_open_progressive": True,
    },
    discriminators=[
        "bo'g'imning yallig'lanishli og'rig'i",
        "ertalabki qotishish",
        "ba'zan isitma/tizimli kasallik bilan",
    ],
    red_flags=[
        "kuchli yallig'lanish",
        "bo'g'im destruksiyasi",
    ],
)

tmj_arthrosis = Disease(
    id="tmj_arthrosis",
    name_uz="TMJ artrozi (osteoartroz)",
    name_ru="Артроз ВНЧС (остеоартроз)",
    name_en="TMJ arthrosis (osteoarthrosis)",
    category="tmj",
    core_features={
        "joint_crepitus": True,
        "joint_pain": True,
    },
    optional_features={
        "morning_stiffness": True,
        "jaw_deviation": True,
    },
    negative_features={
        "jaw_clicking": True,
        "fever": True,
        "jaw_locking": True,
    },
    discriminators=[
        "bo'g'imda krepitatsiya (qum g'ichirlashi)",
        "degenerativ-distrofik o'zgarishlar",
        "uzoq davom etgan, kuchsiz og'riq",
    ],
    red_flags=[
        "harakat hajmining kamayishi",
        "bo'g'im deformatsiyasi",
    ],
)

tmj_disc_dislocation = Disease(
    id="tmj_disc_dislocation",
    name_uz="Disk dislokatsiyasi (TMJ)",
    name_ru="Смещение диска ВНЧС",
    name_en="TMJ disc dislocation",
    category="tmj",
    core_features={
        "jaw_clicking": True,
        "jaw_locking": True,
    },
    optional_features={
        "jaw_deviation": True,
        "joint_pain": True,
    },
    negative_features={
        "joint_crepitus": True,
        "fever": True,
        "cannot_open_progressive": True,
    },
    discriminators=[
        "shiqillash bilan birga jag'ning qulflanishi",
        "disk reduksiyasi bilan/siz siljishi",
        "og'iz ochishda blok hissi",
    ],
    red_flags=[
        "doimiy qulflanish (ochilmaslik)",
    ],
)

tmj_ankylosis = Disease(
    id="tmj_ankylosis",
    name_uz="TMJ ankilozi",
    name_ru="Анкилоз ВНЧС",
    name_en="TMJ ankylosis",
    category="tmj",
    core_features={
        "cannot_open_progressive": True,
        "trismus": True,
    },
    optional_features={
        "recent_injury": True,
    },
    negative_features={
        "jaw_clicking": True,
        "joint_pain": True,
        "joint_crepitus": True,
    },
    discriminators=[
        "og'iz ochilishining doimiy (suyak/fibroz) cheklanishi",
        "bo'g'imning birikib qolishi",
        "ko'pincha travma/infeksiya oqibati",
    ],
    red_flags=[
        "ovqatlanish/nafas olishning qiyinlashishi",
        "yuz assimetriyasi (bolalarda)",
    ],
)

# ─────────────────────────────────────────────
#  EXPORT
# ─────────────────────────────────────────────
TMJ_DISEASES = [
    tmj_dysfunction,
    tmj_arthritis,
    tmj_arthrosis,
    tmj_disc_dislocation,
    tmj_ankylosis,
]
