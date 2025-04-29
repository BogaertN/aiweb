// memory_stack_panel.js

function updateMemoryVisualizer() {
    fetch("/memory_stack")
        .then(res => res.json())
        .then(data => {
            const threadDisplay = document.getElementById("activeThreads");
            const loadDisplay = document.getElementById("symbolicLoad");

            const threads = data.active_threads || 0;
            const load = data.current_symbolic_load || 0;

            threadDisplay.innerText = `Active Threads: ${threads}`;
            loadDisplay.innerText = `Symbolic Load: ${load}%`;

            // Pulse color based on load severity
            const loadElement = document.getElementById("symbolicLoad");
            if (load >= 75) {
                loadElement.style.color = "#ff5555";  // red
            } else if (load >= 50) {
                loadElement.style.color = "#ffaa00";  // orange
            } else {
                loadElement.style.color = "#00ffcc";  // green/calm
            }
        })
        .catch(err => console.error("Memory stack fetch failed:", err));
}

// Interval update
setInterval(updateMemoryVisualizer, 2500);
updateMemoryVisualizer();
