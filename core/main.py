from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json


def initializeChromeDriver():
    # This method will initialize the chrome driver,and launch it in full screen mode.
    try:
        options = Options()
        options.headless = True
        s = Service(
            "/mnt/c/Sammit/Learnings material/Python practice/Seleniumpet/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=options)
        driver.maximize_window()
        return driver
    except Exception as e:
        print("Sorry! Unable to initialize driver due to ", e)


def getwebsite(driver, url):
    # This method will access the website which is passed as a url with the help of the driver which was initialized
    try:
        driver.get(url)
    except Exception as e:
        print("Sorry! Unable to open ", url, " due to ", e)
        print("Closing driver...")
        driver.close()


def login(driver, username, password):
    # This method is used to login to the website with the credentials which are passed to it.

    try:
        # finding the username element and entering the username
        driver.find_element(By.ID, "user-name").send_keys(username)

        # finding the password element and entering the password
        driver.find_element(By.ID, "password").send_keys(password)

        # clicking the login button
        driver.find_element(By.ID, "login-button").click()
    except Exception as e:
        print("Sorry! Unable to login due to ", e)


def getdata(file):
    # This method will read the json file provided to it and will extract and return the details from it.
    try:
        data = json.loads(open(file).read())
    except Exception as e:
        print("Sorry! Unable to get details from file due to ", e)
    return data


def selectallitems(driver, items):
    # This method selects all the items on the page and adds them to the cart.

    # traversing through the list of items passed as an argument and get that item.
    try:
        for item in items:
            item_name = item["itemname"]
            element = f"//div[contains(text(),'{item_name}')]"
            driver.find_element(By.XPATH, (element)).click()
    # adding each element in the cart.
            driver.find_element(
                By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    # clicking on back button after adding the element
            driver.find_element(By.ID, "back-to-products").click()
    except Exception as e:
        print("Sorry! Error in adding item to cart due to ", e)


def checkout(driver, checkout_details):
    # This method will checkout the elements in the cart

    firstname = checkout_details[0]["firstname"]
    lastname = checkout_details[0]["lastname"]
    postalcode = checkout_details[0]["postalcode"]
    try:
        driver.find_element(
            By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys(firstname)
        driver.find_element(By.ID, "last-name").send_keys(lastname)
        driver.find_element(By.ID, "postal-code").send_keys(postalcode)
        driver.find_element(By.ID, "continue").click()

        driver.find_element(By.ID, "finish").click()
    except Exception as e:
        print("Sorry! Unable to checkout due to ", e)


def loginlogout(driver, username, password):

    try:
        login(driver, username, password)
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "logout_sidebar_link").click()
    except Exception as e:
        print("Sorry! Unable to logout due to ", e)


def sortitems(driver):

    values = ["za", "az", "lohi", "hilo"]
    try:
        for value in values:
            Select(driver.find_element(By.CLASS_NAME,
                                       "product_sort_container")).select_by_value(value)
    except Exception as e:
        print("Sorry! Unable to sort items due to ", e)
