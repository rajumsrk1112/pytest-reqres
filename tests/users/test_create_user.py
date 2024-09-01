import pytest
import requests

from consts.constants import BASE_URL, USERS_URI


class TestCreateUser:
    def test_create_user(self):
        data = {
            "name": "Sai raju",
            "job": "Senior SDET"
        }
        response = requests.post(f"{BASE_URL}{USERS_URI}",
                                 data=data)
        assert response.status_code == 201
        json_response = response.json()

        print(response.text)
        assert "name" in json_response and json_response["name"] == data["name"]
        assert "job" in json_response and json_response["job"] == data["job"]
        assert "id" in json_response and isinstance(json_response["id"], str)
        assert "createdAt" in json_response and isinstance(json_response["createdAt"], str)
