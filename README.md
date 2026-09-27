# WoW-3.3.5a-Autologin

A simple Python script to automatically log into a wow client.

This has only been tested on the 3.3.5a WOTLK client.


## Installation

Make sure you have git and python installed.

Clone the directory:
`https://github.com/DenzelVW-xyz/WoW-3.3.5a-Autologin.git`
`cd WoW-3.3.5a-Autologin`

Install the required python packages"
`pip install -r requirements.txt`

Create a copy of `config.json.example` and change it to `config.json`

Then edit `config.json:`

```
{
    "wow_path": "C:\\Path\\To\\World of Warcraft 3.3.5a\\Wow.exe",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "account_name_saved": false
}
```

### wow_path
The full path to your WoW 3.3.5a executable.

### username
Your WoW username

### password
Your WoW password

### account_name_saved
Set this according to the **Remember Account Name** option on the WoW login screen.


# Known Limitations

- Credentials are currently stored as plain text in config.json.
- Login automation depends on keyboard input and the expected WoW login-screen state.
- The WoW window must successfully open within the configured detection timeout.
- Only one account configuration is currently supported.

# Disclaimer 

This project is an independent utility for World of Warcraft 3.3.5a and is not affiliated with or endorsed by Blizzard Entertainment.
Use at your own risk.