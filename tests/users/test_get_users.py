import requests

from consts.constants import BASE_URL, USERS_URI


def validate_user_data(data):
    assert "id" in data and isinstance(data["id"],int)
    assert "email" in data and isinstance(data["email"], str)
    assert "first_name" in data and isinstance(data["first_name"], str)
    assert "last_name" in data and isinstance(data["last_name"], str)
    assert "avatar" in data and isinstance(data["avatar"], str)


class TestGetUsers:
    def test_get_users(self):
        response = requests.get(url=f"{BASE_URL}{USERS_URI}",
                                params={"page": 1})
        assert response.status_code == 200
        response = response.json()
        # Validate main fields in response
        assert "page" in response and isinstance(response["page"], int)
        assert "per_page" in response and isinstance(response["per_page"], int)
        assert "total" in response and isinstance(response["total"], int)
        assert "total_pages" in response and isinstance(response["total_pages"], int)
        assert "data" in response and isinstance(response["data"], list)
        assert "support" in response and isinstance(response["support"], dict)
        # Validate user fields
        for user in response["data"]:
            validate_user_data(data=user)



