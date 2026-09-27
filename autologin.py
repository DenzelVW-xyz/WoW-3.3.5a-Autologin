import json
import subprocess
import time
import os

import pyautogui
import pygetwindow as gw


def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            config = json.load(file)

    except FileNotFoundError:
        raise RuntimeError(
            "config.json was not found. "
            "Copy config.json.example to config.json and configure it."
        )

    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"config.json contains invalid JSON: {error}"
        )

    required = [
        "wow_path",
        "username",
        "password",
        "account_name_saved",
    ]

    for key in required:
        if key not in config:
            raise RuntimeError(
                f"Missing required config option: {key}"
            )

    return config


def validate_wow_path(path):
    if not os.path.isfile(path):
        raise RuntimeError(
            f"WoW executable was not found: {path}"
        )

    if not path.lower().endswith(".exe"):
        raise RuntimeError(
            "wow_path must point to a Windows executable."
        )

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

def login(config):
    print("Logging in...")

    if config.get("account_name_saved", False):
        # WoW already has the account name and password field is focused
        pyautogui.hotkey("ctrl", "a")
        pyautogui.write(config["password"], interval=0.03)

    else:
        # Username field is focused
        pyautogui.hotkey("ctrl", "a")
        pyautogui.write(config["username"], interval=0.03)

        # Move to password field
        pyautogui.press("tab")
        pyautogui.hotkey("ctrl", "a")
        pyautogui.write(config["password"], interval=0.03)

    pyautogui.press("enter")


def main():
    config = load_config()

    validate_wow_path(config["wow_path"])
    
    print("Launching WoW...")
    subprocess.Popen([config["wow_path"]])

    wait_for_wow()
    login(config)

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"\nError: {error}")