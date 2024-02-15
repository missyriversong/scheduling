from django.test import TestCase
from datetime import datetime

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
# Create your tests here.


class Client:
  def __init__(self, name: str, phone: int, cert: str, txtype: str, ft_status: bool): 
    self.name = name    
    self.phone = phone
    self.txtype = txtype
    self.ft_status = ft_status

class Staff:
  def __init__(self, name: str, cert: str, ft_status: bool): 
    self.name = name    
    self.cert = cert
    self.ft_status = ft_status
    
# class Schedule:
#   def __init__(self, date: datetime.date, start_time: datetime.time, end_time: datetime.time):
#     self.date = date
#     self.start_time = start_time
#     self.end_time = end_time


add client
add client txtype


