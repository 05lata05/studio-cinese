# -*- coding: utf-8 -*-
"""Controlla che ogni testo passato a t('…') in index.html abbia la traduzione in i18n_en.js.

Uso:  python tools/check_i18n.py
Stampa i testi senza traduzione (e quelli con segnaposto {n}, {name}… diversi); esce con errore se ce ne sono.
I testi statici dell'HTML non vengono controllati qui: per quelli basta provare l'app in inglese.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
js = open(os.path.join(ROOT, "i18n_en.js"), encoding="utf-8").read()
d = json.loads(js.split("window.I18N_EN = ", 1)[1].strip().rstrip(";"))

logic = src[src.index("// ─── Helpers"):]
keys = []
pos = 0
while True:  # argomenti letterali di t(...), anche dentro i ternari
    i = logic.find("t(", pos)
    if i < 0:
        break
    pos = i + 2
    if i > 0 and (logic[i - 1].isalnum() or logic[i - 1] in "_.$"):
        continue
    depth, j, inq = 1, i + 2, None
    while j < len(logic) and depth:
        ch = logic[j]
        if inq:
            if ch == "\\":
                j += 1
            elif ch == inq:
                inq = None
        elif ch in "'`\"":
            inq = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        j += 1
    seg = re.split(r",\s*\{", logic[i + 2:j - 1])[0]
    for q in re.finditer(r"'((?:[^'\\]|\\.)*)'", seg):
        if re.search(r"[A-Za-zÀ-ÿ]{2}", q.group(1)) and q.group(1) not in keys:
            keys.append(q.group(1))
for m in re.finditer(r"showToast\(\s*'((?:[^'\\]|\\.)*)'", logic):  # i messaggi vengono tradotti da showToast
    keys.append(m.group(1))
for blk in ("POLIMI_MQ_CATEGORIES", "TONGJI_MQ_CATEGORIES"):  # etichette e codici delle categorie del Mega-Quiz
    seg = logic[logic.index("const " + blk):]
    keys += re.findall(r"'([^']*)'", seg[:seg.index("];")])

IGNORE = {"testo italiano", "MISSING_GROQ_KEY", "all"}
missing = sorted({k for k in keys if k not in d and k not in IGNORE})
bad = sorted(k for k, v in d.items() if sorted(re.findall(r"\{\w+\}", k)) != sorted(re.findall(r"\{\w+\}", v)))
for k in missing:
    print("SENZA TRADUZIONE:", k)
for k in bad:
    print("SEGNAPOSTO DIVERSI:", k)
print("%d testi controllati, %d senza traduzione, %d con segnaposto diversi" % (len(set(keys)), len(missing), len(bad)))
sys.exit(1 if missing or bad else 0)
