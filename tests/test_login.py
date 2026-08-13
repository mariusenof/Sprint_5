from data import TestData
from locators import Locators


class TestLogin:

    def test_login_from_main_page(
        self,
        driver,
        registered_user,
        login_user
    ):
        driver.get(TestData.BASE_URL)

        driver.find_element(
            *Locators.LOGIN_ACCOUNT_BUTTON
        ).click()

        order_button = login_user(
            registered_user['email'],
            registered_user['password']
        )

        assert order_button.is_displayed()

    def test_login_from_personal_account(
        self,
        driver,
        registered_user,
        login_user
    ):
        driver.get(TestData.BASE_URL)

        driver.find_element(
            *Locators.PERSONAL_ACCOUNT_LINK
        ).click()

        order_button = login_user(
            registered_user['email'],
            registered_user['password']
        )

        assert order_button.is_displayed()

    def test_login_from_registration_page(
        self,
        driver,
        registered_user,
        login_user
    ):
        driver.get(TestData.BASE_URL)

        driver.find_element(
            *Locators.LOGIN_ACCOUNT_BUTTON
        ).click()

        driver.find_element(
            *Locators.REGISTER_LINK
        ).click()

        driver.find_element(
            *Locators.LOGIN_LINK_ON_REGISTRATION_PAGE
        ).click()

        order_button = login_user(
            registered_user['email'],
            registered_user['password']
        )

        assert order_button.is_displayed()

    def test_login_from_password_recovery_page(
        self,
        driver,
        registered_user,
        login_user
    ):
        driver.get(TestData.BASE_URL)

        driver.find_element(
            *Locators.LOGIN_ACCOUNT_BUTTON
        ).click()

        driver.find_element(
            *Locators.PASSWORD_RECOVERY_LINK
        ).click()

        driver.find_element(
            *Locators.LOGIN_LINK_ON_PASSWORD_RECOVERY_PAGE
        ).click()

        order_button = login_user(
            registered_user['email'],
            registered_user['password']
        )

        assert order_button.is_displayed()