from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class SidebarPage:
    def __init__(self, driver):
        self.driver = driver
        self.sidebar_item = (By.XPATH, "//ul[@class='oxd-main-menu']//li[@class='oxd-main-menu-item-wrapper']//a[@class='oxd-main-menu-item']")
        self.active_sidebar_item = (By.XPATH, "//ul[@class='oxd-main-menu']//li[@class='oxd-main-menu-item-wrapper']//a[@class='oxd-main-menu-item active']")

    def click_item(self, item_text):
        # TODO Modify the method implementation once the bug on prod is fixed by the dev team.
        # xpath = f"//li[@class='oxd-main-menu-item-wrapper']//a[@class='oxd-main-menu-item']//span[contains(text(), '{item_text}')]"
        # Workaround:
        elements = self.driver.find_elements(*self.sidebar_item)
        for element in elements:
            span_element = element.find_element(By.TAG_NAME, "span")
            if span_element.text.strip() == item_text:
                span_element.click()
                return
        raise NoSuchElementException(f"'{item_text}' not found on sidebar.")

    def is_item_active(self, item_text):
        element = self.driver.find_element(*self.active_sidebar_item)
        span_element = element.find_element(By.TAG_NAME, "span")
        if span_element.text.strip() == item_text:
            return True
        raise NoSuchElementException(f"'{item_text}' not found on sidebar.")
