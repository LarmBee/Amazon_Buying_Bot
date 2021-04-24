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
    "https://www.amazon.com/TCL-32-720p-ROKU-Smart/dp/B088S3V3R4/ref=sr_1_2?dchild=1&field-shipping_option-bin=3242350011&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=85a9188d-dbd5-424e-9512-339a1227d37c&pf_rd_r=YQ7Z0JKXTW2ZV2TD3KJ7&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1619265109&rnid=1266092011&s=electronics&sr=1-2")

# check if product is in stock
buy_button = False

# While buy button is active
while not buy_button:
    try:
        # if this works then the product is sold out
        add_to_cart_button = add_button = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[6]/div[6]/div[1]/div[2]/div/div/div/div/div/div/div/form/div/div/div[5]/div[1]/div[1]/span/span/a")
        # alert user on product sell out
        print("The product is sold out but we are trying again")
        # Refresh page in seconds
        time.sleep(2)
        driver.refresh()
    except:
        add_to_cart_button = add_button = driver.find_element_by_id("add-to-cart-button")
        print("Button was clicked and order made")
        add_to_cart_button.click()
        buy_button = True
    # lets click the checkout button and log in
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div/div[4]/div/div/div/span[2]/span/a").click()
    email = WebDriverWait(driver, 10 ).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]")))
    # clear input field
    email.clear()
    # send keys
    email.send_keys("")  # input email address here

    # click continue button
    continue_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input")))

    # click function
    continue_btn.click()

    # password page
    password = WebDriverWait(driver, 10 ).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input")))
    # clear input field
    password.clear()
    # send keys
    password.send_keys("")  # input password here

    # click password button
    password_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input")))

    # click function
    password_btn.click()

    # address click (Assuming you already have a default address)
    address_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/div[1]/form/div/div[1]/div[2]/span/a")))
    address_btn.click()

    # shipping
    shipping_page = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div[1]/form/div[3]/div/div/span[1]/span/input")))
    shipping_page.click()

