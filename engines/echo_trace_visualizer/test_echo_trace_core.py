# test_echo_trace_core.py

from echo_trace_core import EchoTraceVisualizer

def test_echo_trace_visualizer_behavior():
    visualizer = EchoTraceVisualizer()
    trace = visualizer.record_echo("Φ7", 0.92)
    assert trace["origin_phase"] == "Φ7", "Origin phase should match."
    assert trace["signal_strength"] == 0.92, "Signal strength should match."
    print("✅ Echo Trace Visualizer Test Passed.")

if __name__ == "__main__":
    test_echo_trace_visualizer_behavior()
