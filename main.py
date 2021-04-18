import time
import selenium
import urllib.request

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# This might bring up an error so please make sure you have your webdriver path correct
driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")

driver.get(
    "https://www.amazon.com/Planet-Coaster-PlayStation-5/dp/B08F719CVM/ref=sr_1_29?dchild=1&qid=1618773048&refinements=p_n_availability%3A2661601011&rnid=2661599011&sr=8-29&srs=19419354011")

# check if product is in stock
buy_button = False

# While buy button is active
while not buy_button:
    try:
        add_to_cart_button = add_button = driver.find_element_by_id("add-to-cart-button")

        print("Button was clicked and order made")
        add_to_cart_button.click()
        buy_button = True
    # While buy button is not active
    except:

        # if this works then the product is sold out
        add_to_cart_button = add_button = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[6]/div[6]/div[1]/div[2]/div/div/div/div/div/div/div/form/div/div/div[5]/div[1]/div[1]/span/span/a")
        # alert user on product sell out
        print("The product is sold out but we are trying again")
        # Refresh page in seconds
        time.sleep(2)
        driver.refresh()
