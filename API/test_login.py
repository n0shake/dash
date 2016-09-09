import unittest
from User import User

class test_login(unittest.TestCase):
	"""docstring for TestSuite"""
	def setUp(self):
		self.dasherObject = User()
		self.authorizationToken = self.dasherObject.authenticate("frodo.baggins16@yandex.com", "frodobaggins")

	def test_shit(self):
		self.assertNotEqual(self.dasherObject.authorizationToken, None)

	def test_referral_information(self):
		referral_information = self.dasherObject.getReferralDetails()
		self.assertEqual(referral_information.get('referral_code'), "Frodo-Baggins-4089")

	def test_profile_information_fetch(self):
		profileInformation = self.dasherObject.fetchProfileInformation()
		self.assertEqual(profileInformation.get('id'), 13693354)

	def tearDown(self):
		self.dasherObject = None

def main():
	unittest.main()

if __name__ == "__main__":
    main()


	
		
