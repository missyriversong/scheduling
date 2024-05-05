# from django.db import models
# from datetime import datetime
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
# class Client:
#   def __init__(self, id: int, name: str, phone: int, txtype: str):    #?
#     self.id = id
#     self.name = name    
#     self.phone = phone
#     self.txtype = txtype

# class Staff:
#   def __init__(self, id: int, name: str, cert: str, ft_status: bool): 
#     self.id = id
#     self.name = name    
#     self.cert = cert
#     self.ft_status = ft_status


#class Clinic
    #self.name = name

# class Sched:  #aka availability
#   def __init__(self, date: datetime.date, start_time: datetime.time, end_time: datetime.time, available: bool, client: Client, staff: Staff):
#     self.id = id
#     self.date = date
#     self.start_time = start_time
#     self.end_time = end_time
#     self.available = available    # e.g. 3/1/24, 8a-6p clinic open true
  # MtM clientid, staffid, clinicid? 



  # def client_avail(self, client: Client) -> bool:
  #   return self.client and self.available 


# class Appt: 
#   def __init__(self, date: datetime.date, start_time: datetime.time, end_time: datetime.time, client: Client, staff: Staff):
#     self.id = id
#     self.date = date

#     self.start_time = start_time
#     self.end_time = end_time

#   # MtM: clientid, staffid?
#     # client = models.ManyToManyField(Client)
#     # staff = models.ManyToManyField(Staff)
  
#   # https://www.freecodecamp.org/news/python-property-decorator/
#   @property
#   def check_tx(self, client: Client, staff: Staff) -> bool:
#     return client.txtype == staff.cert

#   @property
#   def check_staff_avail(self, staff: Staff, sched: Sched) -> bool:    #MtM staff and sched?
#     return Staff and sched.available == True

  
#  def book()
  # add client appointment 
    # if clinic is open -> schedule?       vs. appointment -> booked interaction btwn client and staff?
        # check if during hours of operation clinic
    # client available
    # staff type matches
      # if staff is available
        # if staff is working 8 hour shift, cannot book if no 1 hour lunch between 11a - 2p  



#not sure when i did the above...starting over:
#identify available appointments on date between time 1 and time 2 and tx=whatever
# bare min-> status available_appointment T/F,  date, start_time, end_time, client_txtype == staff_txtype
# if i have time: -> never on weekend, Saturday, Sunday;  designated holidays..manually enter;  before 8a or after 6p...
# some day to do: -> constraint that every staff had 1 hour lunch booked...?



# from django import datetime

# go come back to this if have time
# class Availability(models.Model):
#   date = models.DateTimeField().date
#   starttime = models.DateTimeField().time  #  how would you specify datetime.time?  if it's a property
#   endtime = models.DateTimeField().time 
#   client = models.ManyToManyField(Client)  
#   staff = models.ManyToManyField(Staff)
#   available = models.BooleanField(default=False)


  
#   def add_staff_available(self, date, starttime, endtime, staff.id):  #?
#     staff_avail = Availability(date = '', starttime = '', endtime = '', available = True)
#     #how would you connect to specific staff?
#     staff_avail.save()

# #params where clients = date
#   def check_available(date, starttime, endtime, staff_avail):
#     if date == staff_avail.date and starttime >= staff_avail.starttime and endtime <= staff_avail.endtime
#     #learn how to pull it by staff 
#     return True
  
  #maybe focus on if staff type = client type then book appointmetn?


#would this go in as services...? adding too much in here?  
#   def check_tx_match(client.txtype, staff.cert)
#     if client.txtype == staff.cert
#     #need staff id

# #use staff ids, to loop through and check_available()

# #if staff available then book appt

# check if available...

#   def book_appt()
    #change avail to false in Avaibility for client and staff

#https://www.codewithjason.com/difference-domains-domain-models-object-models-domain-objects/

from django.db import models
from schedulerarch.domain.model import DomainClient, DomainStaff, DomainAppt

class Client(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  txtype = models.CharField(max_length=5)
  email = models.EmailField(max_length=50)
  date_added = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  
#txtype maybe better as list of tx types 
  class Meta:
    app_label = "schedulerassistant"
#https://docs.djangoproject.com/en/5.0/ref/models/options/

    @staticmethod
    def update_from_domain(domain_client: DomainClient):
        try:
            client = Client.objects.get(id=domain_client.id)
        except Client.DoesNotExist:
            client = Client(id=domain_client.id)

        client.id = domain_client.id
        client.first_name = domain_client.first_name
        client.last_name = domain_client.last_name
        client.txtype = domain_client.txtype
        client.email = domain_client.email
        client.save()

    def to_domain(self) -> DomainClient:
        client = DomainClient(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            txtype=self.txtype,
            email=self.email,
            date_added=self.date_added,
        )
        return client


class Staff(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  cert = models.CharField(max_length=5)
  email = models.EmailField(max_length=50)
  date_added = models.DateField(auto_now_add=True)

# cert maybe change to list of credentials...

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  
  class Meta:
    app_label = "schedulerassistant"

    @staticmethod
    def update_from_domain(domain_staff: DomainStaff):
        try:
            staff = Staff.objects.get(id=domain_staff.id)
        except Staff.DoesNotExist:
            staff = Staff(id=domain_staff.id)

        staff.id = domain_staff.id
        staff.first_name = domain_staff.first_name
        staff.last_name = domain_staff.last_name
        staff.cert = domain_staff.cert
        staff.email = domain_staff.email
        staff.save()

    def to_domain(self) -> DomainStaff:
        staff = DomainStaff(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            cert=self.cert,
            email=self.email,
            date_added=self.date_added,
        )
        return staff
    
class Appt(models.Model):
  date = models.DateField()
  start_time = models.TimeField()
  end_time = models.TimeField()
  service = models.CharField(max_length=5)
  client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_appts")  
  staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_appts')
  # available = models.BooleanField(default=False)
  date_added = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.date}: {self.start_time}-{self.end_time}"
    
  class Meta:
    app_label = "schedulerassistant"


    @staticmethod
    def update_from_domain(domain_appt: DomainAppt):
        try:
            appt = Appt.objects.get(id=domain_appt.id)
        except Appt.DoesNotExist:
            appt = Appt(id=domain_appt.id)

        appt.id = domain_appt.id
        appt.date = domain_appt.date
        appt.start_time = domain_appt.start_time
        appt.end_time = domain_appt.end_time
        appt.service = domain_appt.service
        appt.client = domain_appt.client_id  #? not sure if this is right...client_id or client.id
        appt.staff = domain_appt.staff_id
        appt.save()

        #https://docs.djangoproject.com/en/5.0/topics/db/queries/#using-a-custom-reverse-manager?  

    def to_domain(self) -> DomainAppt:
        appt = DomainAppt(
            id=self.id,
            date=self.date,
            start_time=self.start_time,
            end_time=self.end_time,
            service=self.service,
            client = self.client_id,
            staff = self.client_id,
            date_added=self.date_added,
        )
        return appt
#related name?  https://docs.djangoproject.com/en/5.0/ref/models/options/
#https://mrprabhatmishra.medium.com/how-to-use-related-name-attribute-in-django-model-db6c7d8d20cf


# book appt
# 1. bene gives scheduling team date and service, scheduling staff will either put in their preferred time or clinic hours of operation?  -> seems inefficient
# #what if only afternoons..optional search params...?
# 2. gets list of open time slots for the date by service
# 3. bene selects and books date time service    or  restart process

#i don't know..
# def search_open_sessions(date, service):
#   open_hours = {} ?

# def get_open_sessions(date, staff, service):   #service or staff?
 
def book_appt(date, start_time, end_time, service, client, staff):
  booked_appts = Appt.objects.filter(date=date, staff=staff)  #show us all the appts where staff are booked?   .values?
  for booked_appt in booked_appts:
    #booked appt 9-10, you can't book 8-11, 9a start, 9:59a end 
    if (start_time <= booked_appt.start_time and end_time >= booked_appt.end_time) or (book_appt.start_time <= start_time < book_appt.end_time) or (book_appt.start_time < end_time <= book_appt.end_time):
      return None
  
  appt = Appt.objects.create(date=date, start_time=start_time, end_time=end_time, service=service, client=client, staff=staff)

  return appt

