from appium.webdriver.common.appiumby import AppiumBy

search_button_locators = {
    "android": (AppiumBy.ID, "org.wikipedia.alpha:id/search_container"),
    "ios": (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"),
}

search_input_locators = {
    "android": (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"),
    "ios": (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeSearchField"'),
}

search_result_locators = {
    "android": (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"),
    "ios": (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText"'),
}

skip_button_locators = {
    "android": (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button"),
    "ios": None,
}

popup_close_button = {
    "android": (AppiumBy.ID, "org.wikipedia.alpha:id/closeButton"),
    "ios": None,
}

article_title_locator = {
    "android": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BrowserStack")'),
    "ios": None,
}
