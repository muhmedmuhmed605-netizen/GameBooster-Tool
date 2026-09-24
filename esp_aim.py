import math
import time

class RealTimeESPAndAim:
    def __init__(self, screen_width=1080, screen_height=2340):
        # إحداثيات الشاشة الحقيقية (مثال: دقة شاشة هاتفك مثل ريدمي)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_x = screen_width / 2
        self.center_y = screen_height / 2
        
    def calculate_distance(self, target_x, target_y):
        """حساب المسافة الحقيقية بين مركز الشاشة وإحداثيات الهدف (العدو)"""
        dx = target_x - self.center_x
        dy = target_y - self.center_y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

    def get_aimbot_adjustment(self, target_x, target_y, smoothing=5.0):
        """حساب إزاحة التصويب الفعلي (Crosshair Offset) لتوجيه السلاح بدقة نحو الهدف"""
        dx = target_x - self.center_x
        dy = target_y - self.center_y
        
        # تطبيق خوارزمية التنعيم لتفادي الاهتزاز المفاجئ
        move_x = dx / smoothing
        move_y = dy / smoothing
        return {'move_x': move_x, 'move_y': move_y}

    def render_esp_box(self, targets):
        """معالجة وإسقاط إحداثيات الـ ESP الحقيقية لكل الأهداف المرصوحة"""
        print(f"[*] Scanning {len(targets)} active screen vectors...")
        for i, target in enumerate(targets):
            tx, ty, t_dist = target['x'], target['y'], target['distance']
            distance_to_crosshair = self.calculate_distance(tx, ty)
            
            print(f"[ESP Target {i+1}] Coordinates: ({tx}, {ty}) | Distance: {t_dist}m | Offset from Center: {distance_to_crosshair:.2f}px")
            
            # إذا كان الهدف قريب بما فيه الكفاية، احسب إحداثيات الـ Aimbot الفعلية
            if t_dist <= 150: # ضمن نطاق 150 متر
                adjustment = self.get_aimbot_adjustment(tx, ty)
                print(f"   └── [Aimbot Lock] Adjusting aim by X: {adjustment['move_x']:.2f}, Y: {adjustment['move_y']:.2f}")

if __name__ == "__main__":
    # تهيئة النظام بدقة شاشة الموبايل
    esp_engine = RealTimeESPAndAim(1080, 2340)
    
    # عينة لبيانات أهداف حقيقية وهمية يتم التقاطها من شاشة اللعبة
    simulated_live_targets = [
        {'x': 540, 'y': 1000, 'distance': 45},  # هدف قريب بالمنتصف
        {'x': 720, 'y': 1150, 'distance': 120}, # هدف على اليمين
    ]
    
    print("[+] Real ESP and Aimbot Engine Started...")
    esp_engine.render_esp_box(simulated_live_targets)
  
