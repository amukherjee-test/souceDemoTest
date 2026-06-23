from playwright.sync_api import Page
from logger import get_logger

logger = get_logger()


class InventoryPage:

    def __init__(self, page: Page):

        self.page = page

        self._sort_dropdown = '[data-test="product-sort-container"]'
        self._product_names = '[data-test="inventory-item-name"]'
        self._cart_icon = '#shopping_cart_container'
        self._burger_menu = '#react-burger-menu-btn'
        self._logout_link = '#logout_sidebar_link'

    def add_product_to_cart(self, product_name):

        logger.info(f"Adding to cart: {product_name}")

        self.page.click(
            f"//div[@class='inventory_item']"
            f"[.//div[@data-test='inventory-item-name' and text()='{product_name}']]//button"
        )

        logger.info(f"Added: {product_name}")

    def go_to_cart(self):

        logger.info("Navigating to cart")

        self.page.click(self._cart_icon)

    def sort_by(self, option):

        logger.info(f"Sorting products by: {option}")

        self.page.select_option(self._sort_dropdown, option)

        logger.info("Sort applied")

    def get_product_names(self):

        names = self.page.locator(self._product_names).all_inner_texts()

        logger.info(f"Products listed: {names}")

        return names

    def logout(self):

        logger.info("Opening burger menu")

        self.page.click(self._burger_menu)

        logger.info("Clicking logout")

        self.page.click(self._logout_link)

        logger.info("Logged out successfully")
