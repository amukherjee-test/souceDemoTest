from playwright.sync_api import Page
from logger import get_logger

logger = get_logger()


class CheckoutPage:

    def __init__(self, page: Page):

        self.page = page

        self._first_name = '[data-test="firstName"]'
        self._last_name = '[data-test="lastName"]'
        self._postal_code = '[data-test="postalCode"]'
        self._continue_btn = '[data-test="continue"]'
        self._finish_btn = '[data-test="finish"]'

    def fill_info(self, first_name, last_name, postal_code):

        logger.info("Filling checkout information")

        self.page.fill(self._first_name, first_name)
        self.page.fill(self._last_name, last_name)
        self.page.fill(self._postal_code, postal_code)

        logger.info("Checkout info filled successfully")

    def continue_checkout(self):

        logger.info("Clicking continue button")

        self.page.click(self._continue_btn)

    def finish(self):

        logger.info("Clicking finish button")

        self.page.click(self._finish_btn)

        logger.info("Order completed successfully")
