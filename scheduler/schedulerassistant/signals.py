import csv
from pathlib import Path
from random import randint

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.core.files import File
from django.db.models.signals import post_save

from .consumers import SimpleClientConsumer, SimpleStaffConsumer, SimpleApptConsumer
from .models import Client, Staff, Appt

channel_layer = get_channel_layer()

# receiver as save, ModelName is sender, signal is post
def log_appt_to_csv(sender, instance, **kwargs):
    print("Appointment signal: CSV")

    file = Path(__file__).parent.parent / "schedulerarch" / "domain" / "created_appt_log.csv"
    print(f"Writing to {file}")

    with open(file, "a+", newline="") as csvfile:
        logfile = File(csvfile)
        logwriter = csv.writer(
            logfile,
            delimiter=",",
        )
        logwriter.writerow(
            [
                instance.id,
                instance.date,
                instance.start_time,
                instance.end_time,
                instance.service,
                instance.client,  #not sure would this be client_id or client.id?
                instance.staff,
                instance.date_added,
            ]
        )


def send_appt_to_channel(sender, instance, **kwargs):
    print("Appointment signal: Channel")
    print(f"Sending appointment to channel: {instance}")

    async_to_sync(channel_layer.send)(
        "appt-add", {"type": "print.appointment", "data": instance.url}  #not sure what would make sense to send....
    )
#https://docs.djangoproject.com/en/5.0/topics/signals/

# connect the signal to this receiver
post_save.connect(log_appt_to_csv, sender=Appt)
post_save.connect(send_appt_to_channel, sender=Appt)