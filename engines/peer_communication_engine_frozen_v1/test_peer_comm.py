from peer_comm_core import simulate_peer_message

def test_peer_communication():
    try:
        result = simulate_peer_message()
        print("✅ Test Passed: Peer message simulated.")
        print(result)
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_peer_communication()
