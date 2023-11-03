from os import path
from pathlib import Path
from re import search
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
#doc selenium
# https://selenium-python.readthedocs.io/locating-elements.html
# caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless)
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service = chrome_service,
        options=chrome_options,
    )

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = ('--desable-gpu', '--no-sandbox')
    options = ()
    browser = make_chrome_browser(*options)

    #como antes
    try:
        browser.get('https://www.google.com.br/')
        search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.NAME, 'q')
            )
        )
        search_input.send_keys('lfs world')
        search_input.send_keys(Keys.ENTER)

        results = browser.find_element(By.ID, 'rso')
        links = results.find_elements(By.TAG_NAME, 'a')
        links[0].click()

        search_input_login = browser.find_element(By.CLASS_NAME, 'btn_up')
        search_input_login.click()

        username = browser.find_element(By.NAME, 'loginName')
        username.send_keys('')

        password = browser.find_element(By.NAME, 'loginPassword')
        password.send_keys('')

        login = browser.find_elements(By.CLASS_NAME, 'btn_up')
        login[1].click()
    except:
        print('ops')
    sleep(TIME_TO_WAIT)
