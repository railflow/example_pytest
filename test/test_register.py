from src.utilities.requestUtilities import requestsUtilities
import pytest

class TestRegister:
    def __init__(self):
        self.request_utility = requestsUtilities()

    @pytest.mark.tcid06
    @pytest.mark.register
    @pytest.mark.test_register_successfull
    def test_register_successfull(self):
        rs_api = self.request_utility.post('/api/register', payload={"email": "eve.holt@reqres.in","password": "pistol"})
        assert rs_api['id']
        assert rs_api['token']


    @pytest.mark.tcid07
    @pytest.mark.register
    @pytest.mark.test_register_unsuccessfull
    def test_register_unsuccessfull(self):
        rs_api = self.request_utility.post('/api/register', payload={"email": "sydney@fife"})
        assert rs_api['id']