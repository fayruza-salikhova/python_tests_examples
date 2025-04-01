from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.topbar_header = (By.CLASS_NAME, "oxd-topbar-header-breadcrumb")  # Breadcrumb

    def get_topbar_header_text(self):
        topbar_header = self.driver.find_element(*self.topbar_header)
        return topbar_header.text.strip()

    def is_dashboard_page(self):
        return self.get_topbar_header_text() == "Dashboard"
