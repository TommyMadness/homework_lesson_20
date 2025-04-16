import allure
import requests
from config.settings import settings


def attach_data(name: str, data: str | bytes, type_: allure.attachment_type):
    allure.attach(data, name=name, attachment_type=type_)


def attach_screenshot(browser):
    attach_data(
        name="screenshot",
        data=browser.driver.get_screenshot_as_png(),
        type_=allure.attachment_type.PNG,
    )


def attach_xml(browser):
    attach_data(
        name="screen xml dump",
        data=browser.driver.page_source,
        type_=allure.attachment_type.XML,
    )


def fetch_bstack_session(session_id: str) -> dict:
    return requests.get(
        f"https://api.browserstack.com/app-automate/sessions/{session_id}.json",
        auth=(settings.browserstack_username, settings.browserstack_access_key),
    ).json()


def attach_bstack_video(session_id: str):
    video_url = fetch_bstack_session(session_id)["automation_session"]["video_url"]
    html = (
        "<html><body>"
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        "</video></body></html>"
    )
    attach_data("video recording", html, allure.attachment_type.HTML)
