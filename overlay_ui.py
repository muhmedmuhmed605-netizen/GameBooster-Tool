import time

class FloatingMenuOverlay:
    def __init__(self):
        self.is_visible = False
        self.active_features = {
            "RAM Booster": True,
            "ESP Overlay": False,
            "Aimbot Lock": False
        }

    def toggle_floating_menu(self):
        self.is_visible = not self.is_visible
        if self.is_visible:
            print("[UI] Floating Menu Opened over game interface.")
            self.show_menu_options()
        else:
            print("[UI] Floating Menu Minimized to icon.")

    def show_menu_options(self):
        print("\n--- DAUWOOD'ْس FLOATING PANEL ---")
        for feature, status in self.active_features.items():
            state = "ENABLED [ON]" if status else "DISABLED [OFF]"
            print(f" > {feature}: {state}")
        print("--------------------------------")

    def modify_feature_state(self, feature_name, state: bool):
        if feature_name in self.active_features:
            self.active_features[feature_name] = state
            print(f"[UI Update] {feature_name} set to {state}")

if __name__ == "__main__":
    overlay_ui = FloatingMenuOverlay()
    overlay_ui.toggle_floating_menu()
    
    # تفعيل الميزات الفعلية من القائمة
    overlay_ui.modify_feature_state("ESP Overlay", True)
    overlay_ui.modify_feature_state("Aimbot Lock", True)
    
    overlay_ui.show_menu_options()
  
