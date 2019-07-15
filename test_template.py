import unittest
from base_page import BasePage
from flights_page import FlightsPage
from seats_page import SeatsPage
from test_user import TestUser
from home_page import HomePage
from locators import HomePageLocators, FlightsPageLocators, SeatsPageLocators, ExtrasPageLocators, PaymentPageLocators,\
    LoginPageLocators
from selenium import webdriver
from webdrivermanager import ChromeDriverManager


class TestTemplate(unittest.TestCase):

    def setUp(self):
        paths = ChromeDriverManager().download_and_install()
        self.driver = webdriver.Chrome(paths[0])

        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.flights_page = FlightsPage(self.driver)
        self.seats_page = SeatsPage(self.driver)
        self.home_page_locators = HomePageLocators()
        self.flights_page_locators = FlightsPageLocators()
        self.seats_page_locators = SeatsPageLocators()
        self.extras_page_locators = ExtrasPageLocators()
        self.payment_page_locators = PaymentPageLocators()
        self.login_page_locators = LoginPageLocators()
        self.test_user = TestUser()

        self.driver.maximize_window()
        self.driver.get('http://ryanair.com')

    def tearDown(self):
        self.driver.quit()
