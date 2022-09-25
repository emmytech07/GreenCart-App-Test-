
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

BrowserSortedVeggies =[]

service_obj = Service("D:/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#Click on Header
driver.find_element(By.XPATH, "//span[contains(text(),'Veg/fruit name')]").click()

#Collect all Name
# //tr//td[1]
VegeWebElements = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")

for veg in VegeWebElements:
    BrowserSortedVeggies.append(veg.text)

# Copy in another variable
OriginalBrowserSortedList = BrowserSortedVeggies.copy()

#sort this BrowserVeggieList ==> newSortedList -> 
BrowserSortedVeggies.sort()

assert BrowserSortedVeggies ==  OriginalBrowserSortedList

