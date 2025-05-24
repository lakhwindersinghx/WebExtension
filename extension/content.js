function getScrollDepth() {
  const scrolled = window.scrollY;
  const totalHeight = document.body.scrollHeight - window.innerHeight;
  return totalHeight ? (scrolled / totalHeight) * 100 : 0;
}

function sendEventData() {
  const scrollDepth = getScrollDepth();
  const title = document.title;
  const tabUrl = window.location.href;

  fetch("http://localhost:8000/track-event", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ tab_url: tabUrl, title, scroll_depth: scrollDepth })
  }).catch((err) => console.error("Failed to send event:", err));
}

// Send every 30 seconds
setInterval(sendEventData, 30000);

// Optional: send immediately when loaded
sendEventData();
