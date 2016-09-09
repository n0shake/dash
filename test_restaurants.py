import unittest
from User import User
from Restaurant import Restaurant

class test_restaurants(unittest.TestCase):
	"""docstring for test_restaurants"""
	def setUp(self):
		self.userObject = User()
		self.authorizationToken = self.userObject.authenticate("frodo.baggins16@yandex.com", "frodobaggins")

	def test_restaurant_1(self):
		restaurantObject = Restaurant(3748, self.authorizationToken)
		self.assertEquals(restaurantObject.getMenuAndOtherRestaurantDetails()[0].get('id'), 89313)

	# Nirvana
	def test_restaurant_2(self):
		restaurantObject = Restaurant(2680, self.authorizationToken)
		self.assertEquals(restaurantObject.getMenuAndOtherRestaurantDetails()[0].get('id'), 3738)

	def tearDown(self):
		self.userObject = None

def main():
	unittest.main()

if __name__ == "__main__":
    main()