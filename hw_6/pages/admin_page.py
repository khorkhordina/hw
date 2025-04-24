from selenium.webdriver.common.by import By
from hw_6.pages.base_page import BasePage
from hw_6.data.data import Creds
from hw_6.pages.locators.admin_loc import AdminLocators
import time


class AdminPage(BasePage):
    def open(self):
        self.browser.get(f"{self.browser.url}/administration/")
        return self

    def login(self, username=Creds.ADMIN_LOGIN, password=Creds.ADMIN_PASSWORD):
        self.send_keys(AdminLocators.USERNAME_INPUT, username)
        self.send_keys(AdminLocators.PASSWORD_INPUT, password)
        self.click_element(AdminLocators.LOGIN_BUTTON)
        return self

    def go_to_products(self):
        self.click_element(AdminLocators.CATALOG_MENU)
        time.sleep(0.5)
        self.click_element(AdminLocators.PRODUCTS_MENU_ITEM)
        time.sleep(1)
        return self

    def add_product(self, name, meta, model, price, quantity):
        self.click_element(AdminLocators.ADD_NEW_BUTTON)
        self.send_keys(AdminLocators.PRODUCT_NAME_INPUT, name)
        self.send_keys(AdminLocators.META_TITLE_INPUT, meta)

        self.click_element(AdminLocators.DATA_TAB)
        time.sleep(0.5)

        self.send_keys(AdminLocators.MODEL_INPUT, model)
        self.send_keys(AdminLocators.PRICE_INPUT, price)
        self.send_keys(AdminLocators.QUANTITY_INPUT, quantity)

        self.click_element(AdminLocators.SEO_TAB)
        time.sleep(0.5)

        self.send_keys(AdminLocators.SEO_KEYWORD_INPUT, name.lower().replace(" ", "-"))
        self.click_element(AdminLocators.SAVE_BUTTON)
        time.sleep(1)
        return self

    def filter_product(self, name):
        # Прокручиваем страницу вверх
        self.browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)
        # Очищаем и заполняем поле фильтра
        filter_input = self.find(AdminLocators.FILTER_NAME_INPUT)
        filter_input.clear()
        self.send_keys(AdminLocators.FILTER_NAME_INPUT, name)
        # Кликаем кнопку фильтра с помощью JavaScript
        filter_button = self.find(AdminLocators.FILTER_BUTTON)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", filter_button)
        time.sleep(0.5)
        self.browser.execute_script("arguments[0].click();", filter_button)

        time.sleep(2)
        return self

    def is_product_in_list(self, name):

        xpath = f"//td[contains(text(), '{name}')]"
        elements = self.browser.find_elements(By.XPATH, xpath)
        return len(elements) > 0

    def delete_product(self, name):

        self.filter_product(name)
        self.click_element(AdminLocators.SELECT_CHECKBOX)
        self.browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)

        delete_button = self.find(AdminLocators.DELETE_BUTTON)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", delete_button)
        time.sleep(0.5)
        self.browser.execute_script("arguments[0].click();", delete_button)
        time.sleep(0.5)
        self.browser.switch_to.alert.accept()
        time.sleep(1)
        return self

    def is_success_alert_displayed(self):

        return self.is_element_visible(AdminLocators.SUCCESS_ALERT)