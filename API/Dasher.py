import requests
import constants

class Dasher(object):
	"""docstring for Login"""
	def __init__(self):
		super(Dasher, self).__init__()
		self.authorizationToken = None


	def authenticate(self,username, password):

		payload = "{\"email\": \""+username+"\",\"password\" :\""+password+"\"}"

		headers = {'accept': "application/json",'content-type': "application/json"}
		
		response = requests.request("POST", constants.authenticateURL, data=payload, headers=headers)

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
		 response = requests.request("GET", constants.profileInformationURL, headers=headers)

		 return response.json()

	def getReferralDetails(self):

		 headers = {'authorization': self.authorizationToken}
		 response = requests.request("GET", constants.referralDetailsURL, headers=headers)

		 return response.json()

	def callingCrashTracer(self):
		url = "https://crashtracer.apple.com/app/autocomplete_name"
		querystring = {"name_only":"true","nav_app_name":"Facebook"}
		response = requests.request("GET", url, params=querystring)
		print(response.text)
