from selenium.webdriver.common.by import By


class WebsiteLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    SERVICE_LOGO_BUTTON = (By.XPATH, ".//*[contains(@class, 'AppHeader_header__logo')]")
    ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    CONSTRUCTOR_HEADER = (By.XPATH, ".//*[text()='Соберите бургер']")

    BUNS_SECTION_INACTIVE = (By.XPATH, ".//span[text()='Булки']")
    SAUCES_SECTION_INACTIVE = (By.XPATH, ".//span[text()='Соусы']")
    STUFFINGS_SECTION_INACTIVE = (By.XPATH, ".//span[text()='Начинки']")

    BUNS_SECTION_ACTIVE = (
        By.XPATH,
        ".//span[text()='Булки']/ancestor::div[contains(@class, 'current')]",
    )
    SAUCES_SECTION_ACTIVE = (
        By.XPATH,
        ".//span[text()='Соусы']/ancestor::div[contains(@class, 'current')]",
    )
    STUFFINGS_SECTION_ACTIVE = (
        By.XPATH,
        ".//span[text()='Начинки']/ancestor::div[contains(@class, 'current')]",
    )

    LOGIN_INTO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    NAME_INPUT_FORM = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT_FORM = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT_FORM = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    REGISTRATION_BUTTON_FORM = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    LOGIN_TEXT_LINK = (By.XPATH, ".//a[text()='Войти']")
    LOGIN_BUTTON_FORM = (By.XPATH, ".//button[text()='Войти']")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, ".//p[text()='Некорректный пароль']")

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
