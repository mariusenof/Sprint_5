from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import TestData
from locators import Locators


class TestConstructor:

    def test_click_sauces_opens_sauces_section(self, driver):
        driver.get(TestData.BASE_URL)

        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCES_TAB)
        )
        sauces_tab.click()

        WebDriverWait(driver, 10).until(
            lambda browser:
            'tab_tab_type_current' in browser.find_element(
                *Locators.SAUCES_TAB
            ).get_attribute('class')
        )

        assert 'tab_tab_type_current' in driver.find_element(
            *Locators.SAUCES_TAB
        ).get_attribute('class')

    def test_click_fillings_opens_fillings_section(self, driver):
        driver.get(TestData.BASE_URL)

        fillings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.FILLINGS_TAB)
        )
        fillings_tab.click()

        WebDriverWait(driver, 10).until(
            lambda browser:
            'tab_tab_type_current' in browser.find_element(
                *Locators.FILLINGS_TAB
            ).get_attribute('class')
        )

        assert 'tab_tab_type_current' in driver.find_element(
            *Locators.FILLINGS_TAB
        ).get_attribute('class')

    def test_click_buns_opens_buns_section(self, driver):
        driver.get(TestData.BASE_URL)

        # Сначала переходим в другой раздел,
        # потому что «Булки» открыты по умолчанию
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCES_TAB)
        )
        sauces_tab.click()

        WebDriverWait(driver, 10).until(
            lambda browser:
            'tab_tab_type_current' in browser.find_element(
                *Locators.SAUCES_TAB
            ).get_attribute('class')
        )

        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUNS_TAB)
        )
        buns_tab.click()

        WebDriverWait(driver, 10).until(
            lambda browser:
            'tab_tab_type_current' in browser.find_element(
                *Locators.BUNS_TAB
            ).get_attribute('class')
        )

        assert 'tab_tab_type_current' in driver.find_element(
            *Locators.BUNS_TAB
        ).get_attribute('class')