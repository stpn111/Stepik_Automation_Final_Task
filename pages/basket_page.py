from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_items_list_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_LIST_OF_ITEMS), \
            "List of items message is presented, but should not be"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "Basket is empty message is not presented, but should be"
