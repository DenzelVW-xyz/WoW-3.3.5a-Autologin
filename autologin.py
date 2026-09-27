import json
import subprocess
import time

import pyautogui


def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    config = load_config()

    subprocess.Popen([config["wow_path"]])

    print("Waiting for WoW...")
    time.sleep(8)

    pyautogui.write(config["username"])
    pyautogui.press("tab")

    pyautogui.write(config["password"])
    pyautogui.press("enter")


if __name__ == "__main__":
    main()