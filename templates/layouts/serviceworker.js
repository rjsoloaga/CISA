const CACHE_NAME = 'cisa-cache-v1';
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

// Escuchar peticiones para servir desde caché si no hay internet
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});