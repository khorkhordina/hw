import pytest
from hw_6.pages.home_page import HomePage


def test_currency_switching(browser):
    home_page = HomePage(browser)
    home_page.open()
    home_page.select_currency('EUR')
    assert home_page.get_currency_symbol() == '€', "Символ валюты не евро"

    home_page.select_currency('USD')
    assert home_page.get_currency_symbol() == '$', "Символ валюты не доллар"

    home_page.select_currency('GBP')
    assert home_page.get_currency_symbol() == '£', "Символ валюты не фунт"


