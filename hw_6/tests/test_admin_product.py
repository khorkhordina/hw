import pytest
from hw_6.pages.admin_page import AdminPage
from hw_6.data.data import generate_product_data

def test_add_new_product(browser):

    product_data = generate_product_data()
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.login()
    admin_page.go_to_products()

    admin_page.add_product(
        name=product_data["name"],
        meta=product_data["meta_title"],
        model=product_data["model"],
        price=product_data["price"],
        quantity=product_data["quantity"]
    )

    assert admin_page.is_success_alert_displayed(), "Нет сообщения об успешном добавлении"

    admin_page.go_to_products()
    admin_page.filter_product(product_data["name"])
    assert admin_page.is_product_in_list(product_data["name"]), "Продукт не найден в списке"


def test_add_delete_product(browser):

    product_data = generate_product_data()
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.login()
    admin_page.go_to_products()

    admin_page.add_product(
        name=product_data["name"],
        meta=product_data["meta_title"],
        model=product_data["model"],
        price=product_data["price"],
        quantity=product_data["quantity"]
    )

    assert admin_page.is_success_alert_displayed(), "Нет сообщения о добавлении"

    admin_page.go_to_products()
    admin_page.filter_product(product_data["name"])
    assert admin_page.is_product_in_list(product_data["name"]), "Продукт не найден в списке"

    admin_page.delete_product(product_data["name"])
    assert admin_page.is_success_alert_displayed(), "Нет сообщения об удалении"

    admin_page.filter_product(product_data["name"])
    assert not admin_page.is_product_in_list(product_data["name"]), "Продукт найден после удаления"