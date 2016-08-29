import requests

class Login(object):
	"""docstring for Login"""
	def __init__(self):
		super(Login, self).__init__()


	def authenticate(self,username, password):
		url = "https://api.doordash.com/v2/auth/token/"
		payload = "{\"email\": \"chelsea1712@gmail.com\",\"password\" : \"Abhi1712!\"}"

		headers = {
		    'accept': "application/json",
		    'content-type': "application/json"
		    }
		
		response = requests.request("POST", url, data=payload, headers=headers)

		if response.reason == "OK":
			authorizationHeader = []
			authorizationHeader.append("JWT ")
			authorizationHeader.append(response.json().get('token'))
			return ''.join(authorizationHeader)
		else:
			print response.reason
