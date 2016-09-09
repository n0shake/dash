import requests
import constants
import sys

class User(object):
	"""docstring for Login"""
	def __init__(self):
		super(User, self).__init__()
		self.authorizationToken = None


	def authenticate(self,username, password):

		payload = "{\"email\": \""+username+"\",\"password\" :\""+password+"\"}"
		headers = {'accept': "application/json",'content-type': "application/json"}
		
		try:
			response = requests.request("POST", constants.authenticateURL, data=payload, headers=headers)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)

		if response.reason == "OK":
			authorizationHeader = []
			authorizationHeader.append("JWT ")
			authorizationHeader.append(response.json().get('token'))
			self.authorizationToken = ''.join(authorizationHeader)
			return self.authorizationToken
		else:
			print response.reason
			return response.reason

	def fetchProfileInformation(self):

		headers = {'authorization': self.authorizationToken}
		try:
		 	response = requests.request("GET", constants.profileInformationURL, headers=headers)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)

		return response.json()

	def getReferralDetails(self):

		headers = {'authorization': self.authorizationToken}
		try:
			response = requests.request("GET", constants.referralDetailsURL, headers=headers)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)

		return response.json()
