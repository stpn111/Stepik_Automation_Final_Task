from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_price(self):
        cur_price_value = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(ProductPageLocators.PRICE)
        ).text
        basket_price_value = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(ProductPageLocators.PRICE_FIELD)
        ).text
        assert cur_price_value == basket_price_value

    def check_name(self):
        cur_name_value = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(ProductPageLocators.BOOK_NAME)
        ).text
        basket_name_value = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(ProductPageLocators.BOOK_NAME_FIELD)
        ).text
        assert cur_name_value == basket_name_value

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert not self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"