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
