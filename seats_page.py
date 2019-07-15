import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from base_page import BasePage
from locators import SeatsPageLocators


class SeatsPage(BasePage):

    def __init__(self, driver):
        self.seats_page_locators = SeatsPageLocators()
        super().__init__(driver)

    def choose_first_available_seat(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.seats_page_locators.SEAT)))
        time.sleep(1)
        button = self.driver.find_element_by_class_name(self.seats_page_locators.SEAT)
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.seats_page_locators.CONFIRM_BUTTON)))
        button = self.driver.find_element_by_css_selector(self.seats_page_locators.CONFIRM_BUTTON)
        ActionChains(self.driver).move_to_element(button).click(button).perform()

    def choose_first_option_in_select_popup(self, selector):
        element = self.wait_for_element_and_click(selector)
        # time.sleep(1)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)
