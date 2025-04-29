<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ProtoForge — Gilligan Breathing Dashboard</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

    <header>
        <h1>🧠 Gilligan Copilot Breather</h1>
        <div id="gilliganComment" class="gilligan-comment">Initializing...</div>
    </header>

    <main>

        <section class="phase-section">
            <h2>Phase Breather</h2>
            <div id="phaseStatus" class="phase-status">Current Phase: Φ1</div>
        </section>

        <section class="charge-section">
            <h2>Symbolic Capacitor Charge</h2>
            <div class="charge-bar">
                <div id="chargeBarInner" class="charge-bar-inner">100%</div>
            </div>
        </section>

        <section class="drift-section">
            <h2>Drift Arbitration Monitor</h2>
            <div id="driftLog" class="drift-log">
                <div>Waiting for drift data...</div>
            </div>
        </section>

        <section class="memory-section">
            <h2>Memory Stack Status</h2>
            <div id="activeThreads">Active Threads: 0</div>
            <div id="symbolicLoad">Symbolic Load: 0%</div>
        </section>

        <section class="console-section">
            <h2>System Console Output</h2>
            <pre id="systemConsole" class="system-console">
[System initialized.]
            </pre>
        </section>

    </main>

    <script src="/static/dashboard.js"></script>

</body>
</html>

