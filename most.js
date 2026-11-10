document.querySelectorAll('[data-stage]').forEach(button=>button.addEventListener('click',()=>{
 const image=document.getElementById('stage-image');
 image.src=button.dataset.stage; image.alt=button.textContent;
 document.querySelectorAll('[data-stage]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
}));
document.getElementById('repeat')?.addEventListener('click',event=>{
 const active=event.currentTarget.getAttribute('aria-pressed')!=='true';
 event.currentTarget.setAttribute('aria-pressed',String(active));
 document.querySelector('.roof-grid').classList.toggle('repeated',active);
});
