// copilot_voice_panel.js

function updateGilliganVoice() {
    fetch("/gilligan_comment")
        .then(res => res.json())
        .then(data => {
            const voiceBox = document.getElementById("gilliganComment");
            voiceBox.innerText = data.text;

            // Pulse animation
            voiceBox.style.opacity = 0.5;
            setTimeout(() => {
                voiceBox.style.opacity = 1.0;
            }, 300);
        })
        .catch(err => {
            console.error("Gilligan comment fetch error:", err);
        });
}

// Refresh every 4 seconds
setInterval(updateGilliganVoice, 4000);
updateGilliganVoice();
