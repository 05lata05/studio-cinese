# -*- coding: utf-8 -*-
"""Lezioni 14-19 (formato descritto in lessons_a.py)."""

LESSONS = []
L = lambda **kw: LESSONS.append(kw)

# ───────────────────────────── Lezione 14 ─────────────────────────────
L(n=14, zh="今天天气怎么样？", py="Jīntiān tiānqì zěnmeyàng?", it="Che tempo fa oggi?",
  theme="Il tempo e le stagioni; chiedere della salute e dello studio; mandare notizie a casa",
  vocab="""
N|天气|tiānqì|名|tempo (atmosferico)|weather
N|不错|búcuò|形|niente male, buono|not bad, good
N|热|rè|形|caldo|hot
N|夜里|yèli|名|di notte|at night
N|雨|yǔ|名|pioggia|rain
N|风|fēng|名|vento|wind
N|冬天|dōngtiān|名|inverno|winter
N|冷|lěng|形|freddo|cold
N|非常|fēicháng|副|estremamente, molto|very
N|夏天|xiàtiān|名|estate|summer
N|特别|tèbié|副,形|specialmente; speciale|especially; special
N|春天|chūntiān|名|primavera|spring
N|秋天|qiūtiān|名|autunno|autumn
N|季节|jìjié|名|stagione|season
N|阿姨|āyí|名|zia; signora (appellativo)|auntie
N|听说|tīngshuō|动|sentir dire|to hear that
N|身体|shēntǐ|名|corpo; salute|body, health
N|已经|yǐjīng|副|già|already
N|最近|zuìjìn|名|ultimamente|recently
N|学习|xuéxí|动|studiare|to study
N|饭|fàn|名|pasto; riso cotto|meal
N|还可以|hái kěyǐ||non c’è male, passabile|not bad, OK
N|妈妈|māma|名|mamma|mother
N|让|ràng|动|lasciare, far fare|to let, make
N|放心|fàng xīn||stare tranquillo|to feel at ease
N|大衣|dàyī|名|cappotto|overcoat
S|咖啡馆儿|kāfēiguǎnr|名|caffetteria|café
S|孩子|háizi|名|bambino, figlio|child
S|生活|shēnghuó|名,动|vita; vivere|life; to live
""",
  grammar=[
    ("…怎么样？ (tempo, salute, studio)", "Con 怎么样 si chiede com’è una situazione: 天气怎么样? 身体怎么样? 学习怎么样?",
     [("最近身体怎么样？", "Zuìjìn shēntǐ zěnmeyàng?", "Come stai di salute ultimamente?")]),
    ("Esprimere il grado", "Dal più alto al più basso: 非常好 · 很好 · 不错 · 还可以 · 不太好 · 不好. 不错 è un giudizio positivo, 还可以 vuol dire “passabile”.",
     [("今天天气不错。", "Jīntiān tiānqì búcuò.", "Oggi il tempo è bello."),
      ("食堂的菜还可以。", "Shítáng de cài hái kěyǐ.", "I piatti della mensa sono passabili.")]),
    ("王阿姨", "Cognome + 阿姨 si usa per una donna dell’età dei propri genitori (amica di famiglia, vicina di casa). È affettuoso e rispettoso.",
     [("王阿姨，您好！", "Wáng āyí, nín hǎo!", "Buongiorno, zia Wang!")]),
    ("听说 + frase", "“Ho sentito dire che…”: riporta un’informazione ricevuta da altri.",
     [("听说你病了，现在好了吗？", "Tīngshuō nǐ bìng le, xiànzài hǎo le ma?", "Ho sentito che eri malato: adesso stai meglio?")]),
    ("让 + persona + verbo", "“Far sì che / lasciare che qualcuno faccia…”. 请告诉 + persona + messaggio = “di’ a… che…”.",
     [("请告诉我妈妈，让她放心。", "Qǐng gàosu wǒ māma, ràng tā fàng xīn.", "Di’ a mia madre di stare tranquilla.")]),
    ("Il tempo atmosferico: 下雨", "Piovere = 下雨 (下小雨 = piovigginare). Per il vento si dice 风很大 / 有风.",
     [("夜里下了小雨。", "Yèli xiàle xiǎo yǔ.", "Stanotte ha piovigginato."),
      ("这儿的冬天风很大。", "Zhèr de dōngtiān fēng hěn dà.", "Qui d’inverno c’è molto vento.")]),
    ("已经……了", "“Già”: l’azione o il cambiamento sono avvenuti.",
     [("我已经好了。", "Wǒ yǐjīng hǎo le.", "Sono già guarito.")]),
  ],
  dialogue=("Al telefono con la zia Wang", [
    ("王阿姨", "张新，你那儿天气怎么样？", "Zhāng Xīn, nǐ nàr tiānqì zěnmeyàng?", "Zhang Xin, che tempo fa lì da te?"),
    ("张新", "现在是秋天，天气非常好，不冷也不热。", "Xiànzài shì qiūtiān, tiānqì fēicháng hǎo, bù lěng yě bú rè.", "Adesso è autunno, il tempo è bellissimo: né freddo né caldo."),
    ("王阿姨", "听说那儿夏天特别热。", "Tīngshuō nàr xiàtiān tèbié rè.", "Ho sentito dire che lì d’estate fa caldissimo."),
    ("张新", "对，夏天很热，常常下雨。", "Duì, xiàtiān hěn rè, chángcháng xià yǔ.", "Sì, d’estate fa caldo e piove spesso."),
    ("王阿姨", "你最近学习忙吗？", "Nǐ zuìjìn xuéxí máng ma?", "Ultimamente sei impegnata con lo studio?"),
    ("张新", "有点儿忙，不过身体很好。", "Yǒudiǎnr máng, búguò shēntǐ hěn hǎo.", "Un po’, ma sto benissimo."),
    ("王阿姨", "食堂的饭怎么样？", "Shítáng de fàn zěnmeyàng?", "E il cibo della mensa?"),
    ("张新", "菜很多，也很便宜。阿姨，请告诉我妈妈，让她放心。", "Cài hěn duō, yě hěn piányi. Āyí, qǐng gàosu wǒ māma, ràng tā fàng xīn.", "Ci sono tanti piatti e costano poco. Zia, di’ alla mamma di stare tranquilla."),
  ]),
  reading=("Le stagioni secondo Jeff",
    "我是英国人，在中国学习汉语。这儿的春天不冷也不热，不过风很大。夏天非常热，夜里也很热。秋天天气特别好，我特别喜欢秋天。冬天非常冷，我要买一件大衣。",
    "Wǒ shì Yīngguórén, zài Zhōngguó xuéxí Hànyǔ. Zhèr de chūntiān bù lěng yě bú rè, búguò fēng hěn dà. Xiàtiān fēicháng rè, yèli yě hěn rè. Qiūtiān tiānqì tèbié hǎo, wǒ tèbié xǐhuan qiūtiān. Dōngtiān fēicháng lěng, wǒ yào mǎi yí jiàn dàyī.",
    "Sono inglese e studio cinese in Cina. Qui la primavera non è né fredda né calda, però c’è molto vento. L’estate è caldissima, anche di notte. In autunno il tempo è particolarmente bello: l’autunno mi piace moltissimo. L’inverno è freddissimo: devo comprarmi un cappotto.",
    [("这儿的春天怎么样？", "Zhèr de chūntiān zěnmeyàng?", ["不冷也不热，风很大", "非常热", "非常冷", "常常下雨"]),
     ("杰夫特别喜欢哪个季节？", "Jiéfū tèbié xǐhuan nǎge jìjié?", ["秋天", "春天", "夏天", "冬天"]),
     ("冬天杰夫要买什么？", "Dōngtiān Jiéfū yào mǎi shénme?", ["一件大衣", "一辆自行车", "一本书", "一双鞋"])]),
  cloze=[
    ("今天天气 ___？", "Jīntiān tiānqì ___?", "Che tempo fa oggi?", ["怎么样", "什么", "哪儿", "几"], "怎么样 chiede com’è una situazione."),
    ("昨天夜里 ___ 雨了。", "Zuótiān yèli ___ yǔ le.", "Ieri notte ha piovuto.", ["下", "开", "来", "去"], "下雨 = piovere."),
    ("这儿的冬天 ___ 冷。", "Zhèr de dōngtiān ___ lěng.", "Qui l’inverno è freddissimo.", ["非常", "已经", "听说", "最近"], "非常 = estremamente."),
    ("___ 你病了，现在好了吗？", "___ nǐ bìng le, xiànzài hǎo le ma?", "Ho sentito che eri malato: ora stai meglio?", ["听说", "觉得", "告诉", "放心"], "听说 = ho sentito dire che…"),
    ("我 ___ 好了，谢谢。", "Wǒ ___ hǎo le, xièxie.", "Sono già guarito, grazie.", ["已经", "非常", "特别", "最近"], "已经……了 = già."),
    ("请告诉我妈妈，___ 她放心。", "Qǐng gàosu wǒ māma, ___ tā fàng xīn.", "Di’ a mia madre di stare tranquilla.", ["让", "给", "和", "要"], "让 + persona + verbo."),
    ("最近学习忙吗？——还 ___。", "Zuìjìn xuéxí máng ma? — Hái ___.", "Sei impegnato con lo studio? — Così così.", ["可以", "能", "要", "会"], "还可以 = passabile, così così."),
    ("这儿的秋天 ___ 好，不冷也不热。", "Zhèr de qiūtiān ___ hǎo, bù lěng yě bú rè.", "Qui l’autunno è particolarmente bello, né freddo né caldo.", ["特别", "已经", "听说", "让"], "特别 = particolarmente."),
  ],
  reorder=[
    ("今天天气怎么样？", "Jīntiān tiānqì zěnmeyàng?", "Che tempo fa oggi?", ["今天", "天气", "怎么样", "？"]),
    ("听说你感冒了。", "Tīngshuō nǐ gǎnmào le.", "Ho sentito che hai il raffreddore.", ["听说", "你", "感冒", "了", "。"]),
    ("这儿的夏天非常热。", "Zhèr de xiàtiān fēicháng rè.", "Qui l’estate è caldissima.", ["这儿", "的", "夏天", "非常", "热", "。"]),
    ("我已经习惯了。", "Wǒ yǐjīng xíguàn le.", "Mi sono già abituato.", ["我", "已经", "习惯", "了", "。"]),
    ("请告诉我妈妈，我很好。", "Qǐng gàosu wǒ māma, wǒ hěn hǎo.", "Di’ a mia madre che sto bene.", ["请", "告诉", "我妈妈", "，", "我", "很好", "。"]),
    ("你最近身体怎么样？", "Nǐ zuìjìn shēntǐ zěnmeyàng?", "Come stai di salute ultimamente?", ["你", "最近", "身体", "怎么样", "？"]),
  ],
  qa=[
    ("Ti chiedono 「今天天气怎么样？」 ed è una bella giornata. Cosa rispondi?", "jīntiān tiānqì zěnmeyàng?", ["不错。", "不对。", "没关系。", "不客气。"], "不错 = bello, niente male."),
    ("Quale risposta esprime il giudizio più basso?", "", ["不太好。", "还可以。", "不错。", "非常好。"], "不太好 < 还可以 < 不错 < 非常好."),
    ("Come ti rivolgi alla signora Wang, amica di tua madre?", "", ["王阿姨", "阿姨王", "王先生", "王老师"], "Cognome + 阿姨."),
    ("「听说你病了。」 significa…", "tīngshuō nǐ bìng le.", ["Ho sentito dire che sei malato.", "Ti ascolto perché sei malato.", "Dimmi se sei malato.", "Eri malato?"], "听说 = ho sentito dire."),
    ("Quale stagione viene dopo 夏天?", "xiàtiān", ["秋天", "春天", "冬天", "季节"], "春 → 夏 → 秋 → 冬."),
    ("Vuoi che la zia dica a tua madre di stare tranquilla. Quale frase usi?", "", ["请告诉我妈妈，让她放心。", "请让我妈妈告诉放心。", "请放心告诉我妈妈。", "我妈妈让你放心告诉。"], "请告诉 + persona; 让 + persona + verbo."),
    ("Ti chiedono 「你习惯这儿的生活吗？」 e ormai ti sei abituato. Cosa rispondi?", "nǐ xíguàn zhèr de shēnghuó ma?", ["已经习惯了。", "已经不习惯。", "习惯已经。", "还可以习惯了。"], "已经……了 = già."),
  ],
  extra=[("Poesia", "江雪 · 柳宗元", "千山鸟飞绝，万径人踪灭。孤舟蓑笠翁，独钓寒江雪。",
          "Qiān shān niǎo fēi jué, wàn jìng rén zōng miè. Gū zhōu suō lì wēng, dú diào hán jiāng xuě.",
          "Su mille monti è svanito il volo degli uccelli, su diecimila sentieri sono sparite le orme degli uomini. Su una barca solitaria, un vecchio con mantello e cappello di paglia pesca da solo nella neve del fiume gelato.")],
)

# ───────────────────────────── Lezione 15 ─────────────────────────────
L(n=15, zh="一个星期有多少节课？", py="Yí ge xīngqī yǒu duōshao jié kè?", it="Quante lezioni ci sono in una settimana?",
  theme="Calendario scolastico, durata, esperienze passate, ordinali e vacanze",
  vocab="""
N|节|jié|量,名|classificatore per ore di lezione; festa|MW for class periods; festival
N|时候|shíhou|名|momento, tempo (quando)|time, moment
N|放|fàng|动|mettere; (放假) andare in vacanza|to put; to have (a holiday)
N|寒假|hánjià|名|vacanze invernali|winter vacation
N|一月|yīyuè|名|gennaio|January
N|期末|qīmò|名|fine del semestre|end of term
N|考试|kǎoshì|动,名|esame; sostenere un esame|exam; to take an exam
N|开学|kāi xué||iniziare la scuola|school starts
N|过|guo|助|particella dell’esperienza (aver già fatto)|experiential particle
N|长|cháng|形|lungo|long
N|学期|xuéqī|名|semestre|semester
N|语法|yǔfǎ|名|grammatica|grammar
N|每|měi|代|ogni|each, every
N|太|tài|副|troppo; molto|too
N|少|shǎo|形|poco, pochi|few, little
N|只|zhǐ|副|solo, soltanto|only
N|学年|xuénián|名|anno scolastico|school year
N|第|dì|头|prefisso degli ordinali|ordinal prefix
N|年|nián|名|anno|year
N|周|zhōu|名|settimana|week
N|暑假|shǔjià|名|vacanze estive|summer vacation
N|回国|huí guó||tornare nel proprio paese|to return to one's country
N|电影|diànyǐng|名|film|movie
N|书法|shūfǎ|名|calligrafia|calligraphy
N|飞机|fēijī|名|aereo|airplane
N|次|cì|量|volta|time(s)
N|中学|zhōngxué|名|scuola media / superiore|middle school
P|圣诞节|Shèngdàn Jié||Natale|Christmas
P|北京|Běijīng||Pechino|Beijing
P|长城|Chángchéng||Grande Muraglia|the Great Wall
S|结婚|jié hūn||sposarsi|to get married
S|烤鸭|kǎoyā|名|anatra laccata|roast duck
S|万|wàn|数|diecimila|ten thousand
S|国家|guójiā|名|paese, stato|country
S|一样|yíyàng|形|uguale|same
""",
  grammar=[
    ("过: l’esperienza", "Verbo + 过 = aver fatto qualcosa almeno una volta nella vita (o in passato). Negazione: 没(有) + V + 过. Domanda: V过…吗? / V过…没有?",
     [("我去过长城。", "Wǒ qùguo Chángchéng.", "Sono stato alla Grande Muraglia."),
      ("我没吃过烤鸭。", "Wǒ méi chīguo kǎoyā.", "Non ho mai mangiato l’anatra laccata."),
      ("老师说过，一月放寒假。", "Lǎoshī shuōguo, yīyuè fàng hánjià.", "L’insegnante l’ha detto: le vacanze invernali sono a gennaio.")]),
    ("多 + aggettivo: quanto?", "多长时间? = quanto tempo? 多大? = quanti anni? Dopo un numero tondo, 多 vuol dire “e più”: 一个多月 = più di un mese.",
     [("寒假有多长时间？——一个多月。", "Hánjià yǒu duō cháng shíjiān? — Yí ge duō yuè.", "Quanto durano le vacanze invernali? — Più di un mese.")]),
    ("一月 e 一个月", "一月 è il nome del mese (gennaio); 一个月 è una durata (un mese). Allo stesso modo: 星期一 (lunedì) / 一个星期 (una settimana).",
     [("一月放寒假，放一个月。", "Yīyuè fàng hánjià, fàng yí ge yuè.", "A gennaio iniziano le vacanze invernali, che durano un mese.")]),
    ("La durata dopo il verbo", "La durata si mette dopo il verbo: V (+ 了) + durata (+ oggetto).",
     [("我学了半年汉语。", "Wǒ xuéle bàn nián Hànyǔ.", "Ho studiato cinese per sei mesi."),
      ("我们放了十天假。", "Wǒmen fàngle shí tiān jià.", "Abbiamo avuto dieci giorni di vacanza.")]),
    ("第 + numero: gli ordinali", "第一 (primo), 第二次 (la seconda volta), 第三周 (la terza settimana).",
     [("这是我第一次来中国。", "Zhè shì wǒ dì yī cì lái Zhōngguó.", "È la prima volta che vengo in Cina.")]),
    ("每 … 都", "每 + (numero +) classificatore + nome, spesso con 都 prima del verbo: “ogni…”.",
     [("我每天都有课。", "Wǒ měi tiān dōu yǒu kè.", "Ho lezione tutti i giorni.")]),
    ("太……了 · 只 · ……的时候", "太……了 = troppo; 只 = solo; …的时候 = quando…",
     [("我们班的学生太多了。", "Wǒmen bān de xuésheng tài duō le.", "Nella nostra classe ci sono troppi studenti."),
      ("吃饭的时候，我们常常聊天儿。", "Chī fàn de shíhou, wǒmen chángcháng liáo tiānr.", "Quando mangiamo chiacchieriamo spesso.")]),
  ],
  dialogue=("Prima della fine del semestre", [
    ("彼得", "丽莎，期末考试是什么时候？", "Lìshā, qīmò kǎoshì shì shénme shíhou?", "Lisa, quando sono gli esami di fine semestre?"),
    ("丽莎", "老师说过，是一月十号。", "Lǎoshī shuōguo, shì yīyuè shí hào.", "L’ha detto l’insegnante: il 10 gennaio."),
    ("彼得", "有几门考试？", "Yǒu jǐ mén kǎoshì?", "Quanti esami ci sono?"),
    ("丽莎", "三门：语法、口语和听力。", "Sān mén: yǔfǎ, kǒuyǔ hé tīnglì.", "Tre: grammatica, lingua parlata e ascolto."),
    ("彼得", "考试以后就放寒假吗？", "Kǎoshì yǐhòu jiù fàng hánjià ma?", "Dopo gli esami iniziano subito le vacanze?"),
    ("丽莎", "对，放一个多月。你回国吗？", "Duì, fàng yí ge duō yuè. Nǐ huí guó ma?", "Sì, durano più di un mese. Torni a casa?"),
    ("彼得", "不回。我还没去过长城，我想去北京看看。", "Bù huí. Wǒ hái méi qùguo Chángchéng, wǒ xiǎng qù Běijīng kànkan.", "No. Non sono ancora stato alla Grande Muraglia: voglio andare a vedere Pechino."),
    ("丽莎", "我去过两次。北京的烤鸭也很好吃！", "Wǒ qùguo liǎng cì. Běijīng de kǎoyā yě hěn hǎochī!", "Io ci sono stata due volte. E l’anatra laccata di Pechino è buonissima!"),
  ]),
  reading=("La settimana di Peter",
    "彼得这个学期有五门课：语法、口语、听力、汉字和书法。他一个星期有二十二节课，星期一到星期五每天上午都有四节。星期二和星期四下午还有书法课。他们班有十五个学生。彼得说：“课有点儿多，不过我很喜欢。”",
    "Bǐdé zhège xuéqī yǒu wǔ mén kè: yǔfǎ, kǒuyǔ, tīnglì, Hànzì hé shūfǎ. Tā yí ge xīngqī yǒu èrshí’èr jié kè, xīngqīyī dào xīngqīwǔ měi tiān shàngwǔ dōu yǒu sì jié. Xīngqī’èr hé xīngqīsì xiàwǔ hái yǒu shūfǎkè. Tāmen bān yǒu shíwǔ ge xuésheng. Bǐdé shuō: “Kè yǒudiǎnr duō, búguò wǒ hěn xǐhuan.”",
    "Questo semestre Peter ha cinque materie: grammatica, lingua parlata, ascolto, caratteri e calligrafia. Ha 22 ore di lezione alla settimana: dal lunedì al venerdì ogni mattina ne ha quattro, e il martedì e il giovedì pomeriggio c’è anche calligrafia. Nella sua classe ci sono quindici studenti. Peter dice: “Le lezioni sono un po’ tante, ma mi piacciono molto.”",
    [("彼得这个学期有几门课？", "Bǐdé zhège xuéqī yǒu jǐ mén kè?", ["五门", "四门", "三门", "二十二门"]),
     ("彼得一个星期有多少节课？", "Bǐdé yí ge xīngqī yǒu duōshao jié kè?", ["二十二节", "二十节", "十五节", "四节"]),
     ("书法课是什么时候？", "Shūfǎkè shì shénme shíhou?", ["星期二和星期四下午", "每天上午", "星期一下午", "星期五上午"]),
     ("彼得觉得课怎么样？", "Bǐdé juéde kè zěnmeyàng?", ["有点儿多，不过他很喜欢", "太少了", "不太好", "他不喜欢"])]),
  cloze=[
    ("我去 ___ 长城。", "Wǒ qù ___ Chángchéng.", "Sono stato alla Grande Muraglia.", ["过", "着", "的", "吗"], "V + 过 = esperienza."),
    ("寒假有 ___ 长时间？", "Hánjià yǒu ___ cháng shíjiān?", "Quanto durano le vacanze invernali?", ["多", "几", "什么", "怎么"], "多 + aggettivo = quanto…?"),
    ("___ 放寒假，放一个月。(a gennaio)", "___ fàng hánjià, fàng yí ge yuè.", "A gennaio iniziano le vacanze invernali, che durano un mese.", ["一月", "一个月", "第一月", "每月"], "一月 = gennaio; 一个月 = un mese."),
    ("这是我 ___ 一次来中国。", "Zhè shì wǒ ___ yī cì lái Zhōngguó.", "È la prima volta che vengo in Cina.", ["第", "每", "只", "太"], "第 + numero = ordinale."),
    ("我 ___ 天都有课。", "Wǒ ___ tiān dōu yǒu kè.", "Ho lezione tutti i giorni.", ["每", "第", "只", "多"], "每天 = ogni giorno."),
    ("我们班的学生太多 ___。", "Wǒmen bān de xuésheng tài duō ___.", "Nella nostra classe ci sono troppi studenti.", ["了", "过", "着", "吗"], "太……了."),
    ("我 ___ 有三门课，不太多。", "Wǒ ___ yǒu sān mén kè, bú tài duō.", "Ho solo tre materie, non sono tante.", ["只", "每", "第", "太"], "只 = solo."),
    ("吃饭的 ___，我们常常聊天儿。", "Chī fàn de ___, wǒmen chángcháng liáo tiānr.", "Quando mangiamo chiacchieriamo spesso.", ["时候", "时间", "以前", "学期"], "……的时候 = quando…"),
    ("我没吃 ___ 烤鸭。", "Wǒ méi chī ___ kǎoyā.", "Non ho mai mangiato l’anatra laccata.", ["过", "了", "着", "的"], "没 + V + 过 = non aver mai fatto."),
  ],
  reorder=[
    ("一个星期有多少节课？", "Yí ge xīngqī yǒu duōshao jié kè?", "Quante lezioni ci sono in una settimana?", ["一个", "星期", "有", "多少", "节", "课", "？"]),
    ("我去过两次长城。", "Wǒ qùguo liǎng cì Chángchéng.", "Sono stato due volte alla Grande Muraglia.", ["我", "去过", "两次", "长城", "。"]),
    ("你学了多长时间汉语？", "Nǐ xuéle duō cháng shíjiān Hànyǔ?", "Per quanto tempo hai studiato cinese?", ["你", "学了", "多长", "时间", "汉语", "？"]),
    ("我们一月放寒假。", "Wǒmen yīyuè fàng hánjià.", "Le nostre vacanze invernali sono a gennaio.", ["我们", "一月", "放", "寒假", "。"]),
    ("这是我第一次吃烤鸭。", "Zhè shì wǒ dì yī cì chī kǎoyā.", "È la prima volta che mangio l’anatra laccata.", ["这", "是", "我", "第一次", "吃", "烤鸭", "。"]),
    ("我每天上午都有课。", "Wǒ měi tiān shàngwǔ dōu yǒu kè.", "Ho lezione ogni mattina.", ["我", "每天", "上午", "都", "有", "课", "。"]),
  ],
  qa=[
    ("Qual è la differenza tra 「一月」 e 「一个月」?", "yīyuè / yí ge yuè", ["一月 = gennaio; 一个月 = un mese", "一月 = un mese; 一个月 = gennaio", "Sono la stessa cosa", "一月 = lunedì; 一个月 = un mese"], "Il nome del mese non ha il classificatore."),
    ("Non sei mai stato a Pechino. Come lo dici?", "", ["我没去过北京。", "我不去过北京。", "我没去北京过。", "我去过没北京。"], "没 + V + 过."),
    ("Ti chiedono 「寒假有多长时间？」. Quale risposta è adatta?", "hánjià yǒu duō cháng shíjiān?", ["一个多月。", "一月。", "第一个月。", "每个月。"], "Si risponde con una durata."),
    ("Come si dice “la seconda volta”?", "", ["第二次", "二次第", "两次", "第两次"], "第 + numero (二, non 两)."),
    ("「我只有三门课。」 significa…", "wǒ zhǐ yǒu sān mén kè.", ["Ho solo tre materie.", "Ho tre porte.", "Ho tre lezioni al giorno.", "Ho tre esami."], "只 = solo; 门 = classificatore per le materie."),
    ("Come si dice correttamente “Ho studiato cinese per sei mesi”?", "", ["我学了半年汉语。", "我半年学了汉语。", "我学汉语了半年了个。", "半年汉语我学了。"], "La durata va dopo il verbo."),
    ("Ti chiedono 「你看过这个电影吗？」 e l’hai visto. Cosa rispondi?", "nǐ kànguo zhège diànyǐng ma?", ["看过。", "看了过。", "过看。", "没看过了。"], "Risposta breve: V + 过."),
  ],
  extra=[("Poesia", "赋得古原草送别 · 白居易 (prima strofa)", "离离原上草，一岁一枯荣。野火烧不尽，春风吹又生。",
          "Lílí yuán shang cǎo, yí suì yì kū róng. Yěhuǒ shāo bú jìn, chūnfēng chuī yòu shēng.",
          "Rigogliosa l’erba sulla pianura: ogni anno appassisce e rifiorisce. Il fuoco della prateria non riesce a bruciarla del tutto: al soffio del vento di primavera rinasce."),
         ("Cultura", "Date e indirizzi", "", "",
          "In cinese si va sempre dal grande al piccolo. La data: 2025年10月9号 (anno, mese, giorno). L’indirizzo: paese, città, distretto, strada o università, edificio, stanza (中国上海市……大学3号楼502房间). Sulle buste, dopo il nome del destinatario si scrive 收 (“riceve”).")],
)

# ───────────────────────────── Lezione 16 ─────────────────────────────
L(n=16, zh="请问，去动物园怎么走？", py="Qǐngwèn, qù dòngwùyuán zěnme zǒu?", it="Scusi, come si arriva allo zoo?",
  theme="Chiedere e dare indicazioni stradali, appellativi, piani di un edificio",
  vocab="""
N|动物园|dòngwùyuán|名|zoo|zoo
N|走|zǒu|动|camminare, andare; andarsene|to walk, go
N|卖|mài|动|vendere|to sell
N|路人|lùrén|名|passante|passer-by
N|往|wǎng|介|verso, in direzione di|toward
N|前|qián|名|davanti, avanti|front
N|马路|mǎlù|名|strada|road
N|远|yuǎn|形|lontano|far
N|分钟|fēnzhōng|量|minuto (durata)|minute
N|到|dào|动|arrivare; fino a|to arrive
N|不客气|bú kèqi||prego, non c’è di che|you're welcome
N|同学|tóngxué|名|compagno di classe|classmate
N|科|kē|名|reparto (dell’ospedale)|department
N|清楚|qīngchu|形|chiaro|clear
N|再|zài|副|di nuovo; poi|again; then
N|别人|biéren|代|altri, gli altri|other people
N|大夫|dàifu|名|medico, dottore|doctor
N|右|yòu|名|destra|right
N|拐|guǎi|动|girare, svoltare|to turn
N|医院|yīyuàn|名|ospedale|hospital
N|层|céng|量|piano (di un edificio)|floor
N|认识|rènshi|动|conoscere (persone); riconoscere|to know (sb)
N|前边|qiánbian|名|davanti|in front
N|西|xī|名|ovest|west
S|词典|cídiǎn|名|dizionario|dictionary
S|茶叶|cháyè|名|foglie di tè|tea leaves
S|餐厅|cāntīng|名|sala da pranzo, ristorante|dining hall
S|书店|shūdiàn|名|libreria|bookstore
S|明白|míngbai|形,动|chiaro; capire|clear; to understand
S|银行|yínháng|名|banca|bank
S|东|dōng|名|est|east
S|左|zuǒ|名|sinistra|left
S|南|nán|名|sud|south
S|近|jìn|形|vicino|near
S|路口|lùkǒu|名|incrocio|crossroads
""",
  grammar=[
    ("Gli appellativi", "Per rivolgersi a qualcuno: 先生 (signore), 同学 (a uno studente), 大夫 (a un medico), 阿姨 (a una signora dell’età dei genitori). Si mettono all’inizio della frase.",
     [("先生，请问银行在哪儿？", "Xiānsheng, qǐngwèn yínháng zài nǎr?", "Scusi signore, dov’è la banca?"),
      ("大夫，我牙疼。", "Dàifu, wǒ yá téng.", "Dottore, ho mal di denti.")]),
    ("去……怎么走？", "Per chiedere la strada: 去 + luogo + 怎么走? Per rispondere: 往 + direzione + 走 / 拐 (girare).",
     [("请问，去动物园怎么走？", "Qǐngwèn, qù dòngwùyuán zěnme zǒu?", "Scusi, come si va allo zoo?"),
      ("往前走，到路口往右拐。", "Wǎng qián zǒu, dào lùkǒu wǎng yòu guǎi.", "Vada dritto e all’incrocio giri a destra.")]),
    ("Luogo + 就是", "就是 sottolinea “proprio lì / è proprio quello”.",
     [("马路左边就是银行。", "Mǎlù zuǒbian jiù shì yínháng.", "La banca è proprio sul lato sinistro della strada.")]),
    ("Durata + 就到了", "走几分钟就到了 = “in pochi minuti a piedi ci sei”: 就 indica che basta poco.",
     [("走五分钟就到了。", "Zǒu wǔ fēnzhōng jiù dào le.", "In cinque minuti a piedi ci sei.")]),
    ("太谢谢你了！", "Ringraziamento caloroso (“grazie mille!”). Si risponde 不客气 / 不用谢.",
     [("太谢谢您了！——不客气。", "Tài xièxie nín le! — Bú kèqi.", "Grazie mille! — Prego.")]),
    ("I piani: 层 / 楼", "二层 o 二楼 = il secondo piano (in Cina il piano terra è il 一层). 上楼 = salire al piano di sopra.",
     [("牙科在二层，你上楼吧。", "Yákē zài èr céng, nǐ shàng lóu ba.", "Il dentista è al secondo piano: sali pure.")]),
    ("再 (di nuovo / poi)", "再 + verbo: ripetere l’azione o farla in un secondo momento.",
     [("你再问问别人吧。", "Nǐ zài wènwen biéren ba.", "Prova a chiedere a qualcun altro.")]),
  ],
  dialogue=("Per strada", [
    ("丽莎", "先生，请问，去银行怎么走？", "Xiānsheng, qǐngwèn, qù yínháng zěnme zǒu?", "Scusi signore, come si arriva alla banca?"),
    ("路人", "往前走，到路口往右拐。", "Wǎng qián zǒu, dào lùkǒu wǎng yòu guǎi.", "Vada dritto e all’incrocio giri a destra."),
    ("丽莎", "远不远？", "Yuǎn bu yuǎn?", "È lontano?"),
    ("路人", "不远，走五分钟就到了。银行在书店的旁边。", "Bù yuǎn, zǒu wǔ fēnzhōng jiù dào le. Yínháng zài shūdiàn de pángbiān.", "No, in cinque minuti a piedi ci è. La banca è accanto alla libreria."),
    ("丽莎", "是马路左边还是右边？", "Shì mǎlù zuǒbian háishi yòubian?", "Sul lato sinistro o destro della strada?"),
    ("路人", "左边。", "Zuǒbian.", "Sinistro."),
    ("丽莎", "太谢谢您了！", "Tài xièxie nín le!", "Grazie mille!"),
    ("路人", "不客气。", "Bú kèqi.", "Prego."),
  ]),
  reading=("Yamada cerca un dizionario",
    "山田想买一本词典。他问同学：“哪儿卖词典？”同学说：“学校西边有一个书店，往前走，到路口往左拐就是。”山田走了十分钟就到了。书店有三层，词典在二层。山田上楼买了一本汉英词典。",
    "Shāntián xiǎng mǎi yì běn cídiǎn. Tā wèn tóngxué: “Nǎr mài cídiǎn?” Tóngxué shuō: “Xuéxiào xībian yǒu yí ge shūdiàn, wǎng qián zǒu, dào lùkǒu wǎng zuǒ guǎi jiù shì.” Shāntián zǒule shí fēnzhōng jiù dào le. Shūdiàn yǒu sān céng, cídiǎn zài èr céng. Shāntián shàng lóu mǎile yì běn Hàn-Yīng cídiǎn.",
    "Yamada vuole comprare un dizionario. Chiede a un compagno: “Dove vendono dizionari?” Il compagno risponde: “A ovest della scuola c’è una libreria: vai dritto e all’incrocio giri a sinistra, è lì.” Dopo dieci minuti a piedi Yamada arriva. La libreria ha tre piani e i dizionari sono al secondo. Yamada sale e compra un dizionario cinese-inglese.",
    [("山田想买什么？", "Shāntián xiǎng mǎi shénme?", ["一本词典", "一双鞋", "一件衣服", "茶叶"]),
     ("书店在学校的哪边？", "Shūdiàn zài xuéxiào de nǎ biān?", ["西边", "东边", "南边", "北边"]),
     ("词典在几层？", "Cídiǎn zài jǐ céng?", ["二层", "一层", "三层", "四层"]),
     ("山田走了多长时间？", "Shāntián zǒule duō cháng shíjiān?", ["十分钟", "五分钟", "两分钟", "一个小时"])]),
  cloze=[
    ("请问，去动物园怎么 ___？", "Qǐngwèn, qù dòngwùyuán zěnme ___?", "Scusi, come si arriva allo zoo?", ["走", "到", "拐", "卖"], "去……怎么走? = come si arriva a…?"),
    ("___ 前走，到路口往右拐。", "___ qián zǒu, dào lùkǒu wǎng yòu guǎi.", "Vada dritto e all’incrocio giri a destra.", ["往", "在", "从", "到"], "往 = verso."),
    ("到路口往左 ___。", "Dào lùkǒu wǎng zuǒ ___.", "All’incrocio giri a sinistra.", ["拐", "远", "到", "卖"], "拐 = girare, svoltare."),
    ("马路右边 ___ 是银行。", "Mǎlù yòubian ___ shì yínháng.", "La banca è proprio sul lato destro della strada.", ["就", "很", "往", "拐"], "就是 = proprio lì."),
    ("不远，走五分钟就 ___ 了。", "Bù yuǎn, zǒu wǔ fēnzhōng jiù ___ le.", "Non è lontano, in cinque minuti ci sei.", ["到", "走", "去", "往"], "到 = arrivare."),
    ("我不 ___，你问问别人吧。", "Wǒ bù ___, nǐ wènwen biéren ba.", "Non lo so con precisione, chiedi a qualcun altro.", ["清楚", "远", "近", "客气"], "不清楚 = non lo so di preciso."),
    ("牙科在二 ___。", "Yákē zài èr ___.", "Il dentista è al secondo piano.", ["层", "边", "分钟", "路口"], "层 = piano."),
    ("___，请问银行在哪儿？(a un signore)", "___, qǐngwèn yínháng zài nǎr?", "Scusi signore, dov’è la banca?", ["先生", "同学", "大夫", "阿姨"], "先生 = signore."),
    ("太谢谢你 ___！", "Tài xièxie nǐ ___!", "Grazie mille!", ["了", "的", "过", "着"], "太……了."),
  ],
  reorder=[
    ("请问，去动物园怎么走？", "Qǐngwèn, qù dòngwùyuán zěnme zǒu?", "Scusi, come si arriva allo zoo?", ["请问", "，", "去", "动物园", "怎么", "走", "？"]),
    ("往前走，到路口往右拐。", "Wǎng qián zǒu, dào lùkǒu wǎng yòu guǎi.", "Vada dritto e all’incrocio giri a destra.", ["往前走", "，", "到", "路口", "往右", "拐", "。"]),
    ("走几分钟就到了。", "Zǒu jǐ fēnzhōng jiù dào le.", "In pochi minuti a piedi ci sei.", ["走", "几分钟", "就", "到", "了", "。"]),
    ("银行在马路左边。", "Yínháng zài mǎlù zuǒbian.", "La banca è sul lato sinistro della strada.", ["银行", "在", "马路", "左边", "。"]),
    ("你再问问别人吧。", "Nǐ zài wènwen biéren ba.", "Prova a chiedere a qualcun altro.", ["你", "再", "问问", "别人", "吧", "。"]),
    ("请问，哪儿卖鞋？", "Qǐngwèn, nǎr mài xié?", "Scusi, dove vendono scarpe?", ["请问", "，", "哪儿", "卖", "鞋", "？"]),
  ],
  qa=[
    ("Chiedi la strada per la libreria. Quale frase usi?", "", ["请问，去书店怎么走？", "请问，书店怎么去走？", "请问，怎么走书店？", "请问，书店走怎么？"], "去 + luogo + 怎么走?"),
    ("All’ospedale vuoi rivolgerti al medico. Come lo chiami?", "", ["大夫", "同学", "先生们", "阿姨"], "大夫 = dottore."),
    ("Ti ringraziano: 「太谢谢你了！」. Cosa rispondi?", "tài xièxie nǐ le!", ["不客气。", "没问题。", "对不起。", "太好了。"], "不客气 = prego."),
    ("Ti chiedono 「远不远？」 e il posto è a due minuti. Cosa rispondi?", "yuǎn bu yuǎn?", ["不远，很近。", "很远，很近。", "不近，不远。", "远，走两分钟。"], "近 = vicino."),
    ("「往右拐」 significa…", "wǎng yòu guǎi", ["Gira a destra.", "Vai a sinistra.", "Vai dritto.", "Torna indietro."], "往 = verso; 拐 = girare."),
    ("Il passante dice 「我不清楚。」. Che cosa intende?", "wǒ bù qīngchu.", ["Non lo sa con precisione.", "Non ti sente.", "Non ti conosce.", "È occupato."], "清楚 = chiaro, preciso."),
    ("In Cina, che cosa indica 「一层」 in un edificio?", "yī céng", ["Il piano terra", "Il primo piano sopra il piano terra", "Il seminterrato", "L’ultimo piano"], "In Cina il piano terra è il primo piano (一层)."),
  ],
  extra=[("Poesia", "寻隐者不遇 · 贾岛", "松下问童子，言师采药去。只在此山中，云深不知处。",
          "Sōng xià wèn tóngzǐ, yán shī cǎi yào qù. Zhǐ zài cǐ shān zhōng, yún shēn bù zhī chù.",
          "Sotto i pini chiedo al giovane discepolo; dice che il maestro è andato a raccogliere erbe medicinali. “È proprio su questo monte, ma le nuvole sono fitte e non so dove.”")],
)

# ───────────────────────────── Lezione 17 ─────────────────────────────
L(n=17, zh="又好吃又便宜", py="Yòu hǎochī yòu piányi", it="Buono ed economico",
  theme="Al ristorante: ordinare, sapori, quantità, conto; fare confronti",
  vocab="""
N|又……又……|yòu…yòu…||sia… sia…|both… and…
N|光临|guānglín|动|(cortese) venire, onorare con la presenza|to visit (hon.)
N|位|wèi|量|classificatore cortese per persone|MW for people (polite)
N|里面|lǐmian|名|dentro, all’interno|inside
N|辣|là|形|piccante|spicy
N|菜单|càidān|名|menù|menu
N|鱼|yú|名|pesce|fish
N|茄子|qiézi|名|melanzana|eggplant
N|别|bié|副|non (imperativo)|don't
N|担心|dān xīn||preoccuparsi|to worry
N|味道|wèidao|名|sapore|taste, flavour
N|肉|ròu|名|carne|meat
N|够|gòu|动,副|bastare; abbastanza|enough
N|碗|wǎn|量,名|ciotola|bowl
N|米饭|mǐfàn|名|riso bollito|cooked rice
N|啤酒|píjiǔ|名|birra|beer
N|饿|è|形|affamato|hungry
N|马上|mǎshàng|副|subito|right away
N|比|bǐ|介|più di (nei paragoni)|than
N|香|xiāng|形|profumato, saporito|fragrant, tasty
N|饱|bǎo|形|sazio|full
N|打包|dǎ bāo||farsi incartare il cibo avanzato|to take away
N|结账|jié zhàng||pagare il conto|to pay the bill
N|汤|tāng|名|zuppa, brodo|soup
N|难|nán|形|difficile|difficult
N|会|huì|助动,动|saper fare; (futuro) è probabile che|can; will
S|糖醋鱼|tángcùyú|名|pesce in agrodolce|sweet and sour fish
S|西红柿炒鸡蛋|xīhóngshì chǎo jīdàn|名|uova strapazzate al pomodoro|stir-fried tomato and egg
S|鱼香茄子|yúxiāng qiézi|名|melanzane “al profumo di pesce”|fish-flavoured eggplant
S|铁板牛肉|tiěbǎn niúròu|名|manzo alla piastra|sizzling beef
S|炒土豆丝|chǎo tǔdòusī|名|patate saltate a julienne|stir-fried shredded potato
S|本子|běnzi|名|quaderno|notebook
S|椅子|yǐzi|名|sedia|chair
S|床|chuáng|名|letto|bed
S|牛奶|niúnǎi|名|latte|milk
S|冰激凌|bīngjīlíng|名|gelato|ice cream
S|面条儿|miàntiáor|名|noodles, spaghetti cinesi|noodles
""",
  grammar=[
    ("又……又……", "Unisce due qualità presenti insieme, entrambe positive o entrambe negative.",
     [("这儿的菜又好吃又便宜。", "Zhèr de cài yòu hǎochī yòu piányi.", "I piatti di qui sono buoni ed economici."),
      ("我喜欢又酸又甜的菜。", "Wǒ xǐhuan yòu suān yòu tián de cài.", "Mi piacciono i piatti agrodolci.")]),
    ("……什么的", "Alla fine di un elenco: “e così via, eccetera”.",
     [("食堂有饺子、面条儿、米饭什么的。", "Shítáng yǒu jiǎozi, miàntiáor, mǐfàn shénme de.", "In mensa ci sono ravioli, noodles, riso e così via.")]),
    ("来 + quantità + piatto", "Al ristorante 来 significa “portare / prendo…”.",
     [("来一个西红柿炒鸡蛋，两碗米饭。", "Lái yí ge xīhóngshì chǎo jīdàn, liǎng wǎn mǐfàn.", "Ci porti uova al pomodoro e due ciotole di riso.")]),
    ("Il complemento potenziale", "V + 得 + risultato = riuscire; V + 不 + risultato = non riuscire: 吃得完 / 吃不完 (riuscire / non riuscire a finire), 看得懂 / 看不懂, 说不清楚.",
     [("菜太多了，我们吃不完。", "Cài tài duō le, wǒmen chī bu wán.", "I piatti sono troppi, non riusciamo a finirli."),
      ("这个味道我说不清楚。", "Zhège wèidao wǒ shuō bu qīngchu.", "Questo sapore non so spiegarlo bene.")]),
    ("Il paragone con 比", "A 比 B + aggettivo. Per dire “molto di più” si aggiunge 多了, per “un po’” 一点儿. Con 比 non si usa 很 / 非常.",
     [("饺子比面条儿好吃。", "Jiǎozi bǐ miàntiáor hǎochī.", "I ravioli sono più buoni dei noodles."),
      ("今天比昨天冷一点儿。", "Jīntiān bǐ zuótiān lěng yìdiǎnr.", "Oggi fa un po’ più freddo di ieri.")]),
    ("别 + verbo", "Divieto o consiglio negativo: “non…!”.",
     [("别担心，这个菜不辣。", "Bié dān xīn, zhège cài bú là.", "Non preoccuparti, questo piatto non è piccante.")]),
    ("会", "会 + verbo = saper fare (per averlo imparato); può anche indicare che qualcosa probabilmente succederà.",
     [("我会做饺子。", "Wǒ huì zuò jiǎozi.", "So fare i ravioli."),
      ("明天会下雨吗？", "Míngtiān huì xià yǔ ma?", "Domani pioverà?")]),
    ("位", "Classificatore cortese per le persone: 几位? = quanti siete?",
     [("欢迎光临！几位？", "Huānyíng guānglín! Jǐ wèi?", "Benvenuti! Quanti siete?")]),
  ],
  dialogue=("Al ristorante", [
    ("服务员", "欢迎光临！两位吗？", "Huānyíng guānglín! Liǎng wèi ma?", "Benvenuti! Siete in due?"),
    ("刘伟", "对，两位。", "Duì, liǎng wèi.", "Sì, due."),
    ("服务员", "这是菜单。你们吃点儿什么？", "Zhè shì càidān. Nǐmen chī diǎnr shénme?", "Ecco il menù. Che cosa prendete?"),
    ("刘伟", "张新，你想吃什么？", "Zhāng Xīn, nǐ xiǎng chī shénme?", "Zhang Xin, tu cosa vuoi mangiare?"),
    ("张新", "我不吃辣的。来一个西红柿炒鸡蛋吧。", "Wǒ bù chī là de. Lái yí ge xīhóngshì chǎo jīdàn ba.", "Io non mangio piccante. Prendiamo le uova al pomodoro."),
    ("刘伟", "好。再来一个糖醋鱼，一碗汤。", "Hǎo. Zài lái yí ge tángcùyú, yì wǎn tāng.", "Va bene. E poi un pesce in agrodolce e una zuppa."),
    ("服务员", "要米饭吗？", "Yào mǐfàn ma?", "Volete del riso?"),
    ("刘伟", "两碗。菜够吗？", "Liǎng wǎn. Cài gòu ma?", "Due ciotole. Bastano i piatti?"),
    ("张新", "够了。听说这儿的菜又好吃又便宜！", "Gòu le. Tīngshuō zhèr de cài yòu hǎochī yòu piányi!", "Bastano. Dicono che qui si mangi bene e si spenda poco!"),
    ("服务员", "请等一下，菜马上来。", "Qǐng děng yíxià, cài mǎshàng lái.", "Attendete un attimo, i piatti arrivano subito."),
  ]),
  reading=("La trattoria vicino alla scuola",
    "我们学校旁边有一家小饭馆儿，菜又好吃又便宜。我很喜欢那儿的饺子，比食堂的好吃多了。上个星期我和丽莎去吃饭，点了三个菜、两碗面条儿，一共才六十块。菜太多了，我们吃不完，就打包了。",
    "Wǒmen xuéxiào pángbiān yǒu yì jiā xiǎo fànguǎnr, cài yòu hǎochī yòu piányi. Wǒ hěn xǐhuan nàr de jiǎozi, bǐ shítáng de hǎochī duō le. Shàng ge xīngqī wǒ hé Lìshā qù chī fàn, diǎnle sān ge cài, liǎng wǎn miàntiáor, yígòng cái liùshí kuài. Cài tài duō le, wǒmen chī bu wán, jiù dǎ bāo le.",
    "(Racconta Annie) Accanto alla nostra scuola c’è una piccola trattoria dove si mangia bene e si spende poco. Mi piacciono molto i loro ravioli: sono molto più buoni di quelli della mensa. La settimana scorsa ci sono andata con Lisa: abbiamo ordinato tre piatti e due ciotole di noodles, e in tutto abbiamo speso solo sessanta yuan. C’era troppo cibo, non riuscivamo a finirlo e ce lo siamo fatto incartare.",
    [("饭馆儿在哪儿？", "Fànguǎnr zài nǎr?", ["学校旁边", "宿舍里面", "图书馆的西边", "医院的旁边"]),
     ("安妮觉得那儿的饺子怎么样？", "Ānnī juéde nàr de jiǎozi zěnmeyàng?", ["比食堂的好吃多了", "没有食堂的好吃", "有点儿辣", "太贵了"]),
     ("她们一共花了多少钱？", "Tāmen yígòng huāle duōshao qián?", ["六十块", "三十块", "一百块", "十六块"]),
     ("吃不完的菜怎么了？", "Chī bu wán de cài zěnme le?", ["她们打包了", "她们给了朋友", "她们又点了", "她们吃完了"])]),
  cloze=[
    ("这儿的菜 ___ 好吃又便宜。", "Zhèr de cài ___ hǎochī yòu piányi.", "Qui si mangia bene e si spende poco.", ["又", "也", "都", "很"], "又……又…… = sia… sia…"),
    ("饺子 ___ 面条儿好吃。", "Jiǎozi ___ miàntiáor hǎochī.", "I ravioli sono più buoni dei noodles.", ["比", "别", "很", "又"], "A 比 B + aggettivo."),
    ("菜太多了，我们吃不 ___。", "Cài tài duō le, wǒmen chī bu ___.", "I piatti sono troppi, non riusciamo a finirli.", ["完", "过", "了", "的"], "吃不完 = non riuscire a finire."),
    ("___ 担心，这个菜不辣。", "___ dān xīn, zhège cài bú là.", "Non preoccuparti, questo piatto non è piccante.", ["别", "没", "很", "比"], "别 + verbo = non…! (imperativo)."),
    ("欢迎光临！几 ___？", "Huānyíng guānglín! Jǐ ___?", "Benvenuti! Quanti siete?", ["位", "本", "辆", "件"], "位 = classificatore cortese per le persone."),
    ("服务员，___ 两瓶啤酒！", "Fúwùyuán, ___ liǎng píng píjiǔ!", "Cameriere, ci porti due bottiglie di birra!", ["来", "去", "坐", "吃"], "来 = portare / prendere (al ristorante)."),
    ("一碗米饭 ___ 吗？", "Yì wǎn mǐfàn ___ ma?", "Basta una ciotola di riso?", ["够", "饱", "饿", "香"], "够 = bastare."),
    ("我吃 ___ 了，不能再吃了。", "Wǒ chī ___ le, bù néng zài chī le.", "Sono sazio, non riesco a mangiare altro.", ["饱", "饿", "辣", "香"], "吃饱 = mangiare a sazietà."),
    ("我 ___ 做饺子。", "Wǒ ___ zuò jiǎozi.", "So fare i ravioli.", ["会", "比", "别", "够"], "会 = saper fare."),
    ("我们点了鱼、肉、汤 ___。", "Wǒmen diǎnle yú, ròu, tāng ___.", "Abbiamo ordinato pesce, carne, zuppa e così via.", ["什么的", "什么", "怎么样", "多少"], "……什么的 = eccetera."),
  ],
  reorder=[
    ("这儿的菜又好吃又便宜。", "Zhèr de cài yòu hǎochī yòu piányi.", "Qui si mangia bene e si spende poco.", ["这儿", "的", "菜", "又好吃", "又便宜", "。"]),
    ("来一个西红柿炒鸡蛋。", "Lái yí ge xīhóngshì chǎo jīdàn.", "Ci porti uova al pomodoro.", ["来", "一个", "西红柿炒鸡蛋", "。"]),
    ("别担心，这个菜不辣。", "Bié dān xīn, zhège cài bú là.", "Non preoccuparti, questo piatto non è piccante.", ["别", "担心", "，", "这个", "菜", "不辣", "。"]),
    ("今天比昨天冷一点儿。", "Jīntiān bǐ zuótiān lěng yìdiǎnr.", "Oggi fa un po’ più freddo di ieri.", ["今天", "比", "昨天", "冷", "一点儿", "。"]),
    ("我们吃不完，打包吧。", "Wǒmen chī bu wán, dǎ bāo ba.", "Non riusciamo a finirlo: facciamocelo incartare.", ["我们", "吃不完", "，", "打包", "吧", "。"]),
    ("服务员，结账！", "Fúwùyuán, jié zhàng!", "Cameriere, il conto!", ["服务员", "，", "结账", "！"]),
  ],
  qa=[
    ("Il cameriere ti accoglie: 「欢迎光临！几位？」. Siete in tre. Cosa rispondi?", "huānyíng guānglín! jǐ wèi?", ["三位。", "三个位。", "第三位。", "三口。"], "Numero + 位."),
    ("Quale frase è corretta?", "", ["饺子比面条儿好吃。", "饺子比面条儿很好吃。", "饺子比面条儿非常好吃。", "饺子很比面条儿好吃。"], "Con 比 non si usa 很 / 非常."),
    ("Hai finito di mangiare e vuoi pagare. Cosa dici?", "", ["服务员，结账！", "服务员，打包！", "服务员，光临！", "服务员，马上！"], "结账 = pagare il conto."),
    ("Il tuo amico teme che il piatto sia piccante. Lo tranquillizzi:", "", ["别担心，不辣。", "不担心，很辣。", "没担心，辣。", "别辣，担心。"], "别 + verbo = non…!"),
    ("「这个味道我说不清楚。」 significa…", "zhège wèidao wǒ shuō bu qīngchu.", ["Non so spiegare bene questo sapore.", "Questo sapore non è buono.", "Non ho detto niente del sapore.", "Il sapore non è chiaro da vedere."], "V + 不 + risultato = non riuscire."),
    ("Ti chiedono 「你吃饱了吗？」 e hai mangiato abbastanza. Cosa rispondi?", "nǐ chībǎo le ma?", ["吃饱了，谢谢。", "吃饿了，谢谢。", "饱吃了。", "我很饿。"], "吃饱 = essere sazio."),
    ("Che cosa significa 「又酸又甜」?", "yòu suān yòu tián", ["Agrodolce (sia aspro sia dolce)", "Né aspro né dolce", "Più aspro che dolce", "Prima aspro, poi dolce"], "又……又…… = sia… sia…"),
  ],
  extra=[("Poesia", "悯农 · 李绅", "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。",
          "Chú hé rì dāng wǔ, hàn dī hé xià tǔ. Shéi zhī pán zhōng cān, lìlì jiē xīnkǔ.",
          "Zappano il grano sotto il sole di mezzogiorno, il sudore cola sulla terra sotto le piantine. Chi sa che, nel piatto, ogni chicco è frutto di fatica? (I bambini cinesi la imparano per non sprecare il cibo.)"),
         ("Cultura", "Mangiare insieme", "", "",
          "Al ristorante cinese i piatti si ordinano per tutta la tavola e si condividono; di solito si prende circa un piatto a persona più una zuppa, e il riso si ordina a parte. Per chiamare il cameriere si dice ad alta voce 服务员!; chiedere di 打包 gli avanzi è normalissimo.")],
)

# ───────────────────────────── Lezione 18 ─────────────────────────────
L(n=18, zh="我想请你做我的辅导，好吗？", py="Wǒ xiǎng qǐng nǐ zuò wǒ de fǔdǎo, hǎo ma?", it="Vuoi farmi da tutor?",
  theme="Chiedere aiuto per studiare, accordarsi su orari, descrivere come si fa qualcosa",
  vocab="""
N|辅导|fǔdǎo|动,名|seguire nello studio; tutor|to tutor; tutor
N|练习|liànxí|动,名|esercitarsi; esercizio|to practise; exercise
N|小时|xiǎoshí|名|ora (durata)|hour
N|行|xíng|动,形|va bene, d’accordo|OK
N|这样|zhèyàng|代|così, in questo modo|this way
N|互相|hùxiāng|副|reciprocamente|each other
N|水平|shuǐpíng|名|livello|level
N|声调|shēngdiào|名|tono|tone
N|希望|xīwàng|动,名|sperare; speranza|to hope; hope
N|地|de|助|particella avverbiale (agg. + 地 + verbo)|adverbial particle
N|答应|dāying|动|accettare, promettere|to agree
N|从|cóng|介|da (punto di partenza)|from
N|开始|kāishǐ|动|cominciare|to begin
N|教|jiāo|动|insegnare|to teach
N|见|jiàn|动|vedere, incontrare|to meet
N|得|de|助|particella del complemento di grado|structural particle
N|挺|tǐng|副|piuttosto, abbastanza|quite
N|聊|liáo|动|chiacchierare|to chat
N|爱好|àihào|名|hobby, passione|hobby
N|专业|zhuānyè|名|indirizzo di studi, specializzazione|major
N|一定|yídìng|副,形|sicuramente; certo|surely
N|有意思|yǒu yìsi||interessante|interesting
N|参加|cānjiā|动|partecipare|to take part in
N|唱|chàng|动|cantare|to sing
N|厉害|lìhai|形|forte, grave; bravissimo|severe; impressive
P|英语|Yīngyǔ||inglese (lingua)|English
S|帮忙|bāng máng||dare una mano|to help
S|认真|rènzhēn|形|serio, coscienzioso|conscientious
S|首|shǒu|量|classificatore per canzoni e poesie|MW for songs
S|后天|hòutiān|名|dopodomani|day after tomorrow
S|坏|huài|形|cattivo; rotto|bad; broken
S|商量|shāngliang|动|discutere, consultarsi|to discuss
S|方法|fāngfǎ|名|metodo|method
""",
  grammar=[
    ("行 / 那不行", "行 = “va bene, d’accordo”. 那不行 è un rifiuto deciso: “questo no, non se ne parla”.",
     [("你每天辅导我一个小时，行吗？——行。", "Nǐ měi tiān fǔdǎo wǒ yí ge xiǎoshí, xíng ma? — Xíng.", "Mi segui un’ora al giorno, va bene? — Va bene."),
      ("不要钱？那不行！", "Bú yào qián? Nà bù xíng!", "Non vuoi soldi? Non se ne parla!")]),
    ("这样吧", "Introduce una proposta o un compromesso: “facciamo così”.",
     [("这样吧，我们星期三见。", "Zhèyàng ba, wǒmen xīngqīsān jiàn.", "Facciamo così: ci vediamo mercoledì.")]),
    ("Aggettivo + 地 + verbo", "地 trasforma l’aggettivo in un avverbio di modo, prima del verbo: 认真地练习 (esercitarsi con impegno).",
     [("她认真地练习声调。", "Tā rènzhēn de liànxí shēngdiào.", "Si esercita con impegno sui toni."),
      ("他高兴地说：“太好了！”", "Tā gāoxìng de shuō: “Tài hǎo le!”", "Dice contento: “Fantastico!”")]),
    ("Il complemento di grado con 得", "V + 得 + aggettivo descrive come si fa un’azione: 说得很好. Con l’oggetto si ripete il verbo: (V) + O + V + 得 + aggettivo. Domanda: V得怎么样?",
     [("你汉语说得很好！", "Nǐ Hànyǔ shuō de hěn hǎo!", "Parli molto bene il cinese!"),
      ("他唱歌唱得怎么样？——唱得挺好的。", "Tā chàng gē chàng de zěnmeyàng? — Chàng de tǐng hǎo de.", "Come canta? — Canta piuttosto bene.")]),
    ("挺……的", "“Piuttosto, abbastanza” (parlato).",
     [("这个方法挺好的。", "Zhège fāngfǎ tǐng hǎo de.", "Questo metodo è piuttosto buono.")]),
    ("从……开始 · 互相 · 一定", "从 + tempo + 开始 = a partire da; 互相 + verbo = l’un l’altro; 一定 = sicuramente.",
     [("从下星期开始，我每天练习一个小时。", "Cóng xià xīngqī kāishǐ, wǒ měi tiān liànxí yí ge xiǎoshí.", "Dalla settimana prossima mi eserciterò un’ora al giorno."),
      ("我们互相练习口语吧。", "Wǒmen hùxiāng liànxí kǒuyǔ ba.", "Esercitiamoci a vicenda nella lingua parlata."),
      ("我一定参加！", "Wǒ yídìng cānjiā!", "Ci sarò di sicuro!")]),
  ],
  dialogue=("Una richiesta di aiuto", [
    ("彼得", "文静，我想请你帮个忙。", "Wénjìng, wǒ xiǎng qǐng nǐ bāng ge máng.", "Wenjing, vorrei chiederti un favore."),
    ("李文静", "什么事？你说吧。", "Shénme shì? Nǐ shuō ba.", "Che cosa c’è? Dimmi pure."),
    ("彼得", "我的汉字写得不好，你能辅导我吗？", "Wǒ de Hànzì xiě de bù hǎo, nǐ néng fǔdǎo wǒ ma?", "Scrivo male i caratteri: puoi seguirmi tu?"),
    ("李文静", "行啊。一个星期几次？", "Xíng a. Yí ge xīngqī jǐ cì?", "Certo. Quante volte alla settimana?"),
    ("彼得", "三次，每次半个小时，行吗？", "Sān cì, měi cì bàn ge xiǎoshí, xíng ma?", "Tre volte, mezz’ora ogni volta: va bene?"),
    ("李文静", "行。这样吧，星期一、三、五晚上七点，在图书馆。", "Xíng. Zhèyàng ba, xīngqīyī, sān, wǔ wǎnshang qī diǎn, zài túshūguǎn.", "Va bene. Facciamo così: lunedì, mercoledì e venerdì alle sette di sera, in biblioteca."),
    ("彼得", "太好了！从哪天开始？", "Tài hǎo le! Cóng nǎ tiān kāishǐ?", "Perfetto! Da che giorno cominciamo?"),
    ("李文静", "从下星期一开始吧。", "Cóng xià xīngqīyī kāishǐ ba.", "Da lunedì prossimo."),
    ("彼得", "谢谢你！我一定认真练习。", "Xièxie nǐ! Wǒ yídìng rènzhēn liànxí.", "Grazie! Mi eserciterò con impegno, promesso."),
  ]),
  reading=("Il tutor di Peter",
    "李文静是彼得的辅导。她辅导得挺好的，每次都很认真。他们练习写汉字，也聊法国和中国的生活，彼得觉得挺有意思的。现在彼得的汉字写得比以前好多了。他希望下个学期还请文静做他的辅导。",
    "Lǐ Wénjìng shì Bǐdé de fǔdǎo. Tā fǔdǎo de tǐng hǎo de, měi cì dōu hěn rènzhēn. Tāmen liànxí xiě Hànzì, yě liáo Fǎguó hé Zhōngguó de shēnghuó, Bǐdé juéde tǐng yǒu yìsi de. Xiànzài Bǐdé de Hànzì xiě de bǐ yǐqián hǎo duō le. Tā xīwàng xià ge xuéqī hái qǐng Wénjìng zuò tā de fǔdǎo.",
    "Li Wenjing è la tutor di Peter. Lo segue piuttosto bene ed è sempre molto seria. Si esercitano a scrivere caratteri e chiacchierano della vita in Francia e in Cina: Peter lo trova molto interessante. Ora Peter scrive i caratteri molto meglio di prima. Spera di avere Wenjing come tutor anche il prossimo semestre.",
    [("谁是彼得的辅导？", "Shéi shì Bǐdé de fǔdǎo?", ["李文静", "王平", "田老师", "山田"]),
     ("文静辅导得怎么样？", "Wénjìng fǔdǎo de zěnmeyàng?", ["挺好的", "不太好", "不认真", "太快了"]),
     ("现在彼得的汉字写得怎么样？", "Xiànzài Bǐdé de Hànzì xiě de zěnmeyàng?", ["比以前好多了", "没有以前好", "还不太好", "跟以前一样"]),
     ("彼得希望下个学期怎么样？", "Bǐdé xīwàng xià ge xuéqī zěnmeyàng?", ["还请文静做辅导", "回国", "不学汉字了", "去北京旅行"])]),
  cloze=[
    ("他汉语说 ___ 很好。", "Tā Hànyǔ shuō ___ hěn hǎo.", "Parla molto bene il cinese.", ["得", "地", "的", "了"], "V + 得 + aggettivo = complemento di grado."),
    ("她认真 ___ 练习声调。", "Tā rènzhēn ___ liànxí shēngdiào.", "Si esercita con impegno sui toni.", ["地", "得", "的", "了"], "Aggettivo + 地 + verbo."),
    ("这个方法 ___ 好的。", "Zhège fāngfǎ ___ hǎo de.", "Questo metodo è piuttosto buono.", ["挺", "太", "非常", "最"], "挺……的 = piuttosto."),
    ("___ 下星期开始，我每天练习一个小时。", "___ xià xīngqī kāishǐ, wǒ měi tiān liànxí yí ge xiǎoshí.", "Dalla prossima settimana mi eserciterò un’ora al giorno.", ["从", "在", "往", "到"], "从……开始 = a partire da…"),
    ("我们 ___ 练习口语吧。", "Wǒmen ___ liànxí kǒuyǔ ba.", "Esercitiamoci a vicenda nella lingua parlata.", ["互相", "一定", "这样", "挺"], "互相 = l’un l’altro."),
    ("不要钱？那不 ___！", "Bú yào qián? Nà bù ___!", "Non vuoi soldi? Non se ne parla!", ["行", "是", "在", "有"], "那不行 = rifiuto deciso."),
    ("你明天一定要来！——好，我 ___ 来。", "Nǐ míngtiān yídìng yào lái! — Hǎo, wǒ ___ lái.", "Domani devi venire! — D’accordo, verrò di sicuro.", ["一定", "互相", "这样", "挺"], "一定 = sicuramente."),
    ("你的 ___ 是什么？——我喜欢旅行。", "Nǐ de ___ shì shénme? — Wǒ xǐhuan lǚxíng.", "Qual è il tuo hobby? — Mi piace viaggiare.", ["爱好", "专业", "水平", "声调"], "爱好 = hobby."),
    ("我一个星期去两 ___ 图书馆。", "Wǒ yí ge xīngqī qù liǎng ___ túshūguǎn.", "Vado in biblioteca due volte alla settimana.", ["次", "个", "本", "节"], "次 = volta."),
  ],
  reorder=[
    ("我想请你做我的辅导。", "Wǒ xiǎng qǐng nǐ zuò wǒ de fǔdǎo.", "Vorrei che mi facessi da tutor.", ["我", "想", "请你", "做", "我的", "辅导", "。"]),
    ("你汉语说得很好。", "Nǐ Hànyǔ shuō de hěn hǎo.", "Parli molto bene il cinese.", ["你", "汉语", "说", "得", "很好", "。"]),
    ("我们互相练习吧。", "Wǒmen hùxiāng liànxí ba.", "Esercitiamoci a vicenda.", ["我们", "互相", "练习", "吧", "。"]),
    ("她认真地回答了问题。", "Tā rènzhēn de huídále wèntí.", "Ha risposto alla domanda con serietà.", ["她", "认真地", "回答", "了", "问题", "。"]),
    ("从下星期开始辅导。", "Cóng xià xīngqī kāishǐ fǔdǎo.", "Le lezioni con il tutor cominciano dalla settimana prossima.", ["从", "下星期", "开始", "辅导", "。"]),
    ("这个电影挺有意思的。", "Zhège diànyǐng tǐng yǒu yìsi de.", "Questo film è piuttosto interessante.", ["这个", "电影", "挺", "有意思", "的", "。"]),
  ],
  qa=[
    ("Ti offrono di farti da tutor gratis, ma vuoi pagare. Come rifiuti?", "", ["那不行！", "那很行！", "那行不！", "不那行！"], "那不行 = non se ne parla."),
    ("Vuoi dire “Facciamo così: ci vediamo sabato.” Come lo dici?", "", ["这样吧，我们星期六见。", "这样吗，我们星期六见。", "那样了，星期六见我们。", "这样的，我们见星期六。"], "这样吧 introduce una proposta."),
    ("Quale frase è corretta?", "", ["他唱歌唱得很好。", "他唱歌得很好。", "他唱得歌很好。", "他很好唱歌得。"], "Con l’oggetto si ripete il verbo: V + O + V + 得 + aggettivo."),
    ("Ti chiedono 「他辅导得怎么样？」 e pensi che sia bravo. Cosa rispondi?", "tā fǔdǎo de zěnmeyàng?", ["挺好的。", "挺好得。", "好挺的。", "得挺好。"], "挺……的."),
    ("Qual è la differenza tra 地 e 得?", "de", ["地 va prima del verbo (modo), 得 dopo il verbo (grado)", "Sono identici", "地 va dopo il verbo, 得 prima", "地 indica il possesso"], "认真地练习 / 练习得很认真."),
    ("「我们互相练习。」 significa…", "wǒmen hùxiāng liànxí.", ["Ci esercitiamo a vicenda.", "Ci esercitiamo da soli.", "Ci esercitiamo tutti i giorni.", "Ci esercitiamo con l’insegnante."], "互相 = l’un l’altro."),
    ("Ti invitano a una festa e vuoi assicurare che ci sarai. Cosa dici?", "", ["我一定参加！", "我参加一定！", "我挺参加！", "我互相参加！"], "一定 va prima del verbo."),
  ],
  extra=[("Poesia", "鸟鸣涧 · 王维", "人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。",
          "Rén xián guìhuā luò, yè jìng chūn shān kōng. Yuè chū jīng shān niǎo, shí míng chūn jiàn zhōng.",
          "L’uomo è in quiete, cadono i fiori d’osmanto; la notte è silenziosa, la montagna di primavera è vuota. Sorge la luna e spaventa gli uccelli dei monti, che a tratti cantano nel ruscello di primavera.")],
)

# ───────────────────────────── Lezione 19 ─────────────────────────────
L(n=19, zh="我有点儿不舒服", py="Wǒ yǒudiǎnr bù shūfu", it="Non mi sento molto bene",
  theme="Salute e sintomi, dal medico, esami andati male, preoccuparsi per qualcuno, congedarsi",
  vocab="""
N|舒服|shūfu|形|comodo; stare bene|comfortable, well
N|发烧|fā shāo||avere la febbre|to have a fever
N|回去|huíqù||tornare (indietro)|to go back
N|好好儿|hǎohāor|副|per bene, come si deve|properly
N|水|shuǐ|名|acqua|water
N|考|kǎo|动|sostenere un esame, fare un test|to take an exam
N|准备|zhǔnbèi|动|preparare, prepararsi|to prepare
N|没关系|méi guānxi||non importa, non fa niente|it doesn't matter
N|咳嗽|késou|动|tossire|to cough
N|努力|nǔlì|动,形|impegnarsi; diligente|to make an effort
N|关心|guānxīn|动|preoccuparsi per, interessarsi a|to care about
N|得|dé|动|ottenere; prendere (una malattia)|to get
N|重|zhòng|形|pesante; grave|heavy; serious
N|……极了|…jíle||estremamente (agg. + 极了)|extremely
N|陪|péi|动|accompagnare, fare compagnia|to accompany
N|出去|chūqù||uscire|to go out
N|散步|sàn bù||passeggiare|to take a walk
N|这么|zhème|代|così, tanto|so, like this
N|开玩笑|kāi wánxiào||scherzare|to joke
N|先|xiān|副,名|prima (di tutto)|first
N|改天|gǎitiān|副|un altro giorno|another day
N|漂亮|piàoliang|形|bello, carino|pretty
N|妹妹|mèimei|名|sorella minore|younger sister
N|高|gāo|形|alto|tall
N|试|shì|动|provare|to try
N|骑|qí|动|andare (in bici, a cavallo)|to ride
N|复习|fùxí|动|ripassare|to review
S|哭|kū|动|piangere|to cry
S|帮助|bāngzhù|动|aiutare|to help
S|词|cí|名|parola|word
S|姐姐|jiějie|名|sorella maggiore|elder sister
S|站|zhàn|动|stare in piedi|to stand
S|修理|xiūlǐ|动|riparare|to repair
""",
  grammar=[
    ("有点儿 e 一点儿", "有点儿 va PRIMA dell’aggettivo e indica qualcosa di sgradito: 有点儿不舒服. 一点儿 va DOPO l’aggettivo, per confronti o richieste: 好一点儿了, 快一点儿.",
     [("我有点儿发烧。", "Wǒ yǒudiǎnr fā shāo.", "Ho un po’ di febbre."),
      ("今天比昨天好一点儿。", "Jīntiān bǐ zuótiān hǎo yìdiǎnr.", "Oggi sto un po’ meglio di ieri.")]),
    ("好好儿 + verbo raddoppiato", "好好儿 = per bene, come si deve; spesso si unisce a un verbo raddoppiato per dare un consiglio affettuoso.",
     [("考试以前，你要好好儿复习复习。", "Kǎoshì yǐqián, nǐ yào hǎohāor fùxí fùxí.", "Prima dell’esame devi ripassare per bene.")]),
    ("没关系", "“Non importa, non fa niente”: risposta alle scuse o per consolare.",
     [("对不起！——没关系。", "Duìbuqǐ! — Méi guānxi.", "Scusa! — Non fa niente."),
      ("考得不好？没关系，下次好好儿准备。", "Kǎo de bù hǎo? Méi guānxi, xià cì hǎohāor zhǔnbèi.", "L’esame è andato male? Non importa, la prossima volta preparati bene.")]),
    ("没 e 没有", "Entrambi negano 有 e le azioni passate. Come risposta breve si usa solo 没有.",
     [("你复习了吗？——没有。", "Nǐ fùxí le ma? — Méiyǒu.", "Hai ripassato? — No."),
      ("我没准备好。", "Wǒ méi zhǔnbèi hǎo.", "Non mi sono preparato bene.")]),
    ("慢走", "Formula di congedo per chi se ne va (“vai piano, stammi bene”). Chi va via dice 我先走了.",
     [("我先走了，改天聊。——慢走！", "Wǒ xiān zǒu le, gǎitiān liáo. — Màn zǒu!", "Io vado, parliamo un’altra volta. — Ciao, stammi bene!")]),
    ("Aggettivo + 极了 · 这么 + aggettivo", "极了 = estremamente; 这么 = così, tanto.",
     [("今天热极了。", "Jīntiān rè jíle.", "Oggi fa un caldo pazzesco."),
      ("你怎么这么着急？", "Nǐ zěnme zhème zháojí?", "Perché hai così tanta fretta?")]),
  ],
  dialogue=("In ambulatorio", [
    ("大夫", "你哪儿不舒服？", "Nǐ nǎr bù shūfu?", "Dove si sente male?"),
    ("杰夫", "我头疼，还有点儿咳嗽。", "Wǒ tóu téng, hái yǒudiǎnr késou.", "Ho mal di testa e anche un po’ di tosse."),
    ("大夫", "发烧吗？", "Fā shāo ma?", "Ha la febbre?"),
    ("杰夫", "昨天晚上发烧了，今天好一点儿了。", "Zuótiān wǎnshang fā shāo le, jīntiān hǎo yìdiǎnr le.", "Ieri sera avevo la febbre, oggi va un po’ meglio."),
    ("大夫", "你得了感冒，不太重。", "Nǐ déle gǎnmào, bú tài zhòng.", "Ha preso il raffreddore, non è grave."),
    ("杰夫", "明天我有考试，能去吗？", "Míngtiān wǒ yǒu kǎoshì, néng qù ma?", "Domani ho un esame: posso andarci?"),
    ("大夫", "能。今天回去好好儿休息，多喝水。", "Néng. Jīntiān huíqù hǎohāor xiūxi, duō hē shuǐ.", "Sì. Oggi torni a casa, si riposi bene e beva molta acqua."),
    ("杰夫", "谢谢大夫！我先走了。", "Xièxie dàifu! Wǒ xiān zǒu le.", "Grazie, dottore! Allora vado."),
    ("大夫", "慢走！", "Màn zǒu!", "Arrivederci, si riguardi!"),
  ]),
  reading=("Lisa sta meglio",
    "上个星期丽莎病得很重，发烧、咳嗽，三天没有上课。安妮每天陪她去医院，还给她买饭。田老师和同学们都很关心她。现在丽莎好多了，她说：“谢谢大家的关心！我要努力复习，准备期末考试。”",
    "Shàng ge xīngqī Lìshā bìng de hěn zhòng, fā shāo, késou, sān tiān méiyǒu shàng kè. Ānnī měi tiān péi tā qù yīyuàn, hái gěi tā mǎi fàn. Tián lǎoshī hé tóngxuémen dōu hěn guānxīn tā. Xiànzài Lìshā hǎo duō le, tā shuō: “Xièxie dàjiā de guānxīn! Wǒ yào nǔlì fùxí, zhǔnbèi qīmò kǎoshì.”",
    "La settimana scorsa Lisa era molto malata: febbre e tosse, e per tre giorni non è andata a lezione. Annie la accompagnava ogni giorno in ospedale e le comprava anche da mangiare. La professoressa Tian e i compagni erano tutti preoccupati per lei. Ora Lisa sta molto meglio e dice: “Grazie a tutti per l’interessamento! Ora mi impegnerò a ripassare per gli esami di fine semestre.”",
    [("丽莎上个星期怎么了？", "Lìshā shàng ge xīngqī zěnme le?", ["病得很重", "去旅行了", "回国了", "考试了"]),
     ("谁每天陪丽莎去医院？", "Shéi měi tiān péi Lìshā qù yīyuàn?", ["安妮", "田老师", "山田", "王平"]),
     ("丽莎几天没有上课？", "Lìshā jǐ tiān méiyǒu shàng kè?", ["三天", "一天", "五天", "一个星期"]),
     ("现在丽莎要做什么？", "Xiànzài Lìshā yào zuò shénme?", ["努力复习，准备考试", "出去散步", "回国休息", "去医院看病"])]),
  cloze=[
    ("我 ___ 不舒服。", "Wǒ ___ bù shūfu.", "Non mi sento molto bene.", ["有点儿", "一点儿", "一下", "一会儿"], "有点儿 + aggettivo (sgradito)."),
    ("今天比昨天好 ___ 了。", "Jīntiān bǐ zuótiān hǎo ___ le.", "Oggi sto un po’ meglio di ieri.", ["一点儿", "有点儿", "一下", "极了"], "Aggettivo + 一点儿 nei confronti."),
    ("你回去 ___ 休息休息吧。", "Nǐ huíqù ___ xiūxi xiūxi ba.", "Torna a casa e riposati per bene.", ["好好儿", "有点儿", "这么", "先"], "好好儿 = per bene."),
    ("对不起！——___。", "Duìbuqǐ! — ___.", "Scusa! — Non fa niente.", ["没关系", "不客气", "没问题", "开玩笑"], "A 对不起 si risponde 没关系."),
    ("今天天气好 ___！", "Jīntiān tiānqì hǎo ___!", "Oggi il tempo è bellissimo!", ["极了", "一点儿", "有点儿", "这么"], "Aggettivo + 极了 = estremamente."),
    ("我走了。——慢 ___！", "Wǒ zǒu le. — Màn ___!", "Io vado. — Ciao, stammi bene!", ["走", "来", "去", "回"], "慢走 = formula di congedo."),
    ("考得不好，我没 ___ 好。", "Kǎo de bù hǎo, wǒ méi ___ hǎo.", "L’esame è andato male: non mi sono preparato bene.", ["准备", "关心", "陪", "散步"], "准备 = prepararsi."),
    ("别 ___ 了，他不是我男朋友！", "Bié ___ le, tā bú shì wǒ nán péngyou!", "Non scherzare, non è il mio ragazzo!", ["开玩笑", "关心", "准备", "咳嗽"], "开玩笑 = scherzare."),
    ("我想出去散步，你 ___ 我去吧。", "Wǒ xiǎng chūqù sàn bù, nǐ ___ wǒ qù ba.", "Voglio uscire a passeggiare, vieni con me.", ["陪", "考", "等", "试"], "陪 = accompagnare, fare compagnia."),
  ],
  reorder=[
    ("我有点儿不舒服。", "Wǒ yǒudiǎnr bù shūfu.", "Non mi sento molto bene.", ["我", "有点儿", "不", "舒服", "。"]),
    ("你回去好好儿休息吧。", "Nǐ huíqù hǎohāor xiūxi ba.", "Torna a casa e riposati per bene.", ["你", "回去", "好好儿", "休息", "吧", "。"]),
    ("今天比昨天好一点儿。", "Jīntiān bǐ zuótiān hǎo yìdiǎnr.", "Oggi sto un po’ meglio di ieri.", ["今天", "比", "昨天", "好", "一点儿", "。"]),
    ("谢谢你的关心！", "Xièxie nǐ de guānxīn!", "Grazie per l’interessamento!", ["谢谢", "你", "的", "关心", "！"]),
    ("我陪你出去散散步吧。", "Wǒ péi nǐ chūqù sànsan bù ba.", "Ti accompagno a fare due passi.", ["我", "陪你", "出去", "散散步", "吧", "。"]),
    ("我得了重感冒。", "Wǒ déle zhòng gǎnmào.", "Mi sono preso un brutto raffreddore.", ["我", "得了", "重", "感冒", "。"]),
  ],
  qa=[
    ("Quale frase è corretta?", "", ["我有点儿不舒服。", "我一点儿不舒服。", "我不舒服有点儿。", "我舒服有点儿不。"], "有点儿 va prima dell’aggettivo."),
    ("Un amico si scusa: 「对不起，我来晚了。」. Cosa rispondi?", "duìbuqǐ, wǒ lái wǎn le.", ["没关系。", "不客气。", "慢走。", "改天吧。"], "没关系 = non fa niente."),
    ("Un ospite se ne va. Cosa gli dici sulla porta?", "", ["慢走！", "快走！", "别走！", "走慢！"], "慢走 = formula di congedo."),
    ("Ti chiedono 「你复习了吗？」 e non l’hai fatto. Risposta breve corretta:", "nǐ fùxí le ma?", ["没有。", "没。", "不有。", "没了。"], "Da solo si usa 没有, non 没."),
    ("「她病得很重。」 significa…", "tā bìng de hěn zhòng.", ["È molto malata.", "È un po’ malata.", "È guarita.", "Porta un peso."], "V + 得 + aggettivo: grado."),
    ("Il medico ti dice 「多喝水」. Che cosa ti consiglia?", "duō hē shuǐ", ["Bere molta acqua.", "Bere poca acqua.", "Non bere acqua.", "Bere acqua calda."], "多 + verbo = fare di più."),
    ("Un’amica ti propone una passeggiata, ma aspetti un ospite. Cosa dici?", "", ["对不起，改天吧。", "没关系，改天吧。", "慢走，改天吧。", "开玩笑，改天吧。"], "改天 = un altro giorno."),
  ],
  extra=[("Poesia", "相思 · 王维", "红豆生南国，春来发几枝。愿君多采撷，此物最相思。",
          "Hóngdòu shēng nánguó, chūn lái fā jǐ zhī. Yuàn jūn duō cǎixié, cǐ wù zuì xiāngsī.",
          "I fagioli rossi crescono nel sud: a primavera, quanti rametti spuntano? Ti prego, raccoglili in abbondanza: nulla più di loro parla di nostalgia.")],
)
