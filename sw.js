// Service Worker — Studio Cinese PWA
// Strategia: stale-while-revalidate (serve dalla cache se presente, aggiorna in background).
// Copre sia i file del sito sia gli script CDN esterni (Tailwind, HanziWriter), cosi' l'app
// funziona anche offline una volta aperta la prima volta.

const CACHE_NAME = 'studio-cinese-v5'; // aumentare (v2, v3, ...) ad ogni aggiornamento dei file

const APP_SHELL = [
  './',
  './index.html',
  './tongji_data.js',
  './tongji_en.js',
  './i18n_en.js',
  './app.css',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/apple-touch-icon.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(APP_SHELL))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request).then((cached) => {
      const networkFetch = fetch(event.request)
        .then((response) => {
          if (response && (response.ok || response.type === 'opaque')) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          }
          return response;
        })
        .catch(() => cached);
      return cached || networkFetch;
    })
  );
});
