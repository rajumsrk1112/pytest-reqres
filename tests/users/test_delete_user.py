import requests

from consts.constants import BASE_URL, USERS_URI


class TestDeleteUser:
    def test_delete_user(self):
        response = requests.delete(f"{BASE_URL}{USERS_URI}/1")
        assert response.status_code == 204
        assert response.text == ""
