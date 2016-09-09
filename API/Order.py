import requests
import json
import constants
import sys

class Order(object):
	"""docstring for Order"""
	def __init__(self, authorizationToken):
		super(Order, self).__init__()
		self.authorizationToken = authorizationToken
		
	def currentCart(self):

		headers = {'authorization': self.authorizationToken}
		try:
		 	response = requests.request("GET", constants.currentCartURL, headers=headers)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)
		 
		return response.text

	def orderCart(self):

		headers = {'authorization': self.authorizationToken}
		try:
			response = requests.request("GET", constants.orderCartURL, headers=headers)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)

		return response.text

	def addItemToOrder(self, restaurantID, itemID, options, quantity, special_instructions, substitution_preference):

		print "Adding item to order."
		options_in_string = ",".join(str(x) for x in options)
		payload = "{\"item\": \""+str(itemID)+"\", \"options\": ["+options_in_string+"], \"quantity\": "+str(quantity)+", \"restaurant\": \""+str(restaurantID)+"\", \"special_instructions\": \""+special_instructions+"\", \"substitution_preference\": \""+substitution_preference+"\"}"
		headers = {'authorization': self.authorizationToken, 'content-type': "application/json"}
		try:
			response = requests.request("POST", constants.addItemToCartURL, data=payload, headers=headers)
		except Exception, e:
			print e.cause
			sys.exit(1)
		
		data = json.loads(response.text)
		return data



	