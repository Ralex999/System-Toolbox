import subprocess
import os
import sys

def run_command(command, description):
    print(f"\n[#] Running: {description}...")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Error during: {description}")
    
    print("\n" + "-"*45)
    input("Press Enter to return to menu...")

def show_menu():
    print("\n" + "="*45)
    print("   SMDT - System Maintenance Tool")
    print("="*45)
    print(" 1. Quick Diagnostic (DNS Flush)")
    print(" 2. Check ALL Updates (Include Pinned/Unknown)")
    print(" 3. Upgrade All Applications (Standard)")
    print(" 4. Manage Pins (Exclude/Include Apps)")
    print(" 0. Exit")
    print("-" * 45)

def main():
    while True:
        show_menu()
        choice = input("Select an option (0-4): ").strip()

    # --- ПУНКТ 1: ДИАГНОСТИКА ---
        if choice == '1':
            run_command("ipconfig /flushdns", "Flushing DNS Cache")
        
    # --- ПУНКТ 2: ПРОВЕРКА (Здесь мы вернули всё!) ---
        elif choice == '2':
            print("[*] Checking for everything: normal, pinned, and unknown versions...")
            # Флаги --include-pinned и --include-unknown вернут Brave и остальные в список
            run_command("winget upgrade --include-pinned --include-unknown", "Full Updates List")
        
    # --- ПУНКТ 3: ОБНОВЛЕНИЕ ---
        elif choice == '3':
            confirm = input("\nUpgrade all standard apps? (y/n): ")
            if confirm.lower() == 'y':
                run_command("winget upgrade --all", "Upgrading Standard Packages")
        
    # --- ПУНКТ 4: УПРАВЛЕНИЕ ЗАКРЕПЛЕНИЕМ ---
        elif choice == '4':
            print("\n--- Pin Management ---")
            print("To EXCLUDE: winget pin add <AppID>")
            print("To INCLUDE: winget pin remove <AppID>")
            run_command("winget pin list", "Showing Pinned Apps")
        
        elif choice == '0':
            print("\nExiting... Goodbye, Eugene!")
            break
        
        else:
            print("\n[!] Invalid choice, try 0-4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Closing...")
        sys.exit(0)
