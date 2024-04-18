# Usage: python kserve_client.py <profile> <name> <input json file name>
# Ex: python kserve_client.py default sklearnv1 input.json

import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Check if a parameter is provided
if len(sys.argv) > 3:
    INPUT_JSON = sys.argv[1]
    SERVING_TOKEN = sys.argv[2]
    SERVING_ENDPOINT = sys.argv[3]
else:
    print("Please pass valid arguments.")
    exit(1)

# serving request
headers={'Authorization': SERVING_TOKEN, 'Content-Type': 'application/json'}
resp = requests.post(SERVING_ENDPOINT, data=open(INPUT_JSON, 'rb'), headers=headers, verify=False)
print (resp.text)
