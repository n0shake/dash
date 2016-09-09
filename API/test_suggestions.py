import unittest
from User import User
from Suggestions import Suggestions
from geopy.geocoders import Nominatim

class test_suggestions(unittest.TestCase):
	"""docstring for TestSuite"""
	def setUp(self):
		userObject = User()
		authorizationToken = userObject.authenticate("frodo.baggins16@yandex.com", "frodobaggins")
		geolocator = Nominatim()
		currentLocation = geolocator.geocode("650 Almanor Avenue Sunnyvale California")
		self.suggestionObject = Suggestions(authorizationToken, currentLocation)

	def test_suggestions(self):
		suggestions = self.suggestionObject.retrieveSuggestions()
		comparingList = ["Mexican", "Sushi", "Indian", "Pizza", "Breakfast", "BBQ", "Chinese", "Thai", "Italian"]
		self.assertItemsEqual(suggestions, comparingList)

	def test_restaurantListForASuggestion(self):
		restList = self.suggestionObject.listOfRestaurantsForSuggestion("Sushi")
		self.assertEquals(type(restList), list)


	def tearDown(self):
		self.userObject = None

def main():
	unittest.main()

if __name__ == "__main__":
    main()


	
		
