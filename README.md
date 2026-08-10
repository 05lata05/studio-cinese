# Studio Cinese — PWA

App per lo studio del cinese mandarino di Luigi Latagliata, installabile come vera app su smartphone (PWA).

## Struttura
- `index.html` — l'app (identica a `studio_cinese_v4_1.html`, con i tag PWA aggiunti)
- `manifest.json` — nome, icone, colori dell'app installata
- `sw.js` — service worker (funzionamento offline + aggiornamenti in background)
- `icons/` — icone dell'app in varie dimensioni

## Come installarla sul telefono
1. Apri il link pubblico (GitHub Pages) da Chrome (Android) o Safari (iPhone).
2. **Android/Chrome**: tocca il banner "Installa app" oppure Menu (⋮) → "Installa app" / "Aggiungi a schermata Home".
3. **iPhone/Safari**: tocca il pulsante Condividi (□↑) → "Aggiungi a Home".
4. Da quel momento l'icona è sulla home del telefono e si apre a schermo intero, come un'app vera.

## Aggiornare l'app in futuro
Ogni volta che modifichi `index.html` (o gli altri file):
1. Incrementa `CACHE_NAME` in `sw.js` (es. `studio-cinese-v1` → `studio-cinese-v2`) — altrimenti i telefoni che l'hanno già installata continueranno a vedere la versione in cache.
2. Fai commit e push su GitHub — la pagina si aggiorna da sola in pochi minuti.
