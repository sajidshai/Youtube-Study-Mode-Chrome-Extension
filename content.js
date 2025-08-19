console.log("✅ Content script loaded on YouTube!"); // Debug log

function detectVideoId() {
    let url = new URL(window.location.href);
    let videoId = url.searchParams.get("v");

    if (videoId) {
        console.log("🎯 Detected Video ID:", videoId);
        chrome.runtime.sendMessage({ videoId: videoId });
    }
}

// Detect when navigation changes (SPA Fix)
window.addEventListener("yt-navigate-finish", detectVideoId);

// Run detection immediately in case already on a video page
detectVideoId();
