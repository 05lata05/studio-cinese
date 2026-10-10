# -*- coding: utf-8 -*-
"""Lezioni 20-25 (formato descritto in lessons_a.py)."""

LESSONS = []
L = lambda **kw: LESSONS.append(kw)

# ───────────────────────────── Lezione 20 ─────────────────────────────
L(n=20, zh="你的爱好是什么？", py="Nǐ de àihào shì shénme?", it="Qual è il tuo hobby?",
  theme="Hobby, sport e tempo libero; elencare attività; cause e conseguenze",
  vocab="""
N|一般|yìbān|形|di solito; normale|usually; ordinary
N|啦|la|助|particella per elencare (……啦、……啦)|particle (listing)
N|录音|lù yīn||registrazione; registrare|recording
N|旧|jiù|形|vecchio (oggetti), usato|old
N|预习|yùxí|动|preparare la lezione in anticipo|to preview
N|新|xīn|形|nuovo|new
N|节目|jiémù|名|programma, spettacolo|programme
N|周末|zhōumò|名|fine settimana|weekend
N|爬|pá|动|arrampicarsi, salire|to climb
N|山|shān|名|montagna|mountain
N|座|zuò|量|classificatore per monti, edifici, città|MW for mountains, buildings
N|累|lèi|形|stanco; faticoso|tired
N|逛|guàng|动|girare, passeggiare (per negozi)|to stroll
N|街|jiē|名|strada, via|street
N|更|gèng|副|ancora più|even more
N|体育|tǐyù|名|sport, educazione fisica|sports
N|运动|yùndòng|名,动|sport; fare sport|sport; to exercise
N|乒乓球|pīngpāngqiú|名|ping-pong|table tennis
N|队|duì|名|squadra|team
N|差不多|chàbuduō|副,形|quasi; più o meno uguale|almost; about the same
N|学|xué|动|studiare, imparare|to study, learn
N|因为|yīnwèi|连|perché (causa)|because
N|商店|shāngdiàn|名|negozio|shop
S|爱|ài|动|amare|to love
S|记|jì|动|ricordare, annotare|to remember
S|容易|róngyì|形|facile|easy
S|自己|zìjǐ|代|se stesso, da solo|oneself
S|出租车|chūzūchē|名|taxi|taxi
S|公共汽车|gōnggòng qìchē|名|autobus|bus
S|词语|cíyǔ|名|parole ed espressioni|words and phrases
S|附近|fùjìn|名|vicinanze, nei dintorni|nearby
""",
  grammar=[
    ("……啦、……啦", "Nel parlato, 啦 dopo ogni elemento serve a elencare più attività o cose, con tono vivace.",
     [("晚上我一般做作业啦、听录音啦、预习新课啦……", "Wǎnshang wǒ yìbān zuò zuòyè la, tīng lùyīn la, yùxí xīn kè la……", "La sera di solito faccio i compiti, ascolto le registrazioni, preparo la lezione nuova…")]),
    ("真是个……", "真是 + (一)个 + nome esprime un giudizio forte: “sei proprio un…”.",
     [("你真是个好老师！", "Nǐ zhēn shì ge hǎo lǎoshī!", "Sei proprio un bravo insegnante!")]),
    ("差不多", "Come avverbio: “quasi” (差不多每天 = quasi ogni giorno). Come aggettivo: “più o meno uguale”.",
     [("我差不多每个周末都去爬山。", "Wǒ chàbuduō měi ge zhōumò dōu qù pá shān.", "Vado in montagna quasi ogni fine settimana."),
      ("他和我的汉语水平差不多。", "Tā hé wǒ de Hànyǔ shuǐpíng chàbuduō.", "Il suo livello di cinese è più o meno come il mio.")]),
    ("更 (ancora più)", "更 + aggettivo / verbo: un grado ancora maggiore. Si usa anche con 比.",
     [("我喜欢运动，更喜欢打乒乓球。", "Wǒ xǐhuan yùndòng, gèng xǐhuan dǎ pīngpāngqiú.", "Mi piace lo sport, e ancora di più il ping-pong."),
      ("坐出租车比坐公共汽车更快。", "Zuò chūzūchē bǐ zuò gōnggòng qìchē gèng kuài.", "Il taxi è ancora più veloce dell’autobus.")]),
    ("因为……所以……", "因为 introduce la causa, 所以 la conseguenza (si può usare anche uno solo dei due).",
     [("因为下雨，所以我们没去爬山。", "Yīnwèi xià yǔ, suǒyǐ wǒmen méi qù pá shān.", "Siccome pioveva, non siamo andati in montagna.")]),
    ("一般 · 打 + palla", "一般 = di solito. Con gli sport con la palla si usa 打: 打乒乓球, 打篮球.",
     [("周末我一般去逛街。", "Zhōumò wǒ yìbān qù guàng jiē.", "Nel fine settimana di solito vado in giro per negozi."),
      ("你会打乒乓球吗？", "Nǐ huì dǎ pīngpāngqiú ma?", "Sai giocare a ping-pong?")]),
  ],
  dialogue=("Progetti per il fine settimana", [
    ("刘伟", "我喜欢听音乐，也喜欢唱歌。你的爱好是什么？", "Wǒ xǐhuan tīng yīnyuè, yě xǐhuan chàng gē. Nǐ de àihào shì shénme?", "A me piace ascoltare musica e cantare. Qual è il tuo hobby?"),
    ("朴志永", "我爱运动：打篮球啦、爬山啦、骑自行车啦……", "Wǒ ài yùndòng: dǎ lánqiú la, pá shān la, qí zìxíngchē la……", "Adoro lo sport: basket, montagna, bicicletta…"),
    ("刘伟", "你真厉害！", "Nǐ zhēn lìhai!", "Sei fortissimo!"),
    ("朴志永", "这个周末我去西山爬山，你也去吧？", "Zhège zhōumò wǒ qù Xīshān pá shān, nǐ yě qù ba?", "Questo fine settimana vado a scalare le Colline dell’Ovest: vieni anche tu?"),
    ("刘伟", "我不太喜欢爬山。我们一起去唱歌，怎么样？", "Wǒ bú tài xǐhuan pá shān. Wǒmen yìqǐ qù chàng gē, zěnmeyàng?", "La montagna non mi piace molto. Che ne dici se andiamo a cantare insieme?"),
    ("朴志永", "好，星期六爬山，星期天唱歌！", "Hǎo, xīngqīliù pá shān, xīngqītiān chàng gē!", "Va bene: sabato montagna, domenica karaoke!"),
    ("刘伟", "那你的周末更累了！", "Nà nǐ de zhōumò gèng lèi le!", "Così il tuo fine settimana sarà ancora più stancante!"),
  ]),
  reading=("Gli hobby di Li Wenjing",
    "李文静的爱好很多，她喜欢看书、听音乐，也喜欢体育。她是学校篮球队的，差不多每天下午都练习一个小时。周末她一般和朋友去附近的商店逛街。她说：“逛街不累，学习更累！”",
    "Lǐ Wénjìng de àihào hěn duō, tā xǐhuan kàn shū, tīng yīnyuè, yě xǐhuan tǐyù. Tā shì xuéxiào lánqiúduì de, chàbuduō měi tiān xiàwǔ dōu liànxí yí ge xiǎoshí. Zhōumò tā yìbān hé péngyou qù fùjìn de shāngdiàn guàng jiē. Tā shuō: “Guàng jiē bú lèi, xuéxí gèng lèi!”",
    "Li Wenjing ha molti hobby: le piace leggere, ascoltare musica e anche lo sport. Fa parte della squadra di basket della scuola e quasi ogni pomeriggio si allena per un’ora. Nel fine settimana di solito va in giro per i negozi qui vicino con le amiche. Dice: “Girare per negozi non stanca: è studiare che stanca di più!”",
    [("李文静是什么队的？", "Lǐ Wénjìng shì shénme duì de?", ["篮球队", "乒乓球队", "足球队", "汉语队"]),
     ("她差不多每天都做什么？", "Tā chàbuduō měi tiān dōu zuò shénme?", ["练习打篮球", "逛街", "看电视", "爬山"]),
     ("周末她一般干什么？", "Zhōumò tā yìbān gàn shénme?", ["和朋友逛街", "去爬山", "在宿舍睡觉", "回家"]),
     ("她觉得什么更累？", "Tā juéde shénme gèng lèi?", ["学习", "逛街", "运动", "爬山"])]),
  cloze=[
    ("我喜欢看书啦、听音乐 ___……", "Wǒ xǐhuan kàn shū la, tīng yīnyuè ___……", "Mi piace leggere, ascoltare musica…", ["啦", "吗", "吧", "呢"], "啦 serve a elencare."),
    ("你 ___ 是个好学生！", "Nǐ ___ shì ge hǎo xuésheng!", "Sei proprio un bravo studente!", ["真", "很", "太", "更"], "真是个… = sei proprio un…"),
    ("我 ___ 每个周末都去爬山。", "Wǒ ___ měi ge zhōumò dōu qù pá shān.", "Vado in montagna quasi ogni fine settimana.", ["差不多", "因为", "自己", "容易"], "差不多 = quasi."),
    ("___ 下雨，所以我们没去爬山。", "___ xià yǔ, suǒyǐ wǒmen méi qù pá shān.", "Siccome pioveva, non siamo andati in montagna.", ["因为", "所以", "要是", "可是"], "因为……所以……"),
    ("逛街很累，学习 ___ 累。", "Guàng jiē hěn lèi, xuéxí ___ lèi.", "Girare per negozi stanca, studiare stanca ancora di più.", ["更", "比", "因为", "一般"], "更 = ancora più."),
    ("周末你 ___ 干什么？", "Zhōumò nǐ ___ gàn shénme?", "Nel fine settimana che cosa fai di solito?", ["一般", "更", "因为", "差不多"], "一般 = di solito."),
    ("这座山很高，爬上去很 ___。", "Zhè zuò shān hěn gāo, pá shangqu hěn ___.", "Questa montagna è alta: salirci è faticoso.", ["累", "旧", "新", "节目"], "累 = stanco, faticoso."),
    ("你会 ___ 乒乓球吗？", "Nǐ huì ___ pīngpāngqiú ma?", "Sai giocare a ping-pong?", ["打", "做", "爬", "逛"], "打 + sport con la palla."),
    ("学校附近有一 ___ 山。", "Xuéxiào fùjìn yǒu yí ___ shān.", "Vicino alla scuola c’è una montagna.", ["座", "本", "件", "辆"], "座 = classificatore per montagne ed edifici."),
  ],
  reorder=[
    ("你的爱好是什么？", "Nǐ de àihào shì shénme?", "Qual è il tuo hobby?", ["你的", "爱好", "是", "什么", "？"]),
    ("你真是个好学生。", "Nǐ zhēn shì ge hǎo xuésheng.", "Sei proprio un bravo studente.", ["你", "真", "是", "个", "好学生", "。"]),
    ("周末我一般去逛街。", "Zhōumò wǒ yìbān qù guàng jiē.", "Nel fine settimana di solito vado per negozi.", ["周末", "我", "一般", "去", "逛街", "。"]),
    ("我差不多每天都运动。", "Wǒ chàbuduō měi tiān dōu yùndòng.", "Faccio sport quasi tutti i giorni.", ["我", "差不多", "每天", "都", "运动", "。"]),
    ("因为下雨，所以我们没去。", "Yīnwèi xià yǔ, suǒyǐ wǒmen méi qù.", "Siccome pioveva, non ci siamo andati.", ["因为", "下雨", "，", "所以", "我们", "没去", "。"]),
    ("他是学校乒乓球队的。", "Tā shì xuéxiào pīngpāngqiúduì de.", "Fa parte della squadra di ping-pong della scuola.", ["他", "是", "学校", "乒乓球队", "的", "。"]),
  ],
  qa=[
    ("Ti chiedono 「你的爱好是什么？」. Quale risposta è adatta?", "nǐ de àihào shì shénme?", ["我喜欢运动，特别是打篮球。", "我是学生。", "我的专业是汉语。", "我住三号楼。"], "爱好 = hobby."),
    ("Un amico elenca: 「看书啦、听音乐啦……」. A che cosa serve 啦?", "la", ["A elencare più cose", "A fare una domanda", "A dare un ordine", "A indicare il passato"], "……啦、……啦 = elenco nel parlato."),
    ("Quale frase usa correttamente 更?", "", ["坐出租车比坐公共汽车更快。", "坐出租车更比坐公共汽车快。", "坐出租车比更坐公共汽车快。", "更坐出租车比坐公共汽车快。"], "更 va subito prima dell’aggettivo."),
    ("「他们的汉语水平差不多。」 significa…", "tāmen de Hànyǔ shuǐpíng chàbuduō.", ["Hanno più o meno lo stesso livello di cinese.", "Il loro cinese è quasi perfetto.", "Il loro cinese è molto diverso.", "Non studiano quasi il cinese."], "差不多 = più o meno uguale."),
    ("Un compagno nota che studi moltissimo e dice:", "", ["你真是个好学生！", "你是真个好学生！", "你个真是好学生！", "你真好学生是个！"], "真是 + 个 + nome."),
    ("Vuoi dire “Siccome pioveva, non siamo andati”. Quale frase è corretta?", "", ["因为下雨，所以我们没去。", "所以下雨，因为我们没去。", "因为我们没去，所以下雨。", "下雨因为，我们没去所以。"], "因为 = causa, 所以 = conseguenza."),
    ("Che sport si indica con 「打乒乓球」?", "dǎ pīngpāngqiú", ["Ping-pong", "Basket", "Calcio", "Nuoto"], "乒乓球 = ping-pong."),
  ],
  extra=[("Poesia", "春夜喜雨 · 杜甫 (prima strofa)", "好雨知时节，当春乃发生。随风潜入夜，润物细无声。",
          "Hǎo yǔ zhī shíjié, dāng chūn nǎi fāshēng. Suí fēng qián rù yè, rùn wù xì wú shēng.",
          "La pioggia buona conosce la sua stagione: arriva proprio in primavera. Segue il vento e si insinua nella notte, bagna ogni cosa, sottile e silenziosa."),
         ("Cultura", "Come chiamare le persone", "", "",
          "Con gli sconosciuti: 先生 per un uomo; 阿姨 o 大姐 per una donna, secondo l’età; 小朋友 per i bambini; 师傅 per tassisti, operai, cuochi. Con i conoscenti: cognome + titolo (李老师, 王大夫), oppure 小 + cognome per chi è più giovane (小王) e 老 + cognome per chi è più grande (老张).")],
)

# ───────────────────────────── Lezione 21 ─────────────────────────────
L(n=21, zh="八点我正在教室上课呢", py="Bā diǎn wǒ zhèngzài jiàoshì shàng kè ne", it="Alle otto ero in classe a lezione",
  theme="Raccontare quando, dove e come è successo qualcosa; azioni in corso; studiare i caratteri",
  vocab="""
N|正|zhèng|副|proprio; stare (facendo)|in the middle of
N|接|jiē|动|rispondere (al telefono); andare a prendere|to answer; to pick up
N|哎呀|āiyā|叹|oh! accidenti!|oh my!
N|电|diàn|名|elettricità; batteria|electricity
N|忘|wàng|动|dimenticare|to forget
N|充电|chōng diàn||ricaricare (la batteria)|to charge
N|张|zhāng|量|classificatore per oggetti piatti (biglietti, fogli, tavoli)|MW for flat things
N|票|piào|名|biglietto|ticket
N|约|yuē|动|dare appuntamento, invitare|to make an appointment
N|进步|jìnbù|动,形|fare progressi; progresso|to make progress
N|哪里|nǎli|代|ma no! (risposta modesta); dove|not at all; where
N|课本|kèběn|名|libro di testo|textbook
N|办|bàn|动|fare, sbrigare|to do, handle
N|办法|bànfǎ|名|modo, soluzione|way, method
N|跟|gēn|介,连,动|con; e; seguire|with; and; to follow
N|怕|pà|动|avere paura, temere|to be afraid
N|只要……就……|zhǐyào…jiù…||basta che… e allora…|as long as… then…
N|字|zì|名|carattere, parola scritta|character
N|记住|jìzhù||memorizzare, ricordare bene|to remember firmly
N|读|dú|动|leggere (ad alta voce); studiare|to read
N|课文|kèwén|名|testo della lezione|lesson text
N|拼音|pīnyīn|名|pinyin|pinyin
N|最|zuì|副|il più|the most
N|不要|búyào|副|non (imperativo)|don't
N|火车|huǒchē|名|treno|train
N|大学|dàxué|名|università|university
S|去年|qùnián|名|l’anno scorso|last year
""",
  grammar=[
    ("是……的", "Per un’azione già avvenuta, 是……的 mette in risalto QUANDO, DOVE, COME o CON CHI è successa. 是 si può omettere nelle affermazioni, ma non nelle negazioni (不是……的).",
     [("你是什么时候来中国的？——我是去年来的。", "Nǐ shì shénme shíhou lái Zhōngguó de? — Wǒ shì qùnián lái de.", "Quando sei venuto in Cina? — L’anno scorso."),
      ("我是坐火车来的，不是坐飞机来的。", "Wǒ shì zuò huǒchē lái de, bú shì zuò fēijī lái de.", "Sono venuto in treno, non in aereo.")]),
    ("正在……呢", "Indica un’azione in corso in un certo momento, anche nel passato: “stavo facendo”.",
     [("你来的时候，我正在看书呢。", "Nǐ lái de shíhou, wǒ zhèngzài kàn shū ne.", "Quando sei arrivato stavo leggendo.")]),
    ("哪里", "Risposta modesta a un complimento: “ma no, macché”. Spesso ripetuto: 哪里哪里.",
     [("你的汉语进步很大！——哪里，哪里。", "Nǐ de Hànyǔ jìnbù hěn dà! — Nǎli, nǎli.", "Il tuo cinese è migliorato molto! — Ma no, figurati.")]),
    ("只要……就……", "“Basta che… e allora…”: la condizione è sufficiente per ottenere il risultato.",
     [("只要你每天读课文，就能记住生词。", "Zhǐyào nǐ měi tiān dú kèwén, jiù néng jìzhù shēngcí.", "Basta che tu legga il testo ogni giorno e memorizzerai le parole nuove.")]),
    ("快……了", "“Sta per…”: 快 + verbo / tempo + 了.",
     [("快下课了。", "Kuài xià kè le.", "La lezione sta per finire."),
      ("快到周末了！", "Kuài dào zhōumò le!", "Tra poco è fine settimana!")]),
    ("不要 · 跟 · 最", "不要 + verbo = non… (divieto); 跟 + persona + (一起) + verbo = con qualcuno; 最 + aggettivo = il più.",
     [("不要只看拼音。", "Búyào zhǐ kàn pīnyīn.", "Non guardare solo il pinyin."),
      ("你跟我一起练习书法吧。", "Nǐ gēn wǒ yìqǐ liànxí shūfǎ ba.", "Esercitati nella calligrafia con me."),
      ("我最大的问题是汉字。", "Wǒ zuì dà de wèntí shì Hànzì.", "Il mio problema più grande sono i caratteri.")]),
  ],
  dialogue=("Un nuovo compagno", [
    ("山田", "你好！你是新来的同学吗？", "Nǐ hǎo! Nǐ shì xīn lái de tóngxué ma?", "Ciao! Sei il nuovo compagno?"),
    ("一学生", "对，我是上个星期来的。", "Duì, wǒ shì shàng ge xīngqī lái de.", "Sì, sono arrivato la settimana scorsa."),
    ("山田", "你是从哪儿来的？", "Nǐ shì cóng nǎr lái de?", "Da dove vieni?"),
    ("一学生", "我是从韩国来的。", "Wǒ shì cóng Hánguó lái de.", "Vengo dalla Corea."),
    ("山田", "你以前学过汉语吗？", "Nǐ yǐqián xuéguo Hànyǔ ma?", "Avevi già studiato cinese?"),
    ("一学生", "学过一年，是在大学学的。可是我认识的字不多。", "Xuéguo yì nián, shì zài dàxué xué de. Kěshì wǒ rènshi de zì bù duō.", "Sì, per un anno, all’università. Però conosco pochi caratteri."),
    ("山田", "别着急，只要每天读课文，就能记住。", "Bié zháojí, zhǐyào měi tiān dú kèwén, jiù néng jìzhù.", "Non preoccuparti: basta leggere il testo ogni giorno e li memorizzi."),
    ("一学生", "你的汉语说得真好！", "Nǐ de Hànyǔ shuō de zhēn hǎo!", "Parli davvero bene il cinese!"),
    ("山田", "哪里哪里。快上课了，咱们走吧！", "Nǎli nǎli. Kuài shàng kè le, zánmen zǒu ba!", "Ma no, figurati. Sta per iniziare la lezione, andiamo!"),
  ]),
  reading=("Una telefonata persa",
    "昨天晚上八点，王平给安妮打电话，安妮没有接，因为她正在图书馆自习呢。九点半她回宿舍以后才看到。她给王平打电话说：“对不起，我刚才正在自习呢。你有什么事？”王平说：“没什么事，我想问问你，明天的听写你准备好了吗？”",
    "Zuótiān wǎnshang bā diǎn, Wáng Píng gěi Ānnī dǎ diànhuà, Ānnī méiyǒu jiē, yīnwèi tā zhèngzài túshūguǎn zìxí ne. Jiǔ diǎn bàn tā huí sùshè yǐhòu cái kàndào. Tā gěi Wáng Píng dǎ diànhuà shuō: “Duìbuqǐ, wǒ gāngcái zhèngzài zìxí ne. Nǐ yǒu shénme shì?” Wáng Píng shuō: “Méi shénme shì, wǒ xiǎng wènwen nǐ, míngtiān de tīngxiě nǐ zhǔnbèi hǎo le ma?”",
    "Ieri sera alle otto Wang Ping ha telefonato ad Annie, ma lei non ha risposto perché stava studiando in biblioteca. Se n’è accorta solo alle nove e mezza, tornata in dormitorio. Ha richiamato Wang Ping: “Scusa, prima stavo studiando. Che cosa c’è?” Wang Ping ha risposto: “Niente di speciale, volevo chiederti se ti sei preparata per il dettato di domani.”",
    [("王平几点给安妮打电话？", "Wáng Píng jǐ diǎn gěi Ānnī dǎ diànhuà?", ["八点", "九点半", "十点", "七点"]),
     ("安妮为什么没有接电话？", "Ānnī wèi shénme méiyǒu jiē diànhuà?", ["她正在图书馆自习", "她的手机没电了", "她在睡觉", "她在上课"]),
     ("王平想问安妮什么？", "Wáng Píng xiǎng wèn Ānnī shénme?", ["听写准备好了没有", "看不看电影", "去不去吃饭", "她在哪儿"])]),
  cloze=[
    ("我 ___ 去年来中国的。", "Wǒ ___ qùnián lái Zhōngguó de.", "Sono venuto in Cina l’anno scorso.", ["是", "在", "要", "会"], "是……的 sottolinea il tempo."),
    ("你来的时候，我正在看书 ___。", "Nǐ lái de shíhou, wǒ zhèngzài kàn shū ___.", "Quando sei arrivato stavo leggendo.", ["呢", "吗", "吧", "过"], "正在……呢 = stare facendo."),
    ("你的汉语进步很大！——___。", "Nǐ de Hànyǔ jìnbù hěn dà! — ___.", "Il tuo cinese è migliorato molto! — Ma no, figurati.", ["哪里", "哪儿", "什么", "怎么"], "哪里 = risposta modesta."),
    ("___ 每天练习，就一定能学好。", "___ měi tiān liànxí, jiù yídìng néng xuéhǎo.", "Basta esercitarsi ogni giorno per imparare bene.", ["只要", "因为", "可是", "所以"], "只要……就…… = basta che…"),
    ("快上课 ___，我们走吧。", "Kuài shàng kè ___, wǒmen zǒu ba.", "Sta per iniziare la lezione, andiamo.", ["了", "的", "过", "着"], "快……了 = sta per…"),
    ("我的手机没电了，我忘了 ___。", "Wǒ de shǒujī méi diàn le, wǒ wàngle ___.", "Il cellulare è scarico: ho dimenticato di ricaricarlo.", ["充电", "接", "约", "办"], "充电 = ricaricare."),
    ("___ 只看拼音，要多看汉字。", "___ zhǐ kàn pīnyīn, yào duō kàn Hànzì.", "Non guardare solo il pinyin: guarda di più i caratteri.", ["不要", "没有", "不是", "不太"], "不要 + verbo = divieto."),
    ("我有两 ___ 电影票。", "Wǒ yǒu liǎng ___ diànyǐngpiào.", "Ho due biglietti del cinema.", ["张", "本", "件", "辆"], "张 = classificatore per oggetti piatti."),
    ("汉字太难了，我 ___ 学不会。", "Hànzì tài nán le, wǒ ___ xué bu huì.", "I caratteri sono troppo difficili: temo di non riuscire a impararli.", ["怕", "最", "跟", "约"], "怕 = temere."),
    ("这是我 ___ 喜欢的课。", "Zhè shì wǒ ___ xǐhuan de kè.", "Questa è la lezione che mi piace di più.", ["最", "跟", "怕", "太"], "最 = il più."),
  ],
  reorder=[
    ("我是去年来中国的。", "Wǒ shì qùnián lái Zhōngguó de.", "Sono venuto in Cina l’anno scorso.", ["我", "是", "去年", "来", "中国", "的", "。"]),
    ("八点我正在上课呢。", "Bā diǎn wǒ zhèngzài shàng kè ne.", "Alle otto ero a lezione.", ["八点", "我", "正在", "上课", "呢", "。"]),
    ("你是怎么来的？", "Nǐ shì zěnme lái de?", "Come sei venuto?", ["你", "是", "怎么", "来", "的", "？"]),
    ("只要多练习，就能学好。", "Zhǐyào duō liànxí, jiù néng xuéhǎo.", "Basta esercitarsi molto per imparare bene.", ["只要", "多", "练习", "，", "就", "能", "学好", "。"]),
    ("快到周末了。", "Kuài dào zhōumò le.", "Tra poco è fine settimana.", ["快", "到", "周末", "了", "。"]),
    ("你跟我一起练习书法吧。", "Nǐ gēn wǒ yìqǐ liànxí shūfǎ ba.", "Esercitati nella calligrafia con me.", ["你", "跟我", "一起", "练习", "书法", "吧", "。"]),
  ],
  qa=[
    ("Ti chiedono 「你是什么时候来中国的？」. Quale risposta è corretta?", "nǐ shì shénme shíhou lái Zhōngguó de?", ["我是去年来的。", "我去年来。", "我是去年来了。", "我是来的去年。"], "Si risponde con 是……的."),
    ("Ti fanno un complimento per il tuo cinese. Rispondi con modestia:", "", ["哪里哪里。", "哪儿哪儿。", "对，很好。", "没关系。"], "哪里哪里 = ma no, figurati."),
    ("「只要每天读课文，就能记住生词。」 significa…", "zhǐyào měi tiān dú kèwén, jiù néng jìzhù shēngcí.", ["Basta leggere il testo ogni giorno per memorizzare le parole nuove.", "Se non leggi ogni giorno ricordi le parole.", "Bisogna leggere solo le parole nuove.", "Le parole nuove si leggono ogni giorno."], "只要……就…… = condizione sufficiente."),
    ("Quale frase significa “Sta per iniziare la lezione”?", "", ["快上课了。", "上课快了。", "快了上课。", "上课了快。"], "快 + verbo + 了."),
    ("Il cellulare è scarico. Come lo dici?", "", ["我的手机没电了。", "我的手机没有充电了。", "我的电没有手机了。", "手机的我没电了。"], "没电了 = è scarico."),
    ("Ti chiedono 「你是坐火车来的吗？」 e sei venuto in aereo. Cosa rispondi?", "nǐ shì zuò huǒchē lái de ma?", ["不是，我是坐飞机来的。", "不是，我坐飞机来了的。", "没有，我是飞机。", "不，我是坐的飞机来。"], "Negazione: 不是……的."),
    ("「你来的时候，我正在洗衣服呢。」 Che cosa stava facendo chi parla?", "nǐ lái de shíhou, wǒ zhèngzài xǐ yīfu ne.", ["Stava lavando i vestiti.", "Stava comprando vestiti.", "Stava per uscire.", "Ti stava aspettando."], "正在……呢 = azione in corso."),
  ],
  extra=[("Poesia", "劝学 · 颜真卿", "三更灯火五更鸡，正是男儿读书时。黑发不知勤学早，白首方悔读书迟。",
          "Sān gēng dēnghuǒ wǔ gēng jī, zhèng shì nán’ér dú shū shí. Hēi fà bù zhī qín xué zǎo, bái shǒu fāng huǐ dú shū chí.",
          "La lampada accesa a mezzanotte, il gallo che canta all’alba: è proprio il tempo in cui i giovani studiano. Chi, con i capelli neri, non sa studiare presto e con impegno, con la testa bianca si pentirà di aver studiato troppo tardi.")],
)

# ───────────────────────────── Lezione 22 ─────────────────────────────
L(n=22, zh="旅行回来了", py="Lǚxíng huílái le", it="Di ritorno dal viaggio",
  theme="Raccontare un viaggio, distanze, azioni in sequenza e simultanee, pasti cinesi",
  vocab="""
N|回来|huílái||tornare (verso chi parla)|to come back
N|过|guò|动|passare, trascorrere|to spend (time)
N|离|lí|介|da (per indicare la distanza)|from (distance)
N|俩|liǎ|数|due, entrambi (persone)|two (people)
N|安排|ānpái|动,名|organizzare; programma|to arrange; arrangement
N|好玩儿|hǎowánr|形|divertente|fun
N|晚饭|wǎnfàn|名|cena|dinner
N|洗澡|xǐ zǎo||fare la doccia / il bagno|to take a shower
N|得|děi|助动|dovere|must, have to
N|公里|gōnglǐ|量|chilometro|kilometre
N|路上|lùshang|名|per strada, durante il tragitto|on the way
N|一边……一边……|yìbiān…yìbiān…||mentre… (due azioni insieme)|while…
N|出来|chūlái||uscire (verso chi parla)|to come out
N|顿|dùn|量|classificatore per pasti|MW for meals
N|刚|gāng|副|appena|just
N|一块儿|yíkuàir|副|insieme|together
N|以为|yǐwéi|动|credere (a torto)|to think (wrongly)
N|中餐|zhōngcān|名|cucina cinese, pasto cinese|Chinese food
N|笑|xiào|动|ridere, sorridere|to laugh
N|介绍|jièshào|动|presentare|to introduce
N|凉|liáng|形|fresco, freddo|cool, cold
N|饮料|yǐnliào|名|bevanda|beverage
N|最后|zuìhòu|名|alla fine, per ultimo|finally
N|有时候|yǒu shíhou||a volte|sometimes
N|水果|shuǐguǒ|名|frutta|fruit
N|厚|hòu|形|spesso (non sottile)|thick
S|句|jù|量|classificatore per frasi|MW for sentences
S|乌龙茶|wūlóngchá|名|tè oolong|oolong tea
S|着|zháo|动|(dopo il verbo) riuscire, raggiungere lo scopo|result complement
S|打工|dǎ gōng||lavorare part-time|to work part-time
S|重要|zhòngyào|形|importante|important
S|成绩|chéngjì|名|risultati, voti|results, grades
S|经历|jīnglì|名|esperienza (vissuta)|experience
""",
  grammar=[
    ("先……再……", "“Prima… poi…”: due azioni in sequenza (di solito future o abituali).",
     [("我们先去图书馆，再去食堂吧。", "Wǒmen xiān qù túshūguǎn, zài qù shítáng ba.", "Prima andiamo in biblioteca, poi in mensa.")]),
    ("一边……一边……", "Due azioni fatte contemporaneamente dalla stessa persona.",
     [("我常常一边吃饭，一边看手机。", "Wǒ chángcháng yìbiān chī fàn, yìbiān kàn shǒujī.", "Spesso mangio guardando il cellulare.")]),
    ("不是……吗？", "Domanda retorica che esprime sorpresa: “non avevi detto che…? / ma non…?”.",
     [("你不是去旅行了吗？怎么还在这儿？", "Nǐ bú shì qù lǚxíng le ma? Zěnme hái zài zhèr?", "Ma non eri partito per il viaggio? Come mai sei ancora qui?")]),
    ("以为", "“Credere (a torto)”: si pensava una cosa, ma la realtà è diversa.",
     [("我以为你是日本人，你是韩国人啊！", "Wǒ yǐwéi nǐ shì Rìběnrén, nǐ shì Hánguórén a!", "Credevo fossi giapponese, invece sei coreano!")]),
    ("离 (distanza)", "A 离 B + 远 / 近, oppure A 离 B + (有) + distanza.",
     [("宿舍离教室很近。", "Sùshè lí jiàoshì hěn jìn.", "Il dormitorio è vicino alle aule."),
      ("那个地方离学校有十几公里。", "Nàge dìfang lí xuéxiào yǒu shí jǐ gōnglǐ.", "Quel posto dista dalla scuola più di dieci chilometri.")]),
    ("得 děi + verbo", "“Dovere” (parlato). Attenzione: lo stesso carattere si legge de (complemento: 说得很好) e dé (ottenere: 得了感冒).",
     [("食堂快关门了，我们得快点儿去。", "Shítáng kuài guān mén le, wǒmen děi kuài diǎnr qù.", "La mensa sta per chiudere: dobbiamo sbrigarci.")]),
    ("俩 · 刚 / 刚才", "俩 = 两个 (persone): 我们俩. 刚 (avverbio) va prima del verbo; 刚才 (“poco fa”) è un’espressione di tempo e può stare anche prima del soggetto.",
     [("我们俩一块儿去吧。", "Wǒmen liǎ yíkuàir qù ba.", "Andiamoci insieme, noi due."),
      ("我刚到，还没吃饭呢。", "Wǒ gāng dào, hái méi chī fàn ne.", "Sono appena arrivato, non ho ancora mangiato.")]),
  ],
  dialogue=("Di ritorno da Xi’an", [
    ("山田", "彼得，你旅行回来了！玩儿得怎么样？", "Bǐdé, nǐ lǚxíng huílái le! Wánr de zěnmeyàng?", "Peter, sei tornato dal viaggio! Com’è andata?"),
    ("彼得", "好玩儿极了！", "Hǎowánr jíle!", "Divertentissimo!"),
    ("山田", "你去哪儿了？", "Nǐ qù nǎr le?", "Dove sei andato?"),
    ("彼得", "我去了西安，是坐火车去的。", "Wǒ qùle Xī’ān, shì zuò huǒchē qù de.", "Sono andato a Xi’an, in treno."),
    ("山田", "西安离这儿远吗？", "Xī’ān lí zhèr yuǎn ma?", "Xi’an è lontana da qui?"),
    ("彼得", "挺远的，坐火车得五个多小时。", "Tǐng yuǎn de, zuò huǒchē děi wǔ ge duō xiǎoshí.", "Abbastanza: in treno ci vogliono più di cinque ore."),
    ("山田", "你一个人去的吗？", "Nǐ yí ge rén qù de ma?", "Ci sei andato da solo?"),
    ("彼得", "不是，是跟刘伟一块儿去的。我们一边旅行，一边练习口语。", "Bú shì, shì gēn Liú Wěi yíkuàir qù de. Wǒmen yìbiān lǚxíng, yìbiān liànxí kǒuyǔ.", "No, con Liu Wei. Viaggiavamo e intanto ci esercitavamo a parlare."),
    ("山田", "太好了！你吃晚饭了吗？", "Tài hǎo le! Nǐ chī wǎnfàn le ma?", "Fantastico! Hai già cenato?"),
    ("彼得", "还没呢。我刚回来，先休息一下，再去吃饭。", "Hái méi ne. Wǒ gāng huílái, xiān xiūxi yíxià, zài qù chī fàn.", "Non ancora. Sono appena tornato: prima mi riposo un po’, poi vado a mangiare."),
  ]),
  reading=("Una gita in montagna",
    "上个周末，安妮和朋友们去了一个离学校三十多公里的地方，那儿的山非常漂亮。他们是坐公共汽车去的，路上一边聊天儿，一边听音乐。中午他们在一个小饭馆儿吃了一顿中餐，最后还吃了很多水果。晚上回来的时候，大家都很累，可是都觉得好玩儿极了。",
    "Shàng ge zhōumò, Ānnī hé péngyoumen qùle yí ge lí xuéxiào sānshí duō gōnglǐ de dìfang, nàr de shān fēicháng piàoliang. Tāmen shì zuò gōnggòng qìchē qù de, lùshang yìbiān liáo tiānr, yìbiān tīng yīnyuè. Zhōngwǔ tāmen zài yí ge xiǎo fànguǎnr chīle yí dùn zhōngcān, zuìhòu hái chīle hěn duō shuǐguǒ. Wǎnshang huílái de shíhou, dàjiā dōu hěn lèi, kěshì dōu juéde hǎowánr jíle.",
    "Lo scorso fine settimana Annie e i suoi amici sono andati in un posto a più di trenta chilometri dalla scuola, dove le montagne sono bellissime. Ci sono andati in autobus, chiacchierando e ascoltando musica lungo la strada. A mezzogiorno hanno fatto un pranzo cinese in una piccola trattoria e alla fine hanno mangiato anche tanta frutta. La sera, al ritorno, erano tutti stanchi, ma si erano divertiti un sacco.",
    [("那个地方离学校多远？", "Nàge dìfang lí xuéxiào duō yuǎn?", ["三十多公里", "十公里", "三公里", "一百公里"]),
     ("他们是怎么去的？", "Tāmen shì zěnme qù de?", ["坐公共汽车去的", "骑自行车去的", "坐火车去的", "走路去的"]),
     ("他们路上做什么？", "Tāmen lùshang zuò shénme?", ["一边聊天儿，一边听音乐", "一边骑车，一边唱歌", "睡觉", "看书"]),
     ("中午他们吃了什么？", "Zhōngwǔ tāmen chīle shénme?", ["一顿中餐", "饺子", "面包", "西餐"])]),
  cloze=[
    ("我们 ___ 去图书馆，再去食堂吧。", "Wǒmen ___ qù túshūguǎn, zài qù shítáng ba.", "Prima andiamo in biblioteca, poi in mensa.", ["先", "刚", "最后", "一边"], "先……再…… = prima… poi…"),
    ("我常常一边吃饭，___ 看手机。", "Wǒ chángcháng yìbiān chī fàn, ___ kàn shǒujī.", "Spesso mangio guardando il cellulare.", ["一边", "一起", "一块儿", "一下"], "一边……一边……"),
    ("你 ___ 去旅行了吗？怎么还在这儿？", "Nǐ ___ qù lǚxíng le ma? Zěnme hái zài zhèr?", "Ma non eri partito? Come mai sei ancora qui?", ["不是", "没有", "不要", "不用"], "不是……吗? = domanda retorica."),
    ("我 ___ 今天有课，可是今天没有课。", "Wǒ ___ jīntiān yǒu kè, kěshì jīntiān méiyǒu kè.", "Credevo che oggi ci fosse lezione, invece no.", ["以为", "知道", "希望", "介绍"], "以为 = credere a torto."),
    ("宿舍 ___ 教室很近。", "Sùshè ___ jiàoshì hěn jìn.", "Il dormitorio è vicino alle aule.", ["离", "从", "在", "往"], "A 离 B + 近/远."),
    ("食堂快关门了，我们 ___ 快点儿去。", "Shítáng kuài guān mén le, wǒmen ___ kuài diǎnr qù.", "La mensa sta per chiudere: dobbiamo sbrigarci.", ["得", "地", "的", "过"], "得 děi = dovere."),
    ("你们 ___ 一块儿去吧。", "Nǐmen ___ yíkuàir qù ba.", "Andateci insieme, voi due.", ["俩", "两", "二", "双"], "俩 = due (persone), senza classificatore."),
    ("我 ___ 到，还没吃饭呢。", "Wǒ ___ dào, hái méi chī fàn ne.", "Sono appena arrivato, non ho ancora mangiato.", ["刚", "最后", "以为", "有时候"], "刚 = appena."),
    ("我们吃了一 ___ 中餐。", "Wǒmen chīle yí ___ zhōngcān.", "Abbiamo fatto un pranzo cinese.", ["顿", "个", "件", "张"], "顿 = classificatore per i pasti."),
    ("___ 我坐公共汽车，有时候骑自行车。", "___ wǒ zuò gōnggòng qìchē, yǒu shíhou qí zìxíngchē.", "A volte prendo l’autobus, a volte vado in bici.", ["有时候", "最后", "刚", "一边"], "有时候……有时候…… = a volte… a volte…"),
  ],
  reorder=[
    ("我们先吃饭，再去看电影。", "Wǒmen xiān chī fàn, zài qù kàn diànyǐng.", "Prima mangiamo, poi andiamo al cinema.", ["我们", "先", "吃饭", "，", "再", "去", "看电影", "。"]),
    ("他一边听音乐，一边写作业。", "Tā yìbiān tīng yīnyuè, yìbiān xiě zuòyè.", "Fa i compiti ascoltando musica.", ["他", "一边", "听音乐", "，", "一边", "写", "作业", "。"]),
    ("学校离这儿有十公里。", "Xuéxiào lí zhèr yǒu shí gōnglǐ.", "La scuola dista dieci chilometri da qui.", ["学校", "离", "这儿", "有", "十", "公里", "。"]),
    ("你不是去旅行了吗？", "Nǐ bú shì qù lǚxíng le ma?", "Ma non eri partito per il viaggio?", ["你", "不是", "去", "旅行", "了", "吗", "？"]),
    ("我以为你回国了。", "Wǒ yǐwéi nǐ huí guó le.", "Credevo fossi tornato al tuo paese.", ["我", "以为", "你", "回国", "了", "。"]),
    ("我们俩一块儿去吧。", "Wǒmen liǎ yíkuàir qù ba.", "Andiamoci insieme, noi due.", ["我们", "俩", "一块儿", "去", "吧", "。"]),
  ],
  qa=[
    ("「我以为你回国了。」 significa…", "wǒ yǐwéi nǐ huí guó le.", ["Credevo (sbagliando) che fossi tornato al tuo paese.", "So che sei tornato al tuo paese.", "Spero che tu torni al tuo paese.", "Voglio che tu torni al tuo paese."], "以为 = credere a torto."),
    ("Quale frase descrive due azioni simultanee?", "", ["他一边吃饭，一边看电视。", "他先吃饭，再看电视。", "他吃了饭，看了电视。", "他最后看电视。"], "一边……一边……"),
    ("Ti chiedono 「你的宿舍离教室远吗？」 ed è vicino. Cosa rispondi?", "nǐ de sùshè lí jiàoshì yuǎn ma?", ["不远，很近。", "离很近。", "不离远。", "很近远。"], "离 + luogo + 远/近."),
    ("Come si dice “noi due”?", "", ["我们俩", "我们两", "我们二", "我们两俩"], "俩 = 两个."),
    ("Un amico doveva partire, ma lo incontri in dormitorio. Gli chiedi sorpreso:", "", ["你不是去旅行了吗？", "你是去旅行了吗？", "你去不去旅行了？", "你旅行了没有吗？"], "不是……吗? = sorpresa."),
    ("In 「我得走了。」 come si legge 得?", "", ["děi (dovere)", "de (particella)", "dé (ottenere)", "dì"], "得 + verbo = dovere → děi."),
    ("Ti chiedono 「旅行好玩儿吗？」 ed è stato bellissimo. Cosa rispondi?", "lǚxíng hǎowánr ma?", ["好玩儿极了！", "极了好玩儿！", "很好玩儿极了！", "好玩儿得很极了！"], "Aggettivo + 极了, senza 很."),
  ],
  extra=[("Poesia", "清明 · 杜牧", "清明时节雨纷纷，路上行人欲断魂。借问酒家何处有？牧童遥指杏花村。",
          "Qīngmíng shíjié yǔ fēnfēn, lù shang xíngrén yù duàn hún. Jiè wèn jiǔjiā hé chù yǒu? Mùtóng yáo zhǐ Xìnghuā cūn.",
          "Alla festa di Qingming la pioggia cade fitta; i viandanti sulla strada hanno il cuore a pezzi. “Dove si trova un’osteria?” chiedo; il pastorello indica lontano il villaggio dei fiori d’albicocco."),
         ("Cultura", "Le portate di un pranzo cinese", "", "",
          "In un pranzo o una cena con ospiti si comincia di solito con i piatti freddi (凉菜) e le bevande, poi arrivano i piatti caldi (热菜) e il riso; la zuppa arriva spesso verso la fine e si chiude con la frutta. Nel sud della Cina, invece, la zuppa si serve anche all’inizio.")],
)

# ───────────────────────────── Lezione 23 ─────────────────────────────
L(n=23, zh="穿什么衣服合适？", py="Chuān shénme yīfu héshì?", it="Che cosa mi metto?",
  theme="Vestiti e taglie, previsioni del tempo, provare e scegliere, rinunciare",
  vocab="""
N|穿|chuān|动|indossare, vestirsi|to wear
N|合适|héshì|形|adatto, giusto (di taglia)|suitable
N|外边|wàibian|名|fuori|outside
N|天气预报|tiānqì yùbào||previsioni del tempo|weather forecast
N|太阳|tàiyáng|名|sole|sun
N|暖和|nuǎnhuo|形|caldo, tiepido (piacevole)|warm
N|羽绒服|yǔróngfú|名|piumino|down jacket
N|麻烦|máfan|动,名,形|disturbare; fastidio; fastidioso|to bother; trouble
N|样子|yàngzi|名|modello, aspetto|style, appearance
N|好看|hǎokàn|形|bello (da vedere)|good-looking
N|镜子|jìngzi|名|specchio|mirror
N|瘦|shòu|形|magro; stretto (vestiti)|thin; tight
N|短|duǎn|形|corto|short
N|个子|gèzi|名|statura|height
N|大号|dàhào|形|taglia grande|large size
N|肥|féi|形|largo (vestiti); grasso|loose
N|算了|suànle||lascia perdere, pazienza|forget it
N|长|zhǎng|动|crescere|to grow
N|别的|biéde|代|altro|other
N|带|dài|动|portare con sé|to bring
S|胖|pàng|形|grasso, robusto|fat
S|遍|biàn|量|volta (dall’inizio alla fine)|times (whole process)
S|零钱|língqián|名|spiccioli|small change
S|毛笔|máobǐ|名|pennello per calligrafia|writing brush
""",
  grammar=[
    ("还是 (ancora, lo stesso)", "Dopo un tentativo, 还是 + verbo / aggettivo indica che la situazione non cambia: “ancora, lo stesso”.",
     [("我说了两遍，他还是不明白。", "Wǒ shuōle liǎng biàn, tā háishi bù míngbai.", "L’ho detto due volte, ma ancora non capisce.")]),
    ("算了", "“Lascia perdere, pazienza”: si rinuncia a qualcosa.",
     [("没有大号的？算了，我不买了。", "Méiyǒu dàhào de? Suànle, wǒ bù mǎi le.", "Non c’è la taglia grande? Pazienza, non lo compro.")]),
    ("一 + cl. + 比 + 一 + cl.", "Esprime una progressione: “sempre più…”. 一天比一天 = di giorno in giorno.",
     [("他的汉语一天比一天好。", "Tā de Hànyǔ yì tiān bǐ yì tiān hǎo.", "Il suo cinese migliora di giorno in giorno."),
      ("生词一课比一课多。", "Shēngcí yí kè bǐ yí kè duō.", "Le parole nuove aumentano a ogni lezione.")]),
    ("没有一 + cl. + …的", "“Nemmeno uno”: 没有一双合适的 = non ce n’è neanche un paio della misura giusta.",
     [("这些鞋没有一双合适的。", "Zhèxiē xié méiyǒu yì shuāng héshì de.", "Di queste scarpe non ce n’è un paio che vada bene.")]),
    ("不是……，是……", "Corregge la causa o l’interpretazione: “non è che…, è che…”.",
     [("不是这件衣服贵，是我没带钱。", "Bú shì zhè jiàn yīfu guì, shì wǒ méi dài qián.", "Non è che questo vestito sia caro: è che non ho portato soldi.")]),
    ("等……再……", "“Quando…, allora…”: si rimanda l’azione a un momento futuro.",
     [("等我有时间了再去买吧。", "Děng wǒ yǒu shíjiān le zài qù mǎi ba.", "Andrò a comprarlo quando avrò tempo.")]),
    ("最……的了 · aggettivi per i vestiti", "最 + aggettivo + 的了 = “è il più… che ci sia”. Per i vestiti: 大 / 小, 长 / 短, 肥 (largo) / 瘦 (stretto), 合适 (giusto).",
     [("这是最大号的了。", "Zhè shì zuì dàhào de le.", "Questa è la taglia più grande che c’è."),
      ("这条裤子有点儿短。", "Zhè tiáo kùzi yǒudiǎnr duǎn.", "Questi pantaloni sono un po’ corti.")]),
  ],
  dialogue=("Nel negozio di scarpe", [
    ("安妮", "这双鞋样子很好看，我可以试试吗？", "Zhè shuāng xié yàngzi hěn hǎokàn, wǒ kěyǐ shìshi ma?", "Questo modello di scarpe è molto bello: posso provarle?"),
    ("售货员", "当然可以。您穿多大号的？", "Dāngrán kěyǐ. Nín chuān duō dà hào de?", "Certo. Che numero porta?"),
    ("安妮", "三十八号。", "Sānshíbā hào.", "Il 38."),
    ("售货员", "这双是三十八号的，您试一下。", "Zhè shuāng shì sānshíbā hào de, nín shì yíxià.", "Queste sono il 38, le provi pure."),
    ("安妮", "有点儿瘦。有大一点儿的吗？", "Yǒudiǎnr shòu. Yǒu dà yìdiǎnr de ma?", "Sono un po’ strette. Ne ha di un po’ più grandi?"),
    ("售货员", "这双三十九号的怎么样？", "Zhè shuāng sānshíjiǔ hào de zěnmeyàng?", "Che ne dice di queste, numero 39?"),
    ("安妮", "还是不合适，有点儿大。", "Háishi bù héshì, yǒudiǎnr dà.", "Non vanno ancora bene: sono un po’ grandi."),
    ("售货员", "那您试试这种，这种比那种小一点儿。", "Nà nín shìshi zhè zhǒng, zhè zhǒng bǐ nà zhǒng xiǎo yìdiǎnr.", "Allora provi questo modello: veste un po’ più piccolo."),
    ("安妮", "麻烦您了！……这双正合适。", "Máfan nín le! …… Zhè shuāng zhèng héshì.", "Scusi il disturbo! … Queste sono perfette."),
    ("售货员", "不麻烦。", "Bù máfan.", "Nessun disturbo."),
  ]),
  reading=("Il piumino di Yamada",
    "天气预报说，明天比今天冷，夜里还有风。山田只带了一件大衣，不太暖和。他去商店想买一件羽绒服。他试了三件：第一件太短，第二件太肥，第三件颜色不好看。最后他说：“算了，等周末再来买吧。”",
    "Tiānqì yùbào shuō, míngtiān bǐ jīntiān lěng, yèli hái yǒu fēng. Shāntián zhǐ dàile yí jiàn dàyī, bú tài nuǎnhuo. Tā qù shāngdiàn xiǎng mǎi yí jiàn yǔróngfú. Tā shìle sān jiàn: dì yī jiàn tài duǎn, dì èr jiàn tài féi, dì sān jiàn yánsè bù hǎokàn. Zuìhòu tā shuō: “Suànle, děng zhōumò zài lái mǎi ba.”",
    "Le previsioni dicono che domani farà più freddo di oggi e che di notte ci sarà anche vento. Yamada ha portato solo un cappotto, che non è molto caldo. Va in un negozio per comprare un piumino. Ne prova tre: il primo è troppo corto, il secondo troppo largo, il terzo ha un colore brutto. Alla fine dice: “Pazienza, tornerò a comprarlo nel fine settimana.”",
    [("天气预报说明天怎么样？", "Tiānqì yùbào shuō míngtiān zěnmeyàng?", ["比今天冷，夜里有风", "比今天暖和", "下雨", "有太阳，不冷"]),
     ("山田想买什么？", "Shāntián xiǎng mǎi shénme?", ["一件羽绒服", "一件大衣", "一双鞋", "一面镜子"]),
     ("第二件怎么样？", "Dì èr jiàn zěnmeyàng?", ["太肥", "太短", "颜色不好看", "很合适"]),
     ("山田最后买了吗？", "Shāntián zuìhòu mǎi le ma?", ["没买，他想周末再来", "买了第一件", "买了第三件", "买了两件"])]),
  cloze=[
    ("今天很冷，你得 ___ 羽绒服。", "Jīntiān hěn lěng, nǐ děi ___ yǔróngfú.", "Oggi fa freddo: devi metterti il piumino.", ["穿", "戴", "合适", "麻烦"], "穿 = indossare (vestiti, scarpe); 戴 = occhiali, cappelli."),
    ("这件衣服有点儿 ___，有大号的吗？", "Zhè jiàn yīfu yǒudiǎnr ___, yǒu dàhào de ma?", "Questo vestito è un po’ stretto: c’è la taglia grande?", ["瘦", "肥", "长", "暖和"], "瘦 = stretto."),
    ("我试了三件，___ 不合适。", "Wǒ shìle sān jiàn, ___ bù héshì.", "Ne ho provati tre, ma non vanno ancora bene.", ["还是", "或者", "已经", "一定"], "还是 = lo stesso, ancora."),
    ("没有我的号？___，我不买了。", "Méiyǒu wǒ de hào? ___, wǒ bù mǎi le.", "Non c’è la mia taglia? Pazienza, non lo compro.", ["算了", "不客气", "合适", "麻烦"], "算了 = lascia perdere."),
    ("天气一天 ___ 一天冷了。", "Tiānqì yì tiān ___ yì tiān lěng le.", "Fa sempre più freddo, giorno dopo giorno.", ["比", "又", "和", "跟"], "一天比一天 = di giorno in giorno."),
    ("这些鞋没有一双 ___ 的。", "Zhèxiē xié méiyǒu yì shuāng ___ de.", "Di queste scarpe non ce n’è un paio che vada bene.", ["合适", "穿", "试", "带"], "没有一 + cl. + …的 = nemmeno uno."),
    ("不是这件衣服贵，___ 我没带钱。", "Bú shì zhè jiàn yīfu guì, ___ wǒ méi dài qián.", "Non è che il vestito sia caro: è che non ho portato soldi.", ["是", "就", "还", "也"], "不是……，是……"),
    ("等我有时间了 ___ 去吧。", "Děng wǒ yǒu shíjiān le ___ qù ba.", "Ci andrò quando avrò tempo.", ["再", "又", "还", "都"], "等……再…… = quando…, allora…"),
    ("天气 ___ 说明天下雨。", "Tiānqì ___ shuō míngtiān xià yǔ.", "Le previsioni dicono che domani pioverà.", ["预报", "太阳", "样子", "个子"], "天气预报 = previsioni del tempo."),
    ("你 ___ 得真高！", "Nǐ ___ de zhēn gāo!", "Come sei cresciuto alto!", ["长", "穿", "带", "试"], "长 zhǎng = crescere."),
  ],
  reorder=[
    ("穿什么衣服合适？", "Chuān shénme yīfu héshì?", "Che cosa conviene mettersi?", ["穿", "什么", "衣服", "合适", "？"]),
    ("这件衣服有点儿瘦。", "Zhè jiàn yīfu yǒudiǎnr shòu.", "Questo vestito è un po’ stretto.", ["这件", "衣服", "有点儿", "瘦", "。"]),
    ("他的汉语一天比一天好。", "Tā de Hànyǔ yì tiān bǐ yì tiān hǎo.", "Il suo cinese migliora di giorno in giorno.", ["他的", "汉语", "一天", "比", "一天", "好", "。"]),
    ("我试了几件，都不合适。", "Wǒ shìle jǐ jiàn, dōu bù héshì.", "Ne ho provati diversi, ma nessuno va bene.", ["我", "试了", "几件", "，", "都", "不", "合适", "。"]),
    ("算了，我不买了。", "Suànle, wǒ bù mǎi le.", "Pazienza, non lo compro.", ["算了", "，", "我", "不", "买", "了", "。"]),
    ("出去的时候带上大衣吧。", "Chūqù de shíhou dàishang dàyī ba.", "Quando esci, porta il cappotto.", ["出去", "的时候", "带上", "大衣", "吧", "。"]),
  ],
  qa=[
    ("La commessa ti chiede 「您穿多大号的？」. Che cosa vuole sapere?", "nín chuān duō dà hào de?", ["La tua taglia / il tuo numero.", "La tua età.", "Il tuo numero di telefono.", "Quanto sei alto."], "号 = taglia, numero."),
    ("Un vestito ti sta troppo largo. Cosa dici?", "", ["有点儿肥。", "有点儿瘦。", "有点儿短。", "正合适。"], "肥 = largo."),
    ("Non c’è la tua taglia e rinunci. Cosa dici?", "", ["算了。", "麻烦了。", "合适了。", "没有了。"], "算了 = lascia perdere."),
    ("「生词一课比一课多。」 significa…", "shēngcí yí kè bǐ yí kè duō.", ["Le parole nuove aumentano a ogni lezione.", "Ogni lezione ha le stesse parole.", "Solo una lezione ha più parole.", "Le parole nuove sono poche."], "一 + cl. + 比 + 一 + cl. = progressione."),
    ("Quale frase significa “Nessuno di questi vestiti mi sta bene”?", "", ["这些衣服没有一件合适的。", "这些衣服一件没有合适。", "没有这些衣服合适。", "这些衣服都没合适一件。"], "没有一件 + …的."),
    ("Fuori fa freddo. Un amico ti consiglia:", "", ["多穿点儿衣服吧！", "少穿点儿衣服吧！", "你穿得太多了！", "别带大衣！"], "多 + verbo = fare di più."),
    ("La commessa ti ha mostrato molti modelli. Per ringraziarla dici:", "", ["麻烦您了！", "算了！", "合适了！", "您太胖了！"], "麻烦您了 = scusi il disturbo / grazie del disturbo."),
  ],
  extra=[("Poesia", "题都城南庄 · 崔护", "去年今日此门中，人面桃花相映红。人面不知何处去，桃花依旧笑春风。",
          "Qùnián jīnrì cǐ mén zhōng, rén miàn táohuā xiāngyìng hóng. Rén miàn bù zhī hé chù qù, táohuā yījiù xiào chūnfēng.",
          "Un anno fa, in questo stesso giorno, dietro questa porta, il suo volto e i fiori di pesco si tingevano di rosa a vicenda. Ora quel volto non so dove sia andato; i fiori di pesco, come allora, sorridono al vento di primavera.")],
)

# ───────────────────────────── Lezione 24 ─────────────────────────────
L(n=24, zh="你家有什么人？", py="Nǐ jiā yǒu shénme rén?", it="Com’è composta la tua famiglia?",
  theme="La famiglia, i lavori, la scuola; foto e somiglianze",
  vocab="""
N|明年|míngnián|名|l’anno prossimo|next year
N|毕业|bì yè||laurearsi, diplomarsi|to graduate
N|留学|liú xué||studiare all’estero|to study abroad
N|爸爸|bàba|名|papà|father
N|工作|gōngzuò|名,动|lavoro; lavorare|job; to work
N|律师|lǜshī|名|avvocato|lawyer
N|医生|yīshēng|名|medico|doctor
N|哥哥|gēge|名|fratello maggiore|elder brother
N|里|lǐ|名|dentro|inside
N|热情|rèqíng|形|caloroso, ospitale|warm-hearted
N|研究生|yánjiūshēng|名|studente di laurea magistrale / dottorato|postgraduate
N|口|kǒu|量|classificatore per i membri della famiglia|MW for family members
N|大学生|dàxuéshēng|名|studente universitario|university student
N|中学生|zhōngxuéshēng|名|studente delle medie / superiori|middle-school student
N|照片|zhàopiàn|名|foto|photo
N|全|quán|形|tutto, intero|whole
N|女孩儿|nǚháir|名|ragazza, bambina|girl
N|后边|hòubian|名|dietro|behind
N|红|hóng|形|rosso|red
N|像|xiàng|动|somigliare|to resemble
S|弟弟|dìdi|名|fratello minore|younger brother
S|儿子|érzi|名|figlio|son
S|幼儿园|yòu’éryuán|名|asilo|kindergarten
S|女儿|nǚ’ér|名|figlia|daughter
S|高中|gāozhōng|名|scuola superiore|high school
S|世界|shìjiè|名|mondo|world
S|眼睛|yǎnjing|名|occhio|eye
S|老虎|lǎohǔ|名|tigre|tiger
S|猫|māo|名|gatto|cat
S|年级|niánjí|名|anno di corso, classe|grade
""",
  grammar=[
    ("上 + scuola", "上 significa anche “frequentare” una scuola o cominciare un’attività regolare: 上小学, 上中学, 上大学, 上班.",
     [("我弟弟在上高中。", "Wǒ dìdi zài shàng gāozhōng.", "Mio fratello minore va al liceo.")]),
    ("那还用说！", "“Ovvio! Non c’è bisogno di dirlo!”: domanda retorica di conferma.",
     [("你喜欢中国菜吗？——那还用说！", "Nǐ xǐhuan Zhōngguó cài ma? — Nà hái yòng shuō!", "Ti piace la cucina cinese? — Ovvio!")]),
    ("全 + nome", "全 (tutto, intero) va direttamente davanti al nome, senza 的: 全家, 全班, 全校, 全世界.",
     [("我们全班都去了。", "Wǒmen quán bān dōu qù le.", "Ci è andata tutta la classe.")]),
    ("像 (somigliare)", "A 像 B = A somiglia a B. Per l’aspetto: A 长得(很)像 B.",
     [("他的眼睛很像爸爸。", "Tā de yǎnjing hěn xiàng bàba.", "Ha gli occhi del padre."),
      ("你长得很像你哥哥。", "Nǐ zhǎng de hěn xiàng nǐ gēge.", "Assomigli molto a tuo fratello.")]),
    ("La famiglia: 口", "你家有几口人? / 你家有什么人? Il classificatore per i membri della famiglia è 口.",
     [("我家有四口人：爸爸、妈妈、弟弟和我。", "Wǒ jiā yǒu sì kǒu rén: bàba, māma, dìdi hé wǒ.", "Nella mia famiglia siamo in quattro: papà, mamma, mio fratello e io.")]),
    ("会……的", "会 + verbo + 的 esprime una previsione sicura: “di sicuro…”.",
     [("你会喜欢这个地方的。", "Nǐ huì xǐhuan zhège dìfang de.", "Questo posto ti piacerà di sicuro.")]),
  ],
  dialogue=("La famiglia di Liu Wei", [
    ("杰夫", "刘伟，你家有几口人？", "Liú Wěi, nǐ jiā yǒu jǐ kǒu rén?", "Liu Wei, quanti siete in famiglia?"),
    ("刘伟", "四口人：爸爸、妈妈、弟弟和我。", "Sì kǒu rén: bàba, māma, dìdi hé wǒ.", "In quattro: papà, mamma, mio fratello minore e io."),
    ("杰夫", "你爸爸妈妈做什么工作？", "Nǐ bàba māma zuò shénme gōngzuò?", "Che lavoro fanno i tuoi genitori?"),
    ("刘伟", "我爸爸是中学老师，妈妈在医院工作，是大夫。", "Wǒ bàba shì zhōngxué lǎoshī, māma zài yīyuàn gōngzuò, shì dàifu.", "Mio padre insegna alle superiori, mia madre lavora in ospedale: è medico."),
    ("杰夫", "你弟弟呢？", "Nǐ dìdi ne?", "E tuo fratello?"),
    ("刘伟", "他在上高中，明年考大学。", "Tā zài shàng gāozhōng, míngnián kǎo dàxué.", "Va al liceo, l’anno prossimo farà l’esame per l’università."),
    ("杰夫", "你有你们全家的照片吗？", "Nǐ yǒu nǐmen quán jiā de zhàopiàn ma?", "Hai una foto di tutta la famiglia?"),
    ("刘伟", "有，你看，这就是。", "Yǒu, nǐ kàn, zhè jiù shì.", "Sì, guarda, eccola."),
    ("杰夫", "你弟弟长得真像你！", "Nǐ dìdi zhǎng de zhēn xiàng nǐ!", "Tuo fratello ti somiglia proprio!"),
    ("刘伟", "大家都这么说。", "Dàjiā dōu zhème shuō.", "Lo dicono tutti."),
  ]),
  reading=("La famiglia di Yamada",
    "山田家有五口人：爷爷、奶奶、爸爸、妈妈和他。他爸爸是律师，工作很忙；妈妈是售货员。山田是大学生，明年就要毕业了。毕业以后，他想来中国读研究生。他说：“我家里人都很热情，要是你去日本，一定要来我家玩儿！”",
    "Shāntián jiā yǒu wǔ kǒu rén: yéye, nǎinai, bàba, māma hé tā. Tā bàba shì lǜshī, gōngzuò hěn máng; māma shì shòuhuòyuán. Shāntián shì dàxuéshēng, míngnián jiù yào bì yè le. Bì yè yǐhòu, tā xiǎng lái Zhōngguó dú yánjiūshēng. Tā shuō: “Wǒ jiā li rén dōu hěn rèqíng, yàoshi nǐ qù Rìběn, yídìng yào lái wǒ jiā wánr!”",
    "Nella famiglia di Yamada sono in cinque: il nonno, la nonna, il papà, la mamma e lui. Suo padre è avvocato ed è molto impegnato; sua madre è commessa. Yamada è studente universitario e l’anno prossimo si laurea. Dopo la laurea vuole venire in Cina a fare la magistrale. Dice: “A casa mia sono tutti molto ospitali: se vai in Giappone, devi venire a trovarci!”",
    [("山田家有几口人？", "Shāntián jiā yǒu jǐ kǒu rén?", ["五口", "四口", "三口", "六口"]),
     ("山田的爸爸做什么工作？", "Shāntián de bàba zuò shénme gōngzuò?", ["律师", "医生", "老师", "售货员"]),
     ("山田毕业以后想做什么？", "Shāntián bì yè yǐhòu xiǎng zuò shénme?", ["来中国读研究生", "去美国工作", "当律师", "回家工作"]),
     ("山田家里人怎么样？", "Shāntián jiā li rén zěnmeyàng?", ["很热情", "很忙", "不太热情", "都是律师"])]),
  cloze=[
    ("你家有几 ___ 人？", "Nǐ jiā yǒu jǐ ___ rén?", "Quanti siete in famiglia?", ["口", "本", "辆", "张"], "口 = classificatore per i membri della famiglia."),
    ("我妹妹在 ___ 中学。", "Wǒ mèimei zài ___ zhōngxué.", "Mia sorella va alle medie.", ["上", "下", "做", "开"], "上 + scuola = frequentare."),
    ("你会来吗？——那还用 ___！", "Nǐ huì lái ma? — Nà hái yòng ___!", "Verrai? — Ovvio!", ["说", "做", "想", "看"], "那还用说 = ovvio!"),
    ("___ 家人都欢迎你。", "___ jiā rén dōu huānyíng nǐ.", "Tutta la famiglia ti dà il benvenuto.", ["全", "都", "每", "多"], "全 + nome, senza 的."),
    ("你长得很 ___ 你妈妈。", "Nǐ zhǎng de hěn ___ nǐ māma.", "Assomigli molto a tua madre.", ["像", "是", "有", "和"], "像 = somigliare."),
    ("我爸爸在医院 ___，他是医生。", "Wǒ bàba zài yīyuàn ___, tā shì yīshēng.", "Mio padre lavora in ospedale: è medico.", ["工作", "毕业", "留学", "上学"], "工作 = lavorare."),
    ("他明年大学 ___。", "Tā míngnián dàxué ___.", "L’anno prossimo si laurea.", ["毕业", "工作", "留学", "热情"], "毕业 = laurearsi, diplomarsi."),
    ("后边穿 ___ 衣服的是我姐姐。", "Hòubian chuān ___ yīfu de shì wǒ jiějie.", "Quella dietro vestita di rosso è mia sorella maggiore.", ["红", "全", "像", "口"], "红 = rosso."),
    ("你去我家，他们一定会欢迎你 ___。", "Nǐ qù wǒ jiā, tāmen yídìng huì huānyíng nǐ ___.", "Se vieni a casa mia, ti accoglieranno di sicuro.", ["的", "了", "过", "着"], "会……的 = previsione sicura."),
  ],
  reorder=[
    ("你家有什么人？", "Nǐ jiā yǒu shénme rén?", "Com’è composta la tua famiglia?", ["你", "家", "有", "什么", "人", "？"]),
    ("我家有四口人。", "Wǒ jiā yǒu sì kǒu rén.", "Nella mia famiglia siamo in quattro.", ["我", "家", "有", "四", "口", "人", "。"]),
    ("我弟弟在上高中。", "Wǒ dìdi zài shàng gāozhōng.", "Mio fratello minore va al liceo.", ["我", "弟弟", "在", "上", "高中", "。"]),
    ("他长得很像爸爸。", "Tā zhǎng de hěn xiàng bàba.", "Assomiglia molto al padre.", ["他", "长得", "很", "像", "爸爸", "。"]),
    ("这是我们全家的照片。", "Zhè shì wǒmen quán jiā de zhàopiàn.", "Questa è la foto di tutta la nostra famiglia.", ["这", "是", "我们", "全家", "的", "照片", "。"]),
    ("你一定会喜欢这儿的。", "Nǐ yídìng huì xǐhuan zhèr de.", "Questo posto ti piacerà di sicuro.", ["你", "一定", "会", "喜欢", "这儿", "的", "。"]),
  ],
  qa=[
    ("Ti chiedono 「你家有几口人？」. Quale risposta è corretta?", "nǐ jiā yǒu jǐ kǒu rén?", ["四口人。", "四个口。", "四口个人。", "第四口。"], "Numero + 口 + 人."),
    ("Ti chiedono 「你爸爸做什么工作？」 e tuo padre è avvocato. Cosa rispondi?", "nǐ bàba zuò shénme gōngzuò?", ["他是律师。", "他做律师工作的。", "他律师。", "他是做律师吗？"], "Professione: 是 + lavoro."),
    ("「那还用说！」 significa…", "nà hái yòng shuō!", ["Ovvio! / Non c’è bisogno di dirlo!", "Dillo ancora!", "Non dirlo!", "Che cosa hai detto?"], "Domanda retorica di conferma."),
    ("Quale frase è corretta?", "", ["全班同学都来了。", "全的班同学都来了。", "班全同学都来了。", "全班的都同学来了。"], "全 + nome, senza 的."),
    ("Ti chiedono 「你大学毕业了吗？」 e ti laurei l’anno prossimo. Cosa rispondi?", "nǐ dàxué bì yè le ma?", ["还没呢，明年毕业。", "不毕业。", "毕业了明年。", "我上大学毕业。"], "还没呢 = non ancora."),
    ("Come si dice “Lei somiglia molto a sua madre”?", "", ["她长得很像她妈妈。", "她很像长得妈妈。", "她妈妈很像长得她。", "她像很妈妈长得。"], "A 长得很像 B."),
    ("Un compagno guarda una foto: 「哪个是你？」. Tu sei quello dietro. Cosa rispondi?", "nǎge shì nǐ?", ["后边那个是我。", "我是后边。", "后边是我的。", "我后边是。"], "后边那个 = quello dietro."),
  ],
  extra=[("Poesia", "秋浦歌 · 李白 (n. 15)", "白发三千丈，缘愁似个长。不知明镜里，何处得秋霜。",
          "Bái fà sānqiān zhàng, yuán chóu sì gè cháng. Bù zhī míng jìng lǐ, hé chù dé qiū shuāng.",
          "Capelli bianchi lunghi tremila zhang: così lunga è la mia malinconia. Non so, nello specchio lucente, da dove sia venuta questa brina d’autunno.")],
)

# ───────────────────────────── Lezione 25 ─────────────────────────────
L(n=25, zh="寒假打算怎么过？", py="Hánjià dǎsuan zěnme guò?", it="Come passerai le vacanze invernali?",
  theme="Progetti per le vacanze, feste cinesi, prenotare biglietti, fare gli auguri",
  vocab="""
N|结束|jiéshù|动|finire|to end
N|一……就……|yī…jiù…||non appena… (subito)…|as soon as…
N|申请|shēnqǐng|动,名|fare domanda; domanda|to apply; application
N|延长|yáncháng|动|prolungare|to extend
N|老家|lǎojiā|名|paese d’origine|hometown
N|们|men|尾|suffisso del plurale (persone)|plural suffix
N|晚会|wǎnhuì|名|festa (serale)|evening party
N|庆祝|qìngzhù|动|festeggiare|to celebrate
N|新年|xīnnián|名|anno nuovo|New Year
N|需要|xūyào|动|aver bisogno di|to need
N|……的话|…dehuà|助|se (…的话)|if
N|或者|huòzhě|连|oppure (nelle frasi affermative)|or
N|决定|juédìng|动|decidere|to decide
N|预订|yùdìng|动|prenotare|to book
N|可能|kěnéng|副|forse, probabilmente|maybe
N|查|chá|动|cercare, controllare|to check, look up
N|南方|nánfāng|名|il sud|the south
N|左右|zuǒyòu|名|circa|about
N|然后|ránhòu|连|poi, dopodiché|then
N|假期|jiàqī|名|vacanza, periodo di ferie|holiday
N|愉快|yúkuài|形|piacevole, felice|pleasant
P|春节|Chūn Jié||Festa di Primavera (Capodanno cinese)|Spring Festival
P|元旦|Yuándàn||Capodanno (1° gennaio)|New Year's Day
P|昆明|Kūnmíng||Kunming|Kunming
P|云南|Yúnnán||Yunnan|Yunnan
P|海南|Hǎinán||Hainan|Hainan
S|紧张|jǐnzhāng|形|teso, nervoso|nervous
S|健康|jiànkāng|形|sano, in salute|healthy
S|大海|dàhǎi|名|mare|sea
""",
  grammar=[
    ("一……就……", "“Non appena…, subito…”: la seconda azione segue immediatamente la prima. I soggetti possono essere uguali o diversi.",
     [("他一到宿舍就睡觉了。", "Tā yí dào sùshè jiù shuì jiào le.", "Appena arrivato in dormitorio si è messo a dormire."),
      ("这个字很容易，我一看就懂。", "Zhège zì hěn róngyì, wǒ yí kàn jiù dǒng.", "Questo carattere è facile: lo capisco al primo sguardo.")]),
    ("元旦 e 春节", "元旦 è il 1° gennaio, il Capodanno del calendario solare. 春节 è il primo giorno del primo mese lunare (fra fine gennaio e febbraio): è la festa tradizionale più importante, in cui si torna al 老家 a festeggiare con la famiglia.",
     [("春节我回老家。", "Chūnjié wǒ huí lǎojiā.", "Per la Festa di Primavera torno al mio paese.")]),
    ("什么 indefinito", "什么 può significare “qualcosa / niente di particolare”, senza fare una domanda.",
     [("你需要买点儿什么吗？", "Nǐ xūyào mǎi diǎnr shénme ma?", "Ti serve comprare qualcosa?"),
      ("不用带什么。", "Búyòng dài shénme.", "Non serve portare niente.")]),
    ("好几 + classificatore", "“Parecchi, un bel po’ di”: davanti a numerale/classificatore o a parole di tempo.",
     [("我等了好几个小时。", "Wǒ děngle hǎojǐ ge xiǎoshí.", "Ho aspettato diverse ore."),
      ("我想去好几个地方。", "Wǒ xiǎng qù hǎojǐ ge dìfang.", "Voglio andare in parecchi posti.")]),
    ("要是……的话", "Rafforza la condizione: “se…”. Spesso con 就 nella seconda parte.",
     [("要是方便的话，带点儿水果来吧。", "Yàoshi fāngbiàn dehuà, dài diǎnr shuǐguǒ lái ba.", "Se ti è comodo, porta un po’ di frutta.")]),
    ("或者 e 还是", "Entrambi significano “o, oppure”: 或者 si usa nelle frasi affermative, 还是 nelle domande.",
     [("你可以坐火车或者坐飞机。", "Nǐ kěyǐ zuò huǒchē huòzhě zuò fēijī.", "Puoi prendere il treno o l’aereo."),
      ("你坐火车还是坐飞机？", "Nǐ zuò huǒchē háishi zuò fēijī?", "Prendi il treno o l’aereo?")]),
    ("先……然后…… · 左右 · 祝", "然后 = poi, dopo (collega due azioni in sequenza); numero + 左右 = circa; 祝 + auguri.",
     [("我们先吃饭，然后去看电影。", "Wǒmen xiān chī fàn, ránhòu qù kàn diànyǐng.", "Prima mangiamo, poi andiamo al cinema."),
      ("我打算玩儿一个星期左右。", "Wǒ dǎsuan wánr yí ge xīngqī zuǒyòu.", "Ho intenzione di fermarmi circa una settimana."),
      ("祝大家新年快乐，身体健康！", "Zhù dàjiā xīnnián kuàilè, shēntǐ jiànkāng!", "Buon anno e buona salute a tutti!")]),
  ],
  dialogue=("Un invito per la Festa di Primavera", [
    ("王平", "山田，寒假你回日本吗？", "Shāntián, hánjià nǐ huí Rìběn ma?", "Yamada, durante le vacanze invernali torni in Giappone?"),
    ("山田", "回。不过我想先在中国过春节，然后再回国。", "Huí. Búguò wǒ xiǎng xiān zài Zhōngguó guò Chūnjié, ránhòu zài huí guó.", "Sì. Però prima vorrei passare la Festa di Primavera in Cina, e poi tornare."),
    ("王平", "那你来我老家过春节吧！我爸爸妈妈一定会欢迎你的。", "Nà nǐ lái wǒ lǎojiā guò Chūnjié ba! Wǒ bàba māma yídìng huì huānyíng nǐ de.", "Allora vieni a festeggiare al mio paese! I miei genitori saranno felicissimi."),
    ("山田", "真的吗？太好了！你老家在哪儿？", "Zhēn de ma? Tài hǎo le! Nǐ lǎojiā zài nǎr?", "Davvero? Fantastico! Dov’è il tuo paese?"),
    ("王平", "在云南，离昆明不远。", "Zài Yúnnán, lí Kūnmíng bù yuǎn.", "Nello Yunnan, non lontano da Kunming."),
    ("山田", "我得带什么礼物吗？", "Wǒ děi dài shénme lǐwù ma?", "Devo portare qualche regalo?"),
    ("王平", "不用带什么。你快点儿预订飞机票吧，春节的票很难买。", "Búyòng dài shénme. Nǐ kuài diǎnr yùdìng fēijīpiào ba, Chūnjié de piào hěn nán mǎi.", "Non serve niente. Piuttosto prenota presto il biglietto aereo: per la Festa di Primavera è difficile trovarne."),
    ("山田", "好，我今天晚上就上网查。", "Hǎo, wǒ jīntiān wǎnshang jiù shàng wǎng chá.", "D’accordo, stasera stessa controllo online."),
    ("王平", "要是有问题的话，就给我打电话。", "Yàoshi yǒu wèntí dehuà, jiù gěi wǒ dǎ diànhuà.", "Se ci sono problemi, chiamami."),
  ]),
  reading=("I programmi di Lisa",
    "期末考试一结束，我就去旅行。我已经预订了一月二十号去西安的火车票。我打算在西安玩儿五天左右，然后去上海，和朋友们一起过春节。春节以后我就回国。祝大家新年快乐！",
    "Qīmò kǎoshì yì jiéshù, wǒ jiù qù lǚxíng. Wǒ yǐjīng yùdìngle yīyuè èrshí hào qù Xī’ān de huǒchēpiào. Wǒ dǎsuan zài Xī’ān wánr wǔ tiān zuǒyòu, ránhòu qù Shànghǎi, hé péngyoumen yìqǐ guò Chūnjié. Chūnjié yǐhòu wǒ jiù huí guó. Zhù dàjiā xīnnián kuàilè!",
    "(Racconta Lisa) Appena finiti gli esami di fine semestre parto per un viaggio. Ho già prenotato il treno per Xi’an del 20 gennaio. Penso di restare a Xi’an circa cinque giorni, poi andrò a Shanghai a festeggiare la Festa di Primavera con gli amici. Dopo la Festa tornerò a casa. Buon anno a tutti!",
    [("丽莎什么时候去旅行？", "Lìshā shénme shíhou qù lǚxíng?", ["期末考试一结束就去", "元旦以前", "春节以后", "二月"]),
     ("她怎么去西安？", "Tā zěnme qù Xī’ān?", ["坐火车", "坐飞机", "骑自行车", "坐公共汽车"]),
     ("她在西安玩儿多长时间？", "Tā zài Xī’ān wánr duō cháng shíjiān?", ["五天左右", "十天左右", "一个月", "两天"]),
     ("她在哪儿过春节？", "Tā zài nǎr guò Chūnjié?", ["上海", "西安", "北京", "她的国家"])]),
  cloze=[
    ("我一放假 ___ 回国。", "Wǒ yí fàng jià ___ huí guó.", "Appena iniziano le vacanze torno al mio paese.", ["就", "才", "再", "还"], "一……就…… = non appena…"),
    ("你需要买点儿 ___ 吗？", "Nǐ xūyào mǎi diǎnr ___ ma?", "Ti serve comprare qualcosa?", ["什么", "哪儿", "怎么", "谁"], "什么 indefinito = qualcosa."),
    ("我等了好 ___ 个小时。", "Wǒ děngle hǎo ___ ge xiǎoshí.", "Ho aspettato diverse ore.", ["几", "次", "些", "少"], "好几 + cl. = parecchi."),
    ("要是方便的 ___，带点儿水果来吧。", "Yàoshi fāngbiàn de ___, dài diǎnr shuǐguǒ lái ba.", "Se ti è comodo, porta un po’ di frutta.", ["话", "左右", "然后", "或者"], "要是……的话 = se…"),
    ("你可以坐火车 ___ 坐飞机。", "Nǐ kěyǐ zuò huǒchē ___ zuò fēijī.", "Puoi prendere il treno o l’aereo.", ["或者", "还是", "因为", "所以"], "Nelle frasi affermative: 或者."),
    ("我们先吃饭，___ 去看电影。", "Wǒmen xiān chī fàn, ___ qù kàn diànyǐng.", "Prima mangiamo, poi andiamo al cinema.", ["然后", "或者", "以后", "因为"], "然后 collega due azioni in sequenza; 以后 di solito segue un verbo (吃饭以后)."),
    ("我打算在云南玩儿十天 ___。", "Wǒ dǎsuan zài Yúnnán wánr shí tiān ___.", "Penso di stare nello Yunnan una decina di giorni.", ["左右", "以后", "然后", "的话"], "Numero + 左右 = circa."),
    ("祝大家假期 ___！", "Zhù dàjiā jiàqī ___!", "Buone vacanze a tutti!", ["愉快", "紧张", "健康", "需要"], "假期愉快 = buone vacanze."),
    ("学期快 ___ 了。", "Xuéqī kuài ___ le.", "Il semestre sta per finire.", ["结束", "决定", "申请", "预订"], "结束 = finire."),
    ("春节的票很难买，你得早点儿 ___。", "Chūnjié de piào hěn nán mǎi, nǐ děi zǎo diǎnr ___.", "I biglietti per la Festa di Primavera sono difficili da trovare: devi prenotare presto.", ["预订", "庆祝", "延长", "结束"], "预订 = prenotare."),
  ],
  reorder=[
    ("寒假打算怎么过？", "Hánjià dǎsuan zěnme guò?", "Come pensi di passare le vacanze invernali?", ["寒假", "打算", "怎么", "过", "？"]),
    ("我一下课就去图书馆。", "Wǒ yí xià kè jiù qù túshūguǎn.", "Appena finisce la lezione vado in biblioteca.", ["我", "一", "下课", "就", "去", "图书馆", "。"]),
    ("我想去好几个地方。", "Wǒ xiǎng qù hǎojǐ ge dìfang.", "Voglio andare in parecchi posti.", ["我", "想", "去", "好几个", "地方", "。"]),
    ("你坐火车或者坐飞机都行。", "Nǐ zuò huǒchē huòzhě zuò fēijī dōu xíng.", "Puoi prendere sia il treno sia l’aereo, va bene uguale.", ["你", "坐火车", "或者", "坐飞机", "都", "行", "。"]),
    ("我们先去西安，然后去北京。", "Wǒmen xiān qù Xī’ān, ránhòu qù Běijīng.", "Prima andiamo a Xi’an, poi a Pechino.", ["我们", "先", "去", "西安", "，", "然后", "去", "北京", "。"]),
    ("祝你新年快乐！", "Zhù nǐ xīnnián kuàilè!", "Buon anno!", ["祝", "你", "新年", "快乐", "！"]),
  ],
  qa=[
    ("Che cos’è il 「春节」?", "Chūn Jié", ["Il Capodanno lunare, la festa tradizionale più importante", "Il 1° gennaio", "Una festa di aprile", "Il compleanno dell’imperatore"], "春节 = Festa di Primavera."),
    ("Che cos’è il 「元旦」?", "Yuándàn", ["Il 1° gennaio, Capodanno del calendario solare", "Il Capodanno lunare", "Natale", "La festa di metà autunno"], "元旦 = 1° gennaio."),
    ("Quale frase usa correttamente 或者?", "", ["我明天去或者后天去。", "你喝茶或者喝咖啡？", "或者你去吗？", "你去或者不去？"], "或者 nelle affermazioni; nelle domande si usa 还是."),
    ("Vuoi augurare buone vacanze a tutti. Cosa dici?", "", ["祝大家假期愉快！", "祝大家假期紧张！", "大家祝假期愉快！", "祝假期大家愉快！"], "祝 + persona + augurio."),
    ("「我一到家就给你打电话。」 significa…", "wǒ yí dào jiā jiù gěi nǐ dǎ diànhuà.", ["Appena arrivo a casa ti telefono.", "Arrivo a casa e un giorno ti chiamo.", "Ti ho chiamato da casa.", "Ti chiamo prima di arrivare a casa."], "一……就…… = non appena…"),
    ("Ti chiedono 「你需要什么吗？」 e non ti serve niente. Cosa rispondi?", "nǐ xūyào shénme ma?", ["不需要什么，谢谢。", "我需要什么。", "什么不需要。", "我不什么需要。"], "什么 indefinito: “niente (di particolare)”."),
    ("Un amico è molto agitato prima dell’esame. Gli dici:", "", ["别紧张！", "别健康！", "别愉快！", "别决定！"], "紧张 = teso, nervoso."),
  ],
  extra=[("Poesia", "早发白帝城 · 李白", "朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。",
          "Zhāo cí Báidì cǎiyún jiān, qiān lǐ Jiānglíng yí rì huán. Liǎng àn yuán shēng tí bú zhù, qīng zhōu yǐ guò wàn chóng shān.",
          "All’alba lascio Baidi tra nuvole colorate; mille li fino a Jiangling, e torno in un giorno. Dalle due rive le grida delle scimmie non si fermano, e la barca leggera ha già passato diecimila montagne."),
         ("Cultura", "I convenevoli", "", "",
          "I cinesi si salutano spesso con domande: 吃了吗？ (hai mangiato?), 去哪儿？ (dove vai?), 最近忙吗？, oppure commentando ciò che l’altro sta facendo (上课去呀？). Sono formule di cortesia: si risponde brevemente (吃了 / 还可以 / 出去一下). Anche 改天聊聊 o 有空儿来玩儿 nel salutarsi sono gentilezze, non inviti veri: un invito vero indica giorno e ora.")],
)
