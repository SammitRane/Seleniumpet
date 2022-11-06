import pytest
import sys
import core.main as app
from selenium.webdriver.common.by import By

#This test case will test the initialization of the chrome driver
def test_initdriver():
    driver = app.initializeChromeDriver()
    assert driver is not None

#This test case will test whether we are able to reach the website 
def test_getwebsite():
    url = "https://www.saucedemo.com/"
    driver = app.initializeChromeDriver()
    app.getwebsite(driver, url)
    assert driver.find_element(By.ID, "root") is not None

#This test case will check the login and logout feature
def test_loginlogout():
    url = "https://www.saucedemo.com/"
    creds_data = app.getdata("./core/input/creds.json")
    driver = app.initializeChromeDriver()
    app.getwebsite(driver, url)
    app.loginlogout(driver, creds_data["username"], creds_data["password"])
    assert driver.find_element(By.ID, "root") is not None

#This test case will check the sorting feature
def test_sort():
    driver = setup()
    app.sortitems(driver)
    assert driver.find_element(By.ID, "root") is not None

#This test case will select all the items and check them out
def test_selectallcheckout():
    driver = setup()
    items = app.getdata("./core/input/items.json")
    checkout_details = app.getdata("./core/input/checkoutdetails.json")
    app.selectallitems(driver, items)
    app.checkout(driver, checkout_details)
    assert driver.find_element(By.ID, "back-to-products") is not None

#This method is used to create a basic setup for all the test cases with some predefined steps
def setup():
    try:
        url = "https://www.saucedemo.com/"
        creds_data = app.getdata("./core/input/creds.json")
        driver = app.initializeChromeDriver()
        app.getwebsite(driver, url)
        app.login(driver, creds_data["username"], creds_data["password"])
        return driver
    except Exception as e:
        print("Sorry! Unable to setup for pytest due to ", e)
