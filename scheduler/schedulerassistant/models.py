from django.db import models
from datetime import datetime
# https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/
# https://www.geeksforgeeks.org/how-to-convert-datetime-to-date-in-python/
# https://www.geeksforgeeks.org/extract-time-from-datetime-in-python/


#behavior first
  # add client appointment 
    # if clinic is open -> schedule?       vs. appointment -> booked interaction btwn client and staff?
        # check if during hours of operation clinic
    # client available
    # staff type matches
      # if staff is available
        # if staff is working 8 hour shift, cannot book if no 1 hour lunch between 11a - 2p 
  # if all this matches and appt has been added, mark them as unavailable?  


# Create your models here.


class Client:
  def __init__(self, name: str, phone: int, txtype: str):    #?
    self.name = name    
    self.phone = phone
    self.txtype = txtype

class Staff:
  def __init__(self, name: str, cert: str, ft_status: bool): 
    self.name = name    
    self.cert = cert
    self.ft_status = ft_status

#class Clinic
    #self.name = name

class Sched:  #aka availability
  def __init__(self, date: datetime.date, start_time: datetime.time, end_time: datetime.time, available: bool):
    self.date = date
    self.start_time = start_time
    self.end_time = end_time
    self.available = available    # e.g. 3/1/24, 8a-6p clinic open true
  # 1tM clientid, staffid, clinicid? 
    

class Appt: 
  def __init__(self, date: datetime.date, start_time: datetime.time, end_time: datetime.time):
    self.date = date
    self.start_time = start_time
    self.end_time = end_time
  # MtM: clientid, staffid
    
 
  # add client appointment 
    # if clinic is open -> schedule?       vs. appointment -> booked interaction btwn client and staff?
        # check if during hours of operation clinic
    # client available
    # staff type matches
      # if staff is available
        # if staff is working 8 hour shift, cannot book if no 1 hour lunch between 11a - 2p  



