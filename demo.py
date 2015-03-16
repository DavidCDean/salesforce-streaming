__author__ = 'David C. Dean'


import salesforce_streaming as sf
import time


auth = sf.OAuth(username=user, password=passwd, client_id=clid, client_secret=clscrt)

print('\nAuthenticating...')
if auth.request_token():
    print('\nHandshaking...')
    stream_api = sf.StreamingAPI(instance=auth.get_instance(), token=auth.get_token())
    if stream_api.handshake():
        print('\nSubscribing...')
        stream_api.subscribe('/topic/AllTestObjs')
        print('\nConnecting...')

        while True:
            time.sleep(2)
            stream_api.connect()
            print('\nReconnect...')

else:
    print('Token Request Failed.')




