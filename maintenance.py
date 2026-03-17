import subprocess
import os
import sys

def run_command(command, description):
    print(f"\n[#] Running: {description}...")
    try:
        # Using shell=True for Windows command compatibility
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Error during: {description}")
    
    print("\n" + "-"*45)
    input("Press Enter to return to menu...")

def show_menu():
    print("\n" + "="*45)
    print("      SMDT - System Maintenance Tool")
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

        # --- OPTION 1: DIAGNOSTIC ---
        if choice == '1':
            run_command("ipconfig /flushdns", "Flushing DNS Cache")
        
        # --- OPTION 2: CHECK UPDATES ---
        elif choice == '2':
            print("[*] Scanning for updates: normal, pinned, and unknown versions...")
            # Flags --include-pinned and --include-unknown will show Brave/Chrome and others
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
        # Check if running on Windows
        if os.name != 'nt':
            print("Critical: This tool is designed for Windows only.")
            sys.exit(1)
            
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Closing...")
        sys.exit(0)
