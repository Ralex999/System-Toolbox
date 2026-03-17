import subprocess
import os
import sys

def run_command(command, description):
    print(f"\n[#] Running: {description}...")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Error during: {description}")

def show_menu():
    print("\n" + "="*45)
    print("   System Maintenance & Diagnostic Tool")
    print("="*45)
    print(" 1. Quick Diagnostic (DNS Flush)")
    print(" 2. Check for Updates (Winget List)")
    print(" 3. Upgrade All Applications")
    print(" 4. Manage Pins (Exclude/Include)")
    print(" 0. Exit")
    print("-" * 45)

def main():
    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == '1':
            run_command("ipconfig /flushdns", "Flushing DNS Cache")
        
        elif choice == '2':
            run_command("winget upgrade --include-pinned", "Checking Updates")
        
        elif choice == '3':
            confirm = input("Are you sure you want to upgrade ALL? (y/n): ")
            if confirm.lower() == 'y':
                run_command("winget upgrade --all", "Upgrading All Packages")
        
        elif choice == '4':
            print("\n--- Pin Management ---")
            print("To exclude an app: winget pin add <AppID>")
            print("To remove exclusion: winget pin remove <AppID>")
            run_command("winget pin list", "Showing Pinned Apps")
        
        elif choice == '0':
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
