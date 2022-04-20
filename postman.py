import requests
url = "https://172.16.13.15/ins"
payload="{\r\n  \"ins_api\": {\r\n    \"version\": \"1.0\",\r\n    \"type\": \"cli_conf\",\r\n    \"chunk\": \"0\",\r\n    \"sid\": \"1\",\r\n    \"input\": \"no vlan 2021\",\r\n    \"output_format\": \"json\"\r\n  }\r\n}"
headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Content-Type': 'text/plain',
  'Cookie': 'nxapi_auth=admin:6c3Doe4LKsHuB/ey675u7BRjTsI='
}
response = requests.request("POST", url, headers=headers, data=payload, verify= False)

print(response.text)
