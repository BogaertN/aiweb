// field_overlay_renderer.js

const canvas = document.getElementById("fieldCanvas");
const ctx = canvas.getContext("2d");

canvas.width = 600;
canvas.height = 200;

function fetchFieldDataAndRender() {
    fetch("/breath_status")
        .then(res => res.json())
        .then(data => {
            const phase = data.phase;
            const amplitude = (phase / 9).toFixed(3); // simulate amplitude from phase

            drawField(parseInt(phase), parseFloat(amplitude));
        })
        .catch(err => {
            console.error("Field fetch error:", err);
        });
}

function drawField(phase, amplitude) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const barCount = 9;
    const barWidth = canvas.width / barCount;
    const maxBarHeight = canvas.height;

    for (let i = 1; i <= barCount; i++) {
        const height = (i === phase) ? amplitude * maxBarHeight : 0.1 * maxBarHeight;
        const x = (i - 1) * barWidth;
        const y = canvas.height - height;

        ctx.fillStyle = (i === phase) ? "#00ffcc" : "#005555";
        ctx.fillRect(x + 5, y, barWidth - 10, height);
    }

    // Optional: add label text
    ctx.fillStyle = "#00ffcc";
    ctx.font = "16px monospace";
    ctx.fillText(`Φ${phase} | Amplitude: ${amplitude}`, 10, 20);
}

// Update every 2 seconds
setInterval(fetchFieldDataAndRender, 2000);
fetchFieldDataAndRender();
