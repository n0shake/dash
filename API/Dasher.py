import requests
import constants

class Dasher(object):
	"""docstring for Login"""
	def __init__(self):
		super(Dasher, self).__init__()
		self.generatedToken = None


	def authenticate(self,username, password):

		payload = "{\"email\": \""+username+"\",\"password\" :\""+password+"\"}"

		headers = {'accept': "application/json",'content-type': "application/json"}
		
		response = requests.request("POST", constants.authenticateURL, data=payload, headers=headers)

		if response.reason == "OK":
			authorizationHeader = []
			authorizationHeader.append("JWT ")
			authorizationHeader.append(response.json().get('token'))
			self.generatedToken = ''.join(authorizationHeader)
			return self.generatedToken
		else:
			print response.reason
			return response.reason

	def fetchProfileInformation(self):

		 headers = {'authorization': self.generatedToken}
		 response = requests.request("GET", constants.profileInformationURL, headers=headers)

		 return response.json()

	def getReferrelDetails(self):

		 headers = {'authorization': self.generatedToken}
		 response = requests.request("GET", constants.referralDetailsURL, headers=headers)

		 return response.json()
