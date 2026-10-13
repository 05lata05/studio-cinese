# -*- coding: utf-8 -*-
"""Esercizi aggiuntivi per lezione (si sommano a quelli di lessons_*.py).
Stessi formati:
cloze   : (frase con ___, pinyin, traduzione, [opzioni: la prima è giusta], spiegazione)
reorder : (frase, pinyin, traduzione, [pezzi che uniti danno la frase])
qa      : (domanda in italiano, pinyin del cinese citato, [opzioni: la prima è giusta], spiegazione)
"""

EXTRA = {}
E = lambda n, **kw: EXTRA.setdefault(n, {}).update(kw)

# ───────────────────────────── Lezione 1 ─────────────────────────────
E(1,
  cloze=[
    ("___ 好！", "___ hǎo!", "Ciao!", ["你", "我", "不", "谢"], "你好 = ciao, buongiorno."),
    ("谢谢！——不 ___！", "Xièxie! — Bú ___!", "Grazie! — Prego!", ["客气", "关系", "起", "见"], "A 谢谢 si risponde 不客气 (prego)."),
    ("对不起！——没 ___。", "Duìbuqǐ! — Méi ___.", "Scusa! — Non importa.", ["关系", "客气", "谢谢", "你好"], "A 对不起 si risponde 没关系 (non importa)."),
    ("没关系。___！", "Méi guānxi. ___!", "Non importa. Arrivederci!", ["再见", "你好", "谢谢", "对不起"], "再见 = arrivederci."),
  ],
  reorder=[
    ("没关系，再见！", "Méi guānxi, zàijiàn!", "Non importa, arrivederci!", ["没关系", "，", "再见", "！"]),
    ("谢谢，再见！", "Xièxie, zàijiàn!", "Grazie, arrivederci!", ["谢谢", "，", "再见", "！"]),
  ],
  qa=[
    ("Quale tono ha la sillaba 「妈」 mā (mamma)?", "mā", ["1° tono", "2° tono", "3° tono", "4° tono"], "Il segno ˉ indica il 1° tono, alto e piatto."),
    ("Quale segno indica il 2° tono?", "", ["ˊ", "ˉ", "ˇ", "ˋ"], "Il 2° tono è ascendente: ˊ."),
    ("Quale di queste è una finale semplice?", "", ["ü", "zh", "b", "sh"], "Le finali semplici sono a, o, e, i, u, ü."),
    ("Quale di queste iniziali è aspirata (si pronuncia con un soffio d’aria)?", "", ["t", "d", "b", "g"], "t è la versione aspirata di d."),
    ("Che cosa significa 「对不起」?", "duìbuqǐ", ["Scusa", "Grazie", "Prego", "Arrivederci"], "对不起 = scusa, mi dispiace."),
    ("Qualcuno ti dice 「再见！」. Cosa rispondi?", "zàijiàn!", ["再见！", "谢谢！", "没关系。", "不客气！"], "Al saluto 再见 si risponde con 再见."),
    ("Quale sillaba significa “cavallo”?", "", ["mǎ", "mā", "má", "mà"], "马 mǎ (3° tono) = cavallo; mā = mamma, mà = sgridare."),
    ("Quale parola contiene la finale ü?", "", ["绿色 lǜsè", "汽车 qìchē", "司机 sījī", "读书 dú shū"], "In lǜ la ü si scrive con i puntini."),
  ],
)

# ───────────────────────────── Lezione 2 ─────────────────────────────
E(2,
  cloze=[
    ("___ 钱？", "___ qián?", "Quanto costa?", ["多少", "什么", "谁", "哪"], "多少钱 = quanto costa?"),
    ("对不起，我听不 ___。", "Duìbuqǐ, wǒ tīng bu ___.", "Scusi, non capisco.", ["懂", "好", "起", "见"], "听不懂 = sentire ma non capire."),
    ("请再 ___ 一遍。", "Qǐng zài ___ yí biàn.", "Per favore, ripeti.", ["说", "听", "懂", "谢"], "再说一遍 = dire di nuovo, ripetere."),
    ("明白 ___，谢谢！", "Míngbai ___, xièxie!", "Ho capito, grazie!", ["了", "吗", "呢", "的"], "明白了 = ho capito."),
  ],
  reorder=[
    ("明白了，谢谢！", "Míngbai le, xièxie!", "Ho capito, grazie!", ["明白", "了", "，", "谢谢", "！"]),
    ("对不起，我听不懂。", "Duìbuqǐ, wǒ tīng bu dǒng.", "Scusi, non capisco.", ["对不起", "，", "我", "听", "不", "懂", "。"]),
  ],
  qa=[
    ("Quale di queste è una finale composta?", "", ["ao", "a", "n", "zh"], "In ao si scivola da a a o: è una finale composta."),
    ("Quale sillaba termina con la nasale -ng?", "", ["máng", "mán", "mǎi", "mài"], "-ng si pronuncia con la parte posteriore della lingua: máng."),
    ("Come si scrive in pinyin 「花儿」 (fiore), con il 儿化?", "huār", ["huār", "huā’ér", "huàr", "huāer"], "Il 儿化 si scrive aggiungendo -r alla sillaba: huār."),
    ("Hai capito la spiegazione. Cosa dici?", "", ["明白了。", "我听不懂。", "请再说一遍。", "多少钱？"], "明白了 = ho capito."),
    ("Il venditore dice 「八块。」. Che cosa significa?", "bā kuài.", ["Otto yuan.", "Otto pezzi di pane.", "Ho otto anni.", "Sono le otto."], "块 è l’unità di moneta nella lingua parlata: 八块 = otto yuan."),
    ("Che cosa significa 「请再说一遍」?", "qǐng zài shuō yí biàn", ["Per favore, ripeti.", "Per favore, aspetta.", "Per favore, parla più piano.", "Arrivederci."], "再 = di nuovo, 说 = dire, 一遍 = una volta."),
  ],
)

# ───────────────────────────── Lezione 3 ─────────────────────────────
E(3,
  cloze=[
    ("___ 是什么？", "___ shì shénme?", "Che cos’è questo?", ["这", "我", "你", "多"], "这 = questo."),
    ("厕所在 ___？", "Cèsuǒ zài ___?", "Dov’è il bagno?", ["哪儿", "什么", "多少", "谁"], "哪儿 = dove."),
    ("便宜一点儿 ___！", "Piányi yìdiǎnr ___!", "Un po’ più economico, dai!", ["吧", "吗", "了", "呢"], "吧 a fine frase rende la richiesta più gentile."),
    ("这是 ___。", "Zhè shì ___.", "Questo è tofu.", ["豆腐", "爷爷", "窗户", "木头"], "豆腐 = tofu."),
  ],
  reorder=[
    ("太贵了！", "Tài guì le!", "È troppo caro!", ["太", "贵", "了", "！"]),
    ("请等一会儿。", "Qǐng děng yíhuìr.", "Aspetta un momento, per favore.", ["请", "等", "一会儿", "。"]),
    ("这是豆腐。", "Zhè shì dòufu.", "Questo è tofu.", ["这", "是", "豆腐", "。"]),
  ],
  qa=[
    ("Come si pronuncia 「一点儿」 (un po’)?", "yī diǎnr", ["yìdiǎnr", "yídiǎnr", "yīdiǎnr", "yǐdiǎnr"], "Davanti al 3° tono 一 diventa yì."),
    ("Come si pronuncia 「不是」 (non essere)?", "bù shì", ["bú shì", "bù shì", "bū shì", "bǔ shì"], "Davanti al 4° tono 不 diventa bú."),
    ("Come si pronuncia 「很好」 (molto bene), che ha due 3° toni?", "hěn hǎo", ["hén hǎo", "hěn hǎo con due 3° toni pieni", "hēn hǎo", "hèn hǎo"], "Il primo 3° tono si pronuncia come 2°: hén hǎo."),
    ("Come si scrive u al 3° tono senza iniziale (五, cinque)?", "", ["wǔ", "ǔ", "yǔ", "wú"], "Senza iniziale, u si scrive wu."),
    ("Cerchi il bagno. Cosa chiedi?", "", ["厕所在哪儿？", "这是什么？", "多少钱？", "请等一会儿。"], "厕所在哪儿 = dov’è il bagno?"),
    ("Quale di queste parole ha il tono neutro sulla seconda sillaba?", "", ["豆腐 dòufu", "汽车 qìchē", "绿色 lǜsè", "司机 sījī"], "In dòufu la seconda sillaba non ha segno: è neutra."),
  ],
)

# ───────────────────────────── Lezione 4 ─────────────────────────────
E(4,
  cloze=[
    ("你叫什么 ___？", "Nǐ jiào shénme ___?", "Come ti chiami?", ["名字", "老师", "学生", "汉语"], "名字 = nome."),
    ("他 ___ 中国人。", "Tā ___ Zhōngguórén.", "Lui è cinese.", ["是", "叫", "姓", "都"], "是 = essere."),
    ("您好！您 ___ 什么？", "Nín hǎo! Nín ___ shénme?", "Buongiorno! Qual è il Suo cognome?", ["姓", "是", "的", "都"], "Con le persone più grandi si chiede il cognome: 您姓什么？"),
    ("___ 好！我叫山田。", "___ hǎo! Wǒ jiào Shāntián.", "Ciao a tutti! Mi chiamo Yamada.", ["大家", "我们", "你们", "老师"], "大家好 = ciao a tutti."),
    ("我是老师，你们是 ___。", "Wǒ shì lǎoshī, nǐmen shì ___.", "Io sono l’insegnante, voi siete studenti.", ["学生", "名字", "汉语", "中国"], "学生 = studente."),
  ],
  reorder=[
    ("您好，田老师！", "Nín hǎo, Tián lǎoshī!", "Buongiorno, professoressa Tian!", ["您", "好", "，", "田", "老师", "！"]),
    ("她是我的老师。", "Tā shì wǒ de lǎoshī.", "Lei è la mia insegnante.", ["她", "是", "我", "的", "老师", "。"]),
    ("我是中国人，你呢？", "Wǒ shì Zhōngguórén, nǐ ne?", "Io sono cinese, e tu?", ["我", "是", "中国人", "，", "你", "呢", "？"]),
    ("大家好，我叫丽莎。", "Dàjiā hǎo, wǒ jiào Lìshā.", "Ciao a tutti, mi chiamo Lisa.", ["大家", "好", "，", "我", "叫", "丽莎", "。"]),
  ],
  qa=[
    ("Vuoi chiedere il cognome alla tua insegnante in modo cortese. Cosa dici?", "", ["您姓什么？", "你叫什么名字？", "你是谁？", "你姓什么名字？"], "Con le persone più grandi si usa 您 e si chiede il cognome."),
    ("「我姓王，叫王平。」 Qual è il cognome?", "wǒ xìng Wáng, jiào Wáng Píng.", ["王", "平", "王平", "我"], "In cinese il cognome viene prima del nome: 王."),
    ("Quale frase è corretta?", "", ["我是留学生。", "我是留学生的。", "是我留学生。", "我留学生是。"], "Soggetto + 是 + nome."),
    ("「你们」 significa…", "nǐmen", ["voi", "noi", "tu", "loro"], "们 forma il plurale dei pronomi: 你 → 你们."),
    ("Lisa chiede 「我是留学生，你呢？」. Wang Ping è cinese. Cosa risponde?", "wǒ shì liúxuéshēng, nǐ ne?", ["我是中国学生。", "我也是留学生。", "我叫留学生。", "我是你呢。"], "呢 riprende la domanda: Wang Ping dice chi è lui."),
  ],
)

# ───────────────────────────── Lezione 5 ─────────────────────────────
E(5,
  cloze=[
    ("我 ___ 是日本人，我是韩国人。", "Wǒ ___ shì Rìběnrén, wǒ shì Hánguórén.", "Non sono giapponese, sono coreano.", ["不", "也", "都", "吗"], "不 + verbo = negazione."),
    ("___ 好！——晚上好！", "___ hǎo! — Wǎnshang hǎo!", "Buonasera! — Buonasera!", ["晚上", "早上", "上午", "下午"], "Si risponde con lo stesso saluto: 晚上好."),
    ("他是 ___？——他是我们的老师。", "Tā shì ___? — Tā shì wǒmen de lǎoshī.", "Chi è lui? — È il nostro insegnante.", ["谁", "哪", "几", "多"], "谁 = chi."),
  ],
  reorder=[
    ("你多大？", "Nǐ duō dà?", "Quanti anni hai?", ["你", "多", "大", "？"]),
    ("他不是美国人。", "Tā bú shì Měiguórén.", "Lui non è americano.", ["他", "不", "是", "美国人", "。"]),
    ("你们都是英国人吗？", "Nǐmen dōu shì Yīngguórén ma?", "Siete tutti inglesi?", ["你们", "都", "是", "英国人", "吗", "？"]),
  ],
  qa=[
    ("Sono le 20:00 e incontri un amico. Come lo saluti?", "", ["晚上好！", "早上好！", "上午好！", "下午好！"], "La sera si dice 晚上好."),
    ("Ti chiedono 「你是美国人吗？」 ma sei francese. Cosa rispondi?", "nǐ shì Měiguórén ma?", ["不，我是法国人。", "不是，我不法国人。", "对，我是法国人。", "我是不美国人。"], "No = 不, poi la nazionalità giusta."),
    ("Come si dice 19?", "", ["十九", "九十", "一九", "十和九"], "Dieci (十) + nove (九)."),
    ("Quale frase usa 也 in modo corretto?", "", ["我也是学生。", "也我是学生。", "我是也学生。", "我是学生也。"], "也 va dopo il soggetto e prima del verbo."),
  ],
)

# ───────────────────────────── Lezione 6 ─────────────────────────────
E(6,
  cloze=[
    ("明天你 ___ 课吗？", "Míngtiān nǐ ___ kè ma?", "Domani hai lezione?", ["有", "是", "在", "叫"], "有 = avere."),
    ("现在八点 ___。(8:15)", "Xiànzài bā diǎn ___.", "Sono le otto e un quarto.", ["一刻", "半", "差", "两分"], "一刻 = un quarto d’ora."),
    ("我七点 ___。", "Wǒ qī diǎn ___.", "Mi alzo alle sette.", ["起床", "睡觉", "下课", "吃饭"], "起床 = alzarsi dal letto."),
    ("十一点五十，该 ___ 了。", "Shíyī diǎn wǔshí, gāi ___ le.", "Sono le 11:50, è ora di finire la lezione.", ["下课", "起床", "上课", "睡觉"], "下课 = finire la lezione."),
  ],
  reorder=[
    ("你几点起床？", "Nǐ jǐ diǎn qǐ chuáng?", "A che ora ti alzi?", ["你", "几", "点", "起床", "？"]),
    ("我从九点到十点有口语课。", "Wǒ cóng jiǔ diǎn dào shí diǎn yǒu kǒuyǔkè.", "Ho lezione di lingua parlata dalle nove alle dieci.",
     ["我", "从", "九点", "到", "十点", "有", "口语课", "。"]),
    ("现在差一刻八点。", "Xiànzài chà yí kè bā diǎn.", "Ora manca un quarto alle otto.", ["现在", "差", "一刻", "八点", "。"]),
  ],
  qa=[
    ("Che ore sono quando senti 「十点半」?", "shí diǎn bàn", ["10:30", "10:15", "9:30", "10:45"], "半 = e mezza."),
    ("Quale frase è corretta?", "", ["我没有手表。", "我不有手表。", "我没手表有。", "我有没手表。"], "La negazione di 有 è 没有."),
    ("Come si dice “domenica”?", "", ["星期天", "星期七", "星期零", "七星期"], "Domenica = 星期天 o 星期日."),
    ("Come si dice 2:05?", "", ["两点零五分", "二点五分", "两点五十", "零五分两点"], "Davanti a 点 si usa 两; :05 = 零五分."),
  ],
)
