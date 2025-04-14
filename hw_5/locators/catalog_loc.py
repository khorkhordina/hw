from selenium.webdriver.common.by import By


class CatalogPageLoc:
    title = (By.XPATH, "//a[text()='Desktops']")
    limits = (By.CSS_SELECTOR, "#input-limit")
    products = (By.XPATH, "//div[@class='product-thumb']")
    compare_button = (By.ID, "compare-total")
    add_to_cart_btn = (By.XPATH, "//button[contains(@formaction,'route=checkout/cart.add')]")


