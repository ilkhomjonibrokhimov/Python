import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")

wait = WebDriverWait(driver, 10)

laptop_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops")))
laptop_button.click()

wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.card h4.card-title'), 'Sony vaio i5'))

next_button = wait.until(EC.element_to_be_clickable((By.ID, 'next2')))
next_button.click()

wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.card h4.card-title'), 'Apple'))

all_laptops = []

cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-block")))
for card in cards:
    title = card.find_element(By.CLASS_NAME, "card-title").text
    price = card.find_element(By.TAG_NAME, "h5").text
    description = card.find_element(By.CLASS_NAME, "card-text").text
    print(f"\n{title}\n{price}\n{description}")
    all_laptops.append({
        "name": title,
        "price": price,
        "description": description
    })

with open("laptops.json", 'w', encoding='utf-8') as file:
    json.dump(all_laptops, file, indent=4)

print("Data saved to laptops.json")

driver.quit()

