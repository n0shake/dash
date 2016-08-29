import requests
from CuratedRestaurants import CuratedRestaurants

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
			self.generatedToken = ''.join(authorizationHeader)
		else:
			print response.reason

	def fetchProfileInformation(self, username, password):

		 self.authenticate(username, password)

		 url = "https://api.doordash.com/v2/consumer/me/"
		 headers = {'authorization': self.generatedToken}
		 response = requests.request("GET", url, headers=headers)

		 return response.json().get('id')

	def getReferrelDetails(self):

		 url = "https://api.doordash.com/v2/consumer/me/referral_detail/"
		 headers = {'authorization': self.generatedToken}
		 response = requests.request("GET", url, headers=headers)

		 return response.json()

dasherObject = Dasher()
restaurantList = CuratedRestaurants(dasherObject.authenticate("asdasd", "sadasjkd"))
restaurantList.getTheWholeList()