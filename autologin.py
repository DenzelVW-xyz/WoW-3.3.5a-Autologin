import json
import subprocess
import time

import pyautogui
import pygetwindow as gw


def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)


def wait_for_wow(timeout=30):
    print("Waiting for World of Warcraft...")

    start = time.time()

    while time.time() - start < timeout:
        windows = gw.getWindowsWithTitle("World of Warcraft")

        if windows:
            window = windows[0]
            print("WoW window detected!")

            # Give the client a moment to finish initializing
            time.sleep(1)

            try:
                if window.isMinimized:
                    window.restore()

                window.activate()
            except Exception as error:
                print(f"Could not activate window: {error}")

            time.sleep(1)
            return window

        time.sleep(0.25)

    raise TimeoutError("WoW window was not detected within 30 seconds.")


def main():
    config = load_config()

    print("Launching WoW...")
    subprocess.Popen([config["wow_path"]])

    wait_for_wow()

    print("Logging in...")

    pyautogui.write(config["username"], interval=0.03)
    pyautogui.press("tab")
    pyautogui.write(config["password"], interval=0.03)
    pyautogui.press("enter")


if __name__ == "__main__":
    main()