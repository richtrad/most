(() => {
  'use strict';
  const paths = new Set(__MOST_LARGE_FILES__);
  const rawBase = '__MOST_RAW_BASE__';
  const project = '/most/';

  function resolve(input, base = document.baseURI) {
    let url, path;
    try {
      url = new URL(input, base);
      path = decodeURIComponent(url.pathname);
    } catch { return null; }
    if (url.origin !== location.origin || !path.startsWith(project)) return null;
    if (!paths.has(path.slice(project.length))) return null;
    return rawBase + url.pathname.slice(project.length) + url.search + url.hash;
  }

  // The street viewers use both fetch (Three.js FileLoader) and XHR.
  const originalFetch = window.fetch.bind(window);
  window.fetch = function (input, init) {
    const requestInput = input instanceof Request;
    const target = resolve(requestInput ? input.url : input);
    const method = (init?.method || (requestInput ? input.method : 'GET')).toUpperCase();
    if (!target || !['GET', 'HEAD'].includes(method)) return originalFetch(input, init);
    const request = new Request(input, init);
    const headers = new Headers();
    for (const name of ['accept', 'range', 'if-none-match', 'if-modified-since']) {
      if (request.headers.has(name)) headers.set(name, request.headers.get(name));
    }
    return originalFetch(target, {method, headers, signal: request.signal,
      credentials: 'omit', mode: 'cors', cache: request.cache});
  };
  const open = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function (method, url, ...rest) {
    const target = /^(get|head)$/i.test(method) && resolve(url);
    return open.call(this, method, target || url, ...rest);
  };

  function fixLink(anchor) {
    if (!anchor?.matches('a[href]')) return;
    const target = resolve(anchor.href);
    if (target) anchor.href = target;
  }
  for (const event of ['pointerdown', 'click', 'contextmenu', 'focusin']) {
    document.addEventListener(event, e => fixLink(e.target.closest?.('a[href]')), true);
  }
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href]').forEach(fixLink);
  });
  if (document.documentElement.hasAttribute('data-most-asset-route')) {
    const target = resolve(location.href);
    if (target) {
      document.addEventListener('DOMContentLoaded', () => {
        const link = document.getElementById('asset');
        if (link) link.href = target;
      });
      location.replace(target);
    }
  }
})();