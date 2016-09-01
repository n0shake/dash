import unittest
from Dasher import Dasher
from Suggestions import Suggestions

class test_suggestions(unittest.TestCase):
	"""docstring for TestSuite"""
	def setUp(self):
		self.dasherObject = Dasher()
		self.authenticationToken = self.dasherObject.authenticate("chelsea1712@gmail.com", "Abhi1712!")

# dasherObject = Dasher()
# dasherObject.authenticate("chelsea1712@gmail.com", "Abhi1712!")

# restaurantSelected = suggestionObject.listOfHotelsForSuggestion("India")
# restaurantObject = Restaurant(restaurantSelected,dasherObject.generatedToken)
# restaurantObject.getMenuAndOtherRestaurantDetails()


	def test_restaurantListForASuggestion(self):
		suggestionObject = Suggestions(dasherObject.generatedToken)
		self.assertNotEqual(self.dasherObject.generatedToken, None)

	def tearDown(self):
		self.dasherObject = None

def main():
	unittest.main()

if __name__ == "__main__":
    main()


	
		
