chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.videoId) {
        let flaskUrl = `http://127.0.0.1:5000/video/${request.videoId}`;
        console.log("Opening Flask URL:", flaskUrl);
        chrome.tabs.create({ url: flaskUrl });
    }
});
