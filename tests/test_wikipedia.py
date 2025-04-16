import pytest
import allure
from helpers import tap_and_verify
from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy
from locators import (
    article_title_locator,
    onboarding_locators,
    popup_close_button,
    skip_button_locators,
    search_button_locators,
    search_input_locators,
    search_result_locators,
)


@allure.title("Search for 'Selenium' and verify results appear")
def test_check_search_functionality(setup_app):
    platform = setup_app

    with allure.step("Skip welcome screen if visible"):
        skip_button = browser.element(skip_button_locators[platform])
        if skip_button.matching(be.visible):
            skip_button.click()

    with allure.step("Click on the search button"):
        browser.element(search_button_locators[platform]).click()

    with allure.step("Type 'Selenium' into search input"):
        browser.element(search_input_locators[platform]).type("Selenium")

    with allure.step("Verify that search results are present and correct"):
        results = browser.all(search_result_locators[platform])
        results.should(have.size_greater_than(0))
        results.first.should(have.text("Selenium"))


@allure.title("Search for 'BrowserStack' and open article")
def test_check_that_search_result_can_be_opened(setup_app):
    platform = setup_app

    with allure.step("Skip welcome screen if visible"):
        skip_button = browser.element(skip_button_locators[platform])
        if skip_button.matching(be.visible):
            skip_button.click()

    with allure.step("Search for 'BrowserStack'"):
        browser.element(search_button_locators[platform]).click()
        browser.element(search_input_locators[platform]).type("BrowserStack")
        results = browser.all(search_result_locators[platform])

    with allure.step("Click on the first result"):
        results.first.click()

    with allure.step("Close 'Wikipedia games' popup if visible"):
        popup_close = browser.element(popup_close_button[platform])
        if popup_close.wait_until(be.present) and popup_close.matching(be.visible):
            popup_close.click()

    with allure.step("Verify article is opened"):
        browser.element(article_title_locator[platform]).should(be.visible)


@allure.title("Complete onboarding flow by skipping all 4 screens")
def test_onboarding_flow(setup_app):
    platform = setup_app

    tap_and_verify(
        platform,
        onboarding_locators["continue"],
        "Check first onboarding screen and tap 'Continue'",
    )
    tap_and_verify(
        platform,
        onboarding_locators["continue"],
        "Check second onboarding screen and tap 'Continue'",
    )
    tap_and_verify(
        platform,
        onboarding_locators["continue"],
        "Check third onboarding screen and tap 'Continue'",
    )
    tap_and_verify(
        platform,
        onboarding_locators["get_started"],
        "Check fourth onboarding screen and tap 'Get Started'",
    )
