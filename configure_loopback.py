import requests
url = "https://172.16.13.15/ins"
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "int lo 10 ;description Baris ;ip address 6.6.6.6 255.255.255.255",
    "output_format": "json"
  }
}
headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Content-Type': 'application/json',
  'Cookie': 'nxapi_auth=admin:6c3Doe4LKsHuB/ey675u7BRjTsI='
}
response = requests.post(url, headers=headers, data=json.dumps(payload),verify=False)

print(response)
