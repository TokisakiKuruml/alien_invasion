import requests

data = {'name':'fuck','age':11}
r = requests.get('https://httpbin.org/get',params=data)
print(r.json())
