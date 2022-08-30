import requests



requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)

# 使用session后
session = requests.session()
session.get('http://httpbin.org/cookies/set/number/22222222')
r = session.get('http://httpbin.org/cookies')

print(r.text)
