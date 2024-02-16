# Usage: python kserve_client.py <profile> <name> <input json file name>
# Ex: python kserve_client.py default sklearnv1 input.json


import configparser
import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config = configparser.ConfigParser()


# Check if a parameter is provided
if len(sys.argv) > 3:
    param1 = sys.argv[1]
    param2 = sys.argv[2]
    param3 = sys.argv[3]
else:
    print("Please provide name.")
    exit(1)

# get http url & token
ini_file ="/home/pranayraj/.d3x.ini"
config.read(ini_file)
url = config.get(param1,"url")
token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoicHJhbmF5cmFqLW1hbmdhbGEiLCJ0eXBlIjoidXNlciIsImlkIjoiZDVlZDg2OGMtNDI3Zi00MWJkLThhMTQtYzk4OWZjZmE1MWQ1In0.jM5eyA5JHSWBn6C_YeZry3R9KYtppsCe_qhXrfyQqLY"


# get deployment details
headers = {'Authorization': token}
r = requests.get(f"{url}/llm/api/deployments/{param2}", headers=headers, verify=False)
deployment = r.json()['deployment']

# get serving details
SERVING_TOKEN = deployment['serving_token']
SERVING_ENDPOINT = f"{url}{deployment['endpoint']}"

# serving request
headers={'Authorization': SERVING_TOKEN, 'Content-Type': 'application/json'}
resp = requests.post(SERVING_ENDPOINT, data=open(param3, 'rb'), headers=headers, verify=False)
print (resp.text)

