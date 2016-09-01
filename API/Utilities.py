import requests
import json
import sys
import constants

class Utilities(object):
	"""docstring for Utilities"""
	def __init__(self):
		super(Utilities, self).__init__()
	
	def getCurrentLocation(self):
		try:
			response = requests.request("GET", constants.locationURL)
		except requests.exceptions.RequestException as e:
			print e.cause
			sys.exit(1)

		latitude = response.json().get("latitude")
		longitude = response.json().get("longitude")
		return str(longitude),str(latitude)