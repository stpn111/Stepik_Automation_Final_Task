from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, "login_form")
    BASKET_BUTTON = (By.XPATH, '//span/a[contains(@href, "/basket/")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.XPATH, '//div[@class="content"]/div[2]/p')
    BASKET_LIST_OF_ITEMS = (By.XPATH, '//div[@class="basket-title hidden-xs"]/div/h2')


class LoginPageLocators:

    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    REPEAT = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    BASKET = (By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
    BOOK_NAME = (By.XPATH, '//h1')
    PRICE = (By.XPATH, '//div/p[contains(@class, "price_color")]')
    BOOK_NAME_FIELD = (By.XPATH, '//div[@id="messages"]/div[1]/div/strong')
    PRICE_FIELD = (By.XPATH, '//div[@id="messages"]/div[3]/div/p/strong')
    # отвратительный локатор, но и задание тоже не очень
    SUCCESS_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1][@class="alert alert-safe alert-noicon alert-success  fade in"]')
