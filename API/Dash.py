from User import User
from Suggestions import Suggestions
from Restaurant import Restaurant
from terminaltables import AsciiTable
import requests
from Order import Order
from Item import Item

class Dash(object):
	"""docstring for Dash"""
	def __init__(self):
		super(Dash, self).__init__()
		self.authorizationToken = None
		self.suggestionObject = None
		self.restaurantID = None
		self.currentSuggestion = None
		self.currentItemID = None
		self.currentItemQuantity = None
		self.currentSpecialInstruction = None
		self.substitutionPreference = None

	def beginDashing(self):
		userObject = User()
		userObject.authenticate("frodo.baggins16@yandex.com", "frodobaggins")
		self.authorizationToken = userObject.authorizationToken
		self.findSuggestions()

	def findSuggestions(self):
		self.suggestionObject = Suggestions(self.authorizationToken)
		choices = self.suggestionObject.retrieveSuggestions()
		self.listSuggestions(choices)
		user_selection = self.promptUserWithMessage("Enter the number corresponding to what'll like to order: ")
		isSelectionValid = self.validateUserSelectionWithRange(user_selection, 1, len(choices))
		if isSelectionValid == True:
			self.currentSuggestion = choices[int(user_selection)-1]
			self.findRestaurantsForSuggestion(self.currentSuggestion)
		else:
			print "Please enter a valid number between 1 and "+str(len(choices))

	def promptUserWithMessage(self, message):
		return raw_input(message)

	def validateUserSelectionWithRange(self, selection, startRange, endRange):
		isSelectionValid = True

		if selection.isdigit() == False:
			print "Please enter a valid digit."
			return

		if int(selection) < startRange or int(selection) > endRange:
			print selection, startRange, endRange
			isSelectionValid = False

		return isSelectionValid

	def listSuggestions(self,choices):
		headerArray = ["No", "What you'll like to order."]
		suggestionArray = []
		suggestionArray.append(headerArray)
		for index, choice in enumerate(choices):
			choiceArray = []
			choiceArray.append(index+1)
			choiceArray.append(choice)
			suggestionArray.append(choiceArray)
		table = AsciiTable(suggestionArray)
		print table.table

	def findRestaurantsForSuggestion(self, suggestion):
		print "Come inside findRestaurantsForSuggestion"
		restaurantsList = self.suggestionObject.listOfRestaurantsForSuggestion(suggestion)
		restaurantIDs = self.listRestaurants(restaurantsList)
		user_restaurantSelection = self.promptUserWithMessage("Select a restaurant number to see the menu: ")
		self.validateUserSelectionWithRange(user_restaurantSelection, 1, len(restaurantIDs))
		self.restaurantID = restaurantIDs[int(user_restaurantSelection)-1]
		self.fetchMenuForRestaurant(restaurantIDs[int(user_restaurantSelection)-1])

	def fetchMenuForRestaurant(self, restaurantID):
		restaurantObject = Restaurant(restaurantID,self.authorizationToken)
		data = restaurantObject.getMenuAndOtherRestaurantDetails()
		self.listMenuForSelectedRestaurant(data)	

	def listRestaurants(self,data):
			resultArray = []
			headerArray = ["No","Name", "Description", "Address", "Delivery Fees", "Rating", "Price Range", "Promotion"]
			restaurantIDs = []
			resultArray.append(headerArray)
			restaurantNumber = 0

			for restaurant in data:
				restaurantDetails = []
				restaurantNumber+=1
				restaurantDetails.append(str(restaurantNumber))
				restaurantDetails.append(restaurant["name"])
				restaurantDetails.append(restaurant["description"])
				restaurantDetails.append(restaurant["address"]["city"])
				restaurantDetails.append(str(restaurant["delivery_fee"]/100 + 0.99) )
				restaurantDetails.append(restaurant["composite_score"])
				restaurantDetails.append(restaurant["price_range"])
				restaurantDetails.append(restaurant["promotion"])
				restaurantIDs.append(restaurant["id"])
				resultArray.append(restaurantDetails)

			table = AsciiTable(resultArray)
			print table.table
			return restaurantIDs	

	def listMenuForSelectedRestaurant(self,data):
		headerArray = ["Number","Name", "Title","Price"]
		itemArray = []
		itemArray.append(headerArray)
		itemNumber = 0
		itemID = []

		if data[0].get('status') == "Closed":
			print "The restaurant you have selected is currently closed. :("
			return
		
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

		user_selection = self.promptUserWithMessage("You can add an item to the cart by entering a number or pressing q to quit: ")

		if self.validateUserSelectionWithRange(user_selection, 1, len(itemArray)) == False:
			return

		if user_selection == "q":
			sys.exit(1)
		else:
			self.currentItemQuantity = self.promptUserWithMessage("How many quantities of the item would you like? ")

			if self.currentItemQuantity.isdigit() == False:
				print "Quantity entered should be a number."
				return

			self.currentSpecialInstruction = self.promptUserWithMessage("If you have any special instructions, mention here or press s to skip: ")
			if self.currentSpecialInstruction == "s":
				self.currentSpecialInstruction = ""

			resultArray = []
			headerArray = ["Number", "Substitution Preference"]
			substitutionChoices = ["Contact me", "Go with Merchant Recommendation", "Refund this item", "Cancel the entire order"]
			resultArray.append(headerArray)
			for index, choice in enumerate(substitutionChoices):
					choiceArray = []
					choiceArray.append(index+1)
					choiceArray.append(choice)
					resultArray.append(choiceArray)

			table = AsciiTable(resultArray)
			print table.table

			self.substitution_preference = self.promptUserWithMessage("If the item is sold out, what's your prefence. Choose a number from the table above: ")

			if self.validateUserSelectionWithRange(self.substitution_preference, 1, 4) == False:
				print "Please select a valid number according to the table."
				return

			self.substitution_preference = "refund"
			self.itemID = itemID[int(user_selection) - 1]
			self.getOptionsForItem()

	def getOptionsForItem(self):

		print "Getting options for the selected item"

		itemObject = Item("JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmlnX2lhdCI6MTQ3MzM3MTkwNiwidXNlciI6eyJpc19zdGFmZiI6ZmFsc2UsImlkIjoxMjYyMDc5NCwiZW1haWwiOiJjaGVsc2VhMTcxMkBnbWFpbC5jb20ifSwiZXhwIjoxNDczMzkzNTA2fQ.8LIPuUXM2B0hsYL1tAWZLKvJGI7mT-PG0ODA6Vcx60k")
		itemDetails = itemObject.getItemOptions(self.restaurantID, self.itemID)

		self.listOptionsForItem(itemDetails)
	
	def listOptionsForItem(self, data):

		if not data.get('extras'):
			self.addOrderToCart([])
			return

		options = data.get('extras')

		tableArray = []
		headerArray = ["Number", "Title", "Type", "Description", "Price"]
		tableArray.append(headerArray)
		choiceID = []
		minimum_options = 0

		if options:
			for option in options:
				for index, choice in enumerate(option["options"]):
					optionArray = []
					choiceID.append(choice["id"])
					optionArray.append(index+1)
					optionArray.append(option["title"])
					optionArray.append(choice["name"])
					optionArray.append(choice["description"])
					optionArray.append(str(choice["price"] / 100))
					tableArray.append(optionArray)
				minimum_options = option["min_num_options"]

		table = AsciiTable(tableArray)
		print table.table
		orderArray = []

		if minimum_options == 1:
			choice_selection = self.promptUserWithMessage("You need to select a minimum of one option to proceed forward: ")
			if self.validateUserSelectionWithRange(choice_selection, 1, len(tableArray) - 1) == False:
				print "Enter a valid selection"
				return
			orderArray.append(choiceID[int(choice_selection) - 1])
			self.addOrderToCart(orderArray)
		else:
			choice_selection = self.promptUserWithMessage("You can add the above options or p to proceed: ")
			if choice_selection == "p":
				self.addOrderToCart([])
			else:
				orderArray.append(choiceID[int(choice_selection) - 1])
				self.addOrderToCart(orderArray)



	def addOrderToCart(self, options):

		orderObject = Order("JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmlnX2lhdCI6MTQ3MzM3MTkwNiwidXNlciI6eyJpc19zdGFmZiI6ZmFsc2UsImlkIjoxMjYyMDc5NCwiZW1haWwiOiJjaGVsc2VhMTcxMkBnbWFpbC5jb20ifSwiZXhwIjoxNDczMzkzNTA2fQ.8LIPuUXM2B0hsYL1tAWZLKvJGI7mT-PG0ODA6Vcx60k")
		data = orderObject.addItemToOrder(self.restaurantID, self.itemID,options, self.currentItemQuantity, self.currentSpecialInstruction, self.substitution_preference)

		self.showTheCurrentCart(data)

	def showTheCurrentCart(self, data):

		print "Your current cart is shown below:"
		tableData = []
		headerArray = ["No" ,"Item Name", "Quantity", "Special Instructions", "Price"]
		tableData.append(headerArray)

		item = data["item"]
		index = 0
		itemData = []
		itemData.append(index+1)
		itemData.append(item["name"])
		itemData.append(data["quantity"])
		itemData.append(data["special_instructions"])
		itemData.append(item["price"])
		tableData.append(itemData)
			

		table = AsciiTable(tableData)
		print table.table

		print "Enter 1 for checking out the menu of the current restaurant"
		print "Enter 2 for finding restaurants for your current suggestions"
		print "Enter 3 for looking at the list of suggestions"


		next_step = self.promptUserWithMessage("What do you want to do next? : ")

		# If the user wants to delete the whole cart, then show them the corresponding options here
		# Show option to go look at the menu of the current restaurant
		# Show option to go look at other restaurants for the current suggestion
		# Show option to go look at the various suggestions

		if self.validateUserSelectionWithRange(next_step, 1, 3) == True:
			
			if int(next_step) == 1:
				self.fetchMenuForRestaurant(self.restaurantID)
			elif int(next_step) == 2:
				self.findRestaurantsForSuggestion(self.currentSuggestion)
			else:
				self.findSuggestions()




if __name__ == "__main__":
	dashObject = Dash()
	dashObject.beginDashing()
	# dashObject.getOptionsForItem(3248, 186619)

			