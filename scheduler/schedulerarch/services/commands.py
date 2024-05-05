import sys
from abc import ABC, abstractmethod
from datetime import datetime
import requests
from injector import Injector, inject   
import pytz
#add database

import requests
from django.db import transaction

from schedulerassistant.models import Appt, Staff, Client
from schedulerarch.domain.model import DomainAppt, DomainStaff, DomainClient


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("A command must implement the execute method")


class PythonTimeStampProvider:
    def __init__(self):
        self.now = datetime.now(pytz.UTC).isoformat()


class AddApptCommand(Command):
    @inject
    def __init__(self, now: PythonTimeStampProvider = PythonTimeStampProvider()):
        self.now = now

    def execute(self, data: DomainAppt, timestamp=None):
        appt = Appt(data.id, data.date, data.start_time, data.end_time, data.service, data.client_id, data.staff_id, data.date_added, timestamp)
        appt.timestamp = self.now

        with transaction.atomic():
            appt.save()


class GetApptCommand(Command):
    def execute(self, data: int, timestamp=None):
        return Appt.objects.get(id=data).to_domain()


class ListApptCommand(Command):
    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self, data=None):
        return Appt.objects.all().order_by(self.order_by)

class DeleteApptCommand(Command):
    def execute(self, data: DomainAppt):
        appt = Appt.objects.get(id=data.id)
        with transaction.atomic():
            appt.delete()


class EditApptCommand(Command):
    def execute(self, data: DomainAppt):
        appt = Appt.update_from_domain(data)
        with transaction.atomic():
            appt.save()