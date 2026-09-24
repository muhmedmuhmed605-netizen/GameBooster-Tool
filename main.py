import sys
import time
from booster import advanced_memory_and_process_analyzer
from esp_aim import RealTimeESPAndAim

def main():
    while True:
        print("\n==========================================")
        print("      DAUWOOD'S ULTIMATE GAME BOOSTER     ")
        print("==========================================")
        print("[1] Start System Optimization & Memory Scan")
        print("[2] Run ESP & Aimbot Coordinate Engine")
        print("[3] Exit")
        
        choice = input("\nSelect an option (1, 2, or 3): ").strip()
        
        if choice == '1':
            print("\n[*] Initializing system optimization sequence...")
            advanced_memory_and_process_analyzer()
        elif choice == '2':
            print("\n[*] Initializing Real-Time ESP & Aimbot Engine...")
            esp_engine = RealTimeESPAndAim(1080, 2340)
            sample_targets = [
                {'x': 540, 'y': 1000, 'distance': 45},
                {'x': 720, 'y': 1150, 'distance': 120},
            ]
            esp_engine.render_esp_box(sample_targets)
        elif choice == '3':
            print("[*] Exiting tool. Goodbye!")
            sys.exit(0)
        else:
            print("[!] Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
    
