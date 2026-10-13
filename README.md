# Studio Cinese — PWA

App per lo studio del cinese mandarino di Luigi Latagliata, installabile come vera app su smartphone (PWA).

## Struttura
- `index.html` — l'app (identica a `studio_cinese_v4_1.html`, con i tag PWA aggiunti)
- `tongji_data.js` — contenuti del corso Tongji (初级汉语口语 1), **generato**: non modificarlo a mano
- `tongji_en.js` — traduzione inglese dei contenuti Tongji, **generato** da `build.py` a partire da `tongji_src/en_*.tsv`
- `i18n_en.js` — testi dell'interfaccia in inglese (italiano → inglese), usati quando la lingua è English
- `tongji_src/` — sorgenti dei contenuti Tongji: `lessons_a.py` (lezioni 1-7), `lessons_b.py` (8-13), `lessons_c.py` (14-19), `lessons_d.py` (20-25), `extra_quiz.py` (esercizi aggiuntivi per lezione), `common.py` (personaggi, categorie, classificatori) e `build.py` (controlla e genera `tongji_data.js`)
- `app.css` — stili Tailwind già compilati, **generato**: si rigenera con `python tools/build_css.py` (poi apri l'indirizzo che stampa) quando in `index.html` si usano classi nuove
- `tools/` — `build_css.py` e `gen_css.html`, che generano `app.css`; `check_i18n.py`, che controlla che ogni testo dell'interfaccia abbia la traduzione inglese
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
- **Meno domande ripetute**: l'app ricorda in quale quiz è uscita ogni domanda e nei quiz successivi propone prima quelle mai viste o viste da più tempo (sincronizzato tra i dispositivi).
- **Esercizi generati per ogni lezione Tongji**, oltre a quelli scritti a mano: significato delle frasi di dialoghi e grammatica (cinese ⇄ traduzione) e caratteri mancanti nelle parole.
- **Dettato (听写)** nel Laboratorio Tratti: a mano (controllo dei tratti, serve la connessione la prima volta) o con la tastiera cinese.
- **AI Tutor collegato al corso**: frasi ed "esercizi su misura" con il solo vocabolario studiato.
- **Progressi per lezione** e punti deboli (corso Tongji), **ricerca nella grammatica**, **tema scuro**.
- **App in italiano o in inglese** (scelta nella schermata di accesso o con il pulsante IT/EN in alto; al primo avvio segue la lingua del browser): in inglese sono tradotti interfaccia, significati dei vocaboli, spiegazioni, esercizi e tutti i contenuti del corso Tongji, quindi l'app è usabile anche da chi non parla italiano.
- **Sincronizzazione** tra dispositivi tramite un Gist segreto di GitHub (Statistiche e Backup › ☁️): serve un token fine-grained con il solo permesso "Gists: Read and write", salvato solo sul dispositivo.

Per modificare i contenuti Tongji: cambia i file in `tongji_src/`, poi esegui `python build.py` dentro quella cartella (con `PYTHONIOENCODING=utf-8` su Windows). Se qualcosa non torna (frasi da riordinare che non ricompongono la frase, opzioni doppie, vocaboli ripetuti…) la build si ferma e indica l'errore.

Traduzione inglese: ogni testo italiano del corso ha una riga `codice<TAB>traduzione` in `tongji_src/en_*.tsv` (il codice sono i primi 8 caratteri dello SHA-1 del testo italiano). Se aggiungi o cambi un testo, la build si ferma e scrive in `tongji_src/en_todo.tsv` le righe da tradurre: completa la traduzione, spostala in uno dei file `en_*.tsv` e rilancia la build (controlla anche che i caratteri cinesi nella traduzione siano gli stessi dell'originale). I testi dell'interfaccia stanno in `i18n_en.js`: ogni testo passato a `t('…')` in `index.html` deve avere lì la sua traduzione, con gli stessi segnaposto (`{n}`, `{name}`…); `python tools/check_i18n.py` segnala quelli mancanti.

## Come installarla sul telefono
1. Apri il link pubblico (GitHub Pages) da Chrome (Android) o Safari (iPhone).
2. **Android/Chrome**: tocca il banner "Installa app" oppure Menu (⋮) → "Installa app" / "Aggiungi a schermata Home".
3. **iPhone/Safari**: tocca il pulsante Condividi (□↑) → "Aggiungi a Home".
4. Da quel momento l'icona è sulla home del telefono e si apre a schermo intero, come un'app vera.

## Aggiornare l'app in futuro
Ogni volta che modifichi `index.html` (o gli altri file):
1. Incrementa `CACHE_NAME` in `sw.js` (es. `studio-cinese-v1` → `studio-cinese-v2`) — altrimenti i telefoni che l'hanno già installata continueranno a vedere la versione in cache.
2. Fai commit e push su GitHub — la pagina si aggiorna da sola in pochi minuti.
