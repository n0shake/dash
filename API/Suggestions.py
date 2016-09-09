import requests
import constants
import json
import sys

class Suggestions(object):
	"""docstring for Suggestions"""
	def __init__(self, token, currentLocation):
		super(Suggestions, self).__init__()
		self.authorizationToken = token
		self.location = currentLocation

	def listOfCuratedRestaurantsForCustomerID(self,customerID):
	
		querystring = {"consumer_id":customerID,"lat":self.location.latitude,"lng":self.location.longitude}
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

		querystring = {"lat":self.location.latitude,"limit":"200","lng":self.location.longitude,"order_type":"asap","query":suggestion,"sort_boost":"0"}
		try:
			response = requests.request("GET", constants.listForSuggestionURL, params=querystring)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)
		
		data = json.loads(response.text)
		return data

