const CACHE_NAME = 'cisa-cache-v4';
const urlsToCache = [
  '/',
  '/static/css/style.css', // Cambiado a style.css
];


// Instalar el Service Worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

// Escuchar peticiones: Estrategia Network-First (Red con fallback a caché)
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .catch(() => caches.match(event.request))
  );
});