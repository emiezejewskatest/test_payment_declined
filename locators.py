class HomePageLocators(object):
    X_ICON = 'cookie-popup__close'
    DEPARTURE = 'input[aria-labelledby="label-airport-selector-from"]'
    DESTINATION = 'input[aria-labelledby="label-airport-selector-to"]'
    CONTINUE_BUTTON = 'button[aria-controls="row-dates-pax row-discount"]'
    CALENDAR = 'calendar-view'
    SEARCH_BUTTON = "button[ng-click *= 'searchFlights']"


class FlightsPageLocators(object):
    FLIGHTS_TABLE_PRICE = "flights-table-price"
    PRICE_BUTTONS = "flights-table-price[on-select-fare *= 'onSelectFare']"
    CONTINUE_FLIGHTS_BUTTON = "button[id='continue']"


class SeatsPageLocators(object):
    SEAT = 'seat-click'
    CONFIRM_BUTTON = 'button[class *= "dialog-overlay-footer__ok-button"]'
    SEAT_MAP_PROMPT_CONTENT = 'seat-map-prompt-content'
    CHOOSE_OTHER_SEATS_BUTTON = 'core-btn-ghost'
    CONTINUE_SEATS_BUTTON = 'button[class *= "dialog-overlay-footer__ok-button"]'


class ExtrasPageLocators(object):
    PAY_BUTTON = 'button[ng-click *= "onContinueBtnClick"]'


class PaymentPageLocators(object):
    LOGIN_BUTTON = 'button[ui-sref = "login"]'
    TITLE = 'select[id *= "title"]'
    FIRST_NAME = 'input[id *= "firstName"]'
    LAST_NAME = 'input[id *= "lastName"]'
    CARD_NUMBER = 'input[id *= "cardNumber"]'
    EXPIRY_MONTH = 'select[name = "expiryMonth"]'
    EXPIRY_YEAR = 'select[name = "expiryYear"]'
    CVV = 'input[placeholder="CVV"]'
    CARD_HOLDER_NAME = 'input[name = "cardHolderName"]'
    CURRENCY = 'select[name = "currency"]'
    ADDRESS_LINE_1 = 'input[name = "billingAddressAddressLine1"]'
    ADDRESS_LINE_2 = 'input[name = "billingAddressAddressLine2"]'
    CITY = 'input[name = "billingAddressCity"]'
    POSTCODE = 'input[name = "billingAddressPostcode"]'
    TICK_ICON = '#checkout > div > form > div.main-area > div.core-card.available-step.after-pax-validation-step > ' \
                'div.body > div.cta > div > label > span > core-icon '
    PAYMENT_BUTTON = 'button[ng-click *= "processPayment"'
    PAYMENT_DECLINED_PROMPT = 'prompt[text-title="common.components.payment_forms.error_title"]'


class LoginPageLocators(object):
    E_MAIL = 'input[type = "email"]'
    PASSWORD = 'input[type = "password"]'
    SUBMIT_BUTTON = 'button[type = "submit"]'