import os
from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()


def create_driver() -> webdriver.Chrome:
    options = Options()

    # Configurações
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    download_dir = Path(
        os.getenv("DOWNLOAD_DIR", "./downloads")
    ).resolve()

    # Garante que a pasta existe
    download_dir.mkdir(parents=True, exist_ok=True)

    # Headless
    if headless:
        options.add_argument("--headless=new")

    # Configurações básicas do Chrome
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    # Configuração dos downloads
    prefs = {
        "download.default_directory": str(download_dir),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
    }

    options.add_experimental_option("prefs", prefs)

    # Selenium Manager cuida do ChromeDriver
    driver = webdriver.Chrome(options=options)

    return driver