import allure
from selene import browser, be


def tap_and_verify(platform, locator, step_title):
    with allure.step(step_title):
        browser.element(locator[platform]).should(be.visible).click()
