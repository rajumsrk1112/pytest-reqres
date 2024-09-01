import requests
import pytest

from consts.constants import BASE_URL, USERS_URI


class TestUpdateUser:
    def test_update_user(self):
        data = {
            "name": "Sai Raju",
            "job": "Senior SDET"
        }
        response = requests.put(f"{BASE_URL}{USERS_URI}/1",
                                data=data)
        assert response.status_code == 200
        json_response = response.json()
        assert ("name" in json_response
                and isinstance(json_response["name"], str)
                and json_response["name"] == data["name"])
        assert ("job" in json_response
                and isinstance(json_response["job"], str)
                and json_response["job"] == data["job"])
        assert ("updatedAt" in json_response
                and isinstance(json_response["updatedAt"], str))
