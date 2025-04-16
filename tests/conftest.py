import allure
import pytest
import allure_commons
import os
import utils

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver

from selene import browser, support
from config.settings import settings


def init_app_session(options):
    with allure.step("Init app session"):
        browser.config.driver = webdriver.Remote(
            command_executor=settings.browserstack_url, options=options
        )
    browser.config.timeout = float(os.getenv("timeout", "20.0"))
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )


def tear_down_session():
    utils.attach_screenshot(browser)
    utils.attach_xml(browser)
    session_id = browser.driver.session_id

    with allure.step("Tear down app session"):
        browser.quit()

    utils.attach_bstack_video(session_id)


def base_capabilities(platform: str):
    bstack_opts = {
        "userName": settings.browserstack_username,
        "accessKey": settings.browserstack_access_key,
        "projectName": "Mobile Wikipedia Tests",
        "buildName": "browserstack-build-1",
        "sessionName": f"{platform.capitalize()} test",
    }

    return {
        "bstack:options": bstack_opts,
        "app": settings.app_url,
    }


@pytest.fixture(scope="function", params=["android", "ios"])
def mobile_management(request):
    platform = request.param
    capabilities = base_capabilities(platform)

    if platform == "android":
        capabilities.update(
            {
                "deviceName": settings.android_device_name,
                "platformName": "android",
                "platformVersion": settings.android_os_version,
                "appWaitActivity": "org.wikipedia.*",
            }
        )
        options = UiAutomator2Options().load_capabilities(capabilities)
    else:
        capabilities.update(
            {
                "deviceName": settings.ios_device_name,
                "platformName": "ios",
                "platformVersion": settings.ios_os_version,
            }
        )
        options = XCUITestOptions().load_capabilities(capabilities)

    init_app_session(options)
    yield platform
    tear_down_session()
