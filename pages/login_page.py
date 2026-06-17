from playwright.sync_api import Page
from logger import get_logger

logger = get_logger()


class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        self.username_txt = '//div[@class="form_group"]/input[@type="text"]'
        self.password_txt = '//div[@class="form_group"]/input[@type="password"]'
        self.login_btn = "#login-button"

    def navigate(self):

        logger.info("Navigating to SauceDemo Website")

        self.page.goto("https://www.saucedemo.com")

        logger.info("Website Loaded Successfully")

    def enter_username(self, username):

        logger.info(f"Entering Username: {username}")

        self.page.locator(self.username_txt).fill(username)

        logger.info("Username Entered Successfully")

    def enter_password(self, password):

        logger.info("Entering Password")

        self.page.locator(self.password_txt).fill(password)

        logger.info("Password Entered Successfully")

    def click_login(self):

        logger.info("Clicking Login Button")

        self.page.locator(self.login_btn).click()

        logger.info("Login Button Clicked")

    def login(self, username, password):

        logger.info("Starting Login Process")

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()

        logger.info("Login Process Completed")