import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_5.locators.regpage_loc import RegPageLoc


class TestRegistrationPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)
        self.browser.get(f"{self.browser.url}/en-gb?route=account/register")

    def test_title_visible(self):
        title = self.wait.until(
            EC.presence_of_element_located(RegPageLoc.title)
        )
        assert title.is_displayed()

    def test_first_name_field_visible(self):
        field = self.wait.until(
            EC.presence_of_element_located(RegPageLoc.first_name)
        )
        assert field.get_attribute("id") == "input-firstname", "Некорректный id поля"

    def test_last_name_field_visible(self):
        field = self.wait.until(
            EC.presence_of_element_located(RegPageLoc.last_name)
        )
        assert field.is_displayed()

    def test_email_field_visible(self):
        field = self.wait.until(
            EC.presence_of_element_located(RegPageLoc.email)
        )
        assert field.get_attribute("type") == "email", "Должен быть тип email"

    def test_password_field_visible(self):
        field = self.wait.until(
            EC.presence_of_element_located(RegPageLoc.password)
        )
        assert field.get_attribute("type") == "password"