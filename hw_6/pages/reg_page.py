from hw_6.pages.base_page import BasePage
from hw_6.pages.locators.reg_loc import RegistrationLocators
import time


class RegistrationPage(BasePage):
    def open(self):
        self.browser.get(f"{self.browser.url}/en-gb?route=account/register")
        self.wait_for_visible(RegistrationLocators.FIRST_NAME)
        return self

    def register(self, firstname, lastname, email, password):

        self.send_keys(RegistrationLocators.FIRST_NAME, firstname)
        self.send_keys(RegistrationLocators.LAST_NAME, lastname)
        self.send_keys(RegistrationLocators.EMAIL, email)
        self.send_keys(RegistrationLocators.PASSWORD, password)

        agree_checkbox = self.find(RegistrationLocators.AGREE_CHECKBOX)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", agree_checkbox)
        time.sleep(0.5)
        self.browser.execute_script("arguments[0].click();", agree_checkbox)

        # Нажимаем Continue на форме через JavaScript
        continue_btn = self.find(RegistrationLocators.CONTINUE_BTN)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", continue_btn)
        time.sleep(0.5)
        self.browser.execute_script("arguments[0].click();", continue_btn)

        time.sleep(2)

        # Проверяем результат регистрации
        if "register" not in self.browser.current_url:
            if self.is_element_visible(RegistrationLocators.SUCCESS_CONTINUE_BTN):
                success_btn = self.find(RegistrationLocators.SUCCESS_CONTINUE_BTN)
                self.browser.execute_script("arguments[0].click();", success_btn)

        return self

    def is_registration_successful(self):
        """Проверяет, успешно ли зарегистрирован пользователь по URL"""
        time.sleep(3)
        current_url = self.browser.current_url
        return "account" in current_url or "success" in current_url