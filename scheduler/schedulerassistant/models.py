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


#should change to models format e.g. CharField?
class Client:
  def __init__(self, id: int, name: str, phone: int, txtype: str):    #?
    self.id = id
    self.name = name    
    self.phone = phone
    self.txtype = txtype
      

class Staff:
  def __init__(self, id: int, name: str, cert: str, ft_status: bool): 
    self.id = id
    self.name = name    
    self.cert = cert
    self.ft_status = ft_status


#class Clinic
    #self.name = name

class Sched:  #aka availability
  def __init__(self, date: datetime.date, start_time: datetime.time, end_time: datetime.time, available: bool, client: Client, staff: Staff):
    self.id = id
    self.date = date
    self.start_time = start_time
    self.end_time = end_time
    self.available = available    # e.g. 3/1/24, 8a-6p clinic open true
  # MtM clientid, staffid, clinicid? 
    

  client = models.ManyToManyField(Client)  
  staff = models.ManyToManyField(Staff)
  
  def client_avail(self, client: Client) -> bool:
    return self.client and self.available 


class Appt: 
  def __init__(self, date: datetime.date, start_time: datetime.time, end_time: datetime.time, client: Client, staff: Staff):
    self.id = id
    self.date = date
    self.start_time = start_time
    self.end_time = end_time

  # MtM: clientid, staffid?
    # client = models.ManyToManyField(Client)
    # staff = models.ManyToManyField(Staff)
  
  # https://www.freecodecamp.org/news/python-property-decorator/
  @property
  def check_tx(self, client: Client, staff: Staff) -> bool:
    return client.txtype == staff.cert

  @property
  def check_staff_avail(self, staff: Staff, sched: Sched) -> bool:    #MtM staff and sched?
    return Staff and sched.available == True

#  def book()
  # add client appointment 
    # if clinic is open -> schedule?       vs. appointment -> booked interaction btwn client and staff?
        # check if during hours of operation clinic
    # client available
    # staff type matches
      # if staff is available
        # if staff is working 8 hour shift, cannot book if no 1 hour lunch between 11a - 2p  



