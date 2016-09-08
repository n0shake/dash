import requests
import constants

class Order(object):
	"""docstring for Order"""
	def __init__(self, generatedToken):
		super(Order, self).__init__()
		self.generatedToken = generatedToken
		
	def currentCart(self):

		headers = {'authorization': self.generatedToken}
		try:
		 	response = requests.request("GET", constants.currentCartURL, headers=headers)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)
		 
		return response.text

	def orderCart(self):

		headers = {'authorization': self.generatedToken}
		try:
			response = requests.request("GET", constants.orderCartURL, headers=headers)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)

		return response.text




	