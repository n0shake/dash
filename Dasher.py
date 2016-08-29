import requests

class Dasher(object):
	"""docstring for Login"""
	def __init__(self):
		super(Dasher, self).__init__()
		self.generatedToken = None


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

	def fetchProfileInformation(self, username, password):

		 url = "https://api.doordash.com/v2/consumer/me/"
		 headers = {'authorization': self.authenticate(username, password)}
		 response = requests.request("GET", url, headers=headers)
		 
		 return response.json().get('id')

dasherObject = Dasher()
dasherObject.fetchProfileInformation("cahsdasd", "ahdasdh")