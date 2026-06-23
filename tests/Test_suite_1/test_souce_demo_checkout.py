import pytest
from pages.login_page import LoginPage
from logger import get_logger

logger = get_logger()


@pytest.mark.webui_soucedemo
def test_valid_login(page):

    page.goto("https://www.saucedemo.com/")

    page.fill('input[data-test="username"]', "visual_user")
    logger.info("Id entered")
    page.fill('input[data-test="password"]', "secret_sauce")
    logger.info("password entered")

    page.click('input[data-test="login-button"]')
    logger.info("logged in successfull...")

    page.wait_for_url("**/inventory.html")

    # Adding products to the cart:
    product_name1 = "Sauce Labs Backpack"
    product_name2 = "Sauce Labs Fleece Jacket"

    page.click(f"//div[@class='inventory_item'][.//div[@data-test='inventory-item-name' and text()='{product_name1}']]//button")
    logger.info(f"added the {product_name1} to cart...")
    page.click(f"//div[@class='inventory_item'][.//div[@data-test='inventory-item-name' and text()='{product_name2}']]//button")
    logger.info(f"added the {product_name2} to cart...")

    # go to the cart section:
    page.click('//div[@id="shopping_cart_container"]')
    logger.info("clicked on cart icon..")

    # click on the checkout:
    page.click('//button[@class="btn btn_action btn_medium checkout_button btn_visual_failure"]')
    logger.info("clicked on checkout button..")

    logger.info("Filling the details in the checkout page")
    page.fill('//div[@class="form_group"]/input[@id="first-name"]', "Arka")
    page.fill('//div[@class="form_group"]/input[@id="last-name"]', "Mukherjee")
    page.fill('//div[@class="form_group"]/input[@id="postal-code"]', "725911")
    logger.info("Details filled successfully")

    #click on the continue button
    page.click("//input[@type='submit' and @data-test='continue']")
    logger.info("clicked on the continue button")
    # click on the finish button:
    page.click('//button[@class="btn btn_action btn_medium cart_button"]')
    logger.info("clicked on the finish button")

    logger.info("Test Case Executed successfully!")