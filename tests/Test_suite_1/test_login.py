import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from logger import get_logger

logger = get_logger()


@pytest.mark.webui_soucedemo
def test_valid_login_and_checkout(page):

    login = LoginPage(page)
    login.navigate()
    login.login("visual_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    logger.info("Login successful")

    inventory = InventoryPage(page)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.add_product_to_cart("Sauce Labs Fleece Jacket")
    inventory.go_to_cart()

    cart = CartPage(page)
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.fill_info("Arka", "Mukherjee", "725911")
    checkout.continue_checkout()
    checkout.finish()

    logger.info("Test Case Executed successfully!")
