from playwright.sync_api import Page
from logger import get_logger

logger = get_logger()


class LoginPage:

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):

        self.page = page

        self._username = 'input[data-test="username"]'
        self._password = 'input[data-test="password"]'
        self._login_btn = 'input[data-test="login-button"]'
        self._error_msg = '[data-test="error"]'

    def navigate(self):

        logger.info("Navigating to SauceDemo Website")

        self.page.goto(self.URL)

        logger.info("Website Loaded Successfully")

    def login(self, username, password):

        logger.info(f"Logging in as: {username}")

        self.page.fill(self._username, username)
        self.page.fill(self._password, password)
        self.page.click(self._login_btn)

        logger.info("Login submitted")

    def get_error_message(self):

        text = self.page.locator(self._error_msg).inner_text()
        logger.info(f"Error message: {text}")
        return text

    def is_login_page_visible(self):

        return self.page.locator(self._login_btn).is_visible()