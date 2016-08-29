import requests
import json

url = "https://api.doordash.com/v2/auth/token/"

payload = "{\n    \"email\": \"chelsea1712@gmail.com\",\n    \"password\" : \"Abhi1712!\"\n}"
headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

authorizationHeader = []
authorizationHeader.append("JWT ")
authorizationHeader.append(response.json().get('token'))

url = "https://api.doordash.com/v2/consumer/me/"

headers = {'authorization': ''.join(authorizationHeader)}

print(headers)

response = requests.request("GET", url, headers=headers)

print(response.json().get('first_name') + " is logged in")
print(response.json().get('default_address').get('printable_address'))

url = "https://api.doordash.com/v1/consumer_search/"

querystring = {"get_suggestions":"1"}
response = requests.request("GET", url, headers=headers, params=querystring)

url = "https://api.doordash.com/v1/curated_categories/"

querystring = {"consumer_id":"12607762","lat":"37.3896127","lng":"-121.9946316"}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

for suggestion in data[0].get('content'):
	print suggestion["name"]
