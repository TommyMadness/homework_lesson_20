import allure
from selene import browser


def attach_screenshot(browser):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=allure.attachment_type.PNG,
    )


def attach_page_source(browser):
    allure.attach(
        browser.driver.page_source,
        name="page source",
        attachment_type=allure.attachment_type.XML,
    )


def attach_bstack_video(session_id: str):
    video_url = f"https://app-automate.browserstack.com/sessions/{session_id}.mp4"
    allure.attach(
        video_url,
        name="BrowserStack session video",
        attachment_type=allure.attachment_type.URI_LIST,
    )
