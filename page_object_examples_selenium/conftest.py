import sys
import os

# Add the project root to the sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page_object_examples_selenium.pages.login_page import LoginPage

def initialize_driver():
    service = Service(executable_path="C:\\Projects\\python_projects\\python_tests_examples\\python_tests_examples\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope="function")
def setup_driver_login_scenarios():
    driver = initialize_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver  # Pass control to the tests
    driver.quit()  # Close the browser after all tests are finished

@pytest.fixture(scope="module")
def setup_driver():
    driver = initialize_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")  # Log in once
    yield driver
    driver.quit()
