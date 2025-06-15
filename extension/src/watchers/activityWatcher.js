const user_id = "testuser";

let startTime = Date.now();

function getScrollDepth() {
  const scrolled = window.scrollY;
  const totalHeight = document.body.scrollHeight - window.innerHeight;
  const percentage = totalHeight ? (scrolled / totalHeight) * 100 : 0;
  return Math.min(100, Math.max(0, percentage)); // Clamp between 0–100
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
  const timestamp = new Date().toISOString();

  if (duration_seconds < 3) return; // Skip short sessions

  fetch("http://localhost:8000/track-event", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id,
      tab_url: tabUrl,
      title,
      scroll_depth: scrollDepth,
      duration_seconds,
      category,
      timestamp
    })
  }).catch((err) => console.error("Failed to send event:", err));

  startTime = now; // Reset
}

export function startWebsiteTracking() {
  let previousUrl = window.location.href;
  let previousTitle = document.title;
  let previousScroll = getScrollDepth();

  setInterval(() => {
    const currentUrl = window.location.href;
    const currentTitle = document.title;
    const currentScroll = getScrollDepth();

    if (
      currentUrl !== previousUrl ||
      currentTitle !== previousTitle ||
      Math.abs(currentScroll - previousScroll) > 10
    ) {
      sendEventData();
      previousUrl = currentUrl;
      previousTitle = currentTitle;
      previousScroll = currentScroll;
    }
  }, 10000);
}

