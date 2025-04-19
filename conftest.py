import os
import pytest
from pathlib import Path

from appium.options.android import UiAutomator2Options
from selene import browser
from appium import webdriver

from config.config import config, credentials
from utils.allure_attachments import (
    attach_screenshot,
    attach_page_source,
    attach_bstack_video,
)

CONTEXT = os.getenv("CONTEXT", "local_emulator")
IS_BSTACK = CONTEXT == "bstack"


@pytest.fixture(scope="function")
def setup_app():
    options = UiAutomator2Options()
    options.platform_name = config.platformName
    options.device_name = config.deviceName
    options.app = config.app if IS_BSTACK else str(Path(config.app).absolute())

    if config.platformVersion:
        options.platform_version = config.platformVersion
    if not IS_BSTACK:
        options.app_wait_activity = config.appWaitActivity

    if IS_BSTACK:
        bstack_opts = {
            "userName": credentials.BSTACK_USERNAME,
            "accessKey": credentials.BSTACK_ACCESS_KEY,
        }
        if config.appiumVersion:
            bstack_opts["appiumVersion"] = config.appiumVersion
        options.set_capability("bstack:options", bstack_opts)

    browser.config.driver = webdriver.Remote(config.remote_url, options=options)
    browser.config.timeout = 10

    yield config.platformName.lower()

    if IS_BSTACK:
        attach_screenshot(browser)
        attach_page_source(browser)
        attach_bstack_video(browser.driver.session_id)

    browser.quit()
