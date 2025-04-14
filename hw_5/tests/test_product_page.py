import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_5.locators.productpage_loc import ProductPageLoc


class TestProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)
        self.browser.get(f"{self.browser.url}/en-gb/product/macbook")

    def test_product_title_visible(self):
        title = self.wait.until(
            EC.visibility_of_element_located(ProductPageLoc.title)
        )
        assert title.is_displayed()

    def test_price_displayed(self):
        price = self.wait.until(
            EC.visibility_of_element_located(ProductPageLoc.price)
        )
        assert price.is_displayed()

    def test_add_to_cart_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(ProductPageLoc.add_to_cart_btn)
        )
        assert button.is_displayed()

    def test_image_displayed(self):
        image = self.wait.until(
            EC.visibility_of_element_located(ProductPageLoc.img_locator)
        )
        assert image.is_displayed(), "Изображение не отображается на странице"

    def test_specification_tab_exists(self):
        specification_tab = self.wait.until(
            EC.presence_of_element_located(ProductPageLoc.specification_tab)
        )
        assert specification_tab is not None, "Вкладки Specification нет на странице"