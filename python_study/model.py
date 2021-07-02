import requests

report_url = 'http://deeprobe-worker-test-01.aurora:4002/v1/model'
resp = requests.get(report_url, params={'file_id': 'bximage_bximage_bximage'})
# len(resp.json()['items'])
print(resp.json())
