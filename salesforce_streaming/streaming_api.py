__author__ = 'David C. Dean'

import requests
import json


class StreamingAPI:

    def __init__(self, instance=None, token=None):
        self.__endpoint = instance + '/cometd/28.0'
        self.__token = token
        self.__hs_data = None
        self.__session = requests.session()

    def handshake(self):
        hs_response = self.__session.post(self.__endpoint, data=self._handshake_payload(), headers=self._get_headers(), stream=True)
        if hs_response.status_code == 200:
            print(hs_response.text)
            self.__hs_data = json.loads(hs_response.text)[0]
            return True
        else:
            print('BAD HANDSHAKE\n')
            return False

    def connect(self):
        cn_response = self.__session.post(self.__endpoint, data=self._connect_payload(), headers=self._get_headers())
        if cn_response.status_code == 200:
            print(cn_response.text)
            return True
        else:
            print('BAD CONNECT\n')
            return False

    def subscribe(self, topic=None):
        sub_response = self.__session.post(self.__endpoint, data=self._subscribe_payload(topic), headers=self._get_headers())
        if sub_response.status_code == 200 and json.loads(sub_response.text)[0]['successful'] == True:
            print(sub_response.text)
            return True
        else:
            print('BAD SUBSCRIBE\n')
            return False

    def get_client_id(self):
        return self.__hs_data['clientId']

    def _subscribe_payload(self, topic=None):
        return json.dumps([{'channel': '/meta/subscribe', 'clientId': self.get_client_id(), 'subscription': topic }])

    def _handshake_payload(self):
        return json.dumps({'supportedConnectionTypes': ['long-polling'], 'version': '1.0', 'channel': '/meta/handshake', 'minimumVersion': '1.0'})

    def _connect_payload(self):
        return json.dumps([{'channel': '/meta/connect', 'clientId': self.get_client_id(), 'connectionType': 'long-polling'}])

    def _get_headers(self):
        return {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + self.__token}
