(() => {
  'use strict';
  const paths = new Set(["3d-modely/galerie/1045.glb", "3d-modely/galerie/262.glb", "3d-modely/galerie/57-normal.glb", "3d-modely/galerie/57.glb", "3d-modely/galerie/cechova.glb", "3d-modely/galerie/kulova.glb", "3d-modely/galerie/mirove-v2.glb", "3d-modely/galerie/mirove-v3.glb", "3d-modely/galerie/mirove.glb", "domy/174/cp_174.blend", "domy/174/cp_174.glb", "domy/174/previous.glb", "domy/35/cp_35.blend", "domy/35/cp_35.glb", "domy/40/cp_40-r16.glb", "domy/40/cp_40-r19.blend", "domy/40/cp_40-r19.glb", "domy/40/cp_40.blend", "domy/40/cp_40.glb", "kulova-257/models/cp257_SOL61.blend", "kulova-257/models/cp257_SOL61.glb", "kulova-259/models/cp259_SOL61.blend", "kulova-259/models/cp259_SOL61.glb", "kulova-259/models/cp259_SOL61_HD_v2.blend", "kulova-259/models/cp259_SOL61_HD_v2.glb", "kulova-261/kulova-261-models-v10.zip", "kulova-261/kulova-261-models-v8.zip", "kulova-261/kulova-261-models-v9.zip", "kulova-261/kulova-261-models.zip", "kulova-261/models/cp261_before.glb", "kulova-261/models/cp261_bevel_a.blend", "kulova-261/models/cp261_bevel_a.glb", "kulova-261/models/cp261_bevel_b.blend", "kulova-261/models/cp261_bevel_b.glb", "kulova-261/models/cp261_bevel_c.blend", "kulova-261/models/cp261_bevel_c.glb", "kulova-261/models/cp261_openings_geometry.blend", "kulova-261/models/cp261_openings_geometry.glb", "kulova-261/models/cp261_openings_inpaint.blend", "kulova-261/models/cp261_openings_inpaint.glb", "kulova-261/models/cp261_v10.blend", "kulova-261/models/cp261_v10.glb", "kulova-261/models/cp261_v7.blend", "kulova-261/models/cp261_v7.glb", "kulova-261/models/cp261_v7_lod1.glb", "kulova-261/models/cp261_v8.blend", "kulova-261/models/cp261_v8.glb", "kulova-261/models/cp261_v9.blend", "kulova-261/models/cp261_v9.glb", "kulova-263/models/cp263_G.blend", "kulova-263/models/cp263_G.glb", "kulova-263/models/cp263_initial_qa_failed.glb", "kulova/models/textured/cp262_study.glb", "mirove-namesti-v4/assets/fbdf21b6daf8b2e7_cp_57_detail.glb", "mirove-namesti-v4/scene-00.bin", "mirove-namesti-v4/scene-01.bin", "mirove-namesti-v4/scene-02.bin", "mirove-namesti-v4/scene-03.bin", "mirove-namesti-v4/scene-04.bin", "mirove-namesti-v4/scene.gltf", "street-evidence-20261104/models/6f89f1975b4b29b26895c5d9.glb", "zatecka/models/zatecka_street.blend"]);
  const rawBase = 'https://raw.githubusercontent.com/richtrad/most/cb4e8121ce14cbed30c84be415e584595e1587ad/';
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