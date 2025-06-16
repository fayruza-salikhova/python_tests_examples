from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

class Page:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

class LoginPage(Page):
    def open(self):
        path = os.path.abspath("C:/Projects/selenium_stub/login.html")
        self.driver.get(f"file:///{path}")

    def login(self, username, password):
        self.driver.find_element("id", "username").send_keys(username)
        self.driver.find_element("id", "password").send_keys(password)
        self.driver.find_element("id", "submit").click()

def log_step(func):
    def wrapper(*args, **kwargs):
        print(f"[STEP] {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[DONE] {func.__name__}")
        return result
    return wrapper

class LoginTests:
    def __init__(self, driver):
        self.page = LoginPage(driver)

    @log_step
    def test_valid_login(self):
        self.page.open()
        self.page.login("user", "pass")

service = Service(executable_path="C:\\Projects\\python_projects\\python_tests_examples\\python_tests_examples\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

login = LoginTests(driver)
login.test_valid_login()

driver.quit()
