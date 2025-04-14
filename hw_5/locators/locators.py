from selenium.webdriver.common.by import By

class HomePageLocators:
    homePageTitle = (By.XPATH, "//h1[contains(text(),'Your Store')]")
    cartButton = (By.XPATH, "//button[@id='cart']")
    searchButton = (By.XPATH, "//button[@class='btn btn-default']")
    logo = (By.XPATH, "//img[@alt='Your Store']")
    menuNavigation = (By.XPATH, "//ul[@class='navbar-nav']")


class CatalogPageLocators:
    catalogPageTitle = (By.XPATH, "//h2[text()='Desktops']")
    filterSection = (By.XPATH, "//div[@id='filter']")
    productList = (By.XPATH, "//div[@class='product-layout']")
    sortDropdown = (By.XPATH, "//select[@id='input-sort']")
    addToCartButton = (By.XPATH, "//button[@data-original-title='Add to Cart']")


class ProductPageLocators:
    productPageTitle = (By.XPATH, "//h1[text()='MacBook']")
    price = (By.XPATH, "//p[@class='price']")
    addToCartButtonProduct = (By.XPATH, "//button[@data-original-title='Add to Cart']")
    descriptionTab = (By.XPATH, "//div[@id='tab-description']")
    reviewsSection = (By.XPATH, "//div[@id='review']")


class AdminPageLocators:
    adminPageTitle = (By.XPATH, "//h2[text()='Admin Panel']")
    usernameField = (By.XPATH, "//input[@id='input-username']")
    passwordField = (By.XPATH, "//input[@id='input-password']")
    loginButton = (By.XPATH, "//button[@class='btn btn-primary']")
    forgottenPasswordLink = (By.XPATH, "//a[text()='Forgotten Password']")


class RegistrationPageLocators:
    registrationPageTitle = (By.XPATH, "//h1[text()='Register Account']")
    firstNameField = (By.XPATH, "//input[@id='input-firstname']")
    lastNameField = (By.XPATH, "//input[@id='input-lastname']")
    emailField = (By.XPATH, "//input[@id='input-email']")
    passwordFieldReg = (By.XPATH, "//input[@id='input-password']")
