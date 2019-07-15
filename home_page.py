import base_page


class HomePage(base_page.BasePage):

    def click_first_available_day(self, departure_index=-1):
        all_days = self.driver.find_elements_by_css_selector('ul.days > *')
        unavailable_days = self.driver.find_elements_by_class_name('unavailable')
        available_day_found = False
        for index, day in enumerate(all_days):
            if day not in unavailable_days and index != departure_index:
                day.click()
                available_day_found = True
                break
        if not available_day_found:
            raise Exception('No available day found')
        return index
