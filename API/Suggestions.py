import requests
import constants
import json
from Dasher import Dasher
from Restaurant import Restaurant
from terminaltables import AsciiTable

class Suggestions(object):
	"""docstring for Suggestions"""
	def __init__(self, token):
		super(Suggestions, self).__init__()
		self.authorizationToken = token

	def retrieveSuggestions(self):
		querystring = {"get_suggestions":"1"}
		response = requests.request("GET", constants.suggestionsURL, params=querystring)
		data = json.loads(response.text)
		print data
		return data

	def listOfHotelsForSuggestion(self,suggestion):
		querystring = {"lat":"37.3896127","limit":"200","lng":"-121.9946316","order_type":"asap","query":suggestion,"sort_boost":"0"}
		response = requests.request("GET", constants.listForSuggestionURL, params=querystring)
		data = json.loads(response.text)
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

		user_input = raw_input("Select a restaurant number to see the menu: ")
		return restaurantIDs[int(user_input)-1]

dasherObject = Dasher()
dasherObject.authenticate("chelsea1712@gmail.com", "Abhi1712!")
suggestionObject = Suggestions(dasherObject.generatedToken)
restaurantSelected = suggestionObject.listOfHotelsForSuggestion("India")
restaurantObject = Restaurant(restaurantSelected,dasherObject.generatedToken)
restaurantObject.getMenuAndOtherRestaurantDetails()
