const u="testuser";let c=Date.now();function s(){const e=window.scrollY,t=document.body.scrollHeight-window.innerHeight,n=t?e/t*100:0;return Math.min(100,Math.max(0,n))}function h(e){const t=new URL(e).hostname;return t.includes("youtube")||t.includes("netflix")?"entertainment":t.includes("linkedin")||t.includes("glassdoor")?"job search":t.includes("google")||t.includes("wikipedia")?"research":t.includes("instagram")||t.includes("twitter")?"social media":"other"}function f(){const e=s(),t=document.title,n=window.location.href,i=Date.now(),o=Math.round((i-c)/1e3),r=h(n),a=new Date().toISOString();o<3||(fetch("http://localhost:8000/track-event",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({user_id:u,tab_url:n,title:t,scroll_depth:e,duration_seconds:o,category:r,timestamp:a})}).catch(d=>console.error("Failed to send event:",d)),c=i)}function w(){let e=window.location.href,t=document.title,n=s();setInterval(()=>{const i=window.location.href,o=document.title,r=s();(i!==e||o!==t||Math.abs(r-n)>10)&&(f(),e=i,t=o,n=r)},1e4)}function l(e){fetch("http://localhost:8000/track-afk",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({state:e,timestamp:new Date().toISOString()})}).catch(t=>console.error("Failed to send AFK event:",t))}function m(){let e=Date.now();const t=3e5;let n=!1;function i(){e=Date.now()}["mousemove","keydown","mousedown","scroll"].forEach(o=>window.addEventListener(o,i)),setInterval(()=>{const o=Date.now()-e;!n&&o>t?(n=!0,l("start")):n&&o<=t&&(n=!1,l("end"))},1e4)}w();m();
