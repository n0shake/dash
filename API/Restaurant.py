import requests
import json
from terminaltables import AsciiTable
from Dasher import Dasher
from Order import Order

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
		response = requests.request("GET", url, headers=headers)
		data = json.loads(response.text)
		headerArray = ["Name", "Title","Price"]
		itemArray = []
		itemArray.append(headerArray)
		itemNumber = 0
		itemID = []

		print("Restaurant status: "+data[0].get('status'))
		
		for category in data[0].get("menu_categories"): 
			items = category["items"]

			for item in items:
				detailArray = []
				itemNumber+=1
				itemID.append(item["id"])
				detailArray.append(str(itemNumber))
				detailArray.append(item["name"])
				detailArray.append(category["title"])
				detailArray.append(str(item["price"]/100 + .99))
				itemArray.append(detailArray)

		table = AsciiTable(itemArray)
		print table.table

		input = raw_input("You can add an item to the cart by entering a number or pressing q to quit: ")

		if input == "q":
			sys.exit(1)
		else:
			# Confirm quantity, special instructions and substitution preference
			quantity = raw_input("How many quantities of the item would you like? ")
			special_instructions = raw_input("If you have any special instructions, mention here or press s to skip: ")
			if special_instructions == "s":
				special_instructions = ""

			url = "https://api.doordash.com/v2/consumer/me/order/current_order/item/"

			payload = "{\"item\":"+str(itemID[int(input)-1])+", \"options\": [], \"quantity\":"+str(quantity)+", \"restaurant\":"+str(self.restaurantID)+", \"special_instructions\": \"\", \"substitution_preference\": \"refund\"}"
			headers = {'authorization': self.generatedToken,'content-type': "application/json"}
			response = requests.request("POST", url, data=payload, headers=headers)
			orderObject = Order(self.generatedToken)
			data = json.loads(orderObject.currentCart())
			currentOrder = data.get("orders")

			for order in currentOrder:
				orderItem = order["order_items"]
				for item in orderItem:
					
				print("You have ordered "+str(order["quantity"])+" of "+str(orderItem["name"])+" . Checkout ya delete?")