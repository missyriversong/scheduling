from django.test import TestCase
from datetime import datetime

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
# Create your tests here.


# # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
# python3 manage.py test
class Client(TestCase):
  def setupTestData(cls): 
    print("setUpTestData: Run once to set up non-modified data for all class methods.")
    pass

