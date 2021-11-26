import requests
payload={'page': 2, 'count':25}
r=requests.get('https://httpbin.org/cookies')
print(r.cookies)