import json

import requests
import pytest

from consts.constants import BASE_URL, USERS_URI

with open("data/users_data.json", "r") as test_data:
    data = json.load(test_data)
    users_data = data["data"]


class TestCreateMultipleUsers:
    @pytest.mark.parametrize("user_data", users_data)
    def test_create_multiple_users(self, user_data):
        print(user_data)
        response = requests.post(f"{BASE_URL}{USERS_URI}", data=user_data)
        json_response=response.json()
        assert response.status_code == 201
        assert ("name" in json_response
                and isinstance(json_response["name"],str)
                and json_response["name"] == user_data["name"])
        assert ("job" in json_response
                and isinstance(json_response["job"], str)
                and json_response["job"] == user_data["job"])
        assert ("id" in json_response
                and isinstance(json_response["id"], str))
