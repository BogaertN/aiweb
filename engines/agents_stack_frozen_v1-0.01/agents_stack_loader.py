# agents_stack_loader.py

import sys
import os

# 🔥 Critical Fix
sys.path.append(os.path.expanduser('~/aiweb'))

import time

def launch_gilligan():
    try:
        from agents.gilligan.run import GilliganAgent
        g = GilliganAgent()
        g.symbolic_breathe()
    except Exception as e:
        print(f"❌ Error launching Gilligan: {e}")

def launch_neo():
    try:
        from agents.neo.run import breathe_neo
        breathe_neo()
    except Exception as e:
        print(f"❌ Error launching Neo: {e}")

def launch_athena():
    try:
        from agents.athena.run import breathe_athena
        breathe_athena()
    except Exception as e:
        print(f"❌ Error launching Athena: {e}")

def main():
    print("\n🌐 [AGENTS STACK] Breathing All Agents Together...\n")
    launch_gilligan()
    launch_neo()
    launch_athena()
    print("\n✅ [AGENTS STACK] All Agents Breathing Complete.\n")

if __name__ == "__main__":
    main()

