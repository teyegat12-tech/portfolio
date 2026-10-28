const asset = name => `assets/${name}`;
const dialog = document.querySelector('#project-dialog');
let activeProject;
const escapeHTML = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const unit = n => `calc(${n} * var(--u))`;
const position = (el, x, y, w, h) => {
  Object.assign(el.style, {left:unit(x), top:unit(y)});
  if (w != null) el.style.width = unit(w);
  if (h != null) el.style.height = unit(h);
  return el;
};
function piece(className, x, y, content = '') {
  const el = document.createElement('div');
  el.className = `piece ${className}`;
  el.innerHTML = content;
  position(el,x,y);
  document.querySelector('#decor').append(el);
  return el;
}
function image(name,x,y,w,h,className='',matrix) {
  const el=document.createElement('img');
  el.src=asset(name); el.alt=''; el.className=className;
  position(el,x,y,w,h);
  if(matrix){el.style.transformOrigin='0 0';el.style.transform=`matrix(${matrix.join(',')},0,0)`;}
  document.querySelector('#decor').append(el);
  return el;
}
function buildDecor(){
  piece('glitch',2,-16,'<img src="assets/959-13-img1.webp" alt="">');
  const bottomGlitch=piece('glitch',2,6913,'<img src="assets/959-13-img1.webp" alt="">');
  bottomGlitch.dataset.bottom='447';
  const tape='<div>AI ПРОЕКТЫ <b>2006</b> #ВПРОЦЕССЕ STUDIO 12 <b class="arrow">↗</b> AI ПРОЕКТЫ <b>2006</b> #ВПРОЦЕССЕ STUDIO 12 <b class="arrow">↗</b></div>';
  piece('white-tape',36,438,tape);
  piece('white-tape',36,4523,tape);
  const crosses=(x,y,extra=false)=>piece('crosses',x,y,`<div class="acid-dot"></div>${extra?'<div class="acid-dot extra"></div>':''}<img class="cross-white" src="assets/946-4777-imgUnion.svg" alt=""><img class="cross-black" src="assets/946-4777-imgUnion1.svg" alt="">`);
  crosses(-6,1744);crosses(-6,5644,true);
  const daring='<span class="do">ДЕЛАЙ!</span><img class="finger-a" src="assets/946-4787-imgGroup.svg" alt=""><img class="finger-b" src="assets/946-4787-imgGroup1.svg" alt=""><span class="bold">СМЕЛЕЕ!</span>';
  piece('daring',-114,2025.347,daring);piece('daring',-114,6207.347,daring);
  const scribble=piece('scribble',125,3329);scribble.style.transform='rotate(90deg)';
  const footerScribble=piece('scribble',6,7224);footerScribble.dataset.bottom='136';
  image('946-4879-img.webp',3869,3569,2334,2157,'screen',[-1,0,0,-1]);
  const lower=image('946-4879-img.webp',2924,9019,2334,2157,'screen',[-1,0,0,-1]);lower.dataset.bottom='-1659';
  const chain=image('946-4875-img5.webp',662,7468.068,2189,294,'',[.8105375,-.5856867,.5856867,.8105375]);chain.dataset.bottom='-108.068';
  const signature=image('946-4888-imgGroup2131330333.svg',1472,6742.77,377.046,315.127);signature.dataset.bottom='617.23';
  const phrases=['STUDIO 12','↗','ИДЕИ В ДЕЛЕ','+','ДЕЛАЙ СМЕЛЕЕ','/','СМОТРИ ПОД ДРУГИМ УГЛОМ','↗','AI ПРОЕКТЫ','+','ПРОБУЙ. СОБИРАЙ. МЕНЯЙ.','/','ИЗ МЫСЛИ — В ФОРМУ','↗','РУЧНОЙ РЕЖИМ','+','ЗА ПРЕДЕЛАМИ РАБОТЫ','/','ЕЩЁ ОДНА ИДЕЯ','↗','НЕ ОТКЛАДЫВАЙ НА ПОТОМ','+','ПРОДОЛЖЕНИЕ СЛЕДУЕТ','/'];
  document.querySelectorAll('.right-edge>div').forEach((el,i)=>el.textContent=Array(12).fill([...phrases.slice(i*8),...phrases.slice(0,i*8)].join('   ')).join('   '));
}
function renderCatalog(groups){
  const tapeWidths=[1018,1183,1365,1228];
  const main=document.querySelector('main');
  groups.forEach((group,i)=>{
    const section=document.createElement('section');section.id=group.id;section.className='catalog-section';section.setAttribute('aria-labelledby',`${group.id}-title`);
    section.innerHTML=`<p class="kicker">${escapeHTML(group.kicker)}</p><h2 class="section-title" id="${group.id}-title"><span class="heading-tape" aria-hidden="true" style="--tape-width:${tapeWidths[i]||1228}"><img src="assets/946-4817-imgJhaTape041.webp" alt=""></span>${escapeHTML(group.title)}</h2><p class="section-description">${escapeHTML(group.description)}</p><div class="projects"></div>`;
    const grid=section.querySelector('.projects');
    group.projects.forEach(project=>{
      const card=document.createElement('article');card.className=`project${project.featured?' featured':''}`;card.id=`project-${project.id}`;
      card.innerHTML=`<p class="project-meta">№ ${escapeHTML(project.id)} / ${escapeHTML(project.status)}</p><h3>${escapeHTML(project.title)}</h3><p class="project-description">${escapeHTML(project.description)}</p>`;
      let action;
      if(!project.links.length){action=document.createElement('span');action.setAttribute('aria-disabled','true');}
      else if(project.links.length===1&&project.links[0].url&&!project.links[0].url.startsWith('http://localhost')){
        action=document.createElement('a');action.href=project.links[0].url;action.target='_blank';action.rel='noopener noreferrer';
      } else {action=document.createElement('button');action.type='button';action.addEventListener('click',()=>openProject(project));action.setAttribute('aria-haspopup','dialog');}
      action.className='project-action';action.textContent=project.action;card.append(action);grid.append(card);
    });
    main.append(section);
  });
}
function readFolder(){try{return localStorage.getItem('studio12-folder')||'';}catch{return '';}}
function writeFolder(value){try{localStorage.setItem('studio12-folder',value);}catch{}}
function renderResources(){
  const list=document.querySelector('#dialog-links');list.replaceChildren();
  activeProject.links.forEach(link=>{
    const local=Boolean(link.local);
    const el=document.createElement(local?'button':'a');el.className='resource';
    if(local){
      el.type='button';
      const folder=document.querySelector('#studio-folder').value.trim().replace(/\/$/,'');
      const absolute=link.local.startsWith('/')?link.local:folder?`${folder}/${link.local}`:link.local;
      el.innerHTML=`${escapeHTML(link.label)} <span aria-hidden="true">↗</span><small>${escapeHTML(absolute)}</small>`;
      el.addEventListener('click',async()=>{
        if(!folder&&!link.local.startsWith('/')){document.querySelector('#dialog-feedback').textContent='Сначала укажи папку Студии 12 ниже.';document.querySelector('#studio-folder').focus();return;}
        try{await navigator.clipboard.writeText(absolute);document.querySelector('#dialog-feedback').textContent='Путь скопирован. В Finder нажми ⌘⇧G и вставь его.';}catch{document.querySelector('#dialog-feedback').textContent=`Скопируй путь вручную: ${absolute}`;}
      });
    }else{
      el.href=link.url;el.target='_blank';el.rel='noopener noreferrer';el.textContent=`${link.label} ↗`;
      if(/^https?:\/\/(localhost|127\.0\.0\.1)/.test(link.url)){const hint=document.createElement('small');hint.textContent='Понадобится запущенный локальный сервер.';el.append(hint);}
    }
    list.append(el);
  });
}
function openProject(project){
  activeProject=project;document.querySelector('#dialog-title').textContent=project.title;document.querySelector('#dialog-feedback').textContent='';document.querySelector('#studio-folder').value=readFolder();document.querySelector('#disk-settings').hidden=!project.links.some(l=>l.local);renderResources();dialog.showModal();
}
document.querySelector('.close-dialog').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});
document.querySelector('#studio-folder').addEventListener('input',event=>{writeFolder(event.target.value);renderResources();});
function alignDecor(){
  const page=document.querySelector('.page');const scale=page.clientWidth/1920;const height=page.offsetHeight/scale;
  document.querySelectorAll('[data-bottom]').forEach(el=>el.style.top=unit(height-Number(el.dataset.bottom)));
  const cycles=Math.max(0,Math.ceil((height-7360)/4182));
  document.querySelectorAll('.continuation').forEach(el=>el.remove());
  const originals=[...document.querySelectorAll('.decor>.white-tape,.decor>.crosses,.decor>.daring,.decor>.scribble')].filter(el=>!el.dataset.bottom);
  for(let cycle=1;cycle<=cycles;cycle++){
    originals.filter(el=>parseFloat(el.style.top.match(/[-\d.]+/)[0])<4400).forEach(el=>{
      const y=parseFloat(el.style.top.match(/[-\d.]+/)[0])+4182*cycle;
      if(y<7360||y>height-600)return;
      const clone=el.cloneNode(true);clone.classList.add('continuation');clone.style.top=unit(y);document.querySelector('#decor').append(clone);
    });
  }
}
async function init(){
  try{
    const response=await fetch('projects.json');if(!response.ok)throw Error(response.status);
    const groups=await response.json();renderCatalog(groups);buildDecor();await document.fonts.ready;alignDecor();new ResizeObserver(alignDecor).observe(document.querySelector('.page'));
  }catch(error){const p=document.createElement('p');p.className='load-error';p.textContent='Каталог не загрузился. Обнови страницу, пожалуйста.';document.querySelector('main').append(p);console.error('Catalog:',error);}
}
init();
