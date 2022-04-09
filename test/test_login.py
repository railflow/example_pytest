from src.utilities.requestUtilities import requestsUtilities
import pytest

class TestLogin:
    def __init__(self):
        self.request_utility = requestsUtilities()


    @pytest.mark.tcid08
    @pytest.mark.login
    @pytest.mark.test_login_successfull
    def test_login_successfull(self):
        rs_api = self.request_utility.post('/api/login', payload={"email": "eve.holt@reqres.in", "password": "cityslicka"})
        assert rs_api['token']


    @pytest.mark.tcid09
    @pytest.mark.login
    @pytest.mark.test_login_unsuccessfull
    def test_login_unsuccessfull(self):
        rs_api = self.request_utility.post('/api/register', payload={"email": "peter@klaven"}, expected_status_code=400)
