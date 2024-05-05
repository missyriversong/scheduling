from django.test import TestCase
from datetime import datetime, date, time   #???maybe this
from .models import Client, Staff, Appt
from rest_framework import status, routers
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse

from .views import ClientViewSet, StaffViewSet, ApptViewSet
# #https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
# # Create your tests here.


# # # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
# # python3 manage.py test

# class Client(TestCase):
#   def setup(self): 
#     # Setup run before every test method.
#     Client.objects.create(first_name = 'Kyle', last_name='K', txtype='pt')

#   def test_first_name(self):
#     client = Client.objects.get(id=1)
  


#   def tearDown(self):
#     # Clean up run after every test method.
#     pass


# #make tests to validate fields
# #make tests to check each 

# import unittest
# #comment out cntl /
# # https://docs.python.org/3/library/unittest.html
# # https://docs.python.org/3/library/unittest.html#class-and-module-fixtures
# class Appointment(unittest.TestCase): 
#   def match_tx_type(self):   
#     self.assertEquals(1, 1)  #client_tx, staff_tx
#   def match_dos(self):
#     self.assertEquals('date', 'date')
  


# #identify available appointments on date between time 1 and time 2 and tx=whatever
#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
#  ./manage.py test schedulerassistant.tests.ModelTests   #errors with class Meta ughhh

class ModelTests(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            id=11,
            first_name="shel",
            last_name="smith",
            txtype="ot",
            email="ssmith@example.com"
        )
        self.staff = Staff.objects.create(
            id=12,
            first_name="jen",
            last_name="johnson",
            cert="ot",
            email="jjohnson@example.com"
        )
        self.appt = Appt.objects.create(
            id=13,
            date='07, 07, 2023',  #doesnt work..
            start_time='07:30',   # ??
            end_time='08:30', 
            service='ot',
            client=11,   #or is it client=client...?  client=Client(etc...)
            staff=12,
        )

    def test_client(self):
        client = Client.objects.get(id=11)
        self.assertEqual(client.first_name, "shel")
        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(Client.objects.get(id=11).service, "ot")
    
    def test_staff(self):
        staff = Staff.objects.get(id=12)
        self.assertEqual(staff.email, "jjohnson@example.com")
    
    def test_appt(self):
        appt = Appt.objects.get(id=13)
        self.assertEqual(appt.date, "07, 07, 2023")
        self.assertEqual(appt.start_time, "07:30")
        self.assertEqual(Appt.objects.count(), 2)
        self.assertEqual(Appt.objects.get(id=13).client_id, 11)        




#  ./manage.py test schedulerassistant.tests.AppTests  
class ApptTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.appt = Appt.objects.create(
            id=1,
            date='07, 08, 2023',  #doesnt work..
            start_time='08:00',   # ??
            end_time='09:00', 
            service='pt',
            client=1,
            staff=1,
        )
        # trying to figure out how date and time data looks for testing..
        #https://www.ericholscher.com/blog/2008/aug/14/using-mock-objects-django-and-python-testing/
        #https://www.geeksforgeeks.org/datefield-django-models/
        #https://www.geeksforgeeks.org/python-datetime-module/  not sure?  

        self.list_url = reverse("schedulerassistant:appt-list")
        self.detail_url = reverse(
            "schedulerassistant:appt-detail", kwargs={"pk": self.appt.id}
        )

    def test_create_appt(self):
        data = {
            "id": 2,
            "date": "07, 09, 2023",
            "start_time": "10:00",
            "end_time": "11:00",
            "service": "ot",
            "client": 3,
            "staff": 4,   #not sure if this fk data makes sense..?
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(Appt.objects.count(), 2)
        self.assertEqual(Appt.objects.get(id=2).service, "ot")

    def test_list_appts(self):
        response = self.client.get(self.list_url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["results"][0]["id"], self.appt.id)

    def test_retrieve_appt(self):
        response = self.client.get(self.detail_url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["id"], self.appt.id)

    def test_delete_appt(self):

        response = self.client.delete(
            reverse("schedulerassistant:appt-detail", kwargs={"pk": self.appt.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Appt.objects.count(), 0)

    def test_update_appt(self):
        data = {
            "id": 2,
            "date": "07, 09, 2023",
            "start_time": "12:00",
            "end_time": "13:00",
            "service": "ot",
            "client": 3,
            "staff": 4,   
        }
        response = self.client.put(
            reverse("schedulerassistant:appt-detail", kwargs={"pk": self.appt.id}),
            data,
            format="json",
        )
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["start_time"], "12:00")


