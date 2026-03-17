import subprocess
import os
import sys

def run_command(command, description):
    print(f"[#] Running: {description}...")
    try:
        # shell=True позволяет запускать системные команды напрямую
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Error or interruption during: {description}")

def main():
    print("============================================")
    print("   System Maintenance & Diagnostic Tool")
    print("============================================\n")
    
    # 1. Сетевая диагностика
    run_command("ipconfig /flushdns", "Flushing DNS Cache")
    
    # 2. Проверка обновлений ПО
    print("[#] Checking for software updates (Winget)...")
    # Добавили --include-pinned, чтобы ты видел вообще всё, что можно обновить
    run_command("winget upgrade --include-pinned", "Checking all packages")

    print("\n[+] Done! All tasks completed.")
    
    # Пауза, чтобы окно не закрывалось сразу после работы
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
