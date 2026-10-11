(function(){
var hd=document.getElementById('hd'),bg=document.getElementById('bg');
bg.onclick=function(){var o=hd.classList.toggle('open');this.setAttribute('aria-expanded',o);this.setAttribute('aria-label',o?'Tutup menu':'Buka menu')};
var h=new Date().getHours();
document.querySelectorAll('[data-o]').forEach(function(e){var r=e.dataset.o.split('-'),open=h>=+r[0]&&h<+r[1];e.className='tag '+(open?'ok':'no');e.textContent=open?(e.dataset.l||'Buka'):'Tutup'});
var f=document.querySelector('form.bar');
if(f){var p=new URLSearchParams(location.search),q=p.get('q')||'',k=p.get('k')||'',w=p.get('w')||'';
f.q.value=q;f.k.value=k;f.w.value=w;var n=0;
document.querySelectorAll('.grid .card[data-k]').forEach(function(c){var ok=(!k||c.dataset.k===k)&&(!w||c.dataset.w===w)&&(!q||c.dataset.t.indexOf(q.toLowerCase())>-1);c.hidden=!ok;if(ok)n++});
document.getElementById('empty').hidden=n>0}
})();
