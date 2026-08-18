from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestLogout:

    def test_logout_from_personal_account(
        self,
        driver,
        logged_in_user
    ):
        driver.find_element(
            *Locators.PERSONAL_ACCOUNT_LINK
        ).click()

        logout_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.LOGOUT_BUTTON
            )
        )

        logout_button.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.LOGIN_BUTTON
            )
        )

        assert login_button.is_displayed()