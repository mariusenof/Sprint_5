from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import TestData
from helpers import generate_email, generate_password
from locators import Locators


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(TestData.BASE_URL)

        # Переход на страницу входа
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()

        # Переход на страницу регистрации
        driver.find_element(*Locators.REGISTER_LINK).click()

        # Заполнение формы регистрации
        driver.find_element(*Locators.REGISTER_NAME_INPUT).send_keys(
            TestData.USER_NAME
        )
        driver.find_element(*Locators.REGISTER_EMAIL_INPUT).send_keys(
            generate_email()
        )
        driver.find_element(*Locators.REGISTER_PASSWORD_INPUT).send_keys(
            generate_password()
        )

        # Отправка формы
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # После успешной регистрации должна открыться форма входа
        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )

        assert login_button.is_displayed()

    def test_registration_with_short_password_shows_error(self, driver):
        driver.get(TestData.BASE_URL)

        # Переход на страницу регистрации
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()

        # Заполнение формы невалидным паролем
        driver.find_element(*Locators.REGISTER_NAME_INPUT).send_keys(
            TestData.USER_NAME
        )
        driver.find_element(*Locators.REGISTER_EMAIL_INPUT).send_keys(
            generate_email()
        )
        driver.find_element(*Locators.REGISTER_PASSWORD_INPUT).send_keys(
            TestData.INVALID_PASSWORD
        )

        # Отправка формы
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка сообщения об ошибке
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.INVALID_PASSWORD_ERROR
            )
        )

        assert error_message.text == 'Некорректный пароль'