from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC


class SignInPage(BasePage):
    USERNAME_FIELD = (By.CSS_SELECTOR, '#email-2')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#field')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[wized="loginButton"]')

    def open_sign_in_page(self):
        self.open('https://soft.reelly.io/sign-in')

    def input_username(self, username):
        self.input_text(username, *self.USERNAME_FIELD)

    def input_password(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_continue_button(self):
        self.wait_for_clickable_element_and_click(*self.CONTINUE_BUTTON)