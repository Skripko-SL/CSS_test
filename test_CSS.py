#import
import os
import pathlib
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent


def Driver_Connect():
    ua = UserAgent(browsers = ['chrome'])
    useragent = ua.random
    path_driver = pathlib.Path('chromedriver.exe')
    path_chromedriver = path_driver.resolve()
    path_user = os.getcwd() + "\Chrome"
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")  # если надо показать окно браузера, то нужно закомментить эту строку
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-site-isolation-trials")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument(f"user-agent={useragent}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"--user-data-dir={path_user}")
    options.add_argument("--mite-audio")

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(executable_path = path_chromedriver, options = options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
                '''})
    return driver


driver = Driver_Connect()
driver.get("https://www.avito.ru/nizhniy_novgorod/kvartiry/2-k._kvartira_625m_1923et._2318399964")

list_CSS = [
"a[class^='iva-item-sliderLink']",
"span[class^='breadcrumbs-linkWrapper']",
"ul[class^='params-paramsList'] li",
"ul[class^='style-item-params'] li",
"span[class^='style-item-address__string']",
"span[class^='style-price-value-main'] span[class^='js-item-price']",
"div[class^='style-item-map-wrapper']",
]

def find_CSS(CSS):
    try:
        elem = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"{CSS}"))
        )
        print('Class ',elem.get_attribute("class"), 'found' )
    except TimeoutException:
        return print(f'Class not found {CSS}')

for x in list_CSS:
    find_CSS(x)