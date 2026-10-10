# -*- coding: utf-8 -*-
"""Lezioni 8-13 (formato descritto in lessons_a.py)."""

LESSONS = []
L = lambda **kw: LESSONS.append(kw)

# ───────────────────────────── Lezione 8 ─────────────────────────────
L(n=8, zh="一共多少钱？", py="Yígòng duōshao qián?", it="Quanto costa in tutto?",
  theme="Fare acquisti: prezzi, colori, classificatori e azioni compiute",
  vocab="""
N|一共|yígòng|副|in tutto, complessivamente|altogether
N|多少|duōshao|代|quanto, quanti|how many, how much
N|服务员|fúwùyuán|名|cameriere, addetto|waiter, attendant
N|要|yào|助动,动|volere; dovere; aver bisogno di|to want, need
N|哪个|nǎge||quale|which one
N|菜|cài|名|piatto, pietanza; verdura|dish
N|块|kuài|量|kuai (= yuan, unità monetaria)|yuan (RMB unit)
N|毛|máo|量|mao (1/10 di yuan, = 角 jiǎo)|jiao, 1/10 yuan
N|还|hái|副|ancora; inoltre, anche|also, in addition
N|那边|nàbiān|代|di là, da quella parte|over there
N|四|sì|数|quattro|four
N|买|mǎi|动|comprare|to buy
N|种|zhǒng|量|tipo, genere|kind, type
N|自行车|zìxíngchē|名|bicicletta|bicycle
N|颜色|yánsè|名|colore|colour
N|黑|hēi|形|nero|black
N|怎么样|zěnmeyàng|代|come?, che ne dici?|how about
N|喜欢|xǐhuan|动|piacere, amare|to like
N|蓝色|lánsè|名|(colore) blu|blue colour
N|车|chē|名|veicolo, auto, bici|vehicle
N|蓝|lán|形|blu|blue
N|售货员|shòuhuòyuán|名|commesso|shop assistant
N|辆|liàng|量|classificatore per veicoli|MW for vehicles
N|百|bǎi|数|cento|hundred
N|看|kàn|动|guardare; leggere|to look at
N|了|le|助|particella di azione compiuta / cambiamento|aspect particle
N|花|huā|动|spendere (soldi, tempo)|to spend
N|本|běn|量|classificatore per libri|MW for books
N|鞋|xié|名|scarpe|shoes
N|件|jiàn|量|classificatore per vestiti, regali, faccende|MW for clothes, matters
N|衣服|yīfu|名|vestiti|clothes
N|喝|hē|动|bere|to drink
N|茶|chá|名|tè|tea
S|支|zhī|量|classificatore per penne|MW for pens
S|双|shuāng|量|paio|pair
S|白|bái|形|bianco|white
S|面包|miànbāo|名|pane|bread
S|杯|bēi|量|tazza, bicchiere|cup, glass
""",
  grammar=[
    ("La moneta cinese (人民币)", "Nel parlato si usano 块 e 毛, nello scritto 元 e 角: 1 块 = 10 毛. Il prezzo si legge unità per unità; l’ultima si può omettere: ¥7,50 = 七块五 (毛); ¥15,40 = 十五块四; ¥2,05 = 两块零五分. Davanti a 块 si dice 两, non 二.",
     [("这个菜八块五。", "Zhège cài bā kuài wǔ.", "Questo piatto costa 8,50 yuan."),
      ("一共两块钱。", "Yígòng liǎng kuài qián.", "In tutto sono due yuan.")]),
    ("Le centinaia", "百 = cento. 340 = 三百四十; 105 = 一百零五 (lo zero in mezzo si dice 零); 200 = 二百 o, nel parlato, 两百.",
     [("这辆自行车三百四十块。", "Zhè liàng zìxíngchē sānbǎi sìshí kuài.", "Questa bicicletta costa 340 yuan.")]),
    ("La struttura con 的 (“quello…”)", "Aggettivo / pronome / luogo + 的 sostituisce un nome già chiaro dal contesto: 黑的 (quello nero), 我的 (il mio), 右边的 (quello a destra).",
     [("黑的、蓝的都有。", "Hēi de, lán de dōu yǒu.", "Ci sono sia quelli neri sia quelli blu."),
      ("我要右边的。", "Wǒ yào yòubian de.", "Voglio quello a destra.")]),
    ("I classificatori (量词)", "Tra numero (o 这 / 那 / 哪) e nome serve un classificatore: 个 è generico, 辆 per veicoli, 种 per tipi, 本 per libri, 件 per vestiti, 双 per paia, 支 per penne, 杯 per bicchieri e tazze.",
     [("一辆自行车", "yí liàng zìxíngchē", "una bicicletta"),
      ("这种车", "zhè zhǒng chē", "questo tipo di bici"),
      ("两本书、一杯茶", "liǎng běn shū, yì bēi chá", "due libri, una tazza di tè")]),
    ("Verbo + 了: azione compiuta", "了 dopo il verbo indica che l’azione è conclusa; spesso è seguito da numero + classificatore + oggetto. La negazione è 没(有) + verbo, senza 了.",
     [("我买了一辆蓝的。", "Wǒ mǎile yí liàng lán de.", "Ne ho comprata una blu."),
      ("我没有买。", "Wǒ méiyǒu mǎi.", "Non l’ho comprata.")]),
    ("…怎么样？", "Chiede un’opinione o propone qualcosa: “che ne dici di…?”.",
     [("这个颜色怎么样？", "Zhège yánsè zěnmeyàng?", "Che ne dici di questo colore?")]),
  ],
  dialogue=("In un negozio di abbigliamento", [
    ("售货员", "您要买什么？", "Nín yào mǎi shénme?", "Che cosa desidera comprare?"),
    ("丽莎", "我要买衣服。", "Wǒ yào mǎi yīfu.", "Vorrei comprare dei vestiti."),
    ("售货员", "您喜欢哪种颜色？", "Nín xǐhuan nǎ zhǒng yánsè?", "Che colore le piace?"),
    ("丽莎", "我喜欢蓝色。这件有蓝的吗？", "Wǒ xǐhuan lánsè. Zhè jiàn yǒu lán de ma?", "Mi piace il blu. Questo c’è in blu?"),
    ("售货员", "蓝的、白的都有。蓝的怎么样？", "Lán de, bái de dōu yǒu. Lán de zěnmeyàng?", "C’è sia blu sia bianco. Che ne dice di quello blu?"),
    ("丽莎", "很好。多少钱？", "Hěn hǎo. Duōshao qián?", "Molto bello. Quanto costa?"),
    ("售货员", "一百二十块。", "Yìbǎi èrshí kuài.", "Centoventi yuan."),
    ("丽莎", "我还要一双鞋。一共多少钱？", "Wǒ hái yào yì shuāng xié. Yígòng duōshao qián?", "Vorrei anche un paio di scarpe. Quanto fa in tutto?"),
    ("售货员", "一共三百零五块。", "Yígòng sānbǎi líng wǔ kuài.", "In tutto sono 305 yuan."),
  ]),
  reading=("Una giornata di spese",
    "今天杰夫花了很多钱。他买了三本书、一支笔、一件白衣服。书一本三十块，笔一支四块五，衣服一百五十八块。他还喝了一杯茶，五块钱。杰夫今天一共花了两百五十七块五。",
    "Jīntiān Jiéfū huāle hěn duō qián. Tā mǎile sān běn shū, yì zhī bǐ, yí jiàn bái yīfu. Shū yì běn sānshí kuài, bǐ yì zhī sì kuài wǔ, yīfu yìbǎi wǔshíbā kuài. Tā hái hēle yì bēi chá, wǔ kuài qián. Jiéfū jīntiān yígòng huāle liǎngbǎi wǔshíqī kuài wǔ.",
    "Oggi Jeff ha speso molti soldi. Ha comprato tre libri, una penna e una maglia bianca. I libri costano 30 yuan l’uno, la penna 4,50 e la maglia 158 yuan. Ha anche bevuto un tè, 5 yuan. Oggi Jeff ha speso in tutto 257,50 yuan.",
    [("杰夫买了几本书？", "Jiéfū mǎile jǐ běn shū?", ["三本", "两本", "一本", "四本"]),
     ("衣服是什么颜色的？", "Yīfu shì shénme yánsè de?", ["白的", "黑的", "蓝的", "红的"]),
     ("笔多少钱？", "Bǐ duōshao qián?", ["四块五", "三十块", "五块", "一百五十八块"]),
     ("杰夫一共花了多少钱？", "Jiéfū yígòng huāle duōshao qián?", ["两百五十七块五", "两百五十二块五", "一百五十八块", "三百块"])]),
  cloze=[
    ("这 ___ 自行车多少钱？", "Zhè ___ zìxíngchē duōshao qián?", "Quanto costa questa bicicletta?", ["辆", "本", "件", "支"], "辆 è il classificatore dei veicoli."),
    ("我买了两 ___ 书。", "Wǒ mǎile liǎng ___ shū.", "Ho comprato due libri.", ["本", "辆", "双", "杯"], "本 è il classificatore dei libri."),
    ("一 ___ 鞋一百二十块。", "Yì ___ xié yìbǎi èrshí kuài.", "Un paio di scarpe costa 120 yuan.", ["双", "件", "本", "支"], "双 = paio."),
    ("黑的、蓝的 ___ 有。", "Hēi de, lán de ___ yǒu.", "Ci sono sia neri sia blu.", ["都", "也", "还", "很"], "都 riassume gli elementi elencati prima."),
    ("我要这个，___ 要那个。", "Wǒ yào zhège, ___ yào nàge.", "Voglio questo e in più quello.", ["还", "都", "很", "了"], "还 = inoltre, in più."),
    ("你喜欢哪 ___ 颜色？", "Nǐ xǐhuan nǎ ___ yánsè?", "Quale colore ti piace?", ["种", "辆", "本", "杯"], "种 = tipo, genere."),
    ("我买 ___ 一件衣服。", "Wǒ mǎi ___ yí jiàn yīfu.", "Ho comprato un vestito.", ["了", "的", "吗", "呢"], "Verbo + 了 = azione compiuta."),
    ("这个颜色 ___？", "Zhège yánsè ___?", "Che ne dici di questo colore?", ["怎么样", "多少", "哪个", "几"], "怎么样 chiede un parere."),
  ],
  reorder=[
    ("一共多少钱？", "Yígòng duōshao qián?", "Quanto costa in tutto?", ["一共", "多少", "钱", "？"]),
    ("我喜欢蓝色的。", "Wǒ xǐhuan lánsè de.", "Mi piace quello blu.", ["我", "喜欢", "蓝色", "的", "。"]),
    ("我买了一辆自行车。", "Wǒ mǎile yí liàng zìxíngchē.", "Ho comprato una bicicletta.", ["我", "买了", "一辆", "自行车", "。"]),
    ("这种车有白的吗？", "Zhè zhǒng chē yǒu bái de ma?", "Questo tipo di bici c’è bianco?", ["这种", "车", "有", "白的", "吗", "？"]),
    ("你要哪个菜？", "Nǐ yào nǎge cài?", "Quale piatto vuoi?", ["你", "要", "哪个", "菜", "？"]),
    ("他花了三百块钱。", "Tā huāle sānbǎi kuài qián.", "Ha speso 300 yuan.", ["他", "花了", "三百", "块", "钱", "。"]),
  ],
  qa=[
    ("Come si legge il prezzo ¥7,50?", "", ["七块五", "七块五十", "七毛五", "七点五块"], "块 + 毛; l’ultima unità si può omettere."),
    ("Come si legge il prezzo ¥15,40?", "", ["十五块四", "十五块四十", "一五块四", "十五毛四"], "15 块 e 4 毛 → 十五块四."),
    ("Ti chiedono 「你要哪个？」 e vuoi quello lì. Cosa rispondi?", "nǐ yào nǎge?", ["我要那个。", "我要哪个。", "我那个要。", "要我那个。"], "那个 = quello."),
    ("Quale classificatore si usa per 「自行车」?", "zìxíngchē", ["辆", "本", "件", "双"], "Per i veicoli si usa 辆."),
    ("Come si dice 340?", "", ["三百四十", "三四十", "三百零四", "三十四百"], "三百 (300) + 四十 (40)."),
    ("Ti chiedono 「黑的怎么样？」 ma il nero non ti piace. Cosa rispondi?", "hēi de zěnmeyàng?", ["我不喜欢黑的，我喜欢蓝的。", "黑的很多钱。", "我买了黑。", "黑的是哪个。"], "Si esprime la preferenza con 喜欢 / 不喜欢."),
    ("Il cameriere dice 「一共二十块。」. Che cosa significa?", "yígòng èrshí kuài.", ["In tutto sono 20 yuan.", "Ognuno costa 20 yuan.", "Mancano 20 yuan.", "Sono più di 20 yuan."], "一共 = in tutto."),
    ("Ti chiedono se hai comprato le scarpe, ma non le hai comprate. Cosa dici?", "", ["我没有买。", "我不买了鞋。", "我没有买了。", "我买没有。"], "La negazione di un’azione passata è 没(有) + verbo, senza 了."),
  ],
  extra=[("Scioglilingua", "吃葡萄不吐葡萄皮", "吃葡萄不吐葡萄皮，不吃葡萄倒吐葡萄皮。", "Chī pútao bù tǔ pútao pí, bù chī pútao dào tǔ pútao pí.",
          "Mangia l’uva senza sputare la buccia; non mangia l’uva e invece sputa la buccia."),
         ("Cultura", "Pagare in Cina", "", "",
          "Nei negozi, nelle mense e perfino nelle bancarelle si paga quasi sempre con il cellulare, inquadrando un codice QR. I contanti si usano sempre meno, ma è bene sapere leggere i prezzi: sui cartellini si scrive ¥ o 元, mentre a voce si dice 块.")],
)

# ───────────────────────────── Lezione 9 ─────────────────────────────
L(n=9, zh="你有什么事？", py="Nǐ yǒu shénme shì?", it="Che cosa c’è? (Di cosa hai bisogno?)",
  theme="Telefonare, numeri di telefono e di stanza, date, compleanni e inviti",
  vocab="""
N|事|shì|名|faccenda, cosa (da fare)|matter, thing
N|作业|zuòyè|名|compiti|homework
N|个|gè|量|classificatore generico|general MW
N|问题|wèntí|名|domanda; problema|question, problem
N|懂|dǒng|动|capire|to understand
N|问|wèn|动|chiedere, domandare|to ask
N|吧|ba|助|particella di proposta / supposizione|modal particle
N|知道|zhīdào|动|sapere, conoscere (un fatto)|to know
N|电话|diànhuà|名|telefono; telefonata|telephone
N|号码|hàomǎ|名|numero|number
N|办公室|bàngōngshì|名|ufficio|office
N|六|liù|数|sei|six
N|零|líng|数|zero|zero
N|给|gěi|介,动|a, per; dare|to, for; to give
N|打|dǎ|动|fare (una telefonata); giocare (a palla)|to make (a call); to play (ball)
N|喂|wèi|叹|pronto? (al telefono)|hello (on the phone)
N|生日|shēngrì|名|compleanno|birthday
N|一起|yìqǐ|副|insieme|together
N|玩儿|wánr|动|divertirsi, giocare, uscire|to play, have fun
N|住|zhù|动|abitare, alloggiare|to live, stay
N|号|hào|量,名|numero; giorno del mese|number; date
N|楼|lóu|名,量|edificio; piano|building; floor
N|说|shuō|动|dire, parlare|to say, speak
N|礼物|lǐwù|名|regalo|gift
N|祝|zhù|动|augurare|to wish
N|快乐|kuàilè|形|felice|happy
N|等|děng|动|aspettare|to wait
N|房间|fángjiān|名|stanza, camera|room
N|月|yuè|名|mese; luna|month
N|昨天|zuótiān|名|ieri|yesterday
N|真|zhēn|副,形|davvero; vero|really; real
N|忙|máng|形|occupato, indaffarato|busy
N|想|xiǎng|动,助动|pensare; volere; sentire la mancanza di|to think; to want; to miss
N|饭馆儿|fànguǎnr|名|ristorante|restaurant
N|去|qù|动|andare|to go
N|打算|dǎsuan|动,名|avere intenzione di; programma|to plan; plan
N|朋友|péngyou|名|amico|friend
S|商场|shāngchǎng|名|centro commerciale|shopping mall
""",
  grammar=[
    ("Il raddoppiamento del verbo", "Ripetere il verbo rende l’azione breve, “di prova”, e il tono più gentile. Verbi di una sillaba: AA o A一A (看看 / 看一看); di due sillabe: ABAB (休息休息). Il secondo verbo ha il tono neutro.",
     [("我们问问老师吧。", "Wǒmen wènwen lǎoshī ba.", "Chiediamo un po’ all’insegnante."),
      ("你看看这本书。", "Nǐ kànkan zhè běn shū.", "Dai un’occhiata a questo libro.")]),
    ("Leggere numeri di telefono e di stanza", "Si leggono cifra per cifra. Nei numeri di telefono e di stanza 1 si dice spesso yāo, per non confonderlo con 七 qī; 0 = 零 líng. Per gli edifici: numero + 号楼.",
     [("我住八号楼六零一。", "Wǒ zhù bā hào lóu liù líng yāo.", "Abito nell’edificio 8, stanza 601."),
      ("她的电话是八二五三零九一六。", "Tā de diànhuà shì bā èr wǔ sān líng jiǔ yāo liù.", "Il suo numero è 82530916.")]),
    ("Al telefono: 喂", "Si risponde o si inizia la telefonata con 喂 (spesso pronunciato wéi). Per chiedere chi è: 是…吗? / 你是谁? Per rispondere: 是我 / 我是…",
     [("喂，是王平吗？——是我。", "Wèi, shì Wáng Píng ma? — Shì wǒ.", "Pronto, è Wang Ping? — Sono io.")]),
    ("吧 per proporre", "Frase + 吧 = proposta o invito: “facciamo…”, “dai…”.",
     [("我们一起去吧！", "Wǒmen yìqǐ qù ba!", "Andiamo insieme!")]),
    ("给 + persona + verbo", "给 introduce la persona a cui (o per cui) si fa l’azione; va prima del verbo.",
     [("我给老师打电话。", "Wǒ gěi lǎoshī dǎ diànhuà.", "Telefono all’insegnante."),
      ("我想给他买件礼物。", "Wǒ xiǎng gěi tā mǎi jiàn lǐwù.", "Vorrei comprargli un regalo.")]),
    ("Date e auguri", "La data va dal grande al piccolo: 月 + 号 (nel parlato) / 日 (nello scritto). Per gli auguri: 祝 + persona + augurio.",
     [("你的生日是几月几号？——十月九号。", "Nǐ de shēngrì shì jǐ yuè jǐ hào? — Shíyuè jiǔ hào.", "Quando è il tuo compleanno? — Il 9 ottobre."),
      ("祝你生日快乐！", "Zhù nǐ shēngrì kuàilè!", "Buon compleanno!")]),
  ],
  dialogue=("Una telefonata", [
    ("山田", "喂，是丽莎吗？", "Wèi, shì Lìshā ma?", "Pronto, sei Lisa?"),
    ("丽莎", "是我。你是谁？", "Shì wǒ. Nǐ shì shéi?", "Sono io. Chi parla?"),
    ("山田", "我是山田。你明天晚上有时间吗？", "Wǒ shì Shāntián. Nǐ míngtiān wǎnshang yǒu shíjiān ma?", "Sono Yamada. Domani sera hai tempo?"),
    ("丽莎", "有时间。你有什么事？", "Yǒu shíjiān. Nǐ yǒu shénme shì?", "Sì. Che cosa c’è?"),
    ("山田", "明天是安妮的生日，我们一起给她买件礼物吧。", "Míngtiān shì Ānnī de shēngrì, wǒmen yìqǐ gěi tā mǎi jiàn lǐwù ba.", "Domani è il compleanno di Annie: compriamole un regalo insieme."),
    ("丽莎", "好！几点？在哪儿？", "Hǎo! Jǐ diǎn? Zài nǎr?", "Va bene! A che ora? Dove?"),
    ("山田", "晚上六点，在五号楼。我住三零二。", "Wǎnshang liù diǎn, zài wǔ hào lóu. Wǒ zhù sān líng èr.", "Alle sei di sera, all’edificio 5. Abito al 302."),
    ("丽莎", "好，再见！", "Hǎo, zàijiàn!", "Perfetto, ciao!"),
  ]),
  reading=("Il compleanno di Wang Ping",
    "今天是十月十二号，是王平的生日。杰夫、安妮、山田都知道。他们给王平买了一件礼物，是一本汉语书。晚上七点，他们一起去王平的宿舍。王平住三号楼五零六。大家说：“祝你生日快乐！”王平说：“谢谢你们！”",
    "Jīntiān shì shíyuè shí’èr hào, shì Wáng Píng de shēngrì. Jiéfū, Ānnī, Shāntián dōu zhīdào. Tāmen gěi Wáng Píng mǎile yí jiàn lǐwù, shì yì běn Hànyǔ shū. Wǎnshang qī diǎn, tāmen yìqǐ qù Wáng Píng de sùshè. Wáng Píng zhù sān hào lóu wǔ líng liù. Dàjiā shuō: “Zhù nǐ shēngrì kuàilè!” Wáng Píng shuō: “Xièxie nǐmen!”",
    "Oggi è il 12 ottobre, il compleanno di Wang Ping. Jeff, Annie e Yamada lo sanno. Hanno comprato un regalo per Wang Ping: un libro di cinese. Alle sette di sera vanno insieme al dormitorio di Wang Ping, che abita nell’edificio 3, stanza 506. Tutti dicono: “Buon compleanno!” e Wang Ping risponde: “Grazie a tutti!”",
    [("王平的生日是几月几号？", "Wáng Píng de shēngrì shì jǐ yuè jǐ hào?", ["十月十二号", "十二月十号", "十月二号", "十二月十二号"]),
     ("他们给王平买了什么礼物？", "Tāmen gěi Wáng Píng mǎile shénme lǐwù?", ["一本汉语书", "一件衣服", "一辆自行车", "一支笔"]),
     ("王平住几号楼？", "Wáng Píng zhù jǐ hào lóu?", ["三号楼", "五号楼", "六号楼", "十二号楼"])]),
  cloze=[
    ("___，是王平吗？", "___, shì Wáng Píng ma?", "Pronto, è Wang Ping?", ["喂", "吧", "请", "祝"], "喂 si usa per iniziare o rispondere a una telefonata."),
    ("我们一起去 ___！", "Wǒmen yìqǐ qù ___!", "Andiamo insieme!", ["吧", "吗", "呢", "的"], "吧 a fine frase = proposta."),
    ("我 ___ 他打电话。", "Wǒ ___ tā dǎ diànhuà.", "Gli telefono.", ["给", "在", "是", "说"], "给 + persona + verbo."),
    ("___ 你生日快乐！", "___ nǐ shēngrì kuàilè!", "Buon compleanno!", ["祝", "给", "说", "问"], "祝 = augurare."),
    ("这个问题我不 ___。", "Zhège wèntí wǒ bù ___.", "Questa domanda non la capisco.", ["懂", "问", "说", "住"], "懂 = capire."),
    ("你 ___ 老师的电话号码吗？", "Nǐ ___ lǎoshī de diànhuà hàomǎ ma?", "Sai il numero di telefono dell’insegnante?", ["知道", "问", "懂", "说"], "知道 = sapere (un’informazione)."),
    ("你住几 ___ 楼？", "Nǐ zhù jǐ ___ lóu?", "In quale edificio abiti?", ["号", "个", "件", "本"], "几号楼 = edificio numero…?"),
    ("我们问 ___ 老师吧。", "Wǒmen wèn ___ lǎoshī ba.", "Chiediamo un po’ all’insegnante.", ["问", "是", "在", "很"], "Raddoppiamento: 问问."),
  ],
  reorder=[
    ("你有什么事？", "Nǐ yǒu shénme shì?", "Che cosa c’è?", ["你", "有", "什么", "事", "？"]),
    ("我给你打电话。", "Wǒ gěi nǐ dǎ diànhuà.", "Ti telefono.", ["我", "给", "你", "打", "电话", "。"]),
    ("明天晚上你有时间吗？", "Míngtiān wǎnshang nǐ yǒu shíjiān ma?", "Domani sera hai tempo?", ["明天", "晚上", "你", "有", "时间", "吗", "？"]),
    ("我住八号楼六零一。", "Wǒ zhù bā hào lóu liù líng yāo.", "Abito nell’edificio 8, stanza 601.", ["我", "住", "八号楼", "六零一", "。"]),
    ("我们一起给他买件礼物吧。", "Wǒmen yìqǐ gěi tā mǎi jiàn lǐwù ba.", "Compriamogli un regalo insieme.", ["我们", "一起", "给他", "买", "件", "礼物", "吧", "。"]),
    ("祝你生日快乐！", "Zhù nǐ shēngrì kuàilè!", "Buon compleanno!", ["祝", "你", "生日", "快乐", "！"]),
  ],
  qa=[
    ("Come si legge il numero di stanza 601?", "", ["liù líng yāo", "liùbǎi líng yī", "liùshíyī", "liù líng qī"], "Cifra per cifra; 1 si legge yāo."),
    ("Rispondi al telefono e ti chiedono 「是安妮吗？」. Sei tu. Cosa dici?", "shì Ānnī ma?", ["是我。", "我是吗。", "是你。", "不是我。"], "是我 = sono io."),
    ("Un amico compie gli anni. Cosa gli dici?", "", ["祝你生日快乐！", "生日你快乐祝！", "谢谢你的生日！", "你生日吗？"], "祝你生日快乐 = buon compleanno."),
    ("Vuoi proporre di andare insieme. Quale frase usi?", "", ["我们一起去吧。", "我们一起去吗？", "我们一起去呢。", "我们一起去的。"], "吧 = proposta."),
    ("Come si raddoppia 「看」 per dire “dare un’occhiata”?", "kàn", ["看看", "看了看了", "看个看", "看的看"], "Verbo di una sillaba: AA (o A一A)."),
    ("Ti chiedono 「你的生日是几月几号？」. Quale risposta è corretta?", "nǐ de shēngrì shì jǐ yuè jǐ hào?", ["十月九号。", "九号十月。", "十个月九号。", "十月九个号。"], "La data va dal grande al piccolo: mese, poi giorno."),
    ("Un amico ti telefona: 「你有什么事？」. Che cosa ti sta chiedendo?", "nǐ yǒu shénme shì?", ["Perché lo hai cercato / di cosa hai bisogno.", "Che cosa possiedi.", "Che lavoro fai.", "Che cosa hai mangiato."], "有什么事 = c’è qualcosa? di cosa hai bisogno?"),
  ],
  extra=[("Poesia", "咏鹅 · 骆宾王", "鹅，鹅，鹅，曲项向天歌。白毛浮绿水，红掌拨清波。",
          "É, é, é, qū xiàng xiàng tiān gē. Bái máo fú lǜ shuǐ, hóng zhǎng bō qīng bō.",
          "Oca, oca, oca: col collo ricurvo canta verso il cielo. Le piume bianche galleggiano sull’acqua verde, le zampe rosse smuovono le onde limpide. (Scritta, si dice, a sette anni.)"),
         ("Scioglilingua", "桌上放个盆儿", "桌上放个盆儿，盆里放个瓶儿。", "Zhuō shang fàng ge pénr, pén li fàng ge píngr.",
          "Sul tavolo c’è una bacinella, nella bacinella c’è una bottiglia. (Per -n / -ng con il 儿化)")],
)

# ───────────────────────────── Lezione 10 ─────────────────────────────
L(n=10, zh="她病了", py="Tā bìng le", it="È malata",
  theme="Stare male, chiedere un permesso, scusarsi per il ritardo",
  vocab="""
N|病|bìng|动,名|ammalarsi; malattia|to be sick; illness
N|怎么|zěnme|代|come; come mai|how; why
N|头|tóu|名|testa|head
N|疼|téng|形|dolorante, fare male|painful
N|感冒|gǎnmào|动,名|prendere il raffreddore; raffreddore|to catch a cold; cold
N|回|huí|动|tornare|to return
N|休息|xiūxi|动|riposare|to rest
N|告诉|gàosu|动|dire (a qualcuno), informare|to tell
N|能|néng|助动|potere, essere in grado|can
N|来|lái|动|venire|to come
N|请|qǐng|动|per favore; invitare; offrire|please; to invite
N|进|jìn|动|entrare|to enter
N|对不起|duìbuqǐ|动|scusa, mi dispiace|sorry
N|晚|wǎn|形|tardi|late
N|才|cái|副|solo (allora), non prima di|only then
N|闹钟|nàozhōng|名|sveglia|alarm clock
N|所以|suǒyǐ|连|quindi, perciò|so, therefore
N|停|tíng|动|fermarsi|to stop
N|大使馆|dàshǐguǎn|名|ambasciata|embassy
N|请假|qǐng jià||chiedere un permesso|to ask for leave
N|天|tiān|名|giorno; cielo|day; sky
N|牙|yá|名|dente|tooth
N|没|méi|动,副|non avere; non (al passato)|not have; not
N|慢|màn|形|lento|slow
S|肚子|dùzi|名|pancia, stomaco|stomach
S|嗓子|sǎngzi|名|gola|throat
S|腿|tuǐ|名|gamba|leg
S|手|shǒu|名|mano|hand
S|迟到|chídào|动|arrivare in ritardo|to be late
""",
  grammar=[
    ("你怎么了？", "Si chiede quando qualcuno sembra stare male o è successo qualcosa: “cos’hai?”, “che ti succede?”. Per rispondere: parte del corpo + 疼.",
     [("你怎么了？——我头疼。", "Nǐ zěnme le? — Wǒ tóu téng.", "Cos’hai? — Ho mal di testa."),
      ("他肚子疼。", "Tā dùzi téng.", "Ha mal di pancia.")]),
    ("了 a fine frase: cambiamento", "了 alla fine della frase segnala una situazione nuova: prima non era così, adesso sì.",
     [("安妮病了，今天不能来上课了。", "Ānnī bìng le, jīntiān bù néng lái shàng kè le.", "Annie si è ammalata, oggi non può (più) venire a lezione.")]),
    ("能 (potere)", "能 + verbo: essere in grado o avere la possibilità di fare qualcosa. Negazione: 不能.",
     [("你能告诉老师吗？", "Nǐ néng gàosu lǎoshī ma?", "Puoi dirlo all’insegnante?"),
      ("明天我不能来。", "Míngtiān wǒ bù néng lái.", "Domani non posso venire.")]),
    ("才 (solo allora, tardi)", "才 + verbo: l’azione avviene più tardi o con più difficoltà del previsto. 你怎么才来? = “come mai arrivi solo adesso?”. Con 才 di solito non si usa 了.",
     [("你怎么才来？", "Nǐ zěnme cái lái?", "Come mai arrivi solo ora?"),
      ("我八点半才起床。", "Wǒ bā diǎn bàn cái qǐ chuáng.", "Mi sono alzato solo alle otto e mezza.")]),
    ("请假 (chiedere un permesso)", "请 + durata + 假: 请一天假, 请半天假. Per scusarsi: 对不起，我来晚了.",
     [("老师，我想请一天假。", "Lǎoshī, wǒ xiǎng qǐng yì tiān jià.", "Professoressa, vorrei chiedere un giorno di permesso.")]),
    ("所以 (quindi)", "Introduce la conseguenza.",
     [("我感冒了，所以没有来上课。", "Wǒ gǎnmào le, suǒyǐ méiyǒu lái shàng kè.", "Avevo il raffreddore, quindi non sono venuto a lezione.")]),
  ],
  dialogue=("Nell’ufficio degli insegnanti", [
    ("山田", "田老师，您好！", "Tián lǎoshī, nín hǎo!", "Buongiorno, professoressa Tian!"),
    ("田老师", "山田，你怎么了？", "Shāntián, nǐ zěnme le?", "Yamada, che cos’hai?"),
    ("山田", "我肚子疼，不能上课了。", "Wǒ dùzi téng, bù néng shàng kè le.", "Ho mal di pancia, non riesco a fare lezione."),
    ("田老师", "你感冒了吗？", "Nǐ gǎnmào le ma?", "Hai preso il raffreddore?"),
    ("山田", "不知道。我想请一天假，回房间休息。", "Bù zhīdào. Wǒ xiǎng qǐng yì tiān jià, huí fángjiān xiūxi.", "Non lo so. Vorrei chiedere un giorno di permesso e tornare in camera a riposare."),
    ("田老师", "好。明天能来吗？", "Hǎo. Míngtiān néng lái ma?", "Va bene. Domani puoi venire?"),
    ("山田", "能。谢谢老师！", "Néng. Xièxie lǎoshī!", "Sì. Grazie, professoressa!"),
  ]),
  reading=("Una mattina storta",
    "今天彼得九点才来上课。他的闹钟停了，所以他八点半才起床。田老师问他：“你怎么了？”彼得说：“对不起，我来晚了。”丽莎今天也没有来，她病了，头很疼。",
    "Jīntiān Bǐdé jiǔ diǎn cái lái shàng kè. Tā de nàozhōng tíng le, suǒyǐ tā bā diǎn bàn cái qǐ chuáng. Tián lǎoshī wèn tā: “Nǐ zěnme le?” Bǐdé shuō: “Duìbuqǐ, wǒ lái wǎn le.” Lìshā jīntiān yě méiyǒu lái, tā bìng le, tóu hěn téng.",
    "Oggi Peter è arrivato a lezione solo alle nove. La sua sveglia si era fermata, quindi si è alzato solo alle otto e mezza. La professoressa Tian gli chiede: “Che ti è successo?” Peter risponde: “Mi scusi, sono in ritardo.” Anche Lisa oggi non è venuta: è malata e ha un forte mal di testa.",
    [("彼得几点来上课？", "Bǐdé jǐ diǎn lái shàng kè?", ["九点", "八点", "八点半", "十点"]),
     ("彼得的闹钟怎么了？", "Bǐdé de nàozhōng zěnme le?", ["停了", "病了", "感冒了", "很疼"]),
     ("丽莎怎么了？", "Lìshā zěnme le?", ["她病了，头很疼", "她来晚了", "她去大使馆了", "她八点半起床"])]),
  cloze=[
    ("你 ___ 了？", "Nǐ ___ le?", "Che cos’hai?", ["怎么", "什么", "哪儿", "几"], "你怎么了 = che ti succede?"),
    ("我头 ___。", "Wǒ tóu ___.", "Ho mal di testa.", ["疼", "病", "晚", "停"], "Parte del corpo + 疼."),
    ("她病了，今天不 ___ 来上课了。", "Tā bìng le, jīntiān bù ___ lái shàng kè le.", "È malata, oggi non può venire a lezione.", ["能", "在", "是", "有"], "能 = potere, essere in grado."),
    ("你怎么 ___ 来？现在九点了！", "Nǐ zěnme ___ lái? Xiànzài jiǔ diǎn le!", "Come mai arrivi solo ora? Sono le nove!", ["才", "都", "也", "很"], "才 = solo allora (più tardi del previsto)."),
    ("闹钟停了，___ 我来晚了。", "Nàozhōng tíng le, ___ wǒ lái wǎn le.", "La sveglia si è fermata, quindi sono arrivato tardi.", ["所以", "可是", "因为", "还"], "所以 introduce la conseguenza."),
    ("我想请半天 ___。", "Wǒ xiǎng qǐng bàn tiān ___.", "Vorrei chiedere mezza giornata di permesso.", ["假", "病", "天", "课"], "请 + durata + 假."),
    ("请 ___！", "Qǐng ___!", "Avanti, entra pure!", ["进", "晚", "停", "疼"], "请进 = avanti, entra."),
    ("对不起，我来 ___ 了。", "Duìbuqǐ, wǒ lái ___ le.", "Scusi, sono arrivato tardi.", ["晚", "才", "停", "疼"], "来晚了 = arrivare in ritardo."),
  ],
  reorder=[
    ("你怎么了？", "Nǐ zěnme le?", "Che cos’hai?", ["你", "怎么", "了", "？"]),
    ("我想回房间休息。", "Wǒ xiǎng huí fángjiān xiūxi.", "Voglio tornare in camera a riposare.", ["我", "想", "回", "房间", "休息", "。"]),
    ("你能告诉老师吗？", "Nǐ néng gàosu lǎoshī ma?", "Puoi dirlo all’insegnante?", ["你", "能", "告诉", "老师", "吗", "？"]),
    ("我八点半才起床。", "Wǒ bā diǎn bàn cái qǐ chuáng.", "Mi sono alzato solo alle otto e mezza.", ["我", "八点半", "才", "起床", "。"]),
    ("明天我要去大使馆。", "Míngtiān wǒ yào qù dàshǐguǎn.", "Domani devo andare all’ambasciata.", ["明天", "我", "要", "去", "大使馆", "。"]),
    ("我想请两天假。", "Wǒ xiǎng qǐng liǎng tiān jià.", "Vorrei chiedere due giorni di permesso.", ["我", "想", "请", "两天", "假", "。"]),
  ],
  qa=[
    ("Un compagno sembra stare male. Cosa gli chiedi?", "", ["你怎么了？", "你是谁？", "你几点了？", "你怎么样了吗？"], "你怎么了 = che cos’hai?"),
    ("Arrivi tardi a lezione. Cosa dici entrando?", "", ["对不起，我来晚了。", "没关系，我来晚了。", "请进，我来晚了。", "谢谢，我来晚了。"], "Ci si scusa con 对不起."),
    ("L’insegnante dice 「你怎么才来？」. Che cosa intende?", "nǐ zěnme cái lái?", ["Come mai arrivi solo adesso?", "Come sei venuto?", "Perché sei venuto?", "Quando verrai?"], "才 = più tardi del previsto."),
    ("Bussano alla porta del tuo ufficio. Cosa dici?", "", ["请进！", "进请！", "请来进！", "你进吗？"], "请进 = avanti!"),
    ("Quale frase significa “Ho mal di denti”?", "", ["我牙疼。", "我疼牙。", "我的牙病。", "牙我疼。"], "Parte del corpo + 疼."),
    ("In 「她病了。」 che cosa indica 了?", "tā bìng le.", ["Un cambiamento: adesso è malata.", "Il futuro.", "Una domanda.", "Il possesso."], "了 a fine frase = situazione nuova."),
    ("Domani devi andare all’ambasciata e non puoi venire a lezione. Cosa dici all’insegnante?", "", ["老师，明天我想请假。", "老师，明天我想上课。", "老师，明天我来晚了。", "老师，明天你能请假吗？"], "请假 = chiedere un permesso."),
  ],
  extra=[("Poesia", "一去二三里 · 邵雍", "一去二三里，烟村四五家。亭台六七座，八九十枝花。",
          "Yí qù èr sān lǐ, yān cūn sì wǔ jiā. Tíngtái liù qī zuò, bā jiǔ shí zhī huā.",
          "Fatti due o tre li, un villaggio nel fumo con quattro o cinque case; sei o sette padiglioni, otto, nove, dieci fiori. (Filastrocca per imparare i numeri da 1 a 10.)"),
         ("Scioglilingua", "天上看，满天星", "天上看，满天星；地上看，有个坑；坑里看，有盘冰。", "Tiān shang kàn, mǎn tiān xīng; dì shang kàn, yǒu ge kēng; kēng li kàn, yǒu pán bīng.",
          "Guardi in cielo: il cielo pieno di stelle; guardi a terra: c’è una buca; guardi nella buca: c’è un piatto di ghiaccio. (Per -n / -ng)"),
         ("Cultura", "I numeri con le mani", "", "",
          "In Cina i numeri da 1 a 10 si mostrano con una sola mano: 6 = pollice e mignolo aperti, 7 = punte delle dita unite, 8 = pollice e indice a “L”, 9 = indice piegato a uncino, 10 = pugno chiuso o due indici incrociati. Su assegni e documenti bancari si usano i numeri “complessi”, difficili da falsificare: 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾.")],
)

# ───────────────────────────── Lezione 11 ─────────────────────────────
L(n=11, zh="我喜欢喝茶", py="Wǒ xǐhuan hē chá", it="Mi piace bere il tè",
  theme="Cibo e bevande, assaggiare e contrattare al mercato, offrire qualcosa a un ospite",
  vocab="""
N|吃|chī|动|mangiare|to eat
N|馒头|mántou|名|panino cotto al vapore|steamed bun
N|饺子|jiǎozi|名|ravioli cinesi|dumplings
N|斤|jīn|量|jin (mezzo chilo)|half kilo
N|大概|dàgài|副,形|probabilmente, circa|probably, about
N|完|wán|动|finire|to finish
N|好吃|hǎochī|形|buono (da mangiare)|delicious
N|葡萄|pútao|名|uva|grapes
N|酸|suān|形|aspro, acido|sour
N|甜|tián|形|dolce|sweet
N|可以|kěyǐ|助动|potere (permesso)|can, may
N|尝|cháng|动|assaggiare|to taste
N|便宜|piányi|形|economico|cheap
N|一点儿|yìdiǎnr|数量|un po’|a little
N|讲价|jiǎng jià||contrattare|to bargain
N|欢迎|huānyíng|动|dare il benvenuto|to welcome
N|坐|zuò|动|sedersi; prendere (un mezzo)|to sit; to take (transport)
N|还是|háishi|连,副|oppure (nelle domande); ancora|or; still
N|咖啡|kāfēi|名|caffè|coffee
N|以前|yǐqián|名|prima, in passato|before
N|桌子|zhuōzi|名|tavolo|table
N|上边|shàngbian|名|sopra|on top
N|点心|diǎnxin|名|dolcetti, snack|snacks, pastries
N|随便|suíbiàn|形|come si vuole, a piacere|as one pleases
N|以后|yǐhòu|名|dopo, in futuro|after; later
N|习惯|xíguàn|动,名|abituarsi; abitudine|to get used to; habit
N|写|xiě|动|scrivere|to write
N|帮|bāng|动|aiutare|to help
S|东西|dōngxi|名|cosa, oggetto|thing
S|白酒|báijiǔ|名|liquore cinese|Chinese liquor
S|橘子|júzi|名|mandarino|mandarin orange
""",
  grammar=[
    ("没问题", "“Nessun problema”: risposta sicura a una richiesta o a un dubbio.",
     [("你能吃完吗？——没问题！", "Nǐ néng chīwán ma? — Méi wèntí!", "Riesci a finirlo? — Nessun problema!")]),
    ("Domanda affermativo-negativa (A不A)", "Si ripete il verbo o l’aggettivo con 不 in mezzo: 酸不酸? 是不是? 有没有? È già una domanda: non si aggiunge 吗.",
     [("这个葡萄酸不酸？", "Zhège pútao suān bu suān?", "Quest’uva è aspra?"),
      ("你喝不喝咖啡？", "Nǐ hē bu hē kāfēi?", "Bevi il caffè?")]),
    ("可以 e 能", "可以 esprime soprattutto un permesso (“si può?”, “posso?”); 能 una capacità o una possibilità. Per chiedere un permesso vanno bene tutti e due; per rifiutarlo si usa 不能 o 不可以.",
     [("我可以尝尝吗？——可以。", "Wǒ kěyǐ chángchang ma? — Kěyǐ.", "Posso assaggiare? — Certo."),
      ("我能吃完一斤饺子。", "Wǒ néng chīwán yì jīn jiǎozi.", "Riesco a finire un jin di ravioli.")]),
    ("斤", "Unità di peso usata al mercato: 一斤 = 500 g, 半斤 = 250 g. Il prezzo si chiede così: 多少钱一斤?",
     [("葡萄多少钱一斤？", "Pútao duōshao qián yì jīn?", "Quanto costa l’uva al jin?")]),
    ("A 还是 B? (domanda alternativa)", "Per far scegliere fra due possibilità si usa 还是; la frase non prende 吗.",
     [("你喝茶还是喝咖啡？", "Nǐ hē chá háishi hē kāfēi?", "Bevi tè o caffè?")]),
    ("以前 e 以后", "Da soli: “prima / in passato” e “dopo / in futuro”. Dopo un verbo o un’indicazione di tempo: …以前 = prima di…, …以后 = dopo…",
     [("我以前喜欢喝咖啡。", "Wǒ yǐqián xǐhuan hē kāfēi.", "Prima mi piaceva il caffè."),
      ("来中国以后，我习惯了喝茶。", "Lái Zhōngguó yǐhòu, wǒ xíguànle hē chá.", "Da quando sono in Cina mi sono abituato a bere il tè.")]),
    ("Aggettivo + 一点儿", "Dopo un aggettivo o un verbo, 一点儿 significa “un po’ (di più)”: 便宜一点儿 = un po’ più economico.",
     [("太贵了，便宜一点儿吧。", "Tài guì le, piányi yìdiǎnr ba.", "È troppo caro, faccia un po’ meno.")]),
  ],
  dialogue=("Alla bancarella della frutta", [
    ("彼得", "这种橘子甜不甜？", "Zhè zhǒng júzi tián bu tián?", "Questi mandarini sono dolci?"),
    ("售货员", "很甜。你可以尝尝。", "Hěn tián. Nǐ kěyǐ chángchang.", "Molto dolci. Può assaggiarli."),
    ("彼得", "真好吃！多少钱一斤？", "Zhēn hǎochī! Duōshao qián yì jīn?", "Buonissimi! Quanto costano al jin?"),
    ("售货员", "五块。", "Wǔ kuài.", "Cinque yuan."),
    ("彼得", "便宜一点儿，可以吗？", "Piányi yìdiǎnr, kěyǐ ma?", "Me li fa un po’ meno?"),
    ("售货员", "四块五吧。你要几斤？", "Sì kuài wǔ ba. Nǐ yào jǐ jīn?", "Facciamo 4,50. Quanti jin ne vuole?"),
    ("彼得", "我要两斤。还要一斤葡萄。", "Wǒ yào liǎng jīn. Hái yào yì jīn pútao.", "Ne voglio due jin. E anche un jin d’uva."),
    ("售货员", "一共十五块。", "Yígòng shíwǔ kuài.", "In tutto sono quindici yuan."),
  ]),
  reading=("I gusti di Yamada",
    "山田是日本人。以前他喜欢喝咖啡，来中国以后，他习惯了喝茶。他也喜欢吃中国菜，很喜欢吃饺子。他说食堂的饺子很好吃，也很便宜，半斤饺子他都能吃完。",
    "Shāntián shì Rìběnrén. Yǐqián tā xǐhuan hē kāfēi, lái Zhōngguó yǐhòu, tā xíguànle hē chá. Tā yě xǐhuan chī Zhōngguó cài, hěn xǐhuan chī jiǎozi. Tā shuō shítáng de jiǎozi hěn hǎochī, yě hěn piányi, bàn jīn jiǎozi tā dōu néng chīwán.",
    "Yamada è giapponese. Prima gli piaceva il caffè; da quando è in Cina si è abituato a bere il tè. Gli piace anche la cucina cinese, soprattutto i ravioli. Dice che i ravioli della mensa sono buonissimi ed economici, e riesce a finirne anche mezzo jin.",
    [("山田以前喜欢喝什么？", "Shāntián yǐqián xǐhuan hē shénme?", ["咖啡", "茶", "白酒", "果汁儿"]),
     ("现在山田习惯喝什么？", "Xiànzài Shāntián xíguàn hē shénme?", ["茶", "咖啡", "白酒", "啤酒"]),
     ("食堂的饺子怎么样？", "Shítáng de jiǎozi zěnmeyàng?", ["好吃，也便宜", "不好吃", "很贵", "很酸"])]),
  cloze=[
    ("这个葡萄酸 ___ 酸？", "Zhège pútao suān ___ suān?", "Quest’uva è aspra?", ["不", "没", "吗", "很"], "A不A: domanda sì/no senza 吗."),
    ("你喝茶 ___ 喝咖啡？", "Nǐ hē chá ___ hē kāfēi?", "Bevi tè o caffè?", ["还是", "或者", "也", "都"], "Nelle domande alternative si usa 还是 (或者 si usa nelle frasi affermative)."),
    ("我 ___ 尝尝吗？", "Wǒ ___ chángchang ma?", "Posso assaggiare?", ["可以", "会", "是", "要"], "可以 = permesso."),
    ("葡萄多少钱一 ___？", "Pútao duōshao qián yì ___?", "Quanto costa l’uva al jin?", ["斤", "本", "辆", "件"], "Al mercato il peso si conta in 斤."),
    ("太贵了，便宜 ___ 吧。", "Tài guì le, piányi ___ ba.", "È troppo caro, faccia un po’ meno.", ["一点儿", "有点儿", "很", "都"], "Aggettivo + 一点儿 = un po’ più…"),
    ("请坐，桌子上边有点心，___ 吃吧。", "Qǐng zuò, zhuōzi shàngbian yǒu diǎnxin, ___ chī ba.", "Siediti, sul tavolo ci sono dei dolcetti: serviti pure.", ["随便", "可以", "以前", "还是"], "随便 = a piacere, liberamente."),
    ("来中国 ___，我习惯了喝茶。", "Lái Zhōngguó ___, wǒ xíguànle hē chá.", "Da quando sono in Cina mi sono abituato al tè.", ["以后", "以前", "还是", "随便"], "…以后 = dopo…"),
    ("半斤饺子，你能吃 ___ 吗？", "Bàn jīn jiǎozi, nǐ néng chī ___ ma?", "Riesci a finire mezzo jin di ravioli?", ["完", "在", "着", "的"], "吃完 = finire di mangiare."),
  ],
  reorder=[
    ("我喜欢喝茶。", "Wǒ xǐhuan hē chá.", "Mi piace bere il tè.", ["我", "喜欢", "喝", "茶", "。"]),
    ("你喝茶还是喝咖啡？", "Nǐ hē chá háishi hē kāfēi?", "Bevi tè o caffè?", ["你", "喝茶", "还是", "喝", "咖啡", "？"]),
    ("我可以尝尝吗？", "Wǒ kěyǐ chángchang ma?", "Posso assaggiare?", ["我", "可以", "尝尝", "吗", "？"]),
    ("这儿的饺子很好吃。", "Zhèr de jiǎozi hěn hǎochī.", "I ravioli di qui sono buonissimi.", ["这儿", "的", "饺子", "很", "好吃", "。"]),
    ("葡萄多少钱一斤？", "Pútao duōshao qián yì jīn?", "Quanto costa l’uva al jin?", ["葡萄", "多少钱", "一", "斤", "？"]),
    ("我以前不习惯喝茶。", "Wǒ yǐqián bù xíguàn hē chá.", "Prima non ero abituato a bere il tè.", ["我", "以前", "不", "习惯", "喝茶", "。"]),
  ],
  qa=[
    ("Un amico ti chiede 「你能吃完吗？」 e sei sicuro di farcela. Cosa rispondi?", "nǐ néng chīwán ma?", ["没问题！", "没关系！", "不客气！", "对不起！"], "没问题 = nessun problema."),
    ("Quale domanda è corretta?", "", ["葡萄甜不甜？", "葡萄甜不甜吗？", "葡萄不甜甜？", "葡萄甜吗不？"], "Con A不A non si aggiunge 吗."),
    ("Il padrone di casa ti chiede 「你喝茶还是喝咖啡？」. Cosa rispondi?", "nǐ hē chá háishi hē kāfēi?", ["我喝茶，谢谢。", "是，我喝。", "我喝还是茶。", "对，还是。"], "Si sceglie una delle due possibilità."),
    ("Quanti grammi sono 「一斤」?", "yì jīn", ["500 g", "1000 g", "250 g", "100 g"], "一斤 = mezzo chilo."),
    ("Al mercato vuoi assaggiare l’uva. Cosa chiedi?", "", ["我可以尝尝吗？", "我会尝尝吗？", "我尝尝可以。", "可以我尝吗？"], "可以 per chiedere il permesso."),
    ("Hai ospiti e li inviti a sedersi. Cosa dici?", "", ["请坐！", "坐请！", "请你坐了。", "你坐吗？"], "请坐 = prego, si sieda."),
    ("Il venditore dice 「我们这儿不讲价。」. Che cosa significa?", "wǒmen zhèr bù jiǎng jià.", ["Qui non si contratta.", "Qui non si parla.", "Qui non è caro.", "Qui non si vende."], "讲价 = contrattare."),
  ],
  extra=[("Poesia", "登鹳雀楼 · 王之涣", "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。",
          "Bái rì yī shān jìn, Huáng Hé rù hǎi liú. Yù qióng qiān lǐ mù, gèng shàng yì céng lóu.",
          "Il sole bianco tramonta dietro i monti, il Fiume Giallo scorre verso il mare. Se vuoi spingere lo sguardo a mille li, sali ancora di un piano della torre."),
         ("Scioglilingua", "六十六岁的刘老头", "说的是六十六条胡同口，住着个六十六岁的刘老头。", "Shuō de shì liùshíliù tiáo hútòng kǒu, zhùzhe ge liùshíliù suì de Liú lǎotóu.",
          "Si racconta che all’imbocco di sessantasei vicoli abita il vecchio Liu di sessantasei anni. (Per l / n e i toni di liù)")],
)

# ───────────────────────────── Lezione 12 ─────────────────────────────
L(n=12, zh="你干什么呢？", py="Nǐ gàn shénme ne?", it="Che cosa stai facendo?",
  theme="Azioni in corso, stati d’animo, chiacchierare e invitare a entrare",
  vocab="""
N|干|gàn|动|fare|to do
N|门|mén|名,量|porta; classificatore per materie|door; MW for courses
N|开|kāi|动|aprire; accendere; tenere (una riunione)|to open; to turn on; to hold
N|着|zhe|助|particella di stato continuo|aspect particle (ongoing)
N|好像|hǎoxiàng|副|sembrare|to seem
N|不太|bú tài|副|non molto|not very
N|高兴|gāoxìng|形|contento|glad
N|有点儿|yǒudiǎnr|副|un po’ (con sfumatura negativa)|a bit (negative)
N|家|jiā|名,量|casa, famiglia; classificatore per negozi|home, family
N|听|tīng|动|ascoltare|to listen
N|一会儿|yíhuìr|数量|un momento|a little while
N|音乐|yīnyuè|名|musica|music
N|咱们|zánmen|代|noi (incluso chi ascolta)|we (inclusive)
N|聊天儿|liáo tiānr||chiacchierare|to chat
N|啊|a|助|particella esclamativa|modal particle
N|进来|jìnlái||entrare (verso chi parla)|to come in
N|做|zuò|动|fare|to do, make
N|听写|tīngxiě|动,名|dettato; fare un dettato|dictation
N|生词|shēngcí|名|parole nuove|new words
N|当然|dāngrán|形|certo, naturalmente|of course
N|回答|huídá|动|rispondere|to answer
N|星期天|xīngqītiān|名|domenica|Sunday
N|为什么|wèi shénme||perché?|why
N|可是|kěshì|连|ma, però|but
N|觉得|juéde|动|sentire; ritenere|to feel; to think
N|电视|diànshì|名|televisione|TV
N|歌|gē|名|canzone|song
N|关|guān|动|chiudere; spegnere|to close; to turn off
N|瓶|píng|名,量|bottiglia|bottle
N|这些|zhèxiē|代|questi|these
S|贵|guì|形|caro, costoso|expensive
S|苹果|píngguǒ|名|mela|apple
S|篮球|lánqiú|名|pallacanestro|basketball
S|戴|dài|动|indossare (occhiali, cappello)|to wear (glasses)
S|眼镜|yǎnjìng|名|occhiali|glasses
S|酒|jiǔ|名|alcolico, vino|alcohol
""",
  grammar=[
    ("有点儿 + aggettivo / verbo", "“Un po’”, quasi sempre per qualcosa di sgradito o negativo: 有点儿累, 有点儿贵, 有点儿想家. (Da non confondere con 一点儿, che va dopo l’aggettivo.)",
     [("我今天有点儿不高兴。", "Wǒ jīntiān yǒudiǎnr bù gāoxìng.", "Oggi sono un po’ giù."),
      ("我有点儿想家。", "Wǒ yǒudiǎnr xiǎng jiā.", "Ho un po’ di nostalgia di casa.")]),
    ("咱们 e 我们", "咱们 comprende sempre chi ascolta (“noi, io e te”); 我们 può anche escluderlo (“noi, ma non tu”).",
     [("咱们一起聊聊天儿吧。", "Zánmen yìqǐ liáoliao tiānr ba.", "Facciamo due chiacchiere, io e te."),
      ("我们明天有课，你们呢？", "Wǒmen míngtiān yǒu kè, nǐmen ne?", "Noi domani abbiamo lezione, e voi?")]),
    ("着: uno stato che dura", "Verbo + 着 descrive uno stato che continua: 门开着 = la porta è aperta. V1 + 着 + V2: si fa V2 mentre dura V1.",
     [("门开着，请进。", "Mén kāizhe, qǐng jìn.", "La porta è aperta, entra pure."),
      ("他听着音乐做作业。", "Tā tīngzhe yīnyuè zuò zuòyè.", "Fa i compiti ascoltando musica.")]),
    ("呢: azione in corso", "Verbo + oggetto + 呢 (o 在 + verbo + 呢) indica un’azione in svolgimento: “sto facendo”.",
     [("你干什么呢？——我做作业呢。", "Nǐ gàn shénme ne? — Wǒ zuò zuòyè ne.", "Che cosa stai facendo? — Sto facendo i compiti.")]),
    ("真的吗？", "“Davvero?”: esprime sorpresa o un po’ di dubbio.",
     [("明天没有课。——真的吗？", "Míngtiān méiyǒu kè. — Zhēn de ma?", "Domani non c’è lezione. — Davvero?")]),
    ("好像 e 觉得", "好像 = “sembra (che)”, impressione esterna; 觉得 = “sento, ritengo”, opinione personale.",
     [("你好像不太高兴。", "Nǐ hǎoxiàng bú tài gāoxìng.", "Sembri un po’ giù."),
      ("我觉得这个习惯不太好。", "Wǒ juéde zhège xíguàn bú tài hǎo.", "Secondo me questa abitudine non è molto buona.")]),
  ],
  dialogue=("Davanti alla stanza di Yamada", [
    ("彼得", "山田，你干什么呢？", "Shāntián, nǐ gàn shénme ne?", "Yamada, che cosa stai facendo?"),
    ("山田", "我写汉字呢，明天有听写。", "Wǒ xiě Hànzì ne, míngtiān yǒu tīngxiě.", "Sto scrivendo caratteri, domani c’è il dettato."),
    ("彼得", "你好像不太高兴。", "Nǐ hǎoxiàng bú tài gāoxìng.", "Sembri un po’ giù."),
    ("山田", "汉字太多了！我有点儿着急。", "Hànzì tài duō le! Wǒ yǒudiǎnr zháojí.", "I caratteri sono troppi! Sono un po’ in ansia."),
    ("彼得", "咱们聊一会儿天儿吧。", "Zánmen liáo yíhuìr tiānr ba.", "Facciamo due chiacchiere."),
    ("山田", "好啊！请进，门开着呢。", "Hǎo a! Qǐng jìn, mén kāizhe ne.", "Volentieri! Entra, la porta è aperta."),
    ("彼得", "你听着音乐写汉字吗？", "Nǐ tīngzhe yīnyuè xiě Hànzì ma?", "Scrivi i caratteri ascoltando musica?"),
    ("山田", "当然！我觉得很好。", "Dāngrán! Wǒ juéde hěn hǎo.", "Certo! Secondo me funziona."),
  ]),
  reading=("Domenica in dormitorio",
    "星期天上午，大家都在宿舍。山田开着门听音乐呢；彼得写汉字呢，明天有听写；安妮、丽莎聊天儿呢。杰夫干什么呢？他还睡觉呢！",
    "Xīngqītiān shàngwǔ, dàjiā dōu zài sùshè. Shāntián kāizhe mén tīng yīnyuè ne; Bǐdé xiě Hànzì ne, míngtiān yǒu tīngxiě; Ānnī, Lìshā liáo tiānr ne. Jiéfū gàn shénme ne? Tā hái shuì jiào ne!",
    "Domenica mattina sono tutti in dormitorio. Yamada ascolta musica con la porta aperta; Peter scrive caratteri, perché domani c’è il dettato; Annie e Lisa chiacchierano. E Jeff che cosa fa? Sta ancora dormendo!",
    [("山田干什么呢？", "Shāntián gàn shénme ne?", ["听音乐呢", "写汉字呢", "聊天儿呢", "睡觉呢"]),
     ("彼得为什么写汉字？", "Bǐdé wèi shénme xiě Hànzì?", ["明天有听写", "他想家", "他不高兴", "他喜欢音乐"]),
     ("杰夫干什么呢？", "Jiéfū gàn shénme ne?", ["睡觉呢", "听音乐呢", "做作业呢", "聊天儿呢"])]),
  cloze=[
    ("你干什么 ___？", "Nǐ gàn shénme ___?", "Che cosa stai facendo?", ["呢", "吗", "着", "很"], "呢 a fine frase = azione in corso."),
    ("他听 ___ 音乐做作业。", "Tā tīng ___ yīnyuè zuò zuòyè.", "Fa i compiti ascoltando musica.", ["着", "了", "过", "的"], "V1 + 着 + V2: due azioni contemporanee."),
    ("我 ___ 想家。", "Wǒ ___ xiǎng jiā.", "Ho un po’ di nostalgia di casa.", ["有点儿", "一点儿", "一会儿", "一下"], "有点儿 + verbo/aggettivo, per qualcosa di negativo."),
    ("___ 一起去吃饭吧！(io e te)", "___ yìqǐ qù chī fàn ba!", "Andiamo a mangiare insieme!", ["咱们", "他们", "你们", "她们"], "咱们 include chi ascolta."),
    ("你 ___ 不太高兴。", "Nǐ ___ bú tài gāoxìng.", "Sembri un po’ giù.", ["好像", "当然", "可是", "为什么"], "好像 = sembrare."),
    ("我 ___ 他是好学生。", "Wǒ ___ tā shì hǎo xuésheng.", "Secondo me è un bravo studente.", ["觉得", "好像", "当然", "可是"], "觉得 = ritenere, pensare."),
    ("你能回答这个问题吗？——___！", "Nǐ néng huídá zhège wèntí ma? — ___!", "Sai rispondere a questa domanda? — Certo!", ["当然", "可是", "好像", "为什么"], "当然 = certo, naturalmente."),
    ("你 ___ 不来上课？", "Nǐ ___ bù lái shàng kè?", "Perché non vieni a lezione?", ["为什么", "什么", "怎么样", "哪儿"], "为什么 = perché?"),
  ],
  reorder=[
    ("你干什么呢？", "Nǐ gàn shénme ne?", "Che cosa stai facendo?", ["你", "干", "什么", "呢", "？"]),
    ("我有点儿想家。", "Wǒ yǒudiǎnr xiǎng jiā.", "Ho un po’ di nostalgia di casa.", ["我", "有点儿", "想", "家", "。"]),
    ("门开着呢。", "Mén kāizhe ne.", "La porta è aperta.", ["门", "开着", "呢", "。"]),
    ("咱们听着音乐聊天儿吧。", "Zánmen tīngzhe yīnyuè liáo tiānr ba.", "Chiacchieriamo ascoltando un po’ di musica.", ["咱们", "听着", "音乐", "聊天儿", "吧", "。"]),
    ("你好像不太高兴。", "Nǐ hǎoxiàng bú tài gāoxìng.", "Sembri un po’ giù.", ["你", "好像", "不太", "高兴", "。"]),
    ("我觉得他不太高兴。", "Wǒ juéde tā bú tài gāoxìng.", "Mi sembra che lui sia un po’ giù.", ["我", "觉得", "他", "不太", "高兴", "。"]),
  ],
  qa=[
    ("Bussano alla porta. Come chiedi chi è?", "", ["谁啊？", "什么啊？", "哪儿啊？", "几啊？"], "谁 = chi."),
    ("Ti chiedono 「你干什么呢？」 e stai facendo i compiti. Cosa rispondi?", "nǐ gàn shénme ne?", ["我做作业呢。", "我做作业吗。", "我做了作业呢。", "做作业我呢。"], "Verbo + oggetto + 呢 = azione in corso."),
    ("Parli con il tuo compagno: vuoi dire “andiamo noi due insieme”. Quale pronome usi?", "", ["咱们", "他们", "你们", "她们"], "咱们 include sempre chi ascolta."),
    ("Un amico ti racconta una notizia incredibile. Cosa rispondi?", "", ["真的吗？", "是的吗？", "对吗了？", "真吗的？"], "真的吗 = davvero?"),
    ("「我有点儿想家。」 significa…", "wǒ yǒudiǎnr xiǎng jiā.", ["Ho un po’ di nostalgia di casa.", "Voglio comprare una casa.", "Penso un po’ alla scuola.", "Sono a casa da un po’."], "想家 = sentire la mancanza di casa."),
    ("Quale frase descrive un’azione in corso?", "", ["我听音乐呢。", "我听了音乐。", "我听过音乐。", "我要听音乐。"], "呢 indica un’azione in svolgimento."),
    ("Quale frase è corretta?", "", ["这件衣服有点儿贵。", "这件衣服贵有点儿。", "这件衣服一点儿贵。", "这件衣服有贵点儿。"], "有点儿 va prima dell’aggettivo."),
  ],
  extra=[("Poesia", "七步诗 · 曹植", "煮豆燃豆萁，豆在釜中泣。本是同根生，相煎何太急？",
          "Zhǔ dòu rán dòu qí, dòu zài fǔ zhōng qì. Běn shì tóng gēn shēng, xiāng jiān hé tài jí?",
          "Si cuociono i fagioli bruciando i loro steli; nella pentola i fagioli piangono: “Siamo nati dalla stessa radice, perché tanta fretta di tormentarci?” (Secondo la leggenda Cao Zhi la compose in sette passi, per ordine del fratello imperatore.)"),
         ("Scioglilingua", "牙刷能刷牙", "牙刷能刷牙，刷牙用牙刷。", "Yáshuā néng shuā yá, shuā yá yòng yáshuā.",
          "Lo spazzolino lava i denti, per lavare i denti si usa lo spazzolino. (Per sh / s)")],
)

# ───────────────────────────── Lezione 13 ─────────────────────────────
L(n=13, zh="我去图书馆借书", py="Wǒ qù túshūguǎn jiè shū", it="Vado in biblioteca a prendere libri in prestito",
  theme="Biblioteca, acquisti online, spedire e ricevere pacchi",
  vocab="""
N|图书馆|túshūguǎn|名|biblioteca|library
N|借|jiè|动|prendere / dare in prestito|to borrow, lend
N|要是|yàoshi|连|se|if
N|和|hé|连,介|e; con|and; with
N|不过|búguò|连|però, ma|but
N|自习|zìxí|动|studiare da solo|self-study
N|着急|zháo jí||preoccuparsi, avere fretta|worried, anxious
N|网|wǎng|名|rete, internet|net, internet
N|上|shàng|动,名|salire; andare (online, a scuola, al piano di sopra); precedente|to go up; to go online; previous
N|方便|fāngbiàn|形|comodo, pratico|convenient
N|价钱|jiàqian|名|prezzo|price
N|下|xià|动,名|scendere; cadere (la pioggia); fare (un ordine); prossimo|to go down; to fall; to place (an order); next
N|订单|dìngdān|名|ordine (d’acquisto)|order
N|送|sòng|动|consegnare; regalare; accompagnare qualcuno|to deliver; to give; to see off
N|快|kuài|形|veloce|fast
N|寄|jì|动|spedire|to mail
N|快递|kuàidì|名|corriere espresso; pacco|express delivery
N|填|tián|动|compilare|to fill in
N|一下|yíxià|数量|un attimo (V + 一下)|once, a bit
N|单|dān|名|modulo, scheda|form
N|对方|duìfāng|名|l’altra parte, il destinatario|the other party
N|付款|fù kuǎn||pagare|to pay
N|找|zhǎo|动|cercare; dare il resto|to look for; to give change
N|刚才|gāngcái|名|poco fa|just now
N|收|shōu|动|ricevere, incassare|to receive
N|旅行|lǚxíng|动|viaggiare|to travel
N|先生|xiānsheng|名|signore; marito|Mr., sir
N|错|cuò|形|sbagliato|wrong
N|手机|shǒujī|名|cellulare|mobile phone
P|英文|Yīngwén||inglese (lingua scritta)|English
P|上海|Shànghǎi||Shanghai|Shanghai
P|西安|Xī’ān||Xi’an|Xi'an
S|话|huà|名|parole, discorso|words
S|发|fā|动|inviare (messaggi, email)|to send
S|用|yòng|动|usare|to use
S|电脑|diànnǎo|名|computer|computer
S|常常|chángcháng|副|spesso|often
S|地址|dìzhǐ|名|indirizzo|address
""",
  grammar=[
    ("要是……就……", "“Se… allora…”: 要是 introduce la condizione, 就 (prima del verbo) la conseguenza.",
     [("要是你不懂，就问老师。", "Yàoshi nǐ bù dǒng, jiù wèn lǎoshī.", "Se non capisci, chiedi all’insegnante."),
      ("要是明天有时间，我就去图书馆。", "Yàoshi míngtiān yǒu shíjiān, wǒ jiù qù túshūguǎn.", "Se domani ho tempo, vado in biblioteca.")]),
    ("不过 e 可是", "Entrambi significano “ma, però”. 不过 è più morbido e spesso aggiunge solo una precisazione; 可是 marca un contrasto più netto.",
     [("这本书很好，不过有点儿贵。", "Zhè běn shū hěn hǎo, búguò yǒudiǎnr guì.", "Questo libro è ottimo, però è un po’ caro.")]),
    ("Verbo + 到", "到 dopo il verbo indica che l’azione raggiunge il suo scopo (借到 = riuscire a prendere in prestito) o arriva in un luogo (送到宿舍, 寄到上海). Negazione: 没(有) + V + 到.",
     [("我没借到那本书。", "Wǒ méi jièdào nà běn shū.", "Non sono riuscito a prendere in prestito quel libro."),
      ("快递送到我的宿舍了。", "Kuàidì sòngdào wǒ de sùshè le.", "Il pacco è stato consegnato al mio dormitorio.")]),
    ("就: prima del previsto", "就 prima del verbo sottolinea che l’azione avviene presto o facilmente (il contrario di 才).",
     [("我八点就起床了。", "Wǒ bā diǎn jiù qǐ chuáng le.", "Mi sono alzato già alle otto."),
      ("今天上午书就送到了。", "Jīntiān shàngwǔ shū jiù sòngdào le.", "Il libro è arrivato già stamattina.")]),
    ("Verbo + 一下", "Rende l’azione breve o la richiesta più cortese: 填一下, 看一下, 等一下.",
     [("请您填一下这个单子。", "Qǐng nín tián yíxià zhège dānzi.", "Compili questo modulo, per favore.")]),
    ("和", "“E / con”: collega nomi e pronomi, non frasi intere. 和……一起 = insieme a…",
     [("我和你一起去。", "Wǒ hé nǐ yìqǐ qù.", "Vengo con te.")]),
  ],
  dialogue=("Comprare un libro online", [
    ("朴志永", "刘伟，我想买一本英文书，图书馆没有。", "Liú Wěi, wǒ xiǎng mǎi yì běn Yīngwén shū, túshūguǎn méiyǒu.", "Liu Wei, voglio comprare un libro in inglese: in biblioteca non c’è."),
    ("刘伟", "你在网上买吧，很方便，价钱也不贵。", "Nǐ zài wǎng shang mǎi ba, hěn fāngbiàn, jiàqian yě bú guì.", "Compralo online: è comodo e il prezzo non è alto."),
    ("朴志永", "可是我不知道怎么买。", "Kěshì wǒ bù zhīdào zěnme mǎi.", "Ma non so come si fa."),
    ("刘伟", "没问题，我帮你下订单。", "Méi wèntí, wǒ bāng nǐ xià dìngdān.", "Nessun problema, ti aiuto a fare l’ordine."),
    ("朴志永", "书能送到宿舍吗？", "Shū néng sòngdào sùshè ma?", "Il libro può essere consegnato in dormitorio?"),
    ("刘伟", "能。要是今天下订单，明天就能送到。", "Néng. Yàoshi jīntiān xià dìngdān, míngtiān jiù néng sòngdào.", "Sì. Se ordini oggi, arriva già domani."),
    ("朴志永", "太好了！我怎么付款？", "Tài hǎo le! Wǒ zěnme fù kuǎn?", "Fantastico! Come pago?"),
    ("刘伟", "用手机付款，很方便。", "Yòng shǒujī fù kuǎn, hěn fāngbiàn.", "Paghi con il cellulare, è semplicissimo."),
  ]),
  reading=("Un pacco velocissimo",
    "昨天下午山田在网上买了一个手机。今天上午快递员就送到他的宿舍了。快递员说：“请你看一下，没有问题就在这儿写你的名字。”山田看了一下，手机很好。他说：“太快了！谢谢你！”",
    "Zuótiān xiàwǔ Shāntián zài wǎng shang mǎile yí ge shǒujī. Jīntiān shàngwǔ kuàidìyuán jiù sòngdào tā de sùshè le. Kuàidìyuán shuō: “Qǐng nǐ kàn yíxià, méiyǒu wèntí jiù zài zhèr xiě nǐ de míngzi.” Shāntián kànle yíxià, shǒujī hěn hǎo. Tā shuō: “Tài kuài le! Xièxie nǐ!”",
    "Ieri pomeriggio Yamada ha comprato un cellulare online. Stamattina il corriere l’ha già consegnato al suo dormitorio. Il corriere dice: “Controlli un attimo: se è tutto a posto, scriva qui il suo nome.” Yamada controlla: il cellulare è perfetto. Dice: “Velocissimo! Grazie!”",
    [("山田在网上买了什么？", "Shāntián zài wǎng shang mǎile shénme?", ["一个手机", "一本书", "一件衣服", "一台电脑"]),
     ("手机送到哪儿了？", "Shǒujī sòngdào nǎr le?", ["山田的宿舍", "图书馆", "教室", "办公室"]),
     ("山田觉得怎么样？", "Shāntián juéde zěnmeyàng?", ["太快了", "太贵了", "有点儿慢", "不方便"])]),
  cloze=[
    ("我去图书馆 ___ 书。", "Wǒ qù túshūguǎn ___ shū.", "Vado in biblioteca a prendere libri in prestito.", ["借", "送", "寄", "收"], "借 = prendere in prestito."),
    ("___ 你不懂，就问老师。", "___ nǐ bù dǒng, jiù wèn lǎoshī.", "Se non capisci, chiedi all’insegnante.", ["要是", "不过", "可是", "所以"], "要是……就…… = se… allora…"),
    ("我去了图书馆，可是没借 ___ 那本书。", "Wǒ qùle túshūguǎn, kěshì méi jiè ___ nà běn shū.", "Sono andato in biblioteca, ma non sono riuscito a prendere quel libro.", ["到", "在", "了", "的"], "没 V 到 = non riuscire a ottenere."),
    ("请你填 ___ 快递单。", "Qǐng nǐ tián ___ kuàidìdān.", "Compila un attimo il modulo di spedizione.", ["一下", "一点儿", "有点儿", "一会儿"], "V + 一下 = un attimo."),
    ("这本书很好，___ 有点儿贵。", "Zhè běn shū hěn hǎo, ___ yǒudiǎnr guì.", "Questo libro è ottimo, però è un po’ caro.", ["不过", "要是", "所以", "和"], "不过 = però."),
    ("快递今天上午 ___ 送到了。", "Kuàidì jīntiān shàngwǔ ___ sòngdào le.", "Il pacco è arrivato già stamattina.", ["就", "才", "都", "还"], "就 + 了 = prima del previsto (才 non va con 了)."),
    ("图书馆几点 ___ 门？", "Túshūguǎn jǐ diǎn ___ mén?", "A che ora chiude la biblioteca?", ["关", "借", "收", "填"], "关门 = chiudere."),
    ("您给我五十，我 ___ 您十块。", "Nín gěi wǒ wǔshí, wǒ ___ nín shí kuài.", "Mi dà cinquanta, le do dieci di resto.", ["找", "收", "送", "借"], "找(钱) = dare il resto."),
  ],
  reorder=[
    ("我去图书馆借书。", "Wǒ qù túshūguǎn jiè shū.", "Vado in biblioteca a prendere libri in prestito.", ["我", "去", "图书馆", "借", "书", "。"]),
    ("在网上买东西很方便。", "Zài wǎng shang mǎi dōngxi hěn fāngbiàn.", "Comprare online è molto comodo.", ["在", "网上", "买", "东西", "很", "方便", "。"]),
    ("请您填一下快递单。", "Qǐng nín tián yíxià kuàidìdān.", "Compili il modulo di spedizione, per favore.", ["请", "您", "填", "一下", "快递单", "。"]),
    ("我没有借到那本书。", "Wǒ méiyǒu jièdào nà běn shū.", "Non sono riuscito a prendere quel libro.", ["我", "没有", "借到", "那本", "书", "。"]),
    ("书送到我的宿舍了。", "Shū sòngdào wǒ de sùshè le.", "Il libro è arrivato al mio dormitorio.", ["书", "送到", "我的", "宿舍", "了", "。"]),
    ("要是你不懂，就问老师。", "Yàoshi nǐ bù dǒng, jiù wèn lǎoshī.", "Se non capisci, chiedi all’insegnante.", ["要是", "你", "不懂", "，", "就", "问", "老师", "。"]),
  ],
  qa=[
    ("Vuoi sapere a che ora chiude la biblioteca. Cosa chiedi?", "", ["图书馆几点关门？", "图书馆关门几点？", "几点图书馆关？", "图书馆是几点关吗？"], "Il tempo va prima del verbo: 几点 + 关门."),
    ("Quale frase usa 和 correttamente?", "", ["我和他都是留学生。", "我是留学生，和他也是。", "我喜欢茶，和我喜欢咖啡。", "和我去图书馆了。"], "和 collega nomi e pronomi, non frasi."),
    ("Il corriere dice 「对方付款」. Che cosa significa?", "duìfāng fù kuǎn", ["Paga il destinatario.", "Paga il mittente.", "È gratis.", "Si paga in contanti."], "对方 = l’altra parte."),
    ("「我没借到那本书。」 significa…", "wǒ méi jièdào nà běn shū.", ["Non sono riuscito a prendere in prestito quel libro.", "Non ho voluto quel libro.", "Ho restituito quel libro.", "Ho comprato quel libro."], "没 V 到 = non riuscire a ottenere."),
    ("Paghi 20 yuan per un pacco che ne costa 15. Il corriere ti dice:", "", ["找您五块。", "收您五块。", "送您五块。", "借您五块。"], "找钱 = dare il resto."),
    ("Quale coppia significa “ma, però”?", "", ["不过 / 可是", "要是 / 就", "和 / 也", "所以 / 还"], "不过 e 可是 = ma, però."),
    ("Ti chiedono 「你常常在网上买东西吗？」 e lo fai spesso. Cosa rispondi?", "nǐ chángcháng zài wǎng shang mǎi dōngxi ma?", ["对，很方便。", "对，很着急。", "不，很方便。", "对，没借到。"], "常常 = spesso."),
  ],
  extra=[("Poesia", "山居秋暝 · 王维 (prima strofa)", "空山新雨后，天气晚来秋。明月松间照，清泉石上流。",
          "Kōng shān xīn yǔ hòu, tiānqì wǎn lái qiū. Míng yuè sōng jiān zhào, qīng quán shí shàng liú.",
          "Sulla montagna deserta, dopo la pioggia appena caduta, l’aria della sera sa d’autunno. La luna chiara brilla tra i pini, la sorgente limpida scorre sulle pietre.")],
)
