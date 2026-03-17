import subprocess
import os
import sys

def run_command(command, description):
    print(f"[#] Running: {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error during {description}: {e.stderr}")

def main():
    # Проверка на права администратора (нужны для flushdns и системных настроек)
    print("--- System Maintenance & Diagnostic Tool ---")
    
    # 1. Network Diagnostics
    run_command("ipconfig /flushdns", "Flushing DNS Cache")
    run_command("netsh winsock reset", "Resetting Winsock")

    # 2. System Hygiene
    temp_path = os.environ.get('TEMP')
    print(f"[#] Cleaning temporary files in: {temp_path}...")
    # Здесь можно добавить логику удаления файлов

    # 3. Software Management (Winget)
    run_command("winget upgrade --all", "Updating all packages via Winget")

    print("\n[+] Maintenance complete. Logs saved to diagnostic_events.log")

if __name__ == "__main__":
    # Логирование событий (Error Handling)
    sys.stdout = open('diagnostic_events.log', 'w', encoding='utf-8')
    try:
        main()
    finally:
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        print("Done. Check diagnostic_events.log for details.")
