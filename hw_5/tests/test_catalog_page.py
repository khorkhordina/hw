import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_5.locators.catalog_loc import CatalogPageLoc



class TestCatalogPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 7)
        self.browser.get(f"{self.browser.url}/en-gb/catalog/desktops")


    def test_title(self):
        title = self.wait.until(
            EC.visibility_of_element_located(CatalogPageLoc.title),
            message="Заголовок каталога не найден"
        )
        assert title.is_displayed(), "Заголовок каталога не отображается"
        assert "Desktops" in title.text, "Некорректный текст заголовка"


    def test_limit(self):
        limits = self.wait.until(
            EC.visibility_of_element_located(CatalogPageLoc.limits)
        )
        assert limits.is_displayed()

    def test_product_compare_button_clickable(self):
        compare_button = self.wait.until(
            EC.element_to_be_clickable(CatalogPageLoc.compare_button),
            message="Кнопка Product Compare не кликабельна"
        )
        assert compare_button.is_displayed(), "Кнопка Product Compare не отображается"
        compare_button.click()


    def test_product_list(self):
        products = self.wait.until(
            EC.visibility_of_element_located(CatalogPageLoc.products),
            message="Список товаров не найден"
        )
        assert products.is_displayed(), "Список товаров не отображается"
        product_elements = products.find_elements(By.XPATH, ".//div")
        assert len(product_elements) > 0, "Список товаров пуст"

    def test_add_to_cart_button(self):
        button = self.wait.until(
            EC.visibility_of_element_located(CatalogPageLoc.add_to_cart_btn),
            message="Кнопка 'Добавить в корзину' не найдена"
        )
        assert button.is_displayed(), "Кнопка не отображается"
        assert button.is_enabled(), "Кнопка должна быть активна"