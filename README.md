# Instagram Follow Bot 🤖

This Python script uses Selenium to automate following users on Instagram.

**Disclaimer:** Use this script responsibly and ethically. Automating actions on Instagram may violate their terms of service.

## Features ✨

* Automates following users from an Instagram account's followers list.
* Handles `ElementClickInterceptedException` to avoid errors.

## Getting Started 🚀

### Prerequisites

* Python 3.x
* Chrome browser
* ChromeDriver (matching your Chrome version)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/SilentAshes/IG-BOT.git
    cd IG-BOT
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Download ChromeDriver:
    * Download the ChromeDriver that corresponds to your Chrome browser version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
    * Place the `chromedriver.exe` file in a directory and update the `PATH` variable in the `IG-BOT.py` script.
    * **Or:** add the chromedriver to your system path.

4.  Set up Environment Variables (Recommended):
    * Create environment variables for your Instagram username, password, and target account. Example:
        * `IG_USERNAME=your_username`
        * `IG_PASSWORD=your_password`
        * `IG_TARGET=target_account`
    * Modify the `IG-BOT.py` script to use these environment variables:

    ```python
    import os
    USER_NAME = 'IG_USERNAME'
    PASSWD = 'IG_PASSWORD'
    ACC_NAME ='IG_TARGET'
    ```

### Usage

1.  Run the script:

    ```bash
    python IG-BOT.py
    ```

2.  The script will open a Chrome browser, log in to Instagram, navigate to the target account's followers list, and follow the first 20 followers **(or as you want)**

### Important Notes

* Be mindful of Instagram's rate limits to avoid account restrictions.
* This script is for educational purposes only. Use it responsibly.

### Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request.

### License

This project is licensed under the [MIT License](LICENSE).
