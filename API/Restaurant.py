import requests
import json
import sys

class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self, details,authorizationToken):
		super(Restaurant, self).__init__()
		self.restaurantID = details
		# self.status = details["status"]
		self.generatedToken = authorizationToken

	def getMenuAndOtherRestaurantDetails(self):

		url = "https://api.doordash.com/v2/restaurant/"+str(self.restaurantID)+"/menu/"
		headers = {'authorization': self.generatedToken}
		try:
			response = requests.request("GET", url, headers=headers)
		except:
			print e.cause
			sys.exit(1)

		data = json.loads(response.text)
		return data