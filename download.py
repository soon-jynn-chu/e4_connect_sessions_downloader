from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time

USERNAME = "username"
PASSWORD = "password"
WEBDRIVER_PATH = "webdriver_path"
URL = "https://www.empatica.com/connect/login.php"

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.automatic_downloads": 1}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(WEBDRIVER_PATH, options=options)

wait = WebDriverWait(driver, 30)

driver.get(URL)

wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(USERNAME)
wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(PASSWORD)
wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/ul[1]/li[2]/a"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/a/button"))).click()

time.sleep(10)
html = driver.page_source
soup = bs(html)
addr = 'https://www.empatica.com/connect/'
id = 'fileDownloadCustomRichExperience'

elements = driver.find_elements(By.ID, id)
for i in range(len(elements)):
    wait.until(EC.element_to_be_clickable(elements[i]))
    elements[i].click()
    print(f"Downloading: ({i}/{len(elements)})")
    time.sleep(10)
    try:
        background_element = driver.find_element(By.ID, "background")
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, background_element)
    except:
        pass
time.sleep(60)
driver.quit()
print("Logged in")
