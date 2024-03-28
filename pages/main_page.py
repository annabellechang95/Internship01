from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    MAIN_MENU_TEXT = (By.CSS_SELECTOR, '.h1-menu')
    BLOCK_MENU_LOCATORS = {
        'Settings': (By.CSS_SELECTOR, '.menu_block_1 [href="/settings"]'),
    }

    def verify_main_page(self):
        self.verify_text('Main menu', *self.MAIN_MENU_TEXT)

    def click_menu_block_button(self, button):
        locator = self.BLOCK_MENU_LOCATORS.get(button)
        self.scroll_to(*locator)
        self.wait_for_clickable_element_and_click(*locator)
