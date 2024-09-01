import requests

from consts.constants import BASE_URL, USERS_URI


class TestGetSingleUserNotFound:
    def test_get_single_user_not_found(self):
        response = requests.get(f"{BASE_URL}{USERS_URI}/123")
        assert response.status_code == 404
        json_response = response.json()
        print(json_response)
        print(type(json_response))
        assert isinstance(json_response, dict)
        assert json_response == {}
