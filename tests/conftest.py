import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--window-size=1920,1080')
    chrome_install = ChromeDriverManager().install()
    folder = os.path.dirname(chrome_install)
    chromedriver_path = os.path.join(folder, "chromedriver.exe")
    chrome_service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()
