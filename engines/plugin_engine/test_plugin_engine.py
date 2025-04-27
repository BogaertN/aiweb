from loader import load_plugins

print("🔍 Scanning for plugins...")
load_plugins()

print("\n📄 Log output:")
with open("test_log.txt", "r") as f:
    print(f.read())
