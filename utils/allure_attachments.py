import allure
import requests

from config.config import credentials


def attach_screenshot(browser):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )


def attach_page_source(browser):
    allure.attach(
        browser.driver.page_source,
        name="Page Source",
        attachment_type=allure.attachment_type.XML,
    )


def attach_bstack_video(session_id: str):
    response = requests.get(
        f"https://api.browserstack.com/app-automate/sessions/{session_id}.json",
        auth=(credentials.BSTACK_USERNAME, credentials.BSTACK_ACCESS_KEY),
    )
    response.raise_for_status()
    data = response.json()
    video_url = data["automation_session"]["video_url"]

    html = (
        "<html><body>"
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        "</video>"
        "</body></html>"
    )
    allure.attach(
        html,
        name="BrowserStack Session Video",
        attachment_type=allure.attachment_type.HTML,
    )


def attach_local_video(raw_video: str):
    html = (
        "<html><body>"
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="data:video/mp4;base64,{raw_video}" type="video/mp4">'
        "</video>"
        "</body></html>"
    )
    allure.attach(
        html,
        name="Local Session Video",
        attachment_type=allure.attachment_type.HTML,
    )
