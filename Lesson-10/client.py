import requests

base_url = 'http://127.0.0.1:8000/'

res = requests.get(base_url + 'posts')
print(res.json())
