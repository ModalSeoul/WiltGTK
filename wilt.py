import os
import json
import requests
from time import sleep

# Misc
AUTH = 'https://wilt.fm/api/api-token-auth/'
SCROBBLE = 'https://wilt.fm/api/scrobbles/'

get = requests.get
post = requests.post


class Wilt:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.logged_in = False
        self.header = {'Authorization': 'Token {}'.format(self.login())}
        self.last_played = ''  # Clarity

    def login(self):
        r = post(AUTH, data={'username': self.user, 'password': self.password})
        if 'token' in r.text:
            self.logged_in = True
            os.system('clear')
        else:
            print('Something went wrong - Not logged in!')
            return None
        return json.loads(r.text)['token']

    def scrobble(self, scrobble):
        if scrobble['song'] != self.last_played:
            r = post(SCROBBLE, data=scrobble, headers=self.header)
            self.last_played = scrobble['song']
        else:
            return None
