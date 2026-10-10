# -*- coding: utf-8 -*-
"""Rigenera app.css, il CSS di Tailwind già compilato che usa l'app.

Va eseguito quando in index.html si usano classi Tailwind nuove:
    python tools/build_css.py
poi apri nel browser l'indirizzo che viene stampato. La pagina tools/gen_css.html
legge index.html, fa generare a Tailwind il CSS delle classi usate e lo rimanda qui,
che lo salva (compattato) in app.css e si chiude da solo.
"""
import http.server
import os
import re
import socketserver
import threading

PORT = 8766
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(ROOT, "app.css")


def minify(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    # Spazi tolti solo attorno a { } , > ; i due punti restano ("a :hover" ≠ "a:hover") e le variabili
    # vuote di Tailwind ("--tw-pan-x: ;") devono conservare lo spazio, altrimenti alcuni browser le scartano.
    css = re.sub(r"\s*([{},>])\s*", r"\1", css)
    css = re.sub(r"(?<!:)\s*;\s*", ";", css)
    return css.strip()


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_POST(self):
        if self.path != "/__save_css":
            self.send_error(404)
            return
        css = self.rfile.read(int(self.headers.get("Content-Length", 0))).decode("utf-8")
        with open(DEST, "w", encoding="utf-8", newline="\n") as f:
            f.write("/* Generato da tools/build_css.py (Tailwind 3.4.17) — non modificare a mano */\n" + minify(css) + "\n")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")
        print("app.css salvato: %d KB" % (os.path.getsize(DEST) // 1024))
        threading.Thread(target=self.server.shutdown).start()

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print("Apri nel browser: http://127.0.0.1:%d/tools/gen_css.html" % PORT)
        httpd.serve_forever()
