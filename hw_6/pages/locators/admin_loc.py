from selenium.webdriver.common.by import By

class AdminLocators:

    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CATALOG_MENU = (By.ID, "menu-catalog")
    PRODUCTS_MENU_ITEM = (By.XPATH, "//a[contains(@href, 'catalog/product')]")
    ADD_NEW_BUTTON = (By.XPATH, "//a[.//i[contains(@class, 'fa-plus')]]")
    FILTER_BUTTON = (By.ID, "button-filter")
    FILTER_NAME_INPUT = (By.NAME, "filter_name")
    PRODUCT_NAME_INPUT = (By.NAME, "product_description[1][name]")
    META_TITLE_INPUT = (By.NAME, "product_description[1][meta_title]")
    MODEL_INPUT = (By.ID, "input-model")
    PRICE_INPUT = (By.NAME, "price")
    QUANTITY_INPUT = (By.NAME, "quantity")
    DATA_TAB = (By.CSS_SELECTOR, "a[href='#tab-data']")
    SEO_TAB = (By.CSS_SELECTOR, "a[href='#tab-seo']")
    SEO_KEYWORD_INPUT = (By.ID, "input-keyword-0-1")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit'][form='form-product']")
    SELECT_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @name='selected[]']")
    DELETE_BUTTON = (By.XPATH, "//button[contains(@formaction, 'catalog/product.delete')]")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert-success")