from src.utilities.requestUtilities import requestsUtilities
import pytest

request_utility = requestsUtilities()

@pytest.mark.tcid06
@pytest.mark.test_register_successfull
def test_register_successfull():
    rs_api = request_utility.post('/api/register', payload={"email": "eve.holt@reqres.in","password": "pistol"})
    assert rs_api['id']
    assert rs_api['token']


@pytest.mark.tcid07
@pytest.mark.test_register_unsuccessfull
def test_register_unsuccessfull():
    rs_api = request_utility.post('/api/register', payload={"email": "sydney@fife"})
    assert rs_api['id']