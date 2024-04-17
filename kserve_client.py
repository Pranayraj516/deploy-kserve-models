# Usage: python kserve_client.py <profile> <name> <input json file name>
# Ex: python kserve_client.py default sklearnv1 input.json

import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Check if a parameter is provided
if len(sys.argv) > 3:
    param1 = sys.argv[1] 
else:
    print("Please provide name.")
    exit(1)

# get serving details
SERVING_TOKEN = sys.argv[2]
SERVING_ENDPOINT = sys.argv[3]
print(SERVING_TOKEN)
print("\n")
print(SERVING_ENDPOINT)
print("\n")

# serving request
headers={'Authorization': SERVING_TOKEN, 'Content-Type': 'application/json'}
print(headers)
print("\n")
resp = requests.post(SERVING_ENDPOINT, data=open(param1, 'rb'), headers=headers, verify=False)
print (resp.text)
