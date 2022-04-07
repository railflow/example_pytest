from src.utilities.requestUtilities import requestsUtilities
import pytest

request_utility = requestsUtilities()

@pytest.mark.tcid01
@pytest.mark.users
@pytest.mark.test_user_list
def test_user_list():
    rs_api = request_utility.get('/api/users?page=2')
    assert rs_api['page'] == 2,"page is not equal to 2"

@pytest.mark.tcid02
@pytest.mark.users
@pytest.mark.test_single_user
def test_single_user():
    rs_api = request_utility.get('/api/users/2')
    assert rs_api['data']['first_name'] == "Janet", "First name is wrong" 

@pytest.mark.tcid03
@pytest.mark.users
@pytest.mark.user_not_found
def test_user_not_found():
    request_utility.get('/api/users/23',expected_status_code=400)

@pytest.mark.tcid04
@pytest.mark.users
@pytest.mark.create_user
def test_create_user():
    data = {"name": "morpheus","job": "leader"}
    rs_api  = request_utility.post('/api/users', payload=data, expected_status_code = 201)
    assert rs_api['name'] == "morpheus", "Name is not matched"
    assert rs_api['id'] , "Id is not generated"

@pytest.mark.tcid05
@pytest.mark.users
@pytest.mark.login_user
def test_login_user():
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    rs_api = request_utility.post('/api/login', payload=data)
    assert rs_api['token'] , "Token is not received"
