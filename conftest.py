import pytest
import os
import allure
from pathlib import Path
from selene import browser, config as selene_config
from appium import webdriver
from config.config import config
from utils.allure_attachments import (
    attach_screenshot,
    attach_page_source,
    attach_bstack_video,
)

IS_BSTACK = config.remote_url.startswith("http")


@pytest.fixture(scope="function")
def setup_app():
    options = {
        "platformName": config.platformName,
        "deviceName": config.deviceName,
        "app": str(Path(config.app).absolute()),
        "appWaitActivity": config.appWaitActivity,
    }
    if config.platformVersion:
        options["platformVersion"] = config.platformVersion

    selene_config.driver = webdriver.Remote(config.remote_url, options)
    selene_config.timeout = 10

    yield config.platformName.lower()

    if IS_BSTACK:
        attach_screenshot(browser)
        attach_page_source(browser)
        attach_bstack_video(browser.driver.session_id)

    browser.quit()
