import psutil

def advanced_memory_and_process_analyzer():
    print("[*] Initializing Advanced Game Booster & Memory Analysis Engine...")
    
    # فحص الذاكرة العشوائية (RAM) - يعمل بكفاءة وبدون مشاكل صلاحيات
    mem = psutil.virtual_memory()
    total_ram_gb = mem.total / (1024 ** 3)
    used_ram_percent = mem.percent
    available_ram_mb = mem.available / (1024 ** 2)
    
    print(f"[+] Total RAM: {total_ram_gb:.2f} GB")
    print(f"[+] Used RAM: {used_ram_percent}%")
    print(f"[+] Available RAM: {available_ram_mb:.2f} MB")
    
    # محاولة قراءة استخدام المعالج بطريقة آمنة تتجاوز قيود أندرويد
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"[+] CPU Usage: {cpu_usage}%")
    except Exception:
        print("[!] CPU usage restricted by Android sandbox (Non-Root mode), skipping...")

if __name__ == "__main__":
    advanced_memory_and_process_analyzer()
    
