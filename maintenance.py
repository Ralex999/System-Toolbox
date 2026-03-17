import subprocess
import os
import sys
import shutil

def run_command(command, description, silent=False):
    print(f"\n[#] Running: {description}...")
    try:
        if silent:
            subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Error during: {description}")

def show_menu():
    print("\n" + "="*45)
    print("      SMDT - System Maintenance Tool")
    print("="*45)
    print(" 1. Quick Diagnostic (DNS Flush + Temp Clean)")
    print(" 2. Check ALL Updates (Include Pinned/Unknown)")
    print(" 3. Upgrade All Applications (Standard)")
    print(" 4. Manage Pins (Exclude/Include Apps)")
    print(" 0. Exit")
    print("-" * 45)

def main():
    while True:
        show_menu()
        choice = input("Select an option (0-4): ").strip()

        # --- OPTION 1: DIAGNOSTIC (DNS + TEMP) ---
        if choice == '1':
            # Part A: DNS Flush
            run_command("ipconfig /flushdns", "Flushing DNS Cache")
            
            # Part B: Temp Cleanup (Integrated)
            print("[#] Running: Cleaning Temporary Files...")
            temp_folder = os.environ.get('TEMP')
            files_deleted = 0
            if temp_folder and os.path.exists(temp_folder):
                for item in os.listdir(temp_folder):
                    item_path = os.path.join(temp_folder, item)
                    try:
                        if os.path.isfile(item_path) or os.path.islink(item_path):
                            os.unlink(item_path)
                            files_deleted += 1
                        elif os.path.isdir(item_path):
                            shutil.rmtree(item_path)
                            files_deleted += 1
                    except:
                        continue
                print(f"[+] Done: Removed {files_deleted} items from Temp.")
            
            print("\n" + "-"*45)
            input("Press Enter to return to menu...")

        # --- OPTION 2: CHECK UPDATES ---
        elif choice == '2':
            print("[*] Scanning for updates: normal, pinned, and unknown versions...")
            run_command("winget upgrade --include-pinned --include-unknown", "Full Updates List")
        
        # --- OPTION 3: UPGRADE ---
        elif choice == '3':
            confirm = input("\nUpgrade all standard apps? (y/n): ")
            if confirm.lower() == 'y':
                run_command("winget upgrade --all", "Upgrading Standard Packages")
        
        # --- OPTION 4: PIN MANAGEMENT ---
        elif choice == '4':
            print("\n--- Pin Management ---")
            print("To EXCLUDE: winget pin add <AppID>")
            print("To INCLUDE: winget pin remove <AppID>")
            run_command("winget pin list", "Showing Pinned Apps")
        
        # --- EXIT ---
        elif choice == '0':
            print("\nExiting... Goodbye!")
            break
        
        else:
            print("\n[!] Invalid choice, please select 0-4.")

if __name__ == "__main__":
    try:
        if os.name != 'nt':
            print("Critical: This tool is designed for Windows only.")
            sys.exit(1)
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Closing...")
        sys.exit(0)
