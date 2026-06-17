import pytest
from playwright.sync_api import sync_playwright
from logger import get_logger

logger = get_logger()


@pytest.fixture(scope="function")
def page():

    logger.info("========== Test Started ==========")

    logger.info("Starting Playwright")

    playwright = sync_playwright().start()

    logger.info("Launching Chromium Browser")

    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=500
    )

    logger.info("Creating Browser Context")

    context = browser.new_context()

    logger.info("Opening New Page")

    page = context.new_page()

    yield page

    logger.info("Closing Browser Context")
    context.close()

    logger.info("Closing Browser")
    browser.close()

    logger.info("Stopping Playwright")
    playwright.stop()

    logger.info("========== Test Finished ==========")