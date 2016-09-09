import requests
import constants
import json

class Suggestions(object):
	"""docstring for Suggestions"""
	def __init__(self, token):
		super(Suggestions, self).__init__()
		self.authorizationToken = token

	def listOfCuratedRestaurantsForCustomerID(self,customerID):
	
		querystring = {"consumer_id":customerID,"lat":"37.3896127","lng":"-121.9946316"}
		headers = {'accept': 'application/json','content-type': 'application/json','authorization' : self.authorization}
		try:
			response = requests.request("GET", constants.curatedCategoriesURL, headers=headers, params=querystring)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)

		data = json.loads(response.text)

		for suggestion in data[0].get('content'):
			print suggestion["name"]

	def retrieveSuggestions(self):

		querystring = {"get_suggestions":"1"}
		try:
			response = requests.request("GET", constants.suggestionsURL, params=querystring)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)

		data = json.loads(response.text)
		return data

	def listOfRestaurantsForSuggestion(self,suggestion):

		querystring = {"lat":"37.3896127","limit":"200","lng":"-121.9946316","order_type":"asap","query":suggestion,"sort_boost":"0"}
		try:
			response = requests.request("GET", constants.listForSuggestionURL, params=querystring)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)
		
		data = json.loads(response.text)
		return data

