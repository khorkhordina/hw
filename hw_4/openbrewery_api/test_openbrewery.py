import pytest
import requests


# Получение списка всех пивоварен
def test_all_breweries(base_url, headers):
    response = requests.get(f"{base_url}/breweries", headers=headers)
    assert response.status_code == 200

    breweries = response.json()
    assert isinstance(breweries, list)
    assert len(breweries) > 0
    assert "name" in breweries[0]
    assert "brewery_type" in breweries[0]

# Получение пивоварни по ID
def test_brewery_id(base_url, headers):
    brewery_id = "06e9fffb-e820-45c9-b107-b52b51013e8f"
    response = requests.get(f"{base_url}/breweries/{brewery_id}", headers=headers)
    assert response.status_code == 200

    brewery = response.json()
    assert brewery["id"] == brewery_id
    assert "name" in brewery
    assert "city" in brewery

# Проверка получения пивоварен по типу
@pytest.mark.parametrize("brewery_type", ["micro", "regional", "brewpub"])
def test_breweries_type(base_url, headers, brewery_type):
    response = requests.get(f"{base_url}/breweries", params={"by_type": brewery_type}, headers=headers)
    assert response.status_code == 200

    breweries = response.json()
    assert all(brewery["brewery_type"] == brewery_type for brewery in breweries)

# Проверка поиска по имени
def test_search_brewery_name(base_url, headers):
    params = {"query": "brew"}
    response = requests.get(f"{base_url}/breweries/search", params=params, headers=headers)

    assert response.status_code == 200
    breweries = response.json()
    assert isinstance(breweries, list)

    if len(breweries) > 0:
        for brewery in breweries:
            assert params["query"].lower() in brewery["name"].lower() or\
                (brewery.get("description") and params["query"].lower() in brewery["description"].lower())

# Проверка фильтрации по штату
@pytest.mark.parametrize("state", ["California", "Texas", "North Dakota"])
def test_breweries_state(base_url, headers, state):
    response = requests.get(f"{base_url}/breweries", params={"by_state": state}, headers=headers)
    assert response.status_code == 200

    breweries = response.json()
    assert isinstance(breweries, list)
    for brewery in breweries:
        assert "state" in brewery
        assert brewery["state"] == state

