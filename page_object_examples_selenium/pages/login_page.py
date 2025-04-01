from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.invalid_creds_message = (By.XPATH, "//div[@role='alert']")

    def wait_for_username_field(self, timeout=15):
        """Explicit wait for the username field."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.username_field)
        )

    def enter_username(self, username):
        """Enter the username into the username field."""
        username_field = self.wait_for_username_field()
        username_field.send_keys(username)

    def enter_password(self, password):
        """Enter the password into the password field."""
        password_field = self.driver.find_element(*self.password_field)
        password_field.send_keys(password)

    def click_login(self):
        """Click the login button."""
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()

    def login(self, username, password):
        """Perform the full login process by entering username, password, and clicking the login button."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_invalid_credentials_message(self):
        return self.driver.find_element(*self.invalid_creds_message).text
