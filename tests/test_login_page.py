from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_should_be_correct_link(browser):
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_url()          # выполняем метод страницы - переходим на страницу логина


def test_should_be_login_form(browser):
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_form()          # выполняем метод страницы - переходим на страницу логина


def test_should_be_register_form(browser):
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_register_form()          # выполняем метод страницы - переходим на страницу логина

# def test_guest_should_see_login_link(browser):
#
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
