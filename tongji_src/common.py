# -*- coding: utf-8 -*-
"""Dati comuni del corso Tongji (初级汉语口语 1).

Tutti i testi, gli esempi e gli esercizi sono ORIGINALI, scritti seguendo il
vocabolario e i punti grammaticali di ciascuna lezione del libro; non sono
copiati dal libro. Le poesie classiche (dinastia Tang ecc.) sono di pubblico dominio.
"""

COURSE_TITLE = "初级汉语口语 1 · Elementary Spoken Chinese 1"

# Nome cinese del parlante -> nome italiano mostrato nell'app
SPEAKERS = {
    "杰夫": "Jeff", "安妮": "Annie", "田老师": "Prof.ssa Tian", "王平": "Wang Ping",
    "彼得": "Peter", "丽莎": "Lisa", "山田": "Yamada", "朴志永": "Piao Zhiyong",
    "李文静": "Li Wenjing", "刘伟": "Liu Wei", "张新": "Zhang Xin",
    "服务员": "Cameriere", "售货员": "Commesso", "一学生": "Uno studente",
    "路人": "Passante", "大夫": "Dottore", "老师": "Insegnante", "快递员": "Corriere",
    "王阿姨": "Zia Wang", "妈妈": "Mamma", "司机": "Tassista",
}

# Personaggi del libro (presentazione generica, parole nostre)
CHARACTERS = [
    ("杰夫", "Jiéfū", "Jeff — studente inglese, 20 anni, classe 2"),
    ("安妮", "Ānnī", "Annie — studentessa americana, classe 2"),
    ("田老师", "Tián lǎoshī", "Prof.ssa Tian — insegnante di cinese della classe 2"),
    ("王平", "Wáng Píng", "Wang Ping — studente universitario cinese"),
    ("彼得", "Bǐdé", "Peter — studente francese, 19 anni, classe 1"),
    ("丽莎", "Lìshā", "Lisa — studentessa tedesca, compagna di stanza di Annie"),
    ("山田", "Shāntián", "Yamada — studente giapponese, classe 2"),
    ("朴志永", "Piáo Zhìyǒng", "Piao Zhiyong — studente coreano, classe 3"),
    ("李文静", "Lǐ Wénjìng", "Li Wenjing — studentessa universitaria cinese"),
    ("刘伟", "Liú Wěi", "Liu Wei — studente universitario cinese"),
    ("张新", "Zhāng Xīn", "Zhang Xin — studentessa universitaria cinese"),
]

# Parte del discorso (abbreviazione cinese) -> categoria mostrata nell'app
POS_CATEGORY = {
    "名": "Sostantivi", "动": "Verbi", "形": "Aggettivi", "副": "Avverbi",
    "代": "Pronomi e interrogativi", "量": "Classificatori", "数": "Numeri",
    "助": "Particelle", "介": "Preposizioni", "连": "Congiunzioni",
    "叹": "Interiezioni", "助动": "Verbi modali", "数量": "Quantità",
    "头": "Prefissi e suffissi", "尾": "Prefissi e suffissi",
}
CAT_PROPER = "Nomi propri"
CAT_PHRASE = "Espressioni"

# Tabella dei classificatori: nome -> classificatori corretti (il primo è il più tipico).
# Solo fatti linguistici; usata per generare l'esercizio "Classificatori".
MEASURE = [
    ("阿姨", "位 个"), ("班", "个"), ("办公室", "个 间"), ("菜", "个 盘 道"),
    ("菜单", "张 份 个"), ("茶", "杯 碗 壶"), ("车", "辆"), ("大学", "所 个"),
    ("大衣", "件"), ("大夫", "位 个"), ("点心", "块 盘 个"), ("电话", "部 个"),
    ("电视", "台"), ("电影", "部 场"), ("动物园", "个 座"), ("饭", "碗 顿"),
    ("饭馆儿", "家 个"), ("房间", "间 个"), ("飞机", "架"), ("服务员", "位 个"),
    ("歌", "首 支"), ("火车", "列 辆 节"), ("饺子", "盘 碗 斤 个"), ("教室", "间 个"),
    ("街", "条"), ("镜子", "面"), ("咖啡", "杯"), ("课", "节 门"), ("课本", "本"),
    ("课文", "篇 段"), ("老师", "位 个"), ("礼物", "件 个"), ("楼", "座 层"),
    ("律师", "位 个"), ("马路", "条"), ("馒头", "个 斤"), ("米饭", "碗"),
    ("朋友", "位 个"), ("啤酒", "瓶 杯"), ("票", "张"), ("葡萄", "串 斤"),
    ("钱", "块 元 毛"), ("人", "个 口"), ("肉", "块 斤"), ("山", "座"),
    ("商店", "家 个"), ("事", "件"), ("手机", "部 个"), ("售货员", "位 个"),
    ("书", "本"), ("水", "杯 瓶 碗"), ("宿舍", "间 个"), ("汤", "碗"),
    ("同学", "位 个"), ("图书馆", "座 个"), ("晚饭", "顿"), ("鞋", "双 只"),
    ("学校", "所 个"), ("医生", "位 个"), ("医院", "家 座"), ("衣服", "件 套"),
    ("饮料", "杯 瓶"), ("鱼", "条 斤"), ("羽绒服", "件"), ("照片", "张"),
    ("中学", "所"), ("桌子", "张"), ("自行车", "辆"), ("椅子", "把"),
    ("词典", "本"), ("本子", "本"), ("笔", "支"), ("床", "张"), ("闹钟", "个"),
    ("问题", "个"), ("手表", "块"), ("眼镜", "副"), ("节目", "个"),
]
# Classificatori usati come distrattori (个 escluso: troppo generico, creerebbe ambiguità)
MW_DISTRACTORS = ["本", "张", "件", "辆", "位", "杯", "瓶", "碗", "条", "双", "座", "节",
                  "门", "台", "部", "家", "间", "首", "支", "顿", "斤", "层", "所", "架",
                  "面", "把", "口", "块", "副", "盘"]
