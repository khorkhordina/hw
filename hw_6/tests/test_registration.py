import pytest
from hw_6.pages.reg_page import RegistrationPage
from hw_6.data.data import generate_user_data
import time

def test_user_registration(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open()
    user_data = generate_user_data()
    registration_page.register(
        firstname=user_data["firstname"],
        lastname=user_data["lastname"],
        email=user_data["email"],
        password=user_data["password"]
    )
    assert registration_page.is_registration_successful(), "Регистрация не выполнена"
    assert "account" in browser.current_url, "Пользователь не перенаправлен на страницу аккаунта"


def test_user_registration_with_invalid_data(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open()

    registration_page.register(
        firstname="",
        lastname="",
        email="",
        password=""
    )
    time.sleep(2)
    assert "register" in browser.current_url, "Регистрация прошла успешно с пустыми данными"