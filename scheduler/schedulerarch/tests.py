from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime

from schedulerassistant.models import Staff, Client, Appt
from schedulerarch.domain.model import DomainStaff, DomainClient, DomainAppt
from schedulerarch.services.commands import (
    AddApptCommand,
    GetApptCommand,
    ListApptCommand,
    DeleteApptCommand,
    EditApptCommand,
)

#./manage.py test schedulerarch.tests.TestCommands    meta issue...?
#https://stackoverflow.com/questions/60919465/typeerror-class-meta-got-invalid-attributes-pythondjango-how-fix-this-er  don't this is the issue...

class TestCommands(TestCase):
    def setUp(self):
        right_now = localtime().date()

        self.domain_appt_1 = DomainAppt(
            id=4,
            date='07, 11, 2023',
            start_time='12:00',
            end_time='13:00', 
            service='st',
            client=5,
            staff=6,
            date_added=right_now,
        )

        self.domain_appt_2 = DomainAppt(
            id=5,
            date='07, 11, 2023',
            start_time='13:00',
            end_time='14:00', 
            service='bt',
            client=5,
            staff=7,
            date_added=right_now,
        )

    def test_command_add(self):
        add_command = AddApptCommand()
        add_command.execute(self.domain_appt_1)
        self.assertEqual(Appt.objects.count(), 1)
        self.assertEqual(Appt.objects.get(id=4).service, self.domain_appt_1.service)

    def test_command_edit(self):
        add_command = AddApptCommand()
        add_command.execute(self.domain_appt_1)
        self.domain_appt_1.service = "ot"

        edit_command = EditApptCommand()
        edit_command.execute(self.domain_appt_1)

        self.assertEqual(Appt.objects.count(), 1)
        self.assertEqual(Appt.objects.get(id=4).service, "ot")

    def test_command_get(self):
        add_command = AddApptCommand()
        add_command.execute(self.domain_appt_1)

        get_command = GetApptCommand()
        get_appt = get_command.execute()  #?

        self.assertEqual(get_appt.service, self.domain_appt_1.service)

    def test_command_list(self):
        add_command = AddApptCommand()
        add_command.execute(self.domain_appt_1)
        add_command.execute(self.domain_appt_2)

        list_command = ListApptCommand()
        list_command.execute()

        self.assertEqual(Appt.objects.count(), 2)

    def test_command_delete(self):
        add_command = AddApptCommand()
        add_command.execute(self.domain_appt_1)

        delete_command = DeleteApptCommand()
        delete_command.execute()  #?

        self.assertEqual(Appt.objects.count(), 0)