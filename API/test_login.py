import unittest
from Dasher import Dasher

class test_login(unittest.TestCase):
	"""docstring for TestSuite"""
	def setUp(self):
		self.dasherObject = Dasher()
		self.authenticationToken = self.dasherObject.authenticate("chelsea1712@gmail.com", "Abhi1712!")

	def test_shit(self):
		self.assertNotEqual(self.dasherObject.generatedToken, None)

	def test_referral_information(self):
		referral_information = self.dasherObject.getReferralDetails()
		self.assertEqual(referral_information.get('referral_code'), "Abhishek-Banthia-7180")

	def test_profile_information_fetch(self):
		profileInformation = self.dasherObject.fetchProfileInformation()
		self.assertEqual(profileInformation.get('id'), 12607762)

	def tearDown(self):
		self.dasherObject = None

def main():
	unittest.main()

if __name__ == "__main__":
    main()


	
		
