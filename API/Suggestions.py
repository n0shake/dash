import requests
import constants
import json
from Dasher import Dasher
from Restaurant import Restaurant
from terminaltables import AsciiTable

class Suggestions(object):
	"""docstring for Suggestions"""
	def __init__(self, token):
		super(Suggestions, self).__init__()
		self.authorizationToken = token

	def getTheWholeList(self):

 		querystring = {"lat":self.latitude,"lng":self.longitude, "order_type" :"asap", "sort_boost":"0", "limit" : "600"}
		headers = {'accept': 'application/json','content-type': 'application/json','authorization' : self.authorization}
		response = requests.request("GET", url, headers=headers, params=querystring)
		data = json.loads(response.text)

		for suggestion in data:
			print suggestion["name"]

	def listOfCuratedRestaurantsForCustomerID(self,customerID):
	
		querystring = {"consumer_id":customerID,"lat":"37.3896127","lng":"-121.9946316"}
		headers = {'accept': 'application/json','content-type': 'application/json','authorization' : self.authorization}
		response = requests.request("GET", constants.curatedCategoriesURL, headers=headers, params=querystring)
		data = json.loads(response.text)

		for suggestion in data[0].get('content'):
			print suggestion["name"]

	def retrieveSuggestions(self):
		querystring = {"get_suggestions":"1"}
		response = requests.request("GET", constants.suggestionsURL, params=querystring)
		data = json.loads(response.text)
		return data

	def listOfHotelsForSuggestion(self,suggestion):
		querystring = {"lat":"37.3896127","limit":"200","lng":"-121.9946316","order_type":"asap","query":suggestion,"sort_boost":"0"}
		response = requests.request("GET", constants.listForSuggestionURL, params=querystring)
		data = json.loads(response.text)
		return data

