# Studio Cinese — PWA

App per lo studio del cinese mandarino di Luigi Latagliata, installabile come vera app su smartphone (PWA).

## Struttura
- `index.html` — l'app (identica a `studio_cinese_v4_1.html`, con i tag PWA aggiunti)
- `tongji_data.js` — contenuti del corso Tongji (初级汉语口语 1), **generato**: non modificarlo a mano
- `tongji_src/` — sorgenti dei contenuti Tongji: `lessons_a.py` (lezioni 1-7), `lessons_b.py` (8-13), `lessons_c.py` (14-19), `lessons_d.py` (20-25), `common.py` (personaggi, categorie, classificatori) e `build.py` (controlla e genera `tongji_data.js`)
- `app.css` — stili Tailwind già compilati, **generato**: si rigenera con `python tools/build_css.py` (poi apri l'indirizzo che stampa) quando in `index.html` si usano classi nuove
- `tools/` — `build_css.py` e `gen_css.html`, che generano `app.css`
- `manifest.json` — nome, icone, colori dell'app installata
- `sw.js` — service worker (funzionamento offline + aggiornamenti in background)
- `icons/` — icone dell'app in varie dimensioni

## I due corsi
All'accesso si sceglie il corso (si può cambiare dal pulsante in alto):
- **Corso Politecnico** — l'app originale, con i dati salvati di sempre.
- **Corso Tongji** — le 25 lezioni del libro: sezione "Lezioni del corso" (vocaboli, grammatica, dialogo, lettura, poesie e scioglilingua), lezione attuale, Mega-Quiz e flashcard filtrabili per intervallo di lezioni (es. dalla 1 alla 4).

Ogni corso ha i propri salvataggi, statistiche e backup. Dialoghi, letture ed esercizi del corso Tongji sono testi originali scritti sul vocabolario e sulla grammatica di ciascuna lezione (non copiati dal libro).

## Funzioni di studio
- **Ripasso di oggi** (ripetizione dilazionata): le parole sbagliate tornano subito, quelle giuste dopo 1, 3, 7, 14, 30, 60, 120 giorni, più 10 parole nuove al giorno. Lo aggiornano Memory, Mega-Quiz e dettato.
- **Obiettivo giornaliero e serie di giorni** (🔥), comuni ai due corsi.
- **Ripeti gli errori** del Mega-Quiz: una domanda sparisce dall'elenco quando la indovini.
- **Dettato (听写)** nel Laboratorio Tratti: a mano (controllo dei tratti, serve la connessione la prima volta) o con la tastiera cinese.
- **AI Tutor collegato al corso**: frasi ed "esercizi su misura" con il solo vocabolario studiato.
- **Progressi per lezione** e punti deboli (corso Tongji), **ricerca nella grammatica**, **tema scuro**, significati dei vocaboli in **italiano o inglese**.
- **Sincronizzazione** tra dispositivi tramite un Gist segreto di GitHub (Statistiche e Backup › ☁️): serve un token fine-grained con il solo permesso "Gists: Read and write", salvato solo sul dispositivo.

Per modificare i contenuti Tongji: cambia i file in `tongji_src/`, poi esegui `python build.py` dentro quella cartella (con `PYTHONIOENCODING=utf-8` su Windows). Se qualcosa non torna (frasi da riordinare che non ricompongono la frase, opzioni doppie, vocaboli ripetuti…) la build si ferma e indica l'errore.

## Come installarla sul telefono
1. Apri il link pubblico (GitHub Pages) da Chrome (Android) o Safari (iPhone).
2. **Android/Chrome**: tocca il banner "Installa app" oppure Menu (⋮) → "Installa app" / "Aggiungi a schermata Home".
3. **iPhone/Safari**: tocca il pulsante Condividi (□↑) → "Aggiungi a Home".
4. Da quel momento l'icona è sulla home del telefono e si apre a schermo intero, come un'app vera.

## Aggiornare l'app in futuro
Ogni volta che modifichi `index.html` (o gli altri file):
1. Incrementa `CACHE_NAME` in `sw.js` (es. `studio-cinese-v1` → `studio-cinese-v2`) — altrimenti i telefoni che l'hanno già installata continueranno a vedere la versione in cache.
2. Fai commit e push su GitHub — la pagina si aggiorna da sola in pochi minuti.
