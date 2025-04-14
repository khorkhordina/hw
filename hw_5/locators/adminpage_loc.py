from selenium.webdriver.common.by import By


class AdminPageLoc:
    username = (By.XPATH, "//input[@id='input-username']")
    password = (By.XPATH, "//input[@id='input-password']")
    login_btn = (By.XPATH, "//button[@class='btn btn-primary']")
    login_info_title = (By.XPATH, "//div[@class='card-header']")
    user_icon = (By.CLASS_NAME, "fa-user")

