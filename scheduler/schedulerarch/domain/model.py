from datetime import datetime, date, time

class DomainClient():
  def __init__(self, id, first_name, last_name,txtype, email, date_added):
    self.id = id
    self.first_name =  first_name
    self.last_name = last_name
    self.txtype = txtype
    self.email = email
    self.date_added =  date_added

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class DomainStaff():
  def __init__(self, id, first_name, last_name, cert, email, date_added):
    self.id = id
    self.first_name =  first_name
    self.last_name = last_name
    self.cert = cert
    self.email = email
    self.date_added =  date_added

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class DomainAppt():
  def __init__(self, date, start_time, end_time, service, client_id, staff_id, date_added):
    self.id = id
    self.date = date     #?  self.datetime.date?  
    self.start_time = start_time
    self.end_time = end_time
    self.service = service
    self.client_id = client_id
    self.staff_id = staff_id   #?  .id...
    self.date_added =  date_added

  def __str__(self):
    return f"{self.date}: {self.start_time}-{self.end_time}"
  

  #https://medium.com/@a01700762/test-forms-with-foreign-keys-in-django-7efc91178a5c  ?