import requests

def test_url_status_code(url, expected_status_code):
    response = requests.get(url)
    assert response.status_code == expected_status_code, (
        f"Для URL '{url}' ожидался статус-код {expected_status_code}, "
        f"но получен {response.status_code}"
    )