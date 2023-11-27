import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


USERNAME = input("Enter your username: ")
PASSWORD = getpass("Enter your password: ")
URL = "https://www.empatica.com/connect/login.php"
DELAY = 20

print("Stay tuned while code is running ...")

driver = webdriver.Chrome()

wait = WebDriverWait(driver, DELAY)

driver.get(URL)

# Enter username and password
wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(USERNAME)
wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(PASSWORD)

# Click the login button
wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/ul[1]/li[2]/a"))
).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/a/button"))).click()

time.sleep(DELAY)
elements = driver.find_elements(By.ID, "fileDownloadCustomRichExperience")
for i in range(len(elements)):
    wait.until(EC.element_to_be_clickable(elements[i]))
    elements[i].click()
    print(f"Downloading: ({i}/{len(elements)})")
    time.sleep(DELAY)
    try:
        background_element = driver.find_element(By.ID, "background")
        driver.execute_script(
            """var element = arguments[0]; element.parentNode.removeChild(element);""",
            background_element,
        )
    except:
        pass

time.sleep(DELAY * 5)
driver.quit()
