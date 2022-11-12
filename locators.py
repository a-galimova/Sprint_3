REGISTRATION_FORM_NAME_INPUT = ".//div/label[text()='Имя']/parent::div/input"  # Поле ввода имени в форме регистрации
REGISTRATION_FORM_EMAIL_INPUT = ".//div/label[text()='Email']/parent::div/input"  # Поле ввода email в форме регистрации
REGISTRATION_FORM_EMAIL_PASSWORD = ".//div/label[text()='Пароль']/parent::div/input"  # Поле ввода пароля в форме регистрации
REGISTRATION_FORM_BUTTON = ".//button[text()='Зарегистрироваться']"  # Кнопка зарегистрироваться на форме регистрации
REGISTRATION_FORM_ERROR_MESSAGE = ".//p[@class='input__error text_type_main-default']"  # Ошибка регистрации на форме регистрации

LOGIN_FORM_HEADER = ".//h2[text()='Вход']"  # Заголовок страницы логина
LOGIN_FORM_EMAIL_INPUT = ".//input[@type='text']"  # Поле ввода email на странице логина
LOGIN_FORM_PASSWORD_INPUT = ".//input[@type='password']"  # Поле ввода пароля на странице логина
LOGIN_PAGE_LOGIN_BUTTON = ".//button[text()='Войти']"  # Кнопка логина на странице логина

MAIN_PAGE_LOGIN_BUTTON = ".//button[text()='Войти в аккаунт']"  # Кнопка логина на главной странице
MAIN_PAGE_ORDER_BUTTON = ".//button[text()='Оформить заказ']"  # Кнопка заказа на главной странице

ACCOUNT_PAGE_SAVE_BUTTON = ".//button[text()='Сохранить']"  # Кнопка сохранить на странице личного кабинет
ACCOUNT_LOG_OUT_BUTTON = ".//button[text()='Выход']"  # Кнопка выхода на странице личного кабинет

CONSTRUCTOR_PAGE_BUN_BUTTON = ".//span[text()='Булки']"  # Кнопка выбора булок на странице конструктора
CONSTRUCTOR_PAGE_SPICY_SAUCE_IMG = ".//img[@alt='Соус Spicy-X']"  # Картинка спайси соуса на странице конструктора
CONSTRUCTOR_PAGE_BUN_IMG = ".//img[@alt='Флюоресцентная булка R2-D3']"  # Картинка булки на странице конструктора
CONSTRUCTOR_PAGE_FILLING_IMG = ".//img[@alt='Мясо бессмертных моллюсков Protostomia']"  # Картинка начинки на странице конструктора
CONSTRUCTOR_PAGE_BUN_DIV = ".//div/span[text()='Булки']/parent::div"  # Блок выбора булок на странице конструктора
CONSTRUCTOR_PAGE_SAUCE_DIV = ".//div/span[text()='Соусы']/parent::div"  # Блок выбора соусов на странице конструктора
CONSTRUCTOR_PAGE_FILLING_DIV = ".//div/span[text()='Начинки']/parent::div"  # Блок выбора начинок на странице конструктора
CONSTRUCTOR_PAGE_SELECTED_INGREDIENT = ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span"  # Выбранный Блок ингредиентов на странице конструктора

