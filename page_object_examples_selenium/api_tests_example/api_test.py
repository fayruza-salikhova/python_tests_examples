import requests
import pytest  # optional here, but needed for running tests with pytest

BASE = "https://jsonplaceholder.typicode.com"
RESOURCE = "posts"

class TestPostsAPI:

    def test_get_list(self):
        resp = requests.get(f"{BASE}/{RESOURCE}")
        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, list)
        assert len(data) > 0

    def test_get_single(self):
        resp = requests.get(f"{BASE}/{RESOURCE}/1")
        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == 1

    def test_post(self):
        new_post = {"title": "foo", "body": "bar", "userId": 1}
        resp = requests.post(f"{BASE}/{RESOURCE}", json=new_post)
        assert resp.status_code == 201  # Created
        data = resp.json()
        assert data["title"] == "foo"
        assert "id" in data

    def test_put(self):
        updated = {"id": 1, "title": "updated", "body": "baz", "userId": 1}
        resp = requests.put(f"{BASE}/{RESOURCE}/1", json=updated)
        assert resp.status_code == 200
        data = resp.json()
        assert data["title"] == "updated"

    def test_patch(self):
        patch = {"title": "patched title"}
        resp = requests.patch(f"{BASE}/{RESOURCE}/1", json=patch)
        assert resp.status_code == 200
        data = resp.json()
        assert data["title"] == "patched title"

    def test_delete(self):
        resp = requests.delete(f"{BASE}/{RESOURCE}/1")
        assert resp.status_code == 200 or resp.status_code == 204  # 200 OK or 204 No Content
