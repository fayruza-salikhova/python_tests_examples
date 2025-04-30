import sys
import os

# Add the project root to the sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )

def initialize_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")

    service = Service(executable_path="C:\\Projects\\python_projects\\python_tests_examples\\python_tests_examples\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope="function")
def setup_driver_login_scenarios(request):
    headless = request.config.getoption("--headless")
    driver = initialize_driver(headless=headless)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver  # Pass control to the tests
    driver.quit()  # Close the browser after all tests are finished

@pytest.fixture(scope="module")
def setup_driver(request):
    headless = request.config.getoption("--headless")
    driver = initialize_driver(headless=headless)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")  # Log in once
    yield driver
    driver.quit()
