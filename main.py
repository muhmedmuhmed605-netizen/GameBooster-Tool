import sys
import time
from booster import advanced_memory_and_process_analyzer

def main():
    print("==========================================")
    print("      DAUWOOD'S LIGHT - GAME BOOSTER      ")
    print("==========================================")
    print("[1] Start System Optimization & Memory Scan")
    print("[2] Exit")
    
    choice = input("\nSelect an option (1 or 2): ").strip()
    
    if choice == '1':
        print("\n[*] Initializing optimization sequence...")
        advanced_memory_and_process_analyzer()
    else:
        print("[*] Exiting tool. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
  
