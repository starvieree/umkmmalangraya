(function(){
var hd=document.getElementById('hd'),bg=document.getElementById('bg');
if(bg){
    bg.onclick=function(){var o=hd.classList.toggle('open');this.setAttribute('aria-expanded',o);this.setAttribute('aria-label',o?'Tutup menu':'Buka menu')};
}
var h=new Date().getHours();
document.querySelectorAll('[data-o]').forEach(function(e){var r=e.dataset.o.split('-'),open=h>=+r[0]&&h<+r[1];e.className='tag '+(open?'ok':'no');e.textContent=open?(e.dataset.l||'Buka'):'Tutup'});

function filterBlog(category) {
    document.querySelectorAll('.grid .card').forEach(function(c){
        var cat = c.querySelector('.tag.c').textContent;
        c.hidden = (category !== 'Semua' && cat !== category);
    });
}

document.querySelectorAll('.row .tag').forEach(function(t){
    t.onclick = function(){
        document.querySelectorAll('.row .tag').forEach(function(x){x.style.background='transparent';x.style.color='var(--text)';x.style.borderColor='var(--line)'});
        this.style.background='var(--p)';this.style.color='#fff';this.style.borderColor='var(--p)';
        filterBlog(this.textContent);
    }
});

// Set "Semua" as active by default
var semuaTag = document.querySelector('.row .tag');
if (semuaTag && semuaTag.textContent === 'Semua') {
    semuaTag.style.background='var(--p)';
    semuaTag.style.color='#fff';
    semuaTag.style.borderColor='var(--p)';
}

function filterCards(q, k, w) {
    var n=0;
    document.querySelectorAll('.grid .card[data-k]').forEach(function(c){
        var ok=(!k||c.dataset.k===k)&&(!w||c.dataset.w===w)&&(!q||c.dataset.t.indexOf(q.toLowerCase())>-1);
        c.hidden=!ok;
        if(ok)n++
    });
    var empty = document.getElementById('empty');
    if(empty) empty.hidden=n>0;
}

var f=document.querySelector('form.bar');
if(f){
    f.addEventListener('input', function(){
        filterCards(f.q.value, f.k.value, f.w.value);
    });
}
})();

window.addEventListener("scroll", () => {
  const topBtn = document.querySelector(".top");
  if (topBtn) {
    if (window.scrollY > 300) topBtn.classList.add("show");
    else topBtn.classList.remove("show");
  }
});
