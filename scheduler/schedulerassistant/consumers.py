import asyncio
import datetime
import json

# Django
from channels.consumer import AsyncConsumer, SyncConsumer   #?https://channels.readthedocs.io/en/stable/topics/consumers.html     sync..?
from channels.generic.http import AsyncHttpConsumer

# Local
from schedulerassistant.models import Appt

#helpful for everyone
class SimpleApptConsumer(AsyncConsumer):
    async def print_appt(self, message):
        print(f"WORKER: Appointment: {message['data']}")

#for client onboarding 
class SimpleClientConsumer(AsyncConsumer):
    async def print_client(self, message):
        print(f"WORKER: Client: {message['data']}")

#for staff orientation hr and clinical training
class SimpleStaffConsumer(AsyncConsumer):
    async def print_staff(self, message):
        print(f"WORKER: Staff: {message['data']}")