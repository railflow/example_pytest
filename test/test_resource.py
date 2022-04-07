from src.utilities.requestUtilities import requestsUtilities
import pytest

request_utility = requestsUtilities()

@pytest.mark.tcid10
@pytest.mark.resource
@pytest.mark.test_list_resources
def test_list_resources():
    rs_api = request_utility.get('/api/unknown')
    assert rs_api['page']


@pytest.mark.tcid11
@pytest.mark.resource
@pytest.mark.test_list_single_resource
def test_list_single_resources():
    rs_api = request_utility.get('/api/unknown/2')
    assert rs_api['data']


@pytest.mark.tcid12
@pytest.mark.resource
@pytest.mark.test_resource_not_found
def test_resource_not_found():
    rs_api = request_utility.get('/api/unknown/23')
