from selenium.webdriver.common.by import By

class RegistrationLocators:
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    AGREE_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BTN = (By.CSS_SELECTOR, "button[type='submit'][class='btn btn-primary']")
    SUCCESS_CONTINUE_BTN = (By.CSS_SELECTOR, "a[class='btn btn-primary']")
