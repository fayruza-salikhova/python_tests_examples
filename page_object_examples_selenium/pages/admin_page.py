from selenium.webdriver.common.by import By

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.topbar_header = (By.CLASS_NAME, "oxd-topbar-header-breadcrumb")

    def get_topbar_header_text(self):
        topbar_header = self.driver.find_element(*self.topbar_header)
        return topbar_header.text.strip()

    def is_admin_page(self):
        return "Admin" in self.get_topbar_header_text()
