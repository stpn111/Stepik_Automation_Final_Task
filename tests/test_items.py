import pytest
from selenium.webdriver.common.by import By

# Типы проверки
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"


class TestBasket:

    def test_basket(self, driver):
        self.driver = driver
        self.driver.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        button = self.driver.find_element(By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
        assert button, 'Page not contains basket button'
