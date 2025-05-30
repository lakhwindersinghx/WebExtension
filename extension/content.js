let startTime = Date.now();

function getScrollDepth() {
  const scrolled = window.scrollY;
  const totalHeight = document.body.scrollHeight - window.innerHeight;
  const percentage= totalHeight ? (scrolled / totalHeight) * 100 : 0;
  return Math.min(100,Math.max(0, percentage));
  
}

function getCategoryFromURL(url) {
  const domain = new URL(url).hostname;
  if (domain.includes("youtube") || domain.includes("netflix")) return "entertainment";
  if (domain.includes("linkedin") || domain.includes("glassdoor")) return "job search";
  if (domain.includes("google") || domain.includes("wikipedia")) return "research";
  if (domain.includes("instagram") || domain.includes("twitter")) return "social media";
  return "other";
}


function sendEventData() {
  const scrollDepth = getScrollDepth();
  const title = document.title;
  const tabUrl = window.location.href;
  const now = Date.now();
  const duration_seconds = Math.round((now - startTime) / 1000);
  const category = getCategoryFromURL(tabUrl);
  const timestamp = new Date().toISOString(); // or leave out and let backend assign

  if (duration_seconds < 3) return; // Skip short visits

  fetch("http://localhost:8000/track-event", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      tab_url: tabUrl,
      title,
      scroll_depth: scrollDepth,
      duration_seconds,
      category,
      timestamp
    })
  }).catch((err) => console.error("Failed to send event:", err));

  startTime = now; // reset timer
}

// Send every 30 seconds
setInterval(sendEventData, 10000);

// Optional: send immediately when loaded
sendEventData();
