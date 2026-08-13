from selenium.webdriver.common.by import By


class Locators:
    LOGIN_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[text()='Войти в аккаунт']"
    )

    PERSONAL_ACCOUNT_LINK = (
        By.XPATH,
        "//p[text()='Личный Кабинет']"
    )

    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//p[text()='Конструктор']"
    )

    LOGO_LINK = (
        By.XPATH,
        "//header//a[@href='/']"
    )

    CREATE_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )

    BUNS_TAB = (
        By.XPATH,
        "//span[text()='Булки']/parent::div"
    )

    SAUCES_TAB = (
        By.XPATH,
        "//span[text()='Соусы']/parent::div"
    )

    FILLINGS_TAB = (
        By.XPATH,
        "//span[text()='Начинки']/parent::div"
    )

    LOGIN_EMAIL_INPUT = (
        By.XPATH,
        "//h2[text()='Вход']/following::form[1]"
        "//label[text()='Email']/following-sibling::input"
    )

    LOGIN_PASSWORD_INPUT = (
        By.XPATH,
        "//h2[text()='Вход']/following::form[1]"
        "//label[text()='Пароль']/following-sibling::input"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//h2[text()='Вход']/following::form[1]"
        "//button[text()='Войти']"
    )

    REGISTER_LINK = (
        By.XPATH,
        "//a[text()='Зарегистрироваться']"
    )

    REGISTER_NAME_INPUT = (
        By.XPATH,
        "//h2[text()='Регистрация']/following::form[1]"
        "//label[text()='Имя']/following-sibling::input"
    )

    REGISTER_EMAIL_INPUT = (
        By.XPATH,
        "//h2[text()='Регистрация']/following::form[1]"
        "//label[text()='Email']/following-sibling::input"
    )

    REGISTER_PASSWORD_INPUT = (
        By.XPATH,
        "//h2[text()='Регистрация']/following::form[1]"
        "//label[text()='Пароль']/following-sibling::input"
    )

    REGISTER_BUTTON = (
        By.XPATH,
        "//h2[text()='Регистрация']/following::form[1]"
        "//button[text()='Зарегистрироваться']"
    )

    LOGIN_LINK_ON_REGISTRATION_PAGE = (
        By.XPATH,
        "//h2[text()='Регистрация']/following::a[text()='Войти'][1]"
    )

    INVALID_PASSWORD_ERROR = (
        By.XPATH,
        "//p[text()='Некорректный пароль']"
    )

    PASSWORD_RECOVERY_LINK = (
        By.XPATH,
        "//a[text()='Восстановить пароль']"
    )

    LOGIN_LINK_ON_PASSWORD_RECOVERY_PAGE = (
        By.XPATH,
        "//h2[text()='Восстановление пароля']"
        "/following::a[text()='Войти'][1]"
    )

    PROFILE_LINK = (
        By.XPATH,
        "//a[text()='Профиль']"
    )

    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[text()='Выход']"
    )