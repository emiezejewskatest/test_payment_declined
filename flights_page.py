import time

from base_page import BasePage


class FlightsPage(BasePage):

    def pick_one_fare_for_both_flights(self, valid_price_buttons):
        fare_selector = "div[ng-repeat *= 'fares track by"
        for button in valid_price_buttons:
            button.click()
            time.sleep(2)
            fare = self.driver.find_elements_by_css_selector(fare_selector)
            fare[2].click()
            time.sleep(2)