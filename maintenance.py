import subprocess
import os
import sys

def run_command(command, description):
    """Выполняет системную команду и ждет нажатия клавиши в конце."""
    print(f"\n[#] Running: {description}...")
    try:
        # shell=True позволяет запускать системные команды напрямую в Windows
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Error during: {description}")
    
    print("\n" + "-"*45)
    input("Press Enter to return to menu...")

def show_menu():
    """Отрисовка главного меню в консоли."""
    # Очистка экрана для красоты (по желанию можно раскомментировать строку ниже)
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "="*45)
    print("   SMDT - System Maintenance Tool")
    print("="*45)
    print(" 1. Quick Diagnostic (DNS Flush)")
    print(" 2. Check Available Updates (Winget)")
    print(" 3. Upgrade All Applications")
    print(" 4. Manage Pins (Exclude/Include Apps)")
    print(" 0. Exit")
    print("-" * 45)

def main():
    while True:
        show_menu()
        choice = input("Select an option (0-4): ").strip()

        if choice == '1':
            # Очистка кэша DNS
            run_command("ipconfig /flushdns", "Flushing DNS Cache")
        
        elif choice == '2':
            # Показывает только те обновления, которые НЕ заблокированы (без --include-pinned)
            run_command("winget upgrade", "Checking Available Updates")
        
        elif choice == '3':
            # Обновление всех доступных программ
            confirm = input("\nAre you sure you want to upgrade ALL? (y/n): ")
            if confirm.lower() == 'y':
                run_command("winget upgrade --all", "Upgrading Everything")
            else:
                print("Action cancelled.")
        
        elif choice == '4':
            # Управление исключенными программами
            print("\n--- Pin Management Instructions ---")
            print("To EXCLUDE an app: winget pin add <AppID>")
            print("To INCLUDE it back: winget pin remove <AppID>")
            print("-" * 35)
            run_command("winget pin list", "Showing Current Pinned Apps")
        
        elif choice == '0':
            print("\nExiting... Goodbye, Eugene!")
            break
        
        else:
            print("\n[!] Invalid choice, please select 0-4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Closing...")
        sys.exit(0)
