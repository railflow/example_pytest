import requests
import json
import logging as logger

class requestsUtilities(object):

    def __init__(self):
        self.base_url = 'https://reqres.in'
        
    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f'Bad Status code.'\
            f"Expected{self.expected_status_code}, Actual status code: {self.status_code},"\
            f"URL: {self.url}, Response Json: {self.rs_json}"

    def post(self, endpoint , payload = None, headers= None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.post(self.url, data = json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API Post response:{self.rs_json} ")

        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type":"application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API Get response:{self.rs_json} ")

        return self.rs_json


    def put(self, endpoint, payload , headers = None, expected_status_code = 200):
        if not headers:
            headers = {"Content-Type":"application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.put(self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API Put response:{self.rs_json} ")

        return self.rs_json