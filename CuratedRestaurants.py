import requests
import json

class CuratedRestaurants(object):
	"""docstring for Restaurants"""
	def __init__(self, authorization):
		super (CuratedRestaurants, self).__init__()
		self.authorization = authorization


	def listOfCuratedRestaurantsForCustomerID(self,customerID):
		url = "https://api.doordash.com/v1/curated_categories/"
		querystring = {"consumer_id":customerID,"lat":"37.3896127","lng":"-121.9946316"}
		headers = {
	    'accept': 'application/json',
	    'content-type': 'application/json',
	     'authorization' : self.authorization}
		response = requests.request("GET", url, headers=headers, params=querystring)
		data = json.loads(response.text)

		for suggestion in data[0].get('content'):
			print suggestion["name"]

 	def getTheWholeList(self):

 		url = "https://api.doordash.com/v1/store_search/"
 		querystring = {"lat":"37.3896127","lng":"-121.9946316", "order_type" :"asap", "sort_boost":"0", "limit" : "600"}
		headers = {'accept': 'application/json','content-type': 'application/json','authorization' : self.authorization}

		response = requests.request("GET", url, headers=headers, params=querystring)
		data = json.loads(response.text)

		for suggestion in data:
			print suggestion["name"]