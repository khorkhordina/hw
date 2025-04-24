from selenium.webdriver.common.by import By

class HomeLocators:
    CURRENCY_DROPDOWN = (By.XPATH, "//a[@data-bs-toggle='dropdown']")
    CURRENCY_EUR = (By.XPATH, "//a[contains(@class, 'dropdown-item') and @href='EUR']")
    CURRENCY_USD = (By.XPATH, "//a[contains(@class, 'dropdown-item') and @href='USD']")
    CURRENCY_GBP = (By.XPATH, "//a[contains(@class, 'dropdown-item') and @href='GBP']")
    PRICE_ELEMENTS = (
    By.XPATH, "//div[contains(@class, 'price')]")