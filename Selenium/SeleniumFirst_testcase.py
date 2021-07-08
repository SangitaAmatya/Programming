from typing import List

import values as values
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import plistlib

driver = webdriver.Chrome (ChromeDriverManager ().install ())
driver.get ("https://www.orbitz.com/")
driver.maximize_window ()
driver.implicitly_wait (20)
title = driver.title
print (title)
assert "Orbitz Hotel Deals, Flights, Cheap Vacations & Rental Cars" in title
Flightclick=driver.find_element_by_xpath ("//span[contains(text(), \"Flights\")]")
Flightclick.click()
Leaving_From = driver.find_element_by_xpath ("//button[@aria-label=\"Leaving from\"]")
Leaving_From.send_keys ("SFO")
values = driver.find_element_by_tag_name("li")
for value in values:
    if value.getText ().contains ("SFO"):
     value.click();
