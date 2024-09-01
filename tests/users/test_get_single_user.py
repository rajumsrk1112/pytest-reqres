import requests

from consts.constants import BASE_URL, USERS_URI


class TestSingleUser:
    def test_get_single_user(self):
        response = requests.get(f"{BASE_URL}{USERS_URI}/2")
        # Validate HTTP status code
        assert response.status_code == 200
        print(f"JSON response: {response.text}")
        response = response.json()
        assert "data" in response and isinstance(response["data"], dict)
        user_data = response["data"]
        assert "id" in user_data and isinstance(user_data["id"], int)
        assert "email" in user_data and isinstance(user_data["email"], str)
        assert "first_name" in user_data and isinstance(user_data["first_name"], str)
        assert "last_name" in user_data and isinstance(user_data["last_name"], str)
        assert "avatar" in user_data and isinstance(user_data["avatar"], str)
