const BACKEND_URL = "http://127.0.0.1:9999/api";
let currentArticles = [];

async function fetchLatestNews() {
    try {
        const response = await fetch(`${BACKEND_URL}/live-feed`);
        currentArticles = await response.json(); 
        const liveNews = currentArticles.slice(0, 6);
        const gridContainer = document.getElementById("news-grid");
        if (!gridContainer) return;

        gridContainer.innerHTML = ""; 
        liveNews.forEach((news, index) => {
            const card = document.createElement("div");
            card.className = "bg-[#131a2a] p-4 rounded-xl border border-gray-800 flex flex-col justify-between h-40 cursor-pointer hover:border-gray-700 transition duration-200";
            card.innerHTML = `
                <div onclick="openNewsInScanner(${index})">
                  <h3 class="font-medium text-sm line-clamp-2 text-white">${news.title}</h3>
                  <p class="text-xs text-gray-400 mt-1 line-clamp-2">${news.content}</p>
                </div>
                <div class="flex justify-between text-xs font-semibold mt-4">
                  <span class="text-gray-500">Accuracy: ${news.accuracy}%</span>
                  <button onclick="event.stopPropagation(); openNewsInScanner(${index})" class="text-green-400 hover:underline cursor-pointer">Verify News</button>
                </div>
            `;
            gridContainer.appendChild(card);
        });
    } catch (err) {
        console.error("Error:", err);
    }
}

function openNewsInScanner(index) {
    const news = currentArticles[index];
    if (!news) return;
    const manualInput = document.getElementById("manual-input");
    if (manualInput) {
        manualInput.value = news.content;
        handleVerifyNews();
    }
}

async function handleVerifyNews() {
    const manualInput = document.getElementById("manual-input").value.trim();
    if (!manualInput) return alert("Please enter text first!");

    const resultArea = document.getElementById("result-area");
    if (resultArea) resultArea.innerHTML = `<p class="text-gray-400 text-sm mt-4 animate-pulse">🔄 Neural cross-checking...</p>`;

    try {
        const response = await fetch(`${BACKEND_URL}/verify-news`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: manualInput })
        });
        const result = await response.json();
        let color = result.score >= 75 ? "text-green-400" : result.score >= 40 ? "text-yellow-400" : "text-red-400";
        
        resultArea.innerHTML = `
          <div class="p-6 bg-[#131a2a] rounded-xl border border-gray-800 space-y-3 mt-6">
            <div class="flex justify-between items-center">
              <h3 class="text-xl font-bold ${color}">${result.status}</h3>
              <span class="bg-[#0b0f19] px-3 py-1 rounded-full border border-gray-700 text-sm font-semibold text-white">Truth Score: ${result.score}%</span>
            </div>
            <p class="text-gray-300 font-medium">${result.description}</p>
            <div class="bg-[#0b0f19] p-4 rounded-lg border border-gray-800 text-sm text-gray-400 space-y-2">
              <p>📍 ${result.explanation_1}</p>
              <p>📍 ${result.explanation_2}</p>
            </div>
          </div>`;
    } catch (err) {
        if (resultArea) resultArea.innerHTML = `<p class="text-red-400 text-sm mt-4">❌ Server unreachable.</p>`;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    fetchLatestNews();
    setInterval(fetchLatestNews, 5000);
});