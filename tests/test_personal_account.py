from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import TestData
from helpers import generate_email, generate_password
from locators import Locators


class TestPersonalAccount:

    def register_and_login_user(self, driver):
        email = generate_email()
        password = generate_password()

        driver.get(TestData.BASE_URL)

        # Переход к регистрации
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()

        # Регистрация
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

        # Ожидание страницы входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )

        # Вход
        driver.find_element(
            *Locators.LOGIN_EMAIL_INPUT
        ).send_keys(email)

        driver.find_element(
            *Locators.LOGIN_PASSWORD_INPUT
        ).send_keys(password)

        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.CREATE_ORDER_BUTTON
            )
        )

    def open_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.PROFILE_LINK
            )
        )

    def test_click_personal_account_opens_profile(self, driver):
        self.register_and_login_user(driver)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        profile_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.PROFILE_LINK
            )
        )

        assert profile_link.is_displayed()

    def test_click_constructor_opens_constructor(self, driver):
        self.register_and_login_user(driver)
        self.open_personal_account(driver)

        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.CREATE_ORDER_BUTTON
            )
        )

        assert order_button.is_displayed()

    def test_click_logo_opens_constructor(self, driver):
        self.register_and_login_user(driver)
        self.open_personal_account(driver)

        driver.find_element(*Locators.LOGO_LINK).click()

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.CREATE_ORDER_BUTTON
            )
        )

        assert order_button.is_displayed()