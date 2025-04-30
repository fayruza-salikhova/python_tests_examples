import pytest
from pages.login_page import LoginPage

@pytest.mark.login
def test_invalid_login_invalid_username(setup_driver_login_scenarios):
    driver = setup_driver_login_scenarios
    login_page = LoginPage(driver)
    login_page.login("InvalidUser", "admin123")
    assert "Invalid credentials" in login_page.get_invalid_credentials_message()

@pytest.mark.login
def test_invalid_login_invalid_password(setup_driver_login_scenarios):
    driver = setup_driver_login_scenarios
    login_page = LoginPage(driver)
    login_page.login("Admin", "InvalidPassword")
    assert "Invalid credentials" in login_page.get_invalid_credentials_message()

@pytest.mark.login
def test_valid_login(setup_driver_login_scenarios):
    driver = setup_driver_login_scenarios
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    assert "OrangeHRM" in driver.title
