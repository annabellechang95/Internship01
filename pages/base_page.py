from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_visible_element(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator), message=f"Element via {locator} is not visible")

    def wait_for_clickable_element(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator), message=f"Element via {locator} is not clickable")

    def wait_for_clickable_element_and_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator), message=f"Element via {locator} is not clickable").click()

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element via {locator} is not visible").send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element via {locator} is not visible").text
        assert expected_text in actual_text, f"\nExpected: {expected_text}.\nActual: {actual_text}."

    def verify_page_url(self, expected_text_in_url):
        url = self.driver.current_url
        assert expected_text_in_url.lower() in url, f'\nExpected: {expected_text_in_url}.\nActual: {url}.'

    def scroll_to(self, *locator):
        element_to_scroll_to = self.wait.until(
            EC.visibility_of_element_located((locator)), message=f'Button not found via locator: {locator}.')
        self.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)

    def store_original_tab(self):
        original_tab = self.driver.current_window_handle
        print(f"Original tab: {original_tab}")
        return original_tab

    def switch_to_original_tab(self, original_tab):
        self.driver.switch_to.window(original_tab)

    def switch_to_new_tab(self):
        self.wait.until(EC.new_window_is_opened)
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])
        print(f"New tab: {self.driver.current_window_handle}")

    def close_current_tab(self):
        self.driver.close()
