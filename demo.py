__author__ = 'David C. Dean'

import salesforce_streaming as sf
import time


from demo_config import user, passwd, clid, clscrt
auth_util = sf.OAuth2(username=user, password=passwd, client_id=clid, client_secret=clscrt)

print('\nAuthenticating...')
if auth_util.request_token():
    print('\nHandshaking...')
    stream_api = sf.StreamingAPI(instance=auth_util.get_instance(), token=auth_util.get_token())
    if stream_api.handshake():
        print('\nSubscribing...')
        stream_api.subscribe('/topic/AllTestObjs')
        print('\nWaiting...')

        while True:
            time.sleep(2)
            stream_api.connect()
            print('\nWaiting...')

else:
    print('Token Request Failed.')




