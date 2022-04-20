import requests
import json
import urllib3


switchuser='admin'
switchpassword='admin'

url='https://172.16.13.1/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show run",
    "output_format": "json"
  }
}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify= False).json()

print(response)
