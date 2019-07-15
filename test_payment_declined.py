import time
import unittest
import xmlrunner

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from test_template import TestTemplate


class TestDeclinedPayment(TestTemplate):

    def test_declined_payment(self):
        x = self.driver.find_element_by_class_name(self.home_page_locators.X_ICON)
        ActionChains(self.driver).move_to_element(x).click(x).perform()
        self.base_page.click_element_and_type_text(self.home_page_locators.DEPARTURE, self.test_user.DEPARTURE_CITY)
        self.base_page.click_element_and_type_text(self.home_page_locators.DESTINATION, self.test_user.DESTINATION_CITY)
        self.base_page.wait_for_element_and_click(self.home_page_locators.CONTINUE_BUTTON)
        calendar = self.driver.find_element_by_class_name(self.home_page_locators.CALENDAR)
        self.driver.execute_script("arguments[0].scrollIntoView();", calendar)
        self.base_page.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.home_page_locators.CALENDAR)))
        index = self.home_page.click_first_available_day()
        self.base_page.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.home_page_locators.CALENDAR)))
        self.home_page.click_first_available_day(index)
        self.base_page.wait_for_element_and_click(self.home_page_locators.SEARCH_BUTTON)
        self.base_page.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, self.flights_page_locators.FLIGHTS_TABLE_PRICE)))
        price_buttons = self.driver.find_elements_by_css_selector(self.flights_page_locators.PRICE_BUTTONS)
        valid_price_buttons = []
        for button in price_buttons:
            if button.size['width'] > 0:
                valid_price_buttons.append(button)
        if len(valid_price_buttons) != 2:
            raise Exception("Didn't found proper value of price buttons")
        self.flights_page.pick_one_fare_for_both_flights(valid_price_buttons)
        self.base_page.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.flights_page_locators.CONTINUE_FLIGHTS_BUTTON)))
        self.base_page.wait_for_element_and_click(self.flights_page_locators.CONTINUE_FLIGHTS_BUTTON)
        self.seats_page.choose_first_available_seat()
        try:
            self.base_page.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, self.seats_page_locators.SEAT_MAP_PROMPT_CONTENT)))
            self.driver.find_element_by_class_name(self.seats_page_locators.CHOOSE_OTHER_SEATS_BUTTON).click()
        except TimeoutException:
            pass  # There wasn't the same place available for second flight
        self.seats_page.choose_first_available_seat()
        time.sleep(2)
        self.base_page.wait_for_element_and_click(self.seats_page_locators.CONTINUE_SEATS_BUTTON)
        time.sleep(1)
        self.base_page.wait_for_element_and_click(self.extras_page_locators.PAY_BUTTON)
        self.base_page.wait_for_element_and_click(self.payment_page_locators.LOGIN_BUTTON)
        self.base_page.click_element_and_type_text(self.login_page_locators.E_MAIL, self.test_user.LOGIN)
        self.base_page.click_element_and_type_text(self.login_page_locators.PASSWORD, self.test_user.PASS)
        self.base_page.wait_for_element_and_click(self.login_page_locators.SUBMIT_BUTTON)
        self.seats_page.choose_first_option_in_select_popup(self.payment_page_locators.TITLE)
        self.base_page.click_element_and_type_text(self.payment_page_locators.FIRST_NAME, self.test_user.FIRST_NAME)
        self.base_page.click_element_and_type_text(self.payment_page_locators.LAST_NAME, self.test_user.LAST_NAME)
        self.base_page.click_element_and_type_text(self.payment_page_locators.CARD_NUMBER, self.test_user.CARD_NUMBER)
        self.seats_page.choose_first_option_in_select_popup(self.payment_page_locators.EXPIRY_MONTH)
        self.seats_page.choose_first_option_in_select_popup(self.payment_page_locators.EXPIRY_YEAR)
        self.base_page.click_element_and_type_text(self.payment_page_locators.CVV, self.test_user.CVV)
        self.base_page.click_element_and_type_text(
            self.payment_page_locators.CARD_HOLDER_NAME, self.test_user.CARD_HOLDER_NAME)
        self.seats_page.choose_first_option_in_select_popup(self.payment_page_locators.CURRENCY)
        self.base_page.click_element_and_type_text(
            self.payment_page_locators.ADDRESS_LINE_1, self.test_user.TEST_ADDRESS_1)
        self.base_page.click_element_and_type_text(
            self.payment_page_locators.ADDRESS_LINE_2, self.test_user.TEST_ADDRESS_2)
        self.base_page.click_element_and_type_text(self.payment_page_locators.CITY, self.test_user.CITY)
        self.base_page.click_element_and_type_text(self.payment_page_locators.POSTCODE, self.test_user.POSTCODE)
        self.base_page.wait_for_element_and_click(self.payment_page_locators.TICK_ICON)
        self.base_page.wait_for_element_and_click(self.payment_page_locators.PAYMENT_BUTTON)
        self.base_page.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, self.payment_page_locators.PAYMENT_DECLINED_PROMPT)))


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='./reports'))
