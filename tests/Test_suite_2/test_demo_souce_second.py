import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from logger import get_logger

logger = get_logger()


@pytest.mark.webui_soucedemo
def test_locked_out_user_login(page):

    login = LoginPage(page)
    login.navigate()
    login.login("locked_out_user", "secret_sauce")

    error_msg = login.get_error_message()
    assert "locked out" in error_msg.lower()

    logger.info("Locked out user test passed")


@pytest.mark.webui_soucedemo
def test_product_sort_z_to_a(page):

    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    logger.info("Login successful")

    inventory = InventoryPage(page)
    inventory.sort_by("za")

    items = inventory.get_product_names()
    assert items == sorted(items, reverse=True), "Products are not sorted Z to A"

    logger.info("Product sort Z to A test passed")


@pytest.mark.webui_soucedemo
def test_logout(page):

    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    logger.info("Login successful")

    inventory = InventoryPage(page)
    inventory.logout()

    page.wait_for_url(LoginPage.URL)
    assert login.is_login_page_visible()

    logger.info("Logout test passed")
