from selenium.webdriver.common.by import By


class HomePageLoc:
    cart_btn = (By.XPATH, "//a[contains(@href, 'route=checkout/cart')]")
    search_btn = (By.XPATH, "//button[@data-lang='en-gb']")
    logo = (By.XPATH, "//img[@alt='Your Store']")
    nav_menu = (By.XPATH, "//nav[@id='top']")
    currency_switcher = (By.XPATH, "//form[contains(@action, 'currency')]//strong")
