from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

f = lambda x: x[1]

def f(x):
    return x*x

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")
try:
    lang = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
    lang.click()
    time.sleep(.1) 
    cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))
finally:
    actions = ActionChains(driver)
    while True:
        print("here")
        actions.click(cookie)
        actions.perform()
        