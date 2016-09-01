import requests
import constants

class Order(object):
	"""docstring for Order"""
	def __init__(self, generatedToken):
		super(Order, self).__init__()
		self.generatedToken = generatedToken
		
	def currentCart(self):

		 headers = {'authorization': self.generatedToken}
		 response = requests.request("GET", constants.currentCartURL, headers=headers)
		 return response.json()

	def orderCart(self):

		 headers = {'authorization': self.generatedToken}
		 response = requests.request("GET", constants.orderCartURL, headers=headers)
		 return response.json()




	