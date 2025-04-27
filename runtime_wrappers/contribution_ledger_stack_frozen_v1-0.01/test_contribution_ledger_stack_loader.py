# test_contribution_ledger_stack_loader.py
# Tests the Contribution Ledger Stack loader

from contribution_ledger_stack_loader import run_contribution_ledger

def run_test():
    try:
        run_contribution_ledger()
        print("✅ Contribution Ledger Stack Test Passed.")
    except Exception as e:
        print(f"❌ Contribution Ledger Stack Test Failed: {e}")

if __name__ == "__main__":
    run_test()
