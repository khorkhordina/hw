import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_5.locators.adminpage_loc import AdminPageLoc


class TestsAdminPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)
        self.browser.get(f"{self.browser.url}/administration")

    def test_admin_page_username_field(self):
        element = self.wait.until(
            EC.presence_of_element_located(AdminPageLoc.username)
        )
        assert element.is_displayed(), "Поле для ввода имени пользователя не отображается"

    def test_admin_page_password_field(self):
        element = self.wait.until(
            EC.presence_of_element_located(AdminPageLoc.password)
        )
        assert element.is_displayed(), "Поле для ввода пароля не отображается"

    def test_admin_page_login_button(self):
        element = self.wait.until(
            EC.presence_of_element_located(AdminPageLoc.login_btn)
        )
        assert element.is_displayed(), "Кнопка логина не отображается"

    def test_login_info_title(self):
        # Ждем появления заголовка на странице
        title_element = self.wait.until(
            EC.presence_of_element_located(AdminPageLoc.login_info_title),
            message="Заголовок Please enter your login details не найден"
        )
        assert title_element.is_displayed(), "Заголовок не отображается"

    def test_user_icon_visible(self):
        element = self.wait.until(
            EC.presence_of_element_located(AdminPageLoc.user_icon),
            message="Иконка пользователя не найдена"
        )
        assert element.is_displayed(), "Иконка пользователя не отображается"
