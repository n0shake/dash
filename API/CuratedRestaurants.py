import requests
import json
import constants

from Utilities import Utilities

class CuratedRestaurants(object):
	"""docstring for Restaurants"""
	def __init__(self, authorization):
		super (CuratedRestaurants, self).__init__()
		self.authorization = authorization
		utilityObject = Utilities()
		currentLocationCoordinates = utilityObject.getCurrentLocation()
		self.longitude = currentLocationCoordinates[0]
		self.latitude = currentLocationCoordinates[1]

	def listOfCuratedRestaurantsForCustomerID(self,customerID):
	
		querystring = {"consumer_id":customerID,"lat":self.latitude,"lng":self.longitude}
		headers = {'accept': 'application/json','content-type': 'application/json','authorization' : self.authorization}
		response = requests.request("GET", constants.curatedCategoriesURL, headers=headers, params=querystring)
		data = json.loads(response.text)

		for suggestion in data[0].get('content'):
			print suggestion["name"]

 	def getTheWholeList(self):

 		querystring = {"lat":self.latitude,"lng":self.longitude, "order_type" :"asap", "sort_boost":"0", "limit" : "600"}
		headers = {'accept': 'application/json','content-type': 'application/json','authorization' : self.authorization}
		response = requests.request("GET", url, headers=headers, params=querystring)
		data = json.loads(response.text)

		for suggestion in data:
			print suggestion["name"]

	def getOnlyIndianRestaurants(self):

		querystring = {"lat":self.latitude,"limit":"200","lng":self.longitude,"order_type":"asap","query":"Indian","sort_boost":"0"}
		headers = {'authorization': self.authorization}
		response = requests.request("GET", constants.storeSearchURL, headers=headers, params=querystring)
		
		data = json.loads(response.text)
		return data

