import logging
import os


def get_logger():

    log_folder = "logs"

    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    logger = logging.getLogger("PlaywrightFramework")

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            "logs/test_execution.log"
        )
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger