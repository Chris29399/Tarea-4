from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import SearchPageLocators


class SearchPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.url = "https://www.deviantart.com"
        self.locator = SearchPageLocators

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def make_a_login_pass(self, input_user, input_password):
        self.driver.find_element(*self.locator.SEARCH_LOG_IN_LINK).click()
        self.driver.save_screenshot("results/log_in_user.png")
        self.driver.find_element(*self.locator.SEARCH_INPUT_USER).send_keys(input_user)
        self.driver.save_screenshot("results/input_user.png")
        self.driver.find_element(*self.locator.SEARCH_LOGIN_BUTTON).click()
        self.driver.save_screenshot("results/log_in_password.png")
        self.driver.find_element(*self.locator.SEARCH_INPUT_PASSWORD).send_keys(input_password)
        self.driver.save_screenshot("results/input_password.png")
        self.driver.find_element(*self.locator.SEARCH_LOGIN_BUTTON).click()
        self.driver.save_screenshot("results/login_pass.png")


