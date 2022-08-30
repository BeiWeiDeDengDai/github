import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1

url = "https://realtime.haohaozhu.me/"

resp = requests.get(url, auth=('zhangyinghao','zyhbwddd210'))
resp.encoding="utf-8"
print(resp.text)

#
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)