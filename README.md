import os
import subprocess
import platform

def clear_dns():
    """Сброс кэша DNS и сети"""
    print("Checking network configuration...")
    if platform.system() == "Windows":
        subprocess.run(["ipconfig", "/flushdns"], capture_output=True)
        subprocess.run(["netsh", "winsock", "reset"], capture_output=True)
        print("DNS cache flushed and Winsock reset.")

def clean_temp():
    """Очистка временных файлов"""
    temp_dir = os.environ.get('TEMP')
    if temp_dir and os.path.exists(temp_dir):
        print(f"Cleaning temporary files in: {temp_dir}")
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception:
                    continue
        print("Cleanup complete.")

def main_menu():
    print("=== System Maintenance Tool ===")
    print("1. Flush DNS & Reset Network")
    print("2. Clean Temporary Files")
    print("3. Full Optimization (1+2)")
    print("0. Exit")
    
    choice = input("\nSelect an option: ")
    
    if choice == '1':
        clear_dns()
    elif choice == '2':
        clean_temp()
    elif choice == '3':
        clear_dns()
        clean_temp()
    elif choice == '0':
        print("Exiting...")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
