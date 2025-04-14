from selenium.webdriver.common.by import By


class RegPageLoc:
    title = (By.XPATH, "//h1[text()='Register Account']")
    first_name = (By.XPATH, "//input[@id='input-firstname']")
    last_name = (By.XPATH, "//input[@id='input-lastname']")
    email = (By.XPATH, "//input[@id='input-email']")
    password = (By.XPATH, "//input[@id='input-password']")