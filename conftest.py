import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import TestData
from helpers import generate_email, generate_password
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture
def registered_user(driver):
    email = generate_email()
    password = generate_password()

    driver.get(TestData.BASE_URL)

    driver.find_element(
        *Locators.LOGIN_ACCOUNT_BUTTON
    ).click()

    driver.find_element(
        *Locators.REGISTER_LINK
    ).click()

    driver.find_element(
        *Locators.REGISTER_NAME_INPUT
    ).send_keys(TestData.USER_NAME)

    driver.find_element(
        *Locators.REGISTER_EMAIL_INPUT
    ).send_keys(email)

    driver.find_element(
        *Locators.REGISTER_PASSWORD_INPUT
    ).send_keys(password)

    driver.find_element(
        *Locators.REGISTER_BUTTON
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            Locators.LOGIN_BUTTON
        )
    )

    return {
        'email': email,
        'password': password
    }


@pytest.fixture
def login_user(driver):
    def login(email, password):
        driver.find_element(
            *Locators.LOGIN_EMAIL_INPUT
        ).send_keys(email)

        driver.find_element(
            *Locators.LOGIN_PASSWORD_INPUT
        ).send_keys(password)

        driver.find_element(
            *Locators.LOGIN_BUTTON
        ).click()

        return WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Locators.CREATE_ORDER_BUTTON
            )
        )

    return login


@pytest.fixture
def logged_in_user(driver, registered_user, login_user):
    login_user(
        registered_user['email'],
        registered_user['password']
    )

    return registered_user