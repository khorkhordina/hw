import pytest
import requests
from jsonschema import validate


def test_list_breeds(base_url):
    response = requests.get(f"{base_url}/breeds/list/all")
    assert response.status_code == 200
    assert response.json().get("status") == "success"

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }

    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize("breed", ["hound", "retriever", "pug", "bulldog", "beagle"])
def test_random_image_by_breed(base_url, breed):
    response = requests.get(f"{base_url}/breed/{breed}/images/random")
    assert response.status_code == 200
    image_url = response.json().get("message", "")
    assert image_url.endswith((".jpg", ".jpeg", ".png"))


@pytest.mark.parametrize("breed,sub_breed", [
    ("hound", "afghan"),
    ("retriever", "golden"),
    ("bulldog", "french"),
    ("sheepdog", "english"),
    ("terrier", "scottish")
])

def test_sub_breed_exists(base_url, breed, sub_breed):
    response = requests.get(f"{base_url}/breed/{breed}/list")
    assert response.status_code == 200
    assert sub_breed in response.json()["message"]


@pytest.mark.parametrize("endpoint,expected_status", [
    ("breeds/image/random", 200),
    ("breed/hound/images", 200),
    ("breed/nonexistentbreed/images", 404),
])

def test_status_code(base_url, endpoint, expected_status):
    response = requests.get(f"{base_url}/{endpoint}")
    assert response.status_code == expected_status


def test_subbreed_list(base_url):
    response = requests.get(f"{base_url}/breed/bulldog/list")
    assert isinstance(response.json().get("message"), list)


def test_invalid_breed(base_url):
    response = requests.get(f"{base_url}/breed/dragon/list")
    assert response.status_code == 404 or response.json().get("status") == "error"