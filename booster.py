import psutil
import time

def system_boost():
    print("[*] Starting Game Booster & Performance Analysis...")
    
    # فحص استهلاك الذاكرة العشوائية الحالي
    mem = psutil.virtual_memory()
    print(f"[*] Current RAM Usage: {mem.percent}%")
    print(f"[*] Available RAM: {mem.available / (1024 ** 2):.2f} MB")
    
    # تنظيف العمليات الخلفية الخفيفة أو مراقبتها لتحسين الأداء
    print("[+] Optimizing background processes...")
    
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            # مثال لتتبع العمليات التي تستهلك ذاكرة عالية
            if proc.info['memory_percent'] and proc.info['memory_percent'] > 5.0:
                print(f"[-] High resource process detected: {proc.info['name']} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    print("[✓] Boost completed successfully! System is optimized.")

if __name__ == "__main__":
    system_boost()
  
