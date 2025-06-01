export function startAFKWatcher(sendAFKEvent) {
  let lastActivity = Date.now();
  const AFK_THRESHOLD = 300_000; // 5 min
  let isAFK = false;

  function resetTimer() {
    lastActivity = Date.now();
  }

  ["mousemove", "keydown", "mousedown", "scroll"].forEach(evt =>
    window.addEventListener(evt, resetTimer)
  );

  setInterval(() => {
    const idle = Date.now() - lastActivity;
    if (!isAFK && idle > AFK_THRESHOLD) {
      isAFK = true;
      sendAFKEvent("start");
    } else if (isAFK && idle <= AFK_THRESHOLD) {
      isAFK = false;
      sendAFKEvent("end");
    }
  }, 10000);
}
