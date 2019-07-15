from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element_and_click(self, selector):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        button = self.driver.find_element_by_css_selector(selector)
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        return button

    def click_element_and_type_text(self, selector, text):
        button = self.wait_for_element_and_click(selector)
        button.send_keys(text)

    def tear_down(self):
        self.driver.quit()
