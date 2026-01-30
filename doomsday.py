import os
import sys
import subprocess

def main():
    # Get Windows version
    windows_version = sys.getwindowsversion()
    
    # Choose appropriate path based on architecture
    if windows_version.architecture == 'AMD64':
        system32_path = "C:\\Windows\\System32"
    else:
        system32_path = "C:\\Windows\\SysWOW64"
    
    # Check if directory exists
    if not os.path.exists(system32_path):
        print(f"{system32_path} does not exist")
        return
    
    # Confirm deletion
    confirm = input(f"Delete {system32_path}? (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled")
        return
    
    # Delete directory
    try:
        subprocess.run(["rmdir", "/s", "/q", system32_path], check=True)
        print("Directory deleted successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting directory: {e}")

if __name__ == "__main__":
    main()
