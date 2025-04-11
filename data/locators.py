from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_LOG_IN_LINK = (By.LINK_TEXT, 'Log In')
    SEARCH_INPUT_USER = (By.XPATH, "//*[@id='username']")
    SEARCH_LOGIN_BUTTON = (By.XPATH, "//*[@id='loginbutton']")
    SEARCH_INPUT_PASSWORD = (By.XPATH, "//*[@id='password']")