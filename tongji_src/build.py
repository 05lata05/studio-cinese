# -*- coding: utf-8 -*-
"""Valida i contenuti del corso Tongji e genera ../tongji_data.js.

Uso:  python build.py
Ogni errore di formato (frasi da riordinare che non ricompongono la frase,
opzioni duplicate, vocaboli doppi, parlanti sconosciuti...) blocca la build.
"""
import glob
import hashlib
import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import common  # noqa: E402

MODULES = ["lessons_a", "lessons_b", "lessons_c", "lessons_d"]
errors = []


def err(msg):
    errors.append(msg)


def has_han(s):
    return re.search(r"[一-鿿]", s or "") is not None


lessons = []
for name in MODULES:
    if os.path.exists(os.path.join(HERE, name + ".py")):
        lessons += importlib.import_module(name).LESSONS
lessons.sort(key=lambda l: l["n"])

# Esercizi aggiuntivi (extra_quiz.py): si sommano a quelli della lezione
if os.path.exists(os.path.join(HERE, "extra_quiz.py")):
    by_n = {l["n"]: l for l in lessons}
    for n, kinds in importlib.import_module("extra_quiz").EXTRA.items():
        if n not in by_n:
            err("extra_quiz: la lezione %d non esiste" % n); continue
        for kind, items in kinds.items():
            if kind not in ("cloze", "reorder", "qa"):
                err("extra_quiz L%d: tipo %r non valido" % (n, kind)); continue
            by_n[n][kind] = list(by_n[n].get(kind, [])) + list(items)

out = {"title": common.COURSE_TITLE,
       "characters": [list(c) for c in common.CHARACTERS],
       "lessons": [], "vocab": [], "cloze": [], "reorder": [], "qa": [], "measure": [],
       "mwPool": common.MW_DISTRACTORS}
seen_vocab = {}

for les in lessons:
    n = les["n"]
    where = "L%d" % n
    # ── vocabolario ──
    for raw in les["vocab"].strip().splitlines():
        parts = raw.split("|")
        if len(parts) != 6:
            err("%s vocab: 6 campi attesi -> %r" % (where, raw)); continue
        t, zh, py, pos, it, en = [p.strip() for p in parts]
        if t not in ("N", "S", "P"):
            err("%s vocab: tipo %r non valido" % (where, t))
        key = (zh, py)  # maiuscola = nome proprio: 张 Zhāng (cognome) ≠ 张 zhāng (classificatore)
        if key in seen_vocab:
            err("%s vocab: %s %s già presente in L%d" % (where, zh, py, seen_vocab[key]))
        seen_vocab[key] = n
        if t == "P":
            cat = common.CAT_PROPER
        elif not pos:
            cat = common.CAT_PHRASE
        else:
            first = pos.split(",")[0]
            cat = common.POS_CATEGORY.get(first)
            if not cat:
                err("%s vocab: pos sconosciuta %r (%s)" % (where, pos, zh)); cat = common.CAT_PHRASE
        out["vocab"].append([n, t, zh, py, cat, it, en, pos])

    # ── grammatica ──
    gram = []
    for g in les.get("grammar", []):
        title, expl, exs = g
        for ex in exs:
            if len(ex) != 3:
                err("%s grammar %r: esempio con %d campi" % (where, title, len(ex)))
        gram.append({"t": title, "x": expl, "ex": [list(e) for e in exs]})

    # ── dialogo ──
    dlg = None
    if les.get("dialogue"):
        d = les["dialogue"]
        scene, lines = d[0], d[1]
        reorderable = d[2] if len(d) > 2 else True
        rows = []
        for ln in lines:
            if len(ln) != 4:
                err("%s dialogo: riga con %d campi" % (where, len(ln))); continue
            spk = ln[0]
            if spk not in common.SPEAKERS:
                err("%s dialogo: parlante sconosciuto %r" % (where, spk))
            rows.append([spk, common.SPEAKERS.get(spk, spk), ln[1], ln[2], ln[3]])
        if reorderable and len({r[0] + r[2] for r in rows}) != len(rows):
            err("%s dialogo: righe duplicate in un dialogo riordinabile" % where)
        dlg = {"scene": scene, "lines": rows, "reorder": bool(reorderable)}

    # ── lettura ──
    rd = None
    if les.get("reading"):
        title, zh, py, it, qs = les["reading"]
        qq = []
        for q in qs:
            qzh, qpy, opts = q
            if len(set(opts)) != len(opts) or len(opts) < 3:
                err("%s lettura: opzioni non valide %r" % (where, opts))
            qq.append([qzh, qpy, opts])
        rd = {"title": title, "zh": zh, "py": py, "it": it, "q": qq}

    # ── esercizi ──
    for c in les.get("cloze", []):
        zh, py, it, opts, exp = c
        if "___" not in zh:
            err("%s cloze senza ___: %s" % (where, zh))
        if len(set(opts)) != len(opts) or len(opts) < 3:
            err("%s cloze opzioni non valide: %r" % (where, opts))
        out["cloze"].append([n, zh, py, it, opts, exp])
    for r in les.get("reorder", []):
        zh, py, it, words = r
        if "".join(words) != zh:
            err("%s riordina: %r != %r" % (where, "".join(words), zh))
        if len(words) < 3:
            err("%s riordina: troppo pochi pezzi in %s" % (where, zh))
        out["reorder"].append([n, zh, py, it, words])
    for q in les.get("qa", []):
        text, py, opts, exp = q
        if len(set(opts)) != len(opts) or len(opts) < 3:
            err("%s qa opzioni non valide: %r" % (where, opts))
        out["qa"].append([n, text, py, opts, exp])

    extra = [{"type": e[0], "title": e[1], "zh": e[2], "py": e[3], "it": e[4]} for e in les.get("extra", [])]
    out["lessons"].append({"n": n, "zh": les["zh"], "py": les["py"], "it": les["it"],
                           "theme": les.get("theme", ""), "grammar": gram,
                           "dialogue": dlg, "reading": rd, "extra": extra})

# ── niente esercizi doppi (stessa frase da completare o da riordinare, stessa domanda con la stessa risposta) ──
for kind, key in (("cloze", lambda x: x[1]), ("reorder", lambda x: x[1]), ("qa", lambda x: (x[1], x[3][0]))):
    seen_ex = {}
    for x in out[kind]:
        k = key(x)
        if k in seen_ex:
            err("%s doppio in L%d e L%d: %s" % (kind, seen_ex[k], x[0], k))
        seen_ex[k] = x[0]

# ── classificatori: solo nomi presenti nel vocabolario ──
vocab_zh = {v[2] for v in out["vocab"]}
for zh, mws in common.MEASURE:
    lst = mws.split()
    if zh in vocab_zh and lst:
        out["measure"].append([zh, lst])

if errors:
    print("ERRORI (%d):" % len(errors))
    for e in errors:
        print("  -", e)
    sys.exit(1)


# ── traduzione inglese ──
# Ogni testo italiano mostrato nell'app ha una traduzione in en_*.tsv (righe "codice<TAB>inglese",
# il codice è l'hash del testo italiano). Se un testo cambia o è nuovo, la build si ferma e scrive
# en_todo.tsv con i testi ancora da tradurre.
def text_id(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:8]


needed = {}


def need(s):
    if isinstance(s, str) and re.search(r"[A-Za-zÀ-ÿ]", s):
        needed[text_id(s)] = s


for les in out["lessons"]:
    need(les["it"]); need(les["theme"])
    for g in les["grammar"]:
        need(g["t"]); need(g["x"])
        for ex in g["ex"]:
            need(ex[2])
    if les["dialogue"]:
        need(les["dialogue"]["scene"])
        for ln in les["dialogue"]["lines"]:
            need(ln[1]); need(ln[4])
    if les["reading"]:
        need(les["reading"]["title"]); need(les["reading"]["it"])
        for q in les["reading"]["q"]:
            for o in q[2]:
                need(o)
    for x in les["extra"]:
        need(x["type"]); need(x["title"]); need(x["it"])
for c in out["cloze"]:
    need(c[3]); need(c[5])
    for o in c[4]:
        need(o)
for r in out["reorder"]:
    need(r[3])
for q in out["qa"]:
    need(q[1]); need(q[4])
    for o in q[3]:
        need(o)

tr = {}
for path in sorted(glob.glob(os.path.join(HERE, "en_*.tsv"))):
    if path.endswith("en_todo.tsv"):
        continue
    with open(path, encoding="utf-8") as f:
        for no, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#"):
                continue
            key, _, val = line.partition("\t")
            if not val.strip():
                errors.append("%s:%d traduzione vuota" % (os.path.basename(path), no))
            tr[key.strip()] = val.strip()

missing = [k for k in needed if k not in tr]
todo = os.path.join(HERE, "en_todo.tsv")
if missing:
    with open(todo, "w", encoding="utf-8", newline="\n") as f:
        for k in missing:
            f.write("%s\t%s\n" % (k, needed[k].replace("\n", " ")))
    errors.append("%d testi senza traduzione inglese: vedi en_todo.tsv" % len(missing))
elif os.path.exists(todo):
    os.remove(todo)
for k in needed:  # i caratteri cinesi citati nel testo devono restare anche nella traduzione
    if k in tr:
        lost = set(re.findall(r"[㐀-鿿]", needed[k])) - set(re.findall(r"[㐀-鿿]", tr[k]))
        if lost:
            errors.append("traduzione %s: mancano i caratteri %s" % (k, "".join(sorted(lost))))
unused = set(tr) - set(needed)

if errors:
    print("ERRORI (%d):" % len(errors))
    for e in errors[:40]:
        print("  -", e)
    sys.exit(1)

js = ("// File generato da tongji_src/build.py — NON modificare a mano.\n"
      "// Contenuti originali basati su vocabolario e grammatica di 初级汉语口语 1.\n"
      "window.TONGJI_DATA = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")
dest = os.path.join(HERE, "..", "tongji_data.js")
with open(dest, "w", encoding="utf-8") as f:
    f.write(js)
en_js = ("// File generato da tongji_src/build.py — NON modificare a mano.\n"
         "// Traduzione inglese dei testi del corso Tongji: testo italiano → testo inglese.\n"
         "window.TONGJI_EN = " + json.dumps({needed[k]: tr[k] for k in needed}, ensure_ascii=False, separators=(",", ":")) + ";\n")
with open(os.path.join(HERE, "..", "tongji_en.js"), "w", encoding="utf-8") as f:
    f.write(en_js)

print("OK -> tongji_data.js (%d KB), tongji_en.js (%d KB, %d testi)%s" % (
    len(js.encode("utf-8")) // 1024, len(en_js.encode("utf-8")) // 1024, len(needed),
    " — %d traduzioni non più usate" % len(unused) if unused else ""))
print("Lezioni: %d | Vocaboli: %d | Cloze: %d | Riordina: %d | Q&A: %d | Classificatori: %d" % (
    len(out["lessons"]), len(out["vocab"]), len(out["cloze"]), len(out["reorder"]),
    len(out["qa"]), len(out["measure"])))
