# -*- coding: utf-8 -*-
"""Lezioni 1-7. Formati:
vocab   : righe "tipo|cinese|pinyin|pos|italiano|inglese"  (tipo N=nuova, S=supplementare, P=nome proprio)
grammar : (titolo, spiegazione, [(esempio_zh, pinyin, italiano), ...])
dialogue: (scena, [(parlante, zh, pinyin, italiano), ...], riordinabile=True)
reading : (titolo, zh, pinyin, italiano, [(domanda_zh, pinyin, [opzioni: la prima è giusta])])
cloze   : (frase con ___, pinyin, traduzione, [opzioni: la prima è giusta], spiegazione)
reorder : (frase, pinyin, traduzione, [pezzi che uniti danno la frase])
qa      : (domanda in italiano, pinyin del cinese citato, [opzioni: la prima è giusta], spiegazione)
extra   : (tipo, titolo, zh, pinyin, italiano)
"""

LESSONS = []
L = lambda **kw: LESSONS.append(kw)

# ───────────────────────────── Lezione 1 ─────────────────────────────
L(n=1, zh="汉语拼音（一）", py="Hànyǔ pīnyīn (yī)", it="Pinyin (1): iniziali, finali semplici, toni",
  theme="Il sistema fonetico: sillaba, iniziali, finali semplici e i quattro toni",
  vocab="""
N|你好|nǐ hǎo||ciao, buongiorno|hello
S|汽车|qìchē|名|automobile|car
S|司机|sījī|名|autista|driver
S|绿色|lǜsè|名|verde|green
S|打的|dǎdī||prendere il taxi|to take a taxi
S|日记|rìjì|名|diario|diary
S|记者|jìzhě|名|giornalista|journalist
S|读书|dú shū||leggere, studiare|to read, study
S|树|shù|名|albero|tree
S|鸡|jī|名|pollo, gallina|chicken
S|猪|zhū|名|maiale|pig
S|马|mǎ|名|cavallo|horse
""",
  grammar=[
    ("La sillaba cinese", "Ogni sillaba è formata da iniziale (声母) + finale (韵母) + tono (声调). Esempio: mā = m + a + 1° tono.",
     [("妈", "mā", "mamma")]),
    ("Le 21 iniziali", "b p m f · d t n l · g k h · j q x · zh ch sh r · z c s. Attenzione alle coppie non aspirata / aspirata: b–p, d–t, g–k, j–q, zh–ch, z–c (la seconda si pronuncia con un soffio d’aria).",
     [("爸 / 怕", "bà / pà", "papà / avere paura")]),
    ("Le finali semplici", "a o e i u ü. La ü si pronuncia come la “u” francese o la “ü” tedesca: si dice “i” arrotondando le labbra.",
     [("女", "nǚ", "femmina")]),
    ("I quattro toni", "1° tono alto e piatto (ˉ), 2° ascendente (ˊ), 3° basso, scende e risale (ˇ), 4° discendente e secco (ˋ). Il segno si scrive sopra la vocale principale. Cambiare tono cambia il significato!",
     [("妈 麻 马 骂", "mā má mǎ mà", "mamma · canapa · cavallo · sgridare")]),
  ],
  dialogue=("Saluti di base", [
    ("杰夫", "你好！", "Nǐ hǎo!", "Ciao!"),
    ("安妮", "你好！", "Nǐ hǎo!", "Ciao!"),
    ("杰夫", "谢谢！", "Xièxie!", "Grazie!"),
    ("安妮", "不客气！", "Bú kèqi!", "Prego!"),
    ("杰夫", "对不起！", "Duìbuqǐ!", "Scusa!"),
    ("安妮", "没关系。再见！", "Méi guānxi. Zàijiàn!", "Non importa. Ciao!"),
  ], False),
  cloze=[],
  reorder=[],
  qa=[
    ("Quale di questi elementi è un’iniziale (声母)?", "", ["zh", "ai", "ong", "üe"], "zh è un’iniziale; ai, ong e üe sono finali."),
    ("Quale tono ha la sillaba 「马」 mǎ (cavallo)?", "mǎ", ["3° tono", "1° tono", "2° tono", "4° tono"], "Il segno ˇ indica il 3° tono."),
    ("Quale di queste sillabe ha il 4° tono?", "", ["bà", "bā", "bá", "bǎ"], "Il segno ˋ indica il 4° tono."),
    ("Quale coppia oppone un’iniziale non aspirata a una aspirata?", "", ["b – p", "m – f", "n – l", "s – sh"], "b si pronuncia senza soffio, p con un soffio d’aria."),
    ("Dove si scrive il segno del tono in una sillaba?", "", ["Sopra la vocale principale", "Sopra l’iniziale", "Alla fine della sillaba", "Non si scrive mai"], "Il tono va sempre sulla vocale principale."),
    ("Qualcuno ti dice 「谢谢！」. Cosa rispondi?", "xièxie!", ["不客气！", "对不起！", "你好！", "谢谢！"], "A 谢谢 si risponde 不客气 (prego)."),
    ("Come si saluta un compagno?", "", ["你好！", "再见！", "对不起！", "不客气！"], "你好 = ciao / buongiorno."),
  ],
  extra=[("Scioglilingua", "妈妈骑马", "妈妈骑马，马慢，妈妈骂马。", "Māma qí mǎ, mǎ màn, māma mà mǎ.",
          "La mamma va a cavallo, il cavallo è lento, la mamma sgrida il cavallo. (Ottimo per i toni di “ma”!)")],
)

# ───────────────────────────── Lezione 2 ─────────────────────────────
L(n=2, zh="汉语拼音（二）", py="Hànyǔ pīnyīn (èr)", it="Pinyin (2): finali composte, nasali, er",
  theme="Finali composte (ai, ao…), finali nasali (-n / -ng), la finale er e la retroflessione 儿化",
  vocab="""
N|多少钱|duōshao qián||quanto costa?|how much is it?
N|我听不懂|wǒ tīng bu dǒng||non capisco (ascoltando)|I don't understand
N|请再说一遍|qǐng zài shuō yí biàn||per favore, ripeti|please say it again
N|明白了|míngbai le||ho capito|I see
S|鸡蛋|jīdàn|名|uovo|egg
S|香蕉|xiāngjiāo|名|banana|banana
S|护照|hùzhào|名|passaporto|passport
S|跳舞|tiào wǔ||ballare|to dance
S|花儿|huār|名|fiore|flower
S|小孩儿|xiǎoháir|名|bambino|child
S|果汁儿|guǒzhīr|名|succo di frutta|juice
S|画儿|huàr|名|quadro, disegno|picture
""",
  grammar=[
    ("Finali composte", "ai ei ao ou · ia ie ua uo üe · iao iou uai uei: si scivola da una vocale all’altra senza pause.",
     [("买 / 美", "mǎi / měi", "comprare / bello")]),
    ("Finali nasali -n / -ng", "an en in un ün terminano con la lingua sui denti (n); ang eng ing ong con la parte posteriore della lingua (ng). Distinguerle è fondamentale: fān ≠ fāng.",
     [("三 / 桑", "sān / sāng", "tre / gelso")]),
    ("La finale er e il 儿化", "er si pronuncia arrotolando la lingua: 二 èr. Aggiunto ad altre sillabe (儿化) rende la finale retroflessa, tipico del nord: 玩儿 wánr, 一点儿 yìdiǎnr.",
     [("玩儿", "wánr", "giocare, divertirsi")]),
  ],
  dialogue=("In un negozio", [
    ("安妮", "多少钱？", "Duōshao qián?", "Quanto costa?"),
    ("售货员", "八块。", "Bā kuài.", "Otto yuan."),
    ("安妮", "对不起，我听不懂。请再说一遍。", "Duìbuqǐ, wǒ tīng bu dǒng. Qǐng zài shuō yí biàn.", "Scusi, non capisco. Può ripetere, per favore?"),
    ("售货员", "八块钱。", "Bā kuài qián.", "Otto yuan."),
    ("安妮", "明白了，谢谢！", "Míngbai le, xièxie!", "Ho capito, grazie!"),
  ], False),
  cloze=[],
  reorder=[
    ("请再说一遍。", "Qǐng zài shuō yí biàn.", "Per favore, ripeti.", ["请", "再", "说", "一遍", "。"]),
    ("我听不懂。", "Wǒ tīng bu dǒng.", "Non capisco.", ["我", "听", "不", "懂", "。"]),
  ],
  qa=[
    ("Quale di queste è una finale nasale?", "", ["ang", "ai", "ou", "ie"], "ang termina con il suono nasale -ng."),
    ("Quale parola ha la finale retroflessa (儿化)?", "", ["玩儿 wánr", "完 wán", "万 wàn", "晚 wǎn"], "Il 儿化 si scrive aggiungendo -r alla sillaba."),
    ("Quale coppia si distingue solo per -n / -ng?", "", ["fān – fāng", "fān – fēn", "fā – fān", "fāng – fēng"], "Solo fān/fāng cambia unicamente la nasale finale."),
    ("Vuoi chiedere il prezzo. Cosa dici?", "", ["多少钱？", "明白了。", "没关系。", "再见！"], "多少钱 = quanto costa?"),
    ("L’insegnante parla troppo veloce e vuoi che ripeta. Cosa dici?", "", ["请再说一遍。", "明白了。", "多少钱？", "不客气。"], "请再说一遍 = per favore, ripeti."),
    ("Qualcuno ti dice 「对不起！」. Cosa rispondi?", "duìbuqǐ!", ["没关系。", "不客气。", "谢谢！", "明白了。"], "A 对不起 si risponde 没关系 (non importa)."),
    ("「我听不懂。」 significa…", "wǒ tīng bu dǒng.", ["Non capisco (quello che sento).", "Non ti sento.", "Non voglio ascoltare.", "Ho capito."], "听不懂 = ascolto ma non capisco."),
  ],
  extra=[("Scioglilingua", "化肥会挥发", "化肥会挥发。黑化肥发灰，灰化肥发黑。", "Huàféi huì huīfā. Hēi huàféi fā huī, huī huàféi fā hēi.",
          "Il fertilizzante evapora. Il fertilizzante nero diventa grigio, quello grigio diventa nero. (Per distinguere f e h)")],
)

# ───────────────────────────── Lezione 3 ─────────────────────────────
L(n=3, zh="汉语拼音（三）", py="Hànyǔ pīnyīn (sān)", it="Pinyin (3): tono neutro, cambi tonali, ortografia",
  theme="Tono neutro, cambi di tono (3°+3°, 一, 不) e regole di scrittura del pinyin",
  vocab="""
N|太贵了|tài guì le||è troppo caro!|too expensive!
N|便宜一点儿吧|piányi yìdiǎnr ba||un po’ più economico?|a bit cheaper?
N|请等一会儿|qǐng děng yíhuìr||aspetta un momento, per favore|please wait a moment
N|这是什么|zhè shì shénme||che cos’è questo?|what is this?
N|厕所在哪儿|cèsuǒ zài nǎr||dov’è il bagno?|where is the toilet?
S|爷爷|yéye|名|nonno (paterno)|grandpa
S|奶奶|nǎinai|名|nonna (paterna)|grandma
S|窗户|chuānghu|名|finestra|window
S|豆腐|dòufu|名|tofu|tofu
S|木头|mùtou|名|legno|wood
S|也许|yěxǔ|副|forse|perhaps
""",
  grammar=[
    ("Il tono neutro (轻声)", "Alcune sillabe si pronunciano brevi e leggere, senza tono: non si scrive alcun segno. Succede spesso con la seconda sillaba ripetuta (妈妈 māma, 谢谢 xièxie) e con particelle come 的, 了, 吗, 呢.",
     [("妈妈", "māma", "mamma")]),
    ("Due terzi toni di seguito", "Quando due 3° toni si incontrano, il primo si pronuncia come 2° tono (ma si scrive sempre 3°).",
     [("你好", "nǐ hǎo → ní hǎo", "ciao")]),
    ("Il cambio di tono di 一", "一 si legge yī da solo o nei numeri; davanti a 1°, 2° e 3° tono diventa yì; davanti al 4° tono diventa yí. Nei libri spesso si scrive già il tono cambiato.",
     [("一天 · 一块", "yì tiān · yí kuài", "un giorno · un pezzo/yuan")]),
    ("Il cambio di tono di 不", "不 si legge bù, ma davanti a un 4° tono diventa bú.",
     [("不好 · 不去", "bù hǎo · bú qù", "non buono · non andare")]),
    ("Regole di ortografia", "Senza iniziale: i → yi, u → wu, ü → yu. Dopo j, q, x la ü si scrive u (ju, qu, xu); dopo l e n mantiene i puntini (lü, nü). iou, uei, uen dopo un’iniziale si accorciano in iu, ui, un (niú, guì, lùn). In iu e ui il tono va sulla seconda vocale.",
     [("绿 · 去 · 牛 · 会", "lǜ · qù · niú · huì", "verde · andare · mucca · sapere")]),
  ],
  dialogue=("Al mercato", [
    ("杰夫", "这是什么？", "Zhè shì shénme?", "Che cos’è questo?"),
    ("售货员", "这是豆腐。", "Zhè shì dòufu.", "È tofu."),
    ("杰夫", "多少钱？", "Duōshao qián?", "Quanto costa?"),
    ("售货员", "十块。", "Shí kuài.", "Dieci yuan."),
    ("杰夫", "太贵了！便宜一点儿吧！", "Tài guì le! Piányi yìdiǎnr ba!", "È troppo caro! Un po’ meno?"),
    ("售货员", "请等一会儿……八块，好吗？", "Qǐng děng yíhuìr…… Bā kuài, hǎo ma?", "Aspetti un momento… otto yuan, va bene?"),
  ], False),
  cloze=[
    ("太 ___ 了！", "Tài ___ le!", "È troppo caro!", ["贵", "是", "在", "叫"], "太贵了 = è troppo caro."),
    ("请 ___ 一会儿。", "Qǐng ___ yíhuìr.", "Aspetta un momento, per favore.", ["等", "是", "有", "叫"], "等 = aspettare."),
    ("这是 ___？", "Zhè shì ___?", "Che cos’è questo?", ["什么", "哪儿", "多少", "几"], "什么 = che cosa."),
  ],
  reorder=[
    ("厕所在哪儿？", "Cèsuǒ zài nǎr?", "Dov’è il bagno?", ["厕所", "在", "哪儿", "？"]),
    ("这是什么？", "Zhè shì shénme?", "Che cos’è questo?", ["这", "是", "什么", "？"]),
    ("便宜一点儿吧！", "Piányi yìdiǎnr ba!", "Un po’ più economico!", ["便宜", "一点儿", "吧", "！"]),
  ],
  qa=[
    ("Come si pronuncia 「你好」?", "nǐ hǎo", ["ní hǎo", "nǐ hǎo con due 3° toni pieni", "nī hǎo", "nì hǎo"], "Due 3° toni: il primo si pronuncia come 2° tono."),
    ("Come si pronuncia 「一天」 (un giorno)?", "yī tiān", ["yì tiān", "yí tiān", "yī tiān", "yǐ tiān"], "Davanti al 1° tono 一 diventa yì."),
    ("Come si pronuncia 「一块」 (uno yuan)?", "yī kuài", ["yí kuài", "yì kuài", "yī kuài", "yǐ kuài"], "Davanti al 4° tono 一 diventa yí."),
    ("Come si pronuncia 「不去」 (non andare)?", "bù qù", ["bú qù", "bù qù", "bū qù", "bǔ qù"], "Davanti al 4° tono 不 diventa bú."),
    ("Come si pronuncia 「不好」 (non buono)?", "bù hǎo", ["bù hǎo", "bú hǎo", "bū hǎo", "bǔ hǎo"], "Davanti al 3° tono 不 resta bù."),
    ("Come si scrive la sillaba “i” al 1° tono senza iniziale?", "", ["yī", "ī", "wī", "yū"], "Senza iniziale, i si scrive yi."),
    ("Come si scrive j + ü al 3° tono (举, alzare)?", "", ["jǔ", "jǚ", "jiǔ", "zhǔ"], "Dopo j, q, x i puntini della ü non si scrivono."),
    ("Come si scrive l + ü al 4° tono (绿, verde)?", "", ["lǜ", "lù", "liù", "lǚ"], "Dopo l e n la ü mantiene i puntini."),
    ("Come si scrive n + iou al 2° tono (牛, mucca)?", "", ["niú", "nióu", "nioú", "nú"], "iou dopo un’iniziale diventa iu; il tono va sulla u."),
    ("In quale parola la seconda sillaba ha il tono neutro?", "", ["妈妈 māma", "老师 lǎoshī", "今天 jīntiān", "学校 xuéxiào"], "Nei nomi di parentela ripetuti la seconda sillaba è neutra."),
    ("Il venditore chiede un prezzo troppo alto. Cosa dici?", "", ["太贵了！便宜一点儿吧！", "请等一会儿。", "明白了。", "厕所在哪儿？"], "太贵了 + 便宜一点儿吧 per contrattare."),
  ],
  extra=[("Scioglilingua", "粉红墙上画凤凰", "粉红墙上画凤凰。", "Fěnhóng qiáng shang huà fènghuáng.",
          "Sul muro rosa si dipinge una fenice. (Per f / h e le nasali)")],
)

# ───────────────────────────── Lezione 4 ─────────────────────────────
L(n=4, zh="你叫什么名字？", py="Nǐ jiào shénme míngzi?", it="Come ti chiami?",
  theme="Salutare, presentarsi, chiedere nome e cognome",
  vocab="""
N|你|nǐ|代|tu|you
N|叫|jiào|动|chiamarsi; chiamare|to be called
N|什么|shénme|代|che cosa, quale|what
N|名字|míngzi|名|nome|name
N|好|hǎo|形|buono, bene|good
N|我|wǒ|代|io, me|I, me
N|你们|nǐmen|代|voi|you (plural)
N|姓|xìng|名,动|cognome; chiamarsi di cognome|surname
N|您|nín|代|Lei (cortesia)|you (polite)
N|老师|lǎoshī|名|insegnante|teacher
N|呢|ne|助|particella interrogativa (“e tu?”)|question particle
N|是|shì|动|essere|to be
N|人|rén|名|persona|person
N|我们|wǒmen|代|noi|we, us
N|留学生|liúxuéshēng|名|studente straniero|international student
N|他|tā|代|lui|he
N|她|tā|代|lei|she
N|都|dōu|副|tutti, entrambi|all, both
N|的|de|助|particella possessiva / strutturale|structural particle
N|大家|dàjiā|代|tutti quanti|everybody
N|学生|xuésheng|名|studente|student
N|汉语|Hànyǔ|名|lingua cinese|Chinese language
P|中国|Zhōngguó||Cina|China
S|张|Zhāng|名|Zhang (cognome)|Zhang (surname)
S|李|Lǐ|名|Li (cognome)|Li (surname)
S|王|Wáng|名|Wang (cognome)|Wang (surname)
S|日本|Rìběn|名|Giappone|Japan
""",
  grammar=[
    ("你好！ / 您好！", "Saluto valido in ogni momento della giornata. 您 è la forma di cortesia: si usa con insegnanti e persone più grandi. Si risponde con lo stesso saluto.",
     [("您好，田老师！", "Nín hǎo, Tián lǎoshī!", "Buongiorno, professoressa Tian!")]),
    ("叫 e 姓", "叫 + nome completo (o nome): “chiamarsi”. 姓 + solo cognome: “avere come cognome”. Con persone più grandi non si chiede 你叫什么名字, ma il cognome.",
     [("我叫王平，我姓王。", "Wǒ jiào Wáng Píng, wǒ xìng Wáng.", "Mi chiamo Wang Ping, di cognome faccio Wang.")]),
    ("…呢？ (e tu?)", "Nome o pronome + 呢 forma una domanda breve che riprende la domanda precedente.",
     [("我是英国人，你呢？", "Wǒ shì Yīngguórén, nǐ ne?", "Io sono inglese, e tu?")]),
    ("都 (tutti)", "都 va dopo il soggetto (che deve essere plurale) e prima del verbo.",
     [("我们都是留学生。", "Wǒmen dōu shì liúxuéshēng.", "Siamo tutti studenti stranieri.")]),
    ("的 possessivo", "A 的 B = “il B di A”. Con persone vicine (famiglia, insegnanti, gruppi) il 的 spesso si omette: 我们老师.",
     [("她是我的老师。", "Tā shì wǒ de lǎoshī.", "Lei è la mia insegnante.")]),
  ],
  dialogue=("Il primo giorno, davanti alla biblioteca", [
    ("王平", "你好！", "Nǐ hǎo!", "Ciao!"),
    ("丽莎", "你好！你叫什么名字？", "Nǐ hǎo! Nǐ jiào shénme míngzi?", "Ciao! Come ti chiami?"),
    ("王平", "我叫王平，我是中国人。你呢？", "Wǒ jiào Wáng Píng, wǒ shì Zhōngguórén. Nǐ ne?", "Mi chiamo Wang Ping, sono cinese. E tu?"),
    ("丽莎", "我叫丽莎，是留学生。", "Wǒ jiào Lìshā, shì liúxuéshēng.", "Mi chiamo Lisa, sono una studentessa straniera."),
    ("王平", "你们的老师姓什么？", "Nǐmen de lǎoshī xìng shénme?", "Come si chiama di cognome la vostra insegnante?"),
    ("丽莎", "我们的老师姓田。", "Wǒmen de lǎoshī xìng Tián.", "La nostra insegnante si chiama Tian."),
  ]),
  reading=("Mi presento",
    "大家好！我叫山田，是日本人。我是留学生。他叫杰夫，她叫安妮。我们都是留学生。我们的老师姓田，她是中国人。",
    "Dàjiā hǎo! Wǒ jiào Shāntián, shì Rìběnrén. Wǒ shì liúxuéshēng. Tā jiào Jiéfū, tā jiào Ānnī. Wǒmen dōu shì liúxuéshēng. Wǒmen de lǎoshī xìng Tián, tā shì Zhōngguórén.",
    "Ciao a tutti! Mi chiamo Yamada, sono giapponese. Sono uno studente straniero. Lui si chiama Jeff, lei si chiama Annie. Siamo tutti studenti stranieri. La nostra insegnante si chiama Tian, è cinese.",
    [("老师姓什么？", "Lǎoshī xìng shénme?", ["姓田", "姓王", "姓张", "姓李"]),
     ("谁是日本人？", "Shéi shì Rìběnrén?", ["山田", "杰夫", "安妮", "田老师"]),
     ("山田是老师吗？", "Shāntián shì lǎoshī ma?", ["不是，他是留学生", "是，他是老师", "是，他是中国人", "不是，他是田老师"])]),
  cloze=[
    ("我 ___ 杰夫。", "Wǒ ___ Jiéfū.", "Mi chiamo Jeff.", ["叫", "姓", "的", "们"], "叫 + nome = chiamarsi."),
    ("我 ___ 田，我是你们的老师。", "Wǒ ___ Tián, wǒ shì nǐmen de lǎoshī.", "Di cognome faccio Tian, sono la vostra insegnante.", ["姓", "叫", "都", "的"], "姓 + cognome."),
    ("我是中国人，你 ___？", "Wǒ shì Zhōngguórén, nǐ ___?", "Io sono cinese, e tu?", ["呢", "的", "都", "们"], "呢 riprende la domanda: “e tu?”."),
    ("我们 ___ 是留学生。", "Wǒmen ___ shì liúxuéshēng.", "Siamo tutti studenti stranieri.", ["都", "呢", "的", "叫"], "都 = tutti, prima del verbo."),
    ("她是我们 ___ 老师。", "Tā shì wǒmen ___ lǎoshī.", "Lei è la nostra insegnante.", ["的", "都", "呢", "叫"], "的 indica il possesso."),
    ("___ 好，田老师！", "___ hǎo, Tián lǎoshī!", "Buongiorno, professoressa Tian! (cortese)", ["您", "我", "他", "她"], "您 è la forma di cortesia di 你."),
  ],
  reorder=[
    ("我叫安妮。", "Wǒ jiào Ānnī.", "Mi chiamo Annie.", ["我", "叫", "安妮", "。"]),
    ("你叫什么名字？", "Nǐ jiào shénme míngzi?", "Come ti chiami?", ["你", "叫", "什么", "名字", "？"]),
    ("我们都是留学生。", "Wǒmen dōu shì liúxuéshēng.", "Siamo tutti studenti stranieri.", ["我们", "都", "是", "留学生", "。"]),
    ("我们的老师姓田。", "Wǒmen de lǎoshī xìng Tián.", "La nostra insegnante si chiama Tian.", ["我们", "的", "老师", "姓", "田", "。"]),
    ("我叫王平，是中国人。", "Wǒ jiào Wáng Píng, shì Zhōngguórén.", "Mi chiamo Wang Ping, sono cinese.", ["我", "叫", "王平", "，", "是", "中国人", "。"]),
  ],
  qa=[
    ("Qualcuno ti saluta con 「你好！」. Cosa rispondi?", "nǐ hǎo!", ["你好！", "我好！", "好！", "是你好。"], "Al saluto 你好 si risponde con 你好."),
    ("Ti chiedono 「你叫什么名字？」. Qual è la risposta corretta?", "nǐ jiào shénme míngzi?", ["我叫杰夫。", "叫杰夫名字。", "是杰夫的。", "我姓杰夫。"], "Si risponde con 我叫 + nome."),
    ("「我叫杰夫，你呢？」 Che cosa ti stanno chiedendo?", "wǒ jiào Jiéfū, nǐ ne?", ["Come ti chiami.", "Come stai.", "Di che paese sei.", "Dove sei."], "呢 riprende la domanda: qui chiede il tuo nome."),
    ("Vuoi dire “Siamo tutti studenti stranieri”. Quale frase è corretta?", "", ["我们都是留学生。", "都我们是留学生。", "我们是都留学生。", "我们留学生都是。"], "都 va dopo il soggetto e prima del verbo."),
    ("Quale frase significa “Lei è la nostra insegnante”?", "", ["她是我们的老师。", "她是老师我们的。", "我们是她的老师。", "她的我们是老师。"], "A 的 B = “il B di A”."),
  ],
  extra=[("Scioglilingua", "八百标兵", "八百标兵奔北坡，炮兵并排北边跑。", "Bābǎi biāobīng bēn běi pō, pàobīng bìngpái běibiān pǎo.",
          "Ottocento soldati corrono verso il pendio a nord, gli artiglieri corrono in fila sul lato nord. (Per b / p)")],
)

# ───────────────────────────── Lezione 5 ─────────────────────────────
L(n=5, zh="你在几班？", py="Nǐ zài jǐ bān?", it="In che classe sei?",
  theme="Salutare al mattino, chiedere nazionalità, età e classe",
  vocab="""
N|在|zài|动,介|essere (in un luogo); in, a|to be at; at
N|几|jǐ|代|quanti? (numero piccolo)|how many
N|班|bān|名,量|classe|class
N|早上|zǎoshang|名|mattina presto|early morning
N|早|zǎo|形|presto; buongiorno!|early; morning!
N|哪|nǎ|代|quale|which
N|国|guó|名|paese, nazione|country
N|也|yě|副|anche|also
N|吗|ma|助|particella interrogativa (sì/no)|question particle
N|不|bù|副|non, no|not, no
N|谁|shéi|代|chi|who
N|对|duì|形|giusto, esatto|right, correct
N|多大|duō dà||quanti anni?|how old
N|十九|shíjiǔ|数|diciannove|nineteen
N|岁|suì|量|anni (di età)|years old
N|二十|èrshí|数|venti|twenty
N|一|yī|数|uno|one
N|二|èr|数|due|two
N|今年|jīnnián|名|quest’anno|this year
N|他们|tāmen|代|loro|they
N|上午|shàngwǔ|名|mattina|morning
N|晚上|wǎnshang|名|sera|evening
N|下午|xiàwǔ|名|pomeriggio|afternoon
N|男|nán|形|maschio, maschile|male
P|美国|Měiguó||Stati Uniti|USA
P|法国|Fǎguó||Francia|France
P|英国|Yīngguó||Regno Unito|UK
S|韩国|Hánguó|名|Corea del Sud|South Korea
S|德国|Déguó|名|Germania|Germany
S|女|nǚ|形|femmina, femminile|female
""",
  grammar=[
    ("早上好！ / 早！", "Saluto del mattino (di solito fino alle 10). Si risponde allo stesso modo. Nello stesso modo: 上午好、下午好、晚上好.",
     [("早上好，彼得！——早！", "Zǎoshang hǎo, Bǐdé! — Zǎo!", "Buongiorno, Peter! — Buongiorno!")]),
    ("Domande con 吗", "Frase affermativa + 吗 = domanda sì/no. Per rispondere: 是 / 对 (sì), 不 + verbo (no).",
     [("你是美国人吗？——不，我是法国人。", "Nǐ shì Měiguórén ma? — Bù, wǒ shì Fǎguórén.", "Sei americano? — No, sono francese.")]),
    ("多大 e 几", "你多大 chiede l’età a coetanei o più giovani. 几 chiede un numero piccolo (di solito sotto il 10): 几班? 几点? Per l’età si dice numero + 岁, senza 是.",
     [("你多大？——我二十岁。", "Nǐ duō dà? — Wǒ èrshí suì.", "Quanti anni hai? — Ho vent’anni."),
      ("你在几班？——我在二班。", "Nǐ zài jǐ bān? — Wǒ zài èr bān.", "In che classe sei? — Sono nella classe 2.")]),
    ("也 (anche)", "也 va sempre dopo il soggetto e prima del verbo: 我也是… Non si dice “也我”.",
     [("我也在二班。", "Wǒ yě zài èr bān.", "Anch’io sono nella classe 2.")]),
    ("I numeri fino a 100", "11 = 十一, 15 = 十五, 20 = 二十, 35 = 三十五, 99 = 九十九, 100 = 一百. Basta combinare decine (numero + 十) e unità.",
     [("十九、二十、二十一", "shíjiǔ, èrshí, èrshíyī", "19, 20, 21")]),
  ],
  dialogue=("Prima della lezione, nel corridoio", [
    ("山田", "早上好！", "Zǎoshang hǎo!", "Buongiorno!"),
    ("丽莎", "早！你是日本人吗？", "Zǎo! Nǐ shì Rìběnrén ma?", "Buongiorno! Sei giapponese?"),
    ("山田", "对，我是日本人。你呢？", "Duì, wǒ shì Rìběnrén. Nǐ ne?", "Sì, sono giapponese. E tu?"),
    ("丽莎", "我是德国人。你在几班？", "Wǒ shì Déguórén. Nǐ zài jǐ bān?", "Sono tedesca. In che classe sei?"),
    ("山田", "二班。你也在二班吗？", "Èr bān. Nǐ yě zài èr bān ma?", "Classe 2. Anche tu sei nella classe 2?"),
    ("丽莎", "不，我在一班。", "Bù, wǒ zài yī bān.", "No, sono nella classe 1."),
  ]),
  reading=("Tre compagni",
    "安妮今年十九岁，她是美国人。杰夫是英国人，今年二十岁。他们都在二班。彼得是法国人，他也十九岁，他在一班。",
    "Ānnī jīnnián shíjiǔ suì, tā shì Měiguórén. Jiéfū shì Yīngguórén, jīnnián èrshí suì. Tāmen dōu zài èr bān. Bǐdé shì Fǎguórén, tā yě shíjiǔ suì, tā zài yī bān.",
    "Annie quest’anno ha diciannove anni, è americana. Jeff è inglese e ha vent’anni. Sono entrambi nella classe 2. Peter è francese, anche lui ha diciannove anni, ed è nella classe 1.",
    [("安妮是哪国人？", "Ānnī shì nǎ guó rén?", ["美国人", "英国人", "法国人", "日本人"]),
     ("杰夫多大？", "Jiéfū duō dà?", ["二十岁", "十九岁", "二十一岁", "十八岁"]),
     ("谁在一班？", "Shéi zài yī bān?", ["彼得", "安妮", "杰夫", "安妮和杰夫"])]),
  cloze=[
    ("你是美国人 ___？", "Nǐ shì Měiguórén ___?", "Sei americano?", ["吗", "呢", "的", "都"], "吗 a fine frase = domanda sì/no."),
    ("我是英国人，他 ___ 是英国人。", "Wǒ shì Yīngguórén, tā ___ shì Yīngguórén.", "Io sono inglese, anche lui è inglese.", ["也", "不", "吗", "的"], "也 = anche, prima del verbo."),
    ("你在 ___ 班？", "Nǐ zài ___ bān?", "In che classe sei?", ["几", "多", "谁", "吗"], "几 chiede un numero piccolo."),
    ("我今年二十 ___。", "Wǒ jīnnián èrshí ___.", "Quest’anno ho vent’anni.", ["岁", "班", "国", "人"], "岁 = anni di età."),
    ("你 ___ 大？", "Nǐ ___ dà?", "Quanti anni hai?", ["多", "几", "谁", "哪"], "多大 chiede l’età."),
    ("你是 ___ 国人？", "Nǐ shì ___ guó rén?", "Di che nazionalità sei?", ["哪", "几", "谁", "多"], "哪国人 = di quale paese."),
    ("他 ___ 谁？", "Tā ___ shéi?", "Chi è lui?", ["是", "在", "叫", "也"], "是 = essere."),
  ],
  reorder=[
    ("你是哪国人？", "Nǐ shì nǎ guó rén?", "Di che paese sei?", ["你", "是", "哪", "国", "人", "？"]),
    ("我也在二班。", "Wǒ yě zài èr bān.", "Anch’io sono nella classe 2.", ["我", "也", "在", "二班", "。"]),
    ("他们都在一班。", "Tāmen dōu zài yī bān.", "Sono tutti nella classe 1.", ["他们", "都", "在", "一班", "。"]),
    ("我今年十九岁。", "Wǒ jīnnián shíjiǔ suì.", "Quest’anno ho diciannove anni.", ["我", "今年", "十九", "岁", "。"]),
    ("你也是法国人吗？", "Nǐ yě shì Fǎguórén ma?", "Anche tu sei francese?", ["你", "也", "是", "法国人", "吗", "？"]),
  ],
  qa=[
    ("Ti chiedono 「你也是美国人吗？」 e sei americano. Cosa rispondi?", "nǐ yě shì Měiguórén ma?", ["对，我是。", "我也。", "也是。", "是也。"], "Per confermare: 对，我是 / 是，我也是美国人."),
    ("Ti chiedono 「你多大？」. Qual è la risposta corretta?", "nǐ duō dà?", ["我二十岁。", "我是二十。", "是二十岁。", "我二十个。"], "Età: 我 + numero + 岁, senza 是."),
    ("Ti chiedono 「他是谁？」. Qual è la risposta adatta?", "tā shì shéi?", ["他是我的老师。", "他二十岁。", "他在二班。", "他是好。"], "谁 chiede chi è la persona."),
    ("Quale frase significa “Sono nella classe 3”?", "", ["我在三班。", "我是三班在。", "我三班在。", "在我三班。"], "在 + classe/luogo = trovarsi in."),
    ("La risposta è 「我是法国人。」. Qual era la domanda?", "wǒ shì Fǎguórén.", ["你是哪国人？", "你多大？", "你在几班？", "你叫什么名字？"], "Si chiedeva la nazionalità."),
    ("Come si dice 35?", "", ["三十五", "五十三", "三五", "三十和五"], "Decine (三十) + unità (五)."),
  ],
  extra=[("Scioglilingua", "四是四", "四是四，十是十，十四是十四，四十是四十。", "Sì shì sì, shí shì shí, shísì shì shísì, sìshí shì sìshí.",
          "Quattro è quattro, dieci è dieci, quattordici è quattordici, quaranta è quaranta. (Per sì / shí)"),
         ("Cultura", "Nomi cinesi", "", "",
          "In cinese il cognome viene prima del nome: in 王平, Wang è il cognome e Ping il nome. Quasi tutti i cognomi hanno un solo carattere (王, 李, 张, 刘, 陈…), pochi ne hanno due (欧阳, 司马). Ai bambini si danno spesso nomignoli con il carattere ripetuto (明明) o con 小 davanti (小王).")],
)

# ───────────────────────────── Lezione 6 ─────────────────────────────
L(n=6, zh="现在几点？", py="Xiànzài jǐ diǎn?", it="Che ore sono?",
  theme="Dire l’ora, i giorni della settimana, l’orario delle lezioni",
  vocab="""
N|现在|xiànzài|名|adesso|now
N|点|diǎn|量,名,动|ora (in punto); punto; ordinare (cibo)|o'clock; to order
N|七|qī|数|sette|seven
N|半|bàn|数|mezzo|half
N|今天|jīntiān|名|oggi|today
N|星期|xīngqī|名|settimana|week
N|八|bā|数|otto|eight
N|没有|méiyǒu|动,副|non avere; non (azione passata)|not have; did not
N|课|kè|名|lezione|class, lesson
N|明天|míngtiān|名|domani|tomorrow
N|有|yǒu|动|avere; esserci|to have; there is
N|上课|shàng kè||andare a lezione, fare lezione|to attend class
N|从……到……|cóng…dào…||da… a…|from… to…
N|九|jiǔ|数|nove|nine
N|五十|wǔshí|数|cinquanta|fifty
N|分|fēn|量,名|minuto; fen (centesimo)|minute; fen
N|口语|kǒuyǔ|名|lingua parlata|spoken language
N|差|chà|动|mancare (per l’ora)|to be short of
N|两|liǎng|数|due (davanti a classificatore)|two
N|该……了|gāi…le||è ora di…|it's time to…
N|再见|zàijiàn|动|arrivederci|goodbye
N|刻|kè|量|quarto d’ora|quarter (hour)
N|钱|qián|名|soldi|money
N|时间|shíjiān|名|tempo|time
N|听力|tīnglì|名|ascolto, comprensione orale|listening
N|汉字|Hànzì|名|carattere cinese|Chinese character
N|下课|xià kè||finire la lezione|class is over
N|起床|qǐ chuáng||alzarsi dal letto|to get up
N|睡觉|shuì jiào||dormire, andare a letto|to sleep
S|手表|shǒubiǎo|名|orologio da polso|watch
S|中文|Zhōngwén|名|cinese (lingua)|Chinese
S|吃饭|chī fàn||mangiare (un pasto)|to have a meal
""",
  grammar=[
    ("Dire l’ora", "点 = ora, 分 = minuti, 半 = mezza, 刻 = quarto, 差 = manca. 8:00 八点 · 8:05 八点零五分 · 8:15 八点一刻 · 8:30 八点半 · 8:45 八点三刻 o 差一刻九点 · 8:55 差五分九点.",
     [("现在七点半。", "Xiànzài qī diǎn bàn.", "Ora sono le sette e mezza."),
      ("差两分九点。", "Chà liǎng fēn jiǔ diǎn.", "Mancano due minuti alle nove.")]),
    ("今天星期几？", "I giorni: 星期一 (lunedì) … 星期六 (sabato), 星期天 / 星期日 (domenica). Davanti a date e giorni il 是 si può omettere.",
     [("今天星期几？——今天星期二。", "Jīntiān xīngqī jǐ? — Jīntiān xīngqī’èr.", "Che giorno è oggi? — Oggi è martedì.")]),
    ("从……到……", "“da… a…”: per intervalli di tempo o di spazio.",
     [("我从八点到十点有课。", "Wǒ cóng bā diǎn dào shí diǎn yǒu kè.", "Ho lezione dalle otto alle dieci.")]),
    ("二 e 两", "Per contare e nei numeri si usa 二 (一、二、三; 十二; 二十). Davanti a un classificatore si usa 两: 两点, 两个人, 两天.",
     [("两点上课。", "Liǎng diǎn shàng kè.", "La lezione è alle due.")]),
    ("该……了", "“È ora di…”: 该 + verbo + 了, secondo l’orario o il buon senso.",
     [("十二点了，该睡觉了。", "Shí’èr diǎn le, gāi shuì jiào le.", "È mezzanotte, è ora di dormire.")]),
    ("没有", "La negazione di 有 è sempre 没有, mai 不有.",
     [("今天上午我没有课。", "Jīntiān shàngwǔ wǒ méiyǒu kè.", "Stamattina non ho lezione.")]),
  ],
  dialogue=("In dormitorio, la mattina", [
    ("杰夫", "彼得，现在几点？", "Bǐdé, xiànzài jǐ diǎn?", "Peter, che ore sono?"),
    ("彼得", "八点一刻。", "Bā diǎn yí kè.", "Le otto e un quarto."),
    ("杰夫", "今天星期几？", "Jīntiān xīngqī jǐ?", "Che giorno è oggi?"),
    ("彼得", "星期二。你有课吗？", "Xīngqī’èr. Nǐ yǒu kè ma?", "Martedì. Hai lezione?"),
    ("杰夫", "有，我九点有听力课。", "Yǒu, wǒ jiǔ diǎn yǒu tīnglìkè.", "Sì, alle nove ho lezione di ascolto."),
    ("彼得", "你该起床了！", "Nǐ gāi qǐ chuáng le!", "È ora che ti alzi!"),
  ]),
  reading=("La giornata di Lisa",
    "今天是星期二。上午丽莎从八点到九点五十有口语课，十点到十一点五十有汉字课。下午她没有课。晚上十一点半她睡觉。",
    "Jīntiān shì xīngqī’èr. Shàngwǔ Lìshā cóng bā diǎn dào jiǔ diǎn wǔshí yǒu kǒuyǔkè, shí diǎn dào shíyī diǎn wǔshí yǒu Hànzìkè. Xiàwǔ tā méiyǒu kè. Wǎnshang shíyī diǎn bàn tā shuì jiào.",
    "Oggi è martedì. La mattina Lisa ha lezione di lingua parlata dalle 8:00 alle 9:50 e lezione di caratteri dalle 10:00 alle 11:50. Il pomeriggio non ha lezione. La sera va a dormire alle 11:30.",
    [("今天星期几？", "Jīntiān xīngqī jǐ?", ["星期二", "星期天", "星期一", "星期六"]),
     ("丽莎几点有汉字课？", "Lìshā jǐ diǎn yǒu Hànzìkè?", ["十点", "八点", "两点", "十一点半"]),
     ("下午丽莎有课吗？", "Xiàwǔ Lìshā yǒu kè ma?", ["没有课", "有口语课", "有汉字课", "有听力课"]),
     ("丽莎几点睡觉？", "Lìshā jǐ diǎn shuì jiào?", ["十一点半", "十点", "九点五十", "八点"])]),
  cloze=[
    ("现在七点 ___。(7:30)", "Xiànzài qī diǎn ___.", "Ora sono le sette e mezza.", ["半", "刻", "分", "差"], "半 = mezza."),
    ("现在 ___ 五分十点。(9:55)", "Xiànzài ___ wǔ fēn shí diǎn.", "Mancano cinque minuti alle dieci.", ["差", "半", "刻", "有"], "差 + minuti + ora = mancano…"),
    ("我 ___ 八点到十点有课。", "Wǒ ___ bā diǎn dào shí diǎn yǒu kè.", "Ho lezione dalle otto alle dieci.", ["从", "在", "有", "该"], "从……到…… = da… a…"),
    ("现在 ___ 点。(2:00)", "Xiànzài ___ diǎn.", "Ora sono le due.", ["两", "二", "双", "俩"], "Davanti a 点 si usa 两, non 二."),
    ("今天上午我 ___ 课。", "Jīntiān shàngwǔ wǒ ___ kè.", "Stamattina non ho lezione.", ["没有", "不有", "不是", "没是"], "La negazione di 有 è 没有."),
    ("十二点了，该睡觉 ___。", "Shí’èr diǎn le, gāi shuì jiào ___.", "È mezzanotte, è ora di dormire.", ["了", "吗", "呢", "的"], "该……了 = è ora di…"),
    ("今天星期 ___？", "Jīntiān xīngqī ___?", "Che giorno della settimana è oggi?", ["几", "什么", "多", "谁"], "星期几 chiede il giorno."),
  ],
  reorder=[
    ("现在几点？", "Xiànzài jǐ diǎn?", "Che ore sono?", ["现在", "几", "点", "？"]),
    ("明天你有课吗？", "Míngtiān nǐ yǒu kè ma?", "Domani hai lezione?", ["明天", "你", "有", "课", "吗", "？"]),
    ("你该上课了。", "Nǐ gāi shàng kè le.", "È ora che tu vada a lezione.", ["你", "该", "上课", "了", "。"]),
    ("今天八点我没有课。", "Jīntiān bā diǎn wǒ méiyǒu kè.", "Oggi alle otto non ho lezione.", ["今天", "八点", "我", "没有", "课", "。"]),
    ("下午从两点到三点五十有听力课。", "Xiàwǔ cóng liǎng diǎn dào sān diǎn wǔshí yǒu tīnglìkè.", "Il pomeriggio c’è lezione di ascolto dalle 2:00 alle 3:50.",
     ["下午", "从", "两点", "到", "三点五十", "有", "听力课", "。"]),
  ],
  qa=[
    ("Ti chiedono 「现在几点？」 e sono le 2:00. Cosa rispondi?", "xiànzài jǐ diǎn?", ["两点。", "二点。", "两个点。", "二个点。"], "Davanti a 点 si dice 两."),
    ("Ti chiedono 「今天星期几？」. Qual è la risposta corretta?", "jīntiān xīngqī jǐ?", ["星期二。", "星期两。", "二星期。", "星期是二。"], "Giorni: 星期 + numero (二, non 两)."),
    ("Ti chiedono 「明天你有课吗？」 e non hai lezione. Cosa rispondi?", "míngtiān nǐ yǒu kè ma?", ["没有课。", "不有课。", "不课。", "没课有。"], "La negazione di 有 è 没有."),
    ("Che ore sono quando senti 「差一刻九点」?", "chà yí kè jiǔ diǎn", ["8:45", "9:15", "9:45", "8:15"], "Manca un quarto alle nove."),
    ("Sono le 23:30 e domani hai lezione presto. Cosa ti dice il compagno?", "", ["你该睡觉了。", "你该起床了。", "你该上课了。", "你该下课了。"], "该 + verbo + 了: è ora di dormire."),
    ("Come si dice 1:15?", "", ["一点一刻", "一点半", "一刻一点", "差一刻一点"], "一刻 = un quarto d’ora."),
  ],
  extra=[("Poesia", "静夜思 · 李白", "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
          "Chuáng qián míngyuè guāng, yí shì dì shang shuāng. Jǔ tóu wàng míngyuè, dī tóu sī gùxiāng.",
          "Davanti al letto la luce chiara della luna: sembra brina sul pavimento. Alzo il capo e guardo la luna, abbasso il capo e penso al mio paese.")],
)

# ───────────────────────────── Lezione 7 ─────────────────────────────
L(n=7, zh="食堂在哪儿？", py="Shítáng zài nǎr?", it="Dov’è la mensa?",
  theme="Chiedere e indicare un luogo, ringraziare; posizione (destra, sinistra, accanto)",
  vocab="""
N|食堂|shítáng|名|mensa|canteen
N|哪儿|nǎr|代|dove|where
N|请问|qǐngwèn|动|scusi, posso chiedere…|excuse me
N|三|sān|数|tre|three
N|教室|jiàoshì|名|aula|classroom
N|这儿|zhèr|代|qui|here
N|谢谢|xièxie|动|grazie|thanks
N|不用|búyòng|副|non serve|no need
N|那儿|nàr|代|lì, là|there
N|边|biān|名|lato (suffisso di luogo)|side
N|宿舍|sùshè|名|dormitorio|dormitory
N|旁边|pángbiān|名|accanto|beside
N|厕所|cèsuǒ|名|bagno, toilette|toilet
N|这个|zhège||questo|this one
N|右边|yòubian|名|a destra|right side
N|那个|nàge||quello|that one
N|左边|zuǒbian|名|a sinistra|left side
N|这|zhè|代|questo|this
N|学校|xuéxiào|名|scuola|school
N|很|hěn|副|molto|very
N|大|dà|形|grande|big
N|地方|dìfang|名|posto, luogo|place
N|那|nà|代,连|quello; allora|that; then
N|书|shū|名|libro|book
N|小|xiǎo|形|piccolo; leggero|small
N|多|duō|形,代|molto, tanti; quanto (多大, 多长)|many; how
S|笔|bǐ|名|penna|pen
S|下边|xiàbian|名|sotto|below
""",
  grammar=[
    ("请问", "“Scusi, posso chiedere…?”: si mette all’inizio di una domanda per essere cortesi.",
     [("请问，厕所在哪儿？", "Qǐngwèn, cèsuǒ zài nǎr?", "Scusi, dov’è il bagno?")]),
    ("谢谢 → 不用谢", "A 谢谢 si risponde 不用谢 o 不客气 (“non c’è di che”).",
     [("谢谢你！——不用谢。", "Xièxie nǐ! — Búyòng xiè.", "Grazie! — Non c’è di che.")]),
    ("旁边、左边、右边", "Per dire dove si trova qualcosa: cosa + 在 + riferimento + (的) + 旁边/左边/右边/上边/下边. Si dice 宿舍的旁边, non 宿舍的旁.",
     [("食堂在宿舍的旁边。", "Shítáng zài sùshè de pángbiān.", "La mensa è accanto al dormitorio.")]),
    ("这、那、哪 / 这儿、那儿、哪儿", "这 = questo (vicino), 那 = quello (lontano), 哪 = quale? Con 儿 indicano luoghi: 这儿 (qui), 那儿 (lì), 哪儿 (dove?). Davanti a un classificatore si dice spesso zhèi, nèi, něi.",
     [("这是教室，那是宿舍。", "Zhè shì jiàoshì, nà shì sùshè.", "Questa è l’aula, quello è il dormitorio.")]),
    ("很 + aggettivo", "Quando l’aggettivo è il predicato non si usa 是, ma di solito 很: 学校很大 (non “学校是大”).",
     [("我们的学校很大。", "Wǒmen de xuéxiào hěn dà.", "La nostra scuola è molto grande.")]),
  ],
  dialogue=("Nel campus, il primo giorno", [
    ("彼得", "请问，留学生宿舍在哪儿？", "Qǐngwèn, liúxuéshēng sùshè zài nǎr?", "Scusa, dov’è il dormitorio degli studenti stranieri?"),
    ("一学生", "在那儿，食堂的左边。", "Zài nàr, shítáng de zuǒbian.", "È lì, a sinistra della mensa."),
    ("彼得", "厕所呢？", "Cèsuǒ ne?", "E il bagno?"),
    ("一学生", "在这个教室的右边。", "Zài zhège jiàoshì de yòubian.", "A destra di quest’aula."),
    ("彼得", "谢谢你！", "Xièxie nǐ!", "Grazie!"),
    ("一学生", "不用谢。", "Búyòng xiè.", "Non c’è di che."),
  ]),
  reading=("La classe di Piao Zhiyong",
    "朴志永在三班。三班的教室不大，在二班教室的右边。留学生食堂很大，在宿舍的旁边。厕所在教室的左边。",
    "Piáo Zhìyǒng zài sān bān. Sān bān de jiàoshì bú dà, zài èr bān jiàoshì de yòubian. Liúxuéshēng shítáng hěn dà, zài sùshè de pángbiān. Cèsuǒ zài jiàoshì de zuǒbian.",
    "Piao Zhiyong è nella classe 3. L’aula della classe 3 non è grande, è a destra dell’aula della classe 2. La mensa degli studenti stranieri è molto grande, è accanto al dormitorio. Il bagno è a sinistra delle aule.",
    [("朴志永在几班？", "Piáo Zhìyǒng zài jǐ bān?", ["三班", "二班", "一班", "四班"]),
     ("三班的教室大吗？", "Sān bān de jiàoshì dà ma?", ["不大", "很大", "在食堂", "在宿舍"]),
     ("食堂在哪儿？", "Shítáng zài nǎr?", ["宿舍的旁边", "教室的左边", "二班的右边", "三班的教室"])]),
  cloze=[
    ("___，厕所在哪儿？", "___, cèsuǒ zài nǎr?", "Scusi, dov’è il bagno?", ["请问", "谢谢", "不用", "再见"], "请问 introduce una domanda cortese."),
    ("谢谢你！——___ 谢。", "Xièxie nǐ! — ___ xiè.", "Grazie! — Non c’è di che.", ["不用", "没有", "不是", "请问"], "不用谢 = non c’è di che."),
    ("食堂在宿舍 ___ 旁边。", "Shítáng zài sùshè ___ pángbiān.", "La mensa è accanto al dormitorio.", ["的", "是", "很", "都"], "Riferimento + 的 + 旁边."),
    ("我们的学校 ___ 大。", "Wǒmen de xuéxiào ___ dà.", "La nostra scuola è molto grande.", ["很", "是", "在", "都"], "Aggettivo predicato: 很 + aggettivo, senza 是."),
    ("请问，三班的教室在 ___？", "Qǐngwèn, sān bān de jiàoshì zài ___?", "Scusi, dov’è l’aula della classe 3?", ["哪儿", "这儿", "那儿", "几"], "哪儿 = dove?"),
    ("厕所不在 ___，在那儿。", "Cèsuǒ bú zài ___, zài nàr.", "Il bagno non è qui, è lì.", ["这儿", "哪儿", "那儿", "什么"], "这儿 = qui, 那儿 = lì."),
  ],
  reorder=[
    ("请问，食堂在哪儿？", "Qǐngwèn, shítáng zài nǎr?", "Scusi, dov’è la mensa?", ["请问", "，", "食堂", "在", "哪儿", "？"]),
    ("厕所在教室的右边。", "Cèsuǒ zài jiàoshì de yòubian.", "Il bagno è a destra dell’aula.", ["厕所", "在", "教室", "的", "右边", "。"]),
    ("这是我们的学校。", "Zhè shì wǒmen de xuéxiào.", "Questa è la nostra scuola.", ["这", "是", "我们", "的", "学校", "。"]),
    ("那个地方很大。", "Nàge dìfang hěn dà.", "Quel posto è molto grande.", ["那个", "地方", "很", "大", "。"]),
    ("宿舍在食堂的左边。", "Sùshè zài shítáng de zuǒbian.", "Il dormitorio è a sinistra della mensa.", ["宿舍", "在", "食堂", "的", "左边", "。"]),
  ],
  qa=[
    ("Qualcuno ti dice 「谢谢你！」. Cosa rispondi?", "xièxie nǐ!", ["不用谢。", "不谢谢。", "没有谢。", "谢谢你。"], "不用谢 = non c’è di che."),
    ("Ti chiedono 「你们的学校大吗？」. Qual è la risposta corretta?", "nǐmen de xuéxiào dà ma?", ["很大。", "是大。", "大是。", "很是大。"], "Aggettivo predicato con 很, senza 是."),
    ("Ti chiedono 「请问，二班的教室在这儿吗？」 ed è proprio qui. Cosa rispondi?", "qǐngwèn, èr bān de jiàoshì zài zhèr ma?", ["对，在这儿。", "这儿是。", "是这儿在。", "在哪儿。"], "Si conferma con 对，在这儿."),
    ("Quale frase significa “La penna è sotto il libro”?", "", ["笔在书的下边。", "书在笔的下边。", "笔是书的下边。", "笔在下边书的。"], "Cosa + 在 + riferimento + 的 + 下边."),
    ("La risposta è 「在那个教室的旁边。」. Qual era la domanda?", "zài nàge jiàoshì de pángbiān.", ["厕所在哪儿？", "这是什么？", "你是哪国人？", "现在几点？"], "Si chiedeva un luogo (哪儿)."),
  ],
  extra=[("Poesia", "春晓 · 孟浩然", "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
          "Chūn mián bù jué xiǎo, chùchù wén tí niǎo. Yè lái fēng yǔ shēng, huā luò zhī duōshǎo.",
          "Nel sonno di primavera non mi accorgo dell’alba; ovunque sento cantare gli uccelli. Stanotte il rumore di vento e pioggia: chissà quanti fiori sono caduti."),
         ("Scioglilingua", "和尚端汤", "和尚端汤上塔，塔滑汤洒汤烫塔。", "Héshang duān tāng shàng tǎ, tǎ huá tāng sǎ tāng tàng tǎ.",
          "Il monaco porta la zuppa sulla pagoda; la pagoda è scivolosa, la zuppa si rovescia e scotta la pagoda.")],
)
