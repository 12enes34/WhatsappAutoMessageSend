from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
# Start browser
driver = webdriver.Chrome()

# Open page in the browser
driver.get("https://web.whatsapp.com/")

# Wait enter the input by user
input("Please enter the any key for continui after scan QR")

message = "Hello (this is Auto message)"

contact_name = ["Bedo","Kubi"]
for i in contact_name:
    # Wait find chatbox
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//span[@title='{i}']")))
    # Auto click on the finded person
    search_box.click()
    # Wait find the wanted person message box
    chat_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
    # Click the message box
    ActionChains(driver).move_to_element(chat_box).click().perform()
    # Auto write message and send
    chat_box.send_keys(message)
    chat_box.send_keys(Keys.RETURN)
    time.sleep(3)
# Quit the browser
driver.quit()