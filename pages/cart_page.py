from playwright.sync_api import Page
from logger import get_logger

logger = get_logger()


class CartPage:

    def __init__(self, page: Page):

        self.page = page

        self._checkout_btn = '[data-test="checkout"]'

    def checkout(self):

        logger.info("Clicking checkout button")

        self.page.click(self._checkout_btn)

        logger.info("Navigated to checkout page")
