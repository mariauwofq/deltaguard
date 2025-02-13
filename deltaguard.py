import sys
import os
import subprocess

try:
    import pygetwindow as gw
    from pywinauto import Desktop
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygetwindow", "pywinauto"])
    import pygetwindow as gw
    from pywinauto import Desktop

class DeltaGuard:
    def __init__(self):
        self.virtual_desktops = []

    def create_virtual_desktop(self):
        # Create a new virtual desktop
        subprocess.run('powershell.exe New-Item -Type Directory -Path "shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}"', shell=True)
        self.virtual_desktops.append({})
        print(f"Created virtual desktop #{len(self.virtual_desktops)}")

    def list_windows_on_current_desktop(self):
        # List windows on the current virtual desktop
        windows = gw.getAllTitles()
        print(f"Windows on the current desktop: {windows}")
        return windows

    def move_window_to_desktop(self, window_title, desktop_index):
        # Move a window to a specific virtual desktop
        if 0 <= desktop_index < len(self.virtual_desktops):
            windows = gw.getWindowsWithTitle(window_title)
            if windows:
                window = windows[0]
                self.virtual_desktops[desktop_index][window_title] = window
                print(f"Moved window '{window_title}' to desktop #{desktop_index + 1}")
            else:
                print(f"No window with title '{window_title}' found.")
        else:
            print("Invalid desktop index.")

    def switch_to_desktop(self, desktop_index):
        # Switch to a specific virtual desktop
        if 0 <= desktop_index < len(self.virtual_desktops):
            print(f"Switched to virtual desktop #{desktop_index + 1}")
            # Implement the actual switch logic here
        else:
            print("Invalid desktop index.")

    def close_virtual_desktop(self, desktop_index):
        # Close a specific virtual desktop
        if 0 <= desktop_index < len(self.virtual_desktops):
            print(f"Closed virtual desktop #{desktop_index + 1}")
            del self.virtual_desktops[desktop_index]
        else:
            print("Invalid desktop index.")

if __name__ == "__main__":
    deltaguard = DeltaGuard()
    deltaguard.create_virtual_desktop()
    deltaguard.list_windows_on_current_desktop()
    deltaguard.move_window_to_desktop("Untitled - Notepad", 0)
    deltaguard.switch_to_desktop(0)
    deltaguard.close_virtual_desktop(0)