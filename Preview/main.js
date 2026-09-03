const c=document.getElementById('c'), ctx=c.getContext('2d');
let W=1280,H=720; function resize(){ const r=document.getElementById('stage').getBoundingClientRect(); const dpr=window.devicePixelRatio||1; W=c.width=Math.floor(r.width*dpr); H=c.height=Math.floor(r.height*dpr); c.style.width=r.width+'px'; c.style.height=r.height+'px'; ctx.setTransform(dpr,0,0,dpr,0,0); }
window.addEventListener('resize',resize); resize();

let anchors=[], cracks=[], dragged=false, dragStart=null, dragEnd=null, stability=1.0, lastPos=null, threads=[];
let photoMode=false;

// helpers
function lerp(a,b,t){return a+(b-a)*t}
function dist(a,b){ return Math.hypot(a.x-b.x,a.y-b.y)}
function rand(min,max){return Math.random()*(max-min)+min}

function addCrack(a,b){
  const segs=12; let pts=[a]; for(let i=1;i<segs;i++){ const t=i/segs; const x=lerp(a.x,b.x,t)+rand(-14,14); const y=lerp(a.y,b.y,t)+rand(-14,14); pts.push({x,y}); } pts.push(b); cracks.push({pts, life:1.0, blend: Math.random()});
  // spawn threads
  for(let i=0;i<3;i++) threads.push({x:b.x+rand(-20,20), y:b.y+rand(-20,20), vx:rand(-0.5,0.5), vy:rand(-0.8,-0.2), life:1});
}

function setStability(){
  // S = 1 - drag/2500*0.4 - angle/90*0.3 + anchors*0.12
  let drag = dragStart&&dragEnd ? dist(dragStart,dragEnd) : 0;
  let angleErr = 0; // simplified: deviation from straight
  if(cracks.length>1){ angleErr = Math.random()*20; }
  let s = 1 - drag/2500*0.4 - angleErr/90*0.3 + anchors.length*0.12;
  s = Math.max(0, Math.min(1.2, s));
  stability = s;
  document.getElementById('stability').textContent = Math.round(s*100)+'%';
  const ring=document.getElementById('ringPath');
  const prog = Math.min(100, s*100);
  ring.style.strokeDasharray = `${prog} 100`;
  ring.style.stroke = s>0.85 ? '#1BFF8A' : s>0.5 ? '#FFD23F' : '#FF4D00';
  const pips=document.querySelectorAll('.pip');
  pips.forEach((p,i)=> p.classList.toggle('on', i < anchors.length));
}

c.addEventListener('pointerdown',e=>{
  const rect=c.getBoundingClientRect(); const x=(e.clientX-rect.left), y=(e.clientY-rect.top);
  dragged=true; dragStart={x,y}; dragEnd={x,y}; lastPos={x,y};
  c.setPointerCapture(e.pointerId);
});
c.addEventListener('pointermove',e=>{
  if(!dragged) return;
  const rect=c.getBoundingClientRect(); const x=(e.clientX-rect.left), y=(e.clientY-rect.top);
  if(lastPos && dist(lastPos,{x,y})>8){ addCrack(lastPos,{x,y}); lastPos={x,y}; dragEnd={x,y}; setStability(); }
});
c.addEventListener('pointerup',e=>{
  if(!dragged) return;
  dragged=false;
  const rect=c.getBoundingClientRect(); const x=(e.clientX-rect.left), y=(e.clientY-rect.top);
  dragEnd={x,y};
  addCrack(dragStart,dragEnd);
  setStability();
  log(`Weave: drag ${Math.round(dist(dragStart,dragEnd))}px → stability ${Math.round(stability*100)}%`);
});
c.addEventListener('contextmenu',e=> e.preventDefault());
c.addEventListener('mousedown',e=>{
  if(e.button===2){
    const rect=c.getBoundingClientRect(); const x=(e.clientX-rect.left), y=(e.clientY-rect.top);
    anchors.push({x,y, t:performance.now()});
    setStability();
    log(`Anchor #${anchors.length} at ${Math.round(x)},${Math.round(y)} — +0.12 stability`);
    // spark
    for(let i=0;i<12;i++) threads.push({x,y, vx:rand(-2,2), vy:rand(-3,-0.5), life:1, color:'#FFD23F'});
    e.preventDefault();
  }
});

function log(msg){
  const el=document.getElementById('log');
  el.textContent = `[${new Date().toLocaleTimeString()}] ${msg}\n` + el.textContent.slice(0,1200);
}

document.getElementById('photoBtn').onclick=()=>{
  photoMode=!photoMode;
  const f=document.getElementById('photoFlash');
  f.style.opacity='0.85'; setTimeout(()=> f.style.opacity='0', 180);
  // confetti
  for(let i=0;i<40;i++) threads.push({x:W/2+rand(-200,200), y:H/2+rand(-100,100), vx:rand(-3,3), vy:rand(-4,-1), life:1, color: ['#FF4D00','#00E5FF','#1BFF8A'][i%3]});
  log(photoMode?'Photo Mode ON — 织裂快门':'Photo Mode OFF');
};
document.getElementById('resetBtn').onclick=()=>{ cracks=[]; anchors=[]; threads=[]; dragStart=null; dragEnd=null; stability=1; setStability(); log('重置 — 尝试把橙色熔岩拖进蓝色雪地，看温泉束'); };
window.addEventListener('keydown',e=>{
  if(e.key.toLowerCase()==='p') document.getElementById('photoBtn').click();
  if(e.key==='r') document.getElementById('resetBtn').click();
});

// long-press for anchor on touch
let pressTimer=null;
c.addEventListener('pointerdown',e=>{ if(e.button!==0) return; const rect=c.getBoundingClientRect(); const sx=(e.clientX-rect.left), sy=(e.clientY-rect.top); pressTimer=setTimeout(()=>{ anchors.push({x:sx,y:sy, t:performance.now()}); setStability(); log(`Anchor (long-press) #${anchors.length}`); }, 600); });
c.addEventListener('pointerup',()=> clearTimeout(pressTimer));
c.addEventListener('pointermove',()=> clearTimeout(pressTimer));

function drawBackground(){
  const g=ctx.createLinearGradient(0,0,W,0);
  g.addColorStop(0,'#1a0a08'); g.addColorStop(0.33,'#0a1a1e'); g.addColorStop(0.66,'#0a1a0f'); g.addColorStop(1,'#141008');
  ctx.fillStyle=g; ctx.fillRect(0,0,W,H);
  // light probes (Lumen)
  function probe(x,y,color){ const rg=ctx.createRadialGradient(x,y,0,x,y,220); rg.addColorStop(0,color+'55'); rg.addColorStop(1,'transparent'); ctx.fillStyle=rg; ctx.fillRect(x-220,y-220,440,440); }
  probe(W*0.22,H*0.5,'#FF4D00'); probe(W*0.55,H*0.45,'#00E5FF'); probe(W*0.83,H*0.55,'#1BFF8A');
  // horizon
  ctx.fillStyle='rgba(255,255,255,0.04)'; ctx.fillRect(0,H*0.68,W,2);
}
function draw(){
  drawBackground();
  // cracks (Nanite fiber)
  cracks.forEach(cr=>{
    ctx.save();
    ctx.lineCap='round'; ctx.lineJoin='round';
    // outer glow
    ctx.strokeStyle='rgba(255,210,63,0.25)'; ctx.lineWidth=10; ctx.beginPath(); ctx.moveTo(cr.pts[0].x, cr.pts[0].y); cr.pts.slice(1).forEach(p=> ctx.lineTo(p.x,p.y)); ctx.stroke();
    // core fiber
    ctx.strokeStyle= cr.blend<0.33? '#FF4D00' : cr.blend<0.66 ? '#00E5FF' : '#1BFF8A'; ctx.lineWidth=2.2; ctx.beginPath(); ctx.moveTo(cr.pts[0].x, cr.pts[0].y); cr.pts.slice(1).forEach(p=> ctx.lineTo(p.x,p.y)); ctx.stroke();
    // inner light
    ctx.strokeStyle='rgba(255,255,255,0.9)'; ctx.lineWidth=0.8; ctx.beginPath(); ctx.moveTo(cr.pts[0].x, cr.pts[0].y); cr.pts.slice(1).forEach(p=> ctx.lineTo(p.x,p.y)); ctx.stroke();
    ctx.restore();
    cr.life-=0.0006; if(cr.life<0) cr.life=0;
  });
  // anchors
  anchors.forEach((a,i)=>{
    const pulse = Math.sin(performance.now()*0.004 + i)*6;
    ctx.beginPath(); ctx.arc(a.x, a.y, 14+pulse*0.3, 0, Math.PI*2); ctx.fillStyle='rgba(255,210,63,0.15)'; ctx.fill();
    ctx.beginPath(); ctx.arc(a.x, a.y, 10, 0, Math.PI*2); ctx.strokeStyle='#FFD23F'; ctx.lineWidth=2; ctx.stroke();
    ctx.beginPath(); ctx.arc(a.x, a.y, 4, 0, Math.PI*2); ctx.fillStyle='#fff'; ctx.fill();
    ctx.fillStyle='#fff'; ctx.font='11px monospace'; ctx.fillText(i+1, a.x+14, a.y-12);
  });
  // drag preview
  if(dragged && dragStart && lastPos){
    ctx.setLineDash([8,8]); ctx.strokeStyle='rgba(255,255,255,0.6)'; ctx.lineWidth=1.2; ctx.beginPath(); ctx.moveTo(dragStart.x,dragStart.y); ctx.lineTo(lastPos.x,lastPos.y); ctx.stroke(); ctx.setLineDash([]);
    ctx.fillStyle='#fff'; ctx.beginPath(); ctx.arc(dragStart.x,dragStart.y,3,0,Math.PI*2); ctx.fill(); ctx.beginPath(); ctx.arc(lastPos.x,lastPos.y,4,0,Math.PI*2); ctx.fill();
  }
  // threads / sparks (Chaos)
  threads.forEach(p=>{
    ctx.globalAlpha = p.life;
    ctx.fillStyle = p.color || 'rgba(255,255,255,0.9)';
    ctx.beginPath(); ctx.arc(p.x,p.y, p.color? 3 : 1.8,0,Math.PI*2); ctx.fill();
    ctx.globalAlpha=1;
    p.x+=p.vx; p.y+=p.vy; p.vy+=0.06; p.life-=0.012;
  });
  threads = threads.filter(p=> p.life>0);
  // seam emissive when stable
  if(stability>0.85 && anchors.length>=2){
    ctx.save(); ctx.globalAlpha=0.08; ctx.fillStyle='#1BFF8A'; ctx.fillRect(0,0,W,H); ctx.restore();
    ctx.fillStyle='rgba(27,255,138,0.9)'; ctx.font='14px monospace'; ctx.fillText('✓ 发光缝 — S>0.85 已稳定', W*0.5-80, 28);
  }
  requestAnimationFrame(draw);
}
draw();
setStability();
log('就绪 — 拖拽撕裂，右键锚定，P拍照。把橙色拖进蓝色触发温泉。');
