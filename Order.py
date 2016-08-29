
class Order(object):
	"""docstring for Order"""
	def __init__(self, generatedToken):
		super(Order, self).__init__()
		self.generatedToken = generatedToken
		
	def currentCart(self):

		 url = "https://api.doordash.com/v2/consumer/me/order_cart/current_cart/"
		 headers = {'authorization': self.generatedToken}
		 response = requests.request("GET", url, headers=headers)
		 return response.json()

	