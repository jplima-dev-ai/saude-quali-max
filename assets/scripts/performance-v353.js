(()=>{"use strict";
const KEY="qualimax-performance-v353",root=location.pathname.includes("/products/")?"../":"./";
const connection=navigator.connection||navigator.mozConnection||navigator.webkitConnection;
const automatic=()=>Boolean(connection?.saveData||["slow-2g","2g"].includes(connection?.effectiveType)||(navigator.deviceMemory&&navigator.deviceMemory<=2));
const preference=()=>{try{return localStorage.getItem(KEY)||"auto"}catch{return"auto"}};
const enabled=()=>preference()==="on"||(preference()==="auto"&&automatic());
const apply=()=>{const lite=enabled();document.documentElement.dataset.performanceMode=lite?"lite":"full";document.documentElement.classList.toggle("modo-leve",lite);if(lite)document.documentElement.dataset.motionLevel="off";return lite};
apply();
document.addEventListener("DOMContentLoaded",()=>{
  const lite=apply(),images=[...document.images];
  images.forEach((img,index)=>{
    img.decoding="async";
    if(index>1&&!img.hasAttribute("fetchpriority"))img.loading="lazy";
    if(!lite)return;
    const src=img.getAttribute("src")||"";
    const file=src.split("/").pop()||"";
    const isFullImage=/(?:^|\/)assets\/images\/[^/]+\.webp$/i.test(src)&&!src.includes("/thumbs/");
    if(isFullImage&&!/logo|hero|avatar|max/i.test(file)){
      img.removeAttribute("srcset");
      img.removeAttribute("sizes");
      img.src=root+"assets/images/thumbs/"+file;
    }
  });
  if(lite){const note=document.createElement("p");note.className="performance-notice";note.setAttribute("role","status");note.textContent="Modo leve ativado para economizar dados e deixar a navegação mais rápida.";document.querySelector("main")?.before(note)}
});
connection?.addEventListener?.("change",apply);
})();
