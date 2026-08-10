from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import TestData
from helpers import generate_email, generate_password
from locators import Locators


class TestLogin:

    def register_user(self, driver):
        email = generate_email()
        password = generate_password()

        driver.get(TestData.BASE_URL)

        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()

        driver.find_element(
            *Locators.REGISTER_NAME_INPUT
        ).send_keys(TestData.USER_NAME)

        driver.find_element(
            *Locators.REGISTER_EMAIL_INPUT
        ).send_keys(email)

        driver.find_element(
            *Locators.REGISTER_PASSWORD_INPUT
        ).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )

        return email, password

    def login(self, driver, email, password):
        driver.find_element(
            *Locators.LOGIN_EMAIL_INPUT
        ).send_keys(email)

        driver.find_element(
            *Locators.LOGIN_PASSWORD_INPUT
        ).send_keys(password)

        driver.find_element(*Locators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.CREATE_ORDER_BUTTON
            )
        )

        return order_button

    def test_login_from_main_page(self, driver):
        email, password = self.register_user(driver)

        driver.get(TestData.BASE_URL)
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()

        order_button = self.login(driver, email, password)

        assert order_button.is_displayed()

    def test_login_from_personal_account(self, driver):
        email, password = self.register_user(driver)

        driver.get(TestData.BASE_URL)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        order_button = self.login(driver, email, password)

        assert order_button.is_displayed()

    def test_login_from_registration_page(self, driver):
        email, password = self.register_user(driver)

        driver.get(TestData.BASE_URL)
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(
            *Locators.LOGIN_LINK_ON_REGISTRATION_PAGE
        ).click()

        order_button = self.login(driver, email, password)

        assert order_button.is_displayed()

    def test_login_from_password_recovery_page(self, driver):
        email, password = self.register_user(driver)

        driver.get(TestData.BASE_URL)
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.PASSWORD_RECOVERY_LINK).click()
        driver.find_element(
            *Locators.LOGIN_LINK_ON_PASSWORD_RECOVERY_PAGE
        ).click()

        order_button = self.login(driver, email, password)

        assert order_button.is_displayed()