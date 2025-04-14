from selenium.webdriver.common.by import By


class ProductPageLoc:
    title = (By.XPATH, "//h1[text()='MacBook']")
    price = (By.XPATH, "//span[@class='price-new']")
    add_to_cart_btn = (By.CLASS_NAME, "btn-primary")
    img_locator = (By.XPATH, "//img[@alt='MacBook']")
    specification_tab = (By.LINK_TEXT, "Specification")



