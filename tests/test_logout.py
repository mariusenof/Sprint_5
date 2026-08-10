from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import TestData
from helpers import generate_email, generate_password
from locators import Locators


class TestLogout:

    def register_and_login_user(self, driver):
        email = generate_email()
        password = generate_password()

        driver.get(TestData.BASE_URL)

        # Регистрация
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

    def test_logout_from_personal_account(self, driver):
        self.register_and_login_user(driver)

        # Переход в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.LOGOUT_BUTTON
            )
        )

        # Выход из аккаунта
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.LOGIN_BUTTON
            )
        )

        assert login_button.is_displayed()