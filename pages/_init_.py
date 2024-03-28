from selenium.webdriver.common.by import By

from pages.base_page import Page


class AddAProjectPage(Page):
    YOUR_NAME_FIELD = (By.ID, "Your-name")
    PHONE_FIELD = (By.ID, "Phone")
    EMAIL_FIELD = (By.ID, "Email-add-project")
    SEND_APPLICATION_BTN = (By.CSS_SELECTOR, "[class*='purchase-access']")

    def verify_right_page_url(self, expected_part_url):
        self.verify_partial_url(expected_part_url)

    def add_test_information(self, name, phone_number, email):
        self.input_text(self.YOUR_NAME_FIELD, name)
        self.input_text(self.PHONE_FIELD, phone_number)
        self.input_text(self.EMAIL_FIELD, email)

    def verify_test_information_entered_correct(self, expected_values):
        required_fields = {
            "Your-name": self.YOUR_NAME_FIELD,
            "Phone": self.PHONE_FIELD,
            "Email-add-project": self.EMAIL_FIELD
        }
        for field, locator in required_fields.items():
            actual_value = self.get_input_value(locator)
            assert actual_value == expected_values[
                field], f"Expected {field}: {expected_values[field]}, Actual {field}: {actual_value}"
            print(actual_value)

    def verify_application_button_clickable(self):
        pass