class FloatingMenuOverlay:
    def __init__(self):
        self.ram_booster = True
        self.esp_overlay = False
        self.aimbot_lock = False

    def toggle_menu(self):
        print("\n--- DAUWOOD'S DRAGON FLOATING PANEL ---")
        print(f"> RAM Booster: {'ENABLED [ON]' if self.ram_booster else 'DISABLED [OFF]'}")
        print(f"> ESP Overlay: {'ENABLED [ON]' if self.esp_overlay else 'DISABLED [OFF]'}")
        print(f"> Aimbot Lock: {'ENABLED [ON]' if self.aimbot_lock else 'DISABLED [OFF]'}")
        print("---------------------------------------")

    def update_settings(self, esp=True, aim=True):
        self.esp_overlay = esp
        self.aimbot_lock = aim
        print(f"[UI Update] ESP Overlay set to {self.esp_overlay}")
        print(f"[UI Update] Aimbot Lock set to {self.aimbot_lock}")
        
