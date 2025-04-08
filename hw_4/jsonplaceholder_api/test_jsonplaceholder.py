import pytest
import requests

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "API-Testing/1.0"
}

@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user(user_id, base_url):
    response = requests.get(f"{base_url}/users/{user_id}", headers=HEADERS)
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["id"] == user_id
    assert "name" in user_data
    assert "email" in user_data


def test_get_posts(base_url):
    response = requests.get(f"{base_url}/posts", headers=HEADERS)
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert "id" in posts[0]
    assert "title" in posts[0]
    assert "body" in posts[0]


@pytest.mark.parametrize("post_id", [1, 3, 5, 10])
def test_get_post_by_id_parametrized(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}", headers=HEADERS)
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id
    assert "title" in post
    assert "body" in post


def test_create_post(base_url):
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(f"{base_url}/posts", json=new_post, headers=HEADERS)
    assert response.status_code == 201
    post = response.json()
    assert post["title"] == new_post["title"]
    assert post["body"] == new_post["body"]
    assert post["userId"] == new_post["userId"]