// Reusable registered-image comparison: original files, no grayscale substitute.
for (const el of document.querySelectorAll('[data-image-compare]')) {
 const before=el.dataset.before,after=el.dataset.after;
 const left=el.dataset.left||'PŘED',right=el.dataset.right||'PO';
 el.innerHTML=`<div class="compare-stage" style="aspect-ratio:${el.dataset.ratio||'1.41'}"><img class="compare-original" src="${before}" alt="${left}"><img class="compare-result" src="${after}" alt="${right}"><span class="compare-label left">${left}</span><span class="compare-label right">${right}</span><span class="compare-divider" aria-hidden="true">↔</span></div><label class="compare-control">Posuňte hranici <input type="range" min="0" max="100" value="50" aria-label="${el.dataset.label||'Porovnání původní a kolorované fotografie'}"></label>`;
 const stage=el.querySelector('.compare-stage'),slider=el.querySelector('input');
 const update=v=>{slider.value=v;stage.style.setProperty('--split',v+'%')};slider.oninput=()=>update(slider.value);
 const move=e=>{const r=stage.getBoundingClientRect();update(Math.min(100,Math.max(0,100*(e.clientX-r.left)/r.width)))};
 stage.onpointerdown=e=>{stage.setPointerCapture(e.pointerId);move(e)};stage.onpointermove=e=>{if(stage.hasPointerCapture(e.pointerId))move(e)};
 stage.onpointerup=e=>{if(stage.hasPointerCapture(e.pointerId))stage.releasePointerCapture(e.pointerId)};
}
