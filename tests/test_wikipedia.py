import pytest
import allure
from appium.webdriver.common.appiumby import AppiumBy
from locators import (
    search_button_locators,
    search_input_locators,
    search_result_locators,
)
from selene import browser, have, be


@allure.title("Search for 'Selenium' and verify results appear")
def test_check_search_functionality(mobile_management):
    with allure.step("Skip iOS app if not Wikipedia"):
        platform = mobile_management
        if platform == "ios":
            pytest.skip("iOS app is not Wikipedia, skipping test.")

    with allure.step("Click on the search button"):
        browser.element(search_button_locators[platform]).click()

    with allure.step("Type 'Selenium' into search input"):
        browser.element(search_input_locators[platform]).type("Selenium")
        results = browser.all(search_result_locators[platform])

    with allure.step("Check that search results are present and correct"):
        results.should(have.size_greater_than(0))
        results.first.should(have.text("Selenium"))


@allure.title("Search for 'BrowserStack' and open article")
def test_check_that_search_result_can_be_opened(mobile_management):
    with allure.step("Skip iOS app if not Wikipedia"):
        platform = mobile_management
        if platform == "ios":
            pytest.skip("iOS app is not Wikipedia, skipping test.")

    with allure.step("Search for 'BrowserStack'"):
        browser.element(search_button_locators[platform]).click()
        browser.element(search_input_locators[platform]).type("BrowserStack")
        results = browser.all(search_result_locators[platform])

    with allure.step("Click on the first result"):
        results.first.click()

    with allure.step("Verify article is opened"):
        browser.element(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BrowserStack")')
        ).should(be.visible)
