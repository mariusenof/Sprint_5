from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestPersonalAccount:

    def open_personal_account(self, driver):
        driver.find_element(
            *Locators.PERSONAL_ACCOUNT_LINK
        ).click()

        return WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.PROFILE_LINK
            )
        )

    def test_click_personal_account_opens_profile(
        self,
        driver,
        logged_in_user
    ):
        profile_link = self.open_personal_account(driver)

        assert profile_link.is_displayed()

    def test_click_constructor_opens_constructor(
        self,
        driver,
        logged_in_user
    ):
        self.open_personal_account(driver)

        driver.find_element(
            *Locators.CONSTRUCTOR_LINK
        ).click()

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.CREATE_ORDER_BUTTON
            )
        )

        assert order_button.is_displayed()

    def test_click_logo_opens_constructor(
        self,
        driver,
        logged_in_user
    ):
        self.open_personal_account(driver)

        driver.find_element(
            *Locators.LOGO_LINK
        ).click()

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.CREATE_ORDER_BUTTON
            )
        )

        assert order_button.is_displayed()