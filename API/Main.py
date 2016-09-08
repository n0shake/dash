from Dasher import Dasher
from Suggestions import Suggestions
from Restaurant import Restaurant
from terminaltables import AsciiTable
import json
import requests
from Order import Order

def beginDashing():
	dasherObject = Dasher()
	dasherObject.authenticate("chelsea1712@gmail.com", "Abhi1712!")
	listSuggestions(dasherObject.authorizationToken)

def listSuggestions(authorizationToken):
	suggestionObject = Suggestions(authorizationToken)
	choices = suggestionObject.retrieveSuggestions()
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
	user_selection = promptUserWithMessage("Enter the number corresponding to what'll like to order: ")
	listHotelsForSuggestions(choices[int(user_selection)-1], suggestionObject)

def promptUserWithMessage(message):
	return raw_input(message)	

def listHotelsForSuggestions(suggestion, suggestionObject):
	restaurantsList = suggestionObject.listOfHotelsForSuggestion(suggestion)
	restaurantIDs = listHotels(restaurantsList)
	user_restaurantSelection = promptUserWithMessage("Select a restaurant number to see the menu: ")
	restaurantObject = Restaurant(restaurantIDs[int(user_restaurantSelection)-1],suggestionObject.authorizationToken)
	data = restaurantObject.getMenuAndOtherRestaurantDetails()
	listMenuForSelectedRestaurant(data, suggestionObject.authorizationToken)

def listHotels(data):
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

def listMenuForSelectedRestaurant(data, authorizationToken):
	print data
	headerArray = ["Number","Name", "Title","Price"]
	itemArray = []
	itemArray.append(headerArray)
	itemNumber = 0
	itemID = []

	if data[0].get('status') == "Closed":
		print "The restaurant you have selected is currently closed"
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

	user_selection = promptUserWithMessage("You can add an item to the cart by entering a number or pressing q to quit: ")

	if user_selection == "q":
		sys.exit(1)
	else:
		# Confirm quantity, special instructions and substitution preference
		quantity = promptUserWithMessage("How many quantities of the item would you like? ")
		special_instructions = promptUserWithMessage("If you have any special instructions, mention here or press s to skip: ")
		if special_instructions == "s":
			special_instructions = ""

	# Add order to the current cart
	# List the cart in a tabular format

def listOrderCart(authorizationToken):
	print "Let's print some order cart."


if __name__ == "__main__":
	beginDashing()
