from selenium.webdriver.common.by import By


class Locators:
    # Главная страница
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

    # Вкладки конструктора
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

    # Форма входа
    LOGIN_EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    LOGIN_PASSWORD_INPUT = (
        By.XPATH,
        "//label[text()='Пароль']/following-sibling::input"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )

    # Ссылки на вход
    LOGIN_LINK_ON_REGISTRATION_PAGE = (
        By.XPATH,
        "//a[text()='Войти']"
    )

    LOGIN_LINK_ON_PASSWORD_RECOVERY_PAGE = (
        By.XPATH,
        "//a[text()='Войти']"
    )

    # Регистрация
    REGISTER_LINK = (
        By.XPATH,
        "//a[text()='Зарегистрироваться']"
    )

    REGISTER_NAME_INPUT = (
        By.XPATH,
        "//label[text()='Имя']/following-sibling::input"
    )

    REGISTER_EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    REGISTER_PASSWORD_INPUT = (
        By.XPATH,
        "//label[text()='Пароль']/following-sibling::input"
    )

    REGISTER_BUTTON = (
        By.XPATH,
        "//button[text()='Зарегистрироваться']"
    )

    INVALID_PASSWORD_ERROR = (
        By.XPATH,
        "//p[text()='Некорректный пароль']"
    )

    # Восстановление пароля
    PASSWORD_RECOVERY_LINK = (
        By.XPATH,
        "//a[text()='Восстановить пароль']"
    )

    # Личный кабинет
    PROFILE_LINK = (
        By.XPATH,
        "//a[text()='Профиль']"
    )

    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[text()='Выход']"
    )