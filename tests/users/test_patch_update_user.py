import requests
import pytest

from consts.constants import BASE_URL, USERS_URI


class TestPatchUpdateUser:
    def test_patch_update_user(self):
        data = {
            "name": "Sai Raju Manthina",
            "job": "Senior SDET",
            "location": "remote"
        }
        response = requests.patch(f"{BASE_URL}{USERS_URI}/1",
                                  data=data)
        assert response.status_code == 200
        json_response = response.json()
        assert ("name" in json_response
                and isinstance(json_response["name"], str)
                and json_response["name"] == data["name"])
        assert ("job" in json_response
                and isinstance(json_response["job"], str)
                and json_response["job"] == data["job"])
        assert ("location" in json_response
                and isinstance(json_response["location"], str)
                and json_response["location"] == data["location"])
