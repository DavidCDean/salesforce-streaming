__author__ = 'David C. Dean'

import requests
import json


class OAuth:

    def __init__(self, endpoint='https://login.salesforce.com', username='', password='', client_id='', client_secret=''):
        self.__endpoint = endpoint
        self.__username = username
        self.__password = password
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__auth_data = None

    def request_token(self):
        request_resp = requests.post(self._get_auth_url(), params=self._get_params())
        if request_resp.status_code == 200:
            self.__auth_data = json.loads(request_resp.text)
            return True
        else:
            return False


    def _get_auth_url(self):
        return self.__endpoint + '/services/oauth2/token'

    def _get_params(self):
        params = {
            'grant_type': 'password',
            'username': self.__username,
            'password': self.__password,
            'client_id': self.__client_id,
            'client_secret': self.__client_secret}
        return params

    def get_token(self):
        return self.__auth_data['access_token']

    def get_instance(self):
        return self.__auth_data['instance_url']
