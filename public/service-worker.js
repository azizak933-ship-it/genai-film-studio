const CACHE_NAME = 'genai-film-v5';
const STATIC_ASSETS = ['/manifest.json'];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(c => c.addAll(STATIC_ASSETS))
  );
  // Take control immediately — don't wait for old SW to die
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    // Delete ALL old caches
    caches.keys().then(keys =>
      Promise.all(keys.map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);

  // ALWAYS network-first for HTML — never serve stale pages
  if (e.request.mode === 'navigate' || url.pathname === '/' || url.pathname.endsWith('.html')) {
    e.respondWith(
      fetch(e.request).catch(() =>
        caches.match('/').then(cached => cached ||
          new Response('<h1>Offline</h1>', { headers: { 'Content-Type': 'text/html' } })
        )
      )
    );
    return;
  }

  // Network-first for all API calls
  if (url.pathname.startsWith('/api/')) {
    e.respondWith(
      fetch(e.request).catch(() =>
        new Response(JSON.stringify({ error: 'offline', offline: true }), {
          status: 503,
          headers: { 'Content-Type': 'application/json' }
        })
      )
    );
    return;
  }

  // Cache-first for static assets (icons, manifest)
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(resp => {
        if (resp && resp.status === 200 && e.request.method === 'GET') {
          const clone = resp.clone();
          caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
        }
        return resp;
      });
    })
  );
});
