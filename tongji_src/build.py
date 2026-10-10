# -*- coding: utf-8 -*-
"""Valida i contenuti del corso Tongji e genera ../tongji_data.js.

Uso:  python build.py
Ogni errore di formato (frasi da riordinare che non ricompongono la frase,
opzioni duplicate, vocaboli doppi, parlanti sconosciuti...) blocca la build.
"""
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

js = ("// File generato da tongji_src/build.py — NON modificare a mano.\n"
      "// Contenuti originali basati su vocabolario e grammatica di 初级汉语口语 1.\n"
      "window.TONGJI_DATA = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")
dest = os.path.join(HERE, "..", "tongji_data.js")
with open(dest, "w", encoding="utf-8") as f:
    f.write(js)

print("OK -> tongji_data.js (%d KB)" % (len(js.encode("utf-8")) // 1024))
print("Lezioni: %d | Vocaboli: %d | Cloze: %d | Riordina: %d | Q&A: %d | Classificatori: %d" % (
    len(out["lessons"]), len(out["vocab"]), len(out["cloze"]), len(out["reorder"]),
    len(out["qa"]), len(out["measure"])))
