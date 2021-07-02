import requests

url = 'http://deeprobe-worker-test-01.aurora:4102/stream'

resp = requests.get(url, stream=True)
for line in resp.iter_lines():
    print(line)
