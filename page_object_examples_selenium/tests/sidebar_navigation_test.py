import pytest

from pages.sidebar_page import SidebarPage
from pages.admin_page import AdminPage

@pytest.mark.sidebar
def test_sidebar_navigation_to_admin(setup_driver):
    sidebar = SidebarPage(setup_driver)
    admin_page = AdminPage(setup_driver)
    sidebar.click_item("Admin")
    assert sidebar.is_item_active("Admin"), "Admin item is not active"
    assert admin_page.is_admin_page(), "Not on the Admin page"
