"""
ASGI config for scheduler project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ChannelNameRouter, ProtocolTypeRouter
#missing import...https://pypi.org/project/django-channels/  says installed...?

from django.core.asgi import get_asgi_application
from schedulerassistant import consumers


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduler.settings')

scheduler_asgi_app = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": scheduler_asgi_app,
        "channel": ChannelNameRouter(
            {
                "appt-add": consumers.SimpleApptConsumer.as_asgi(),
            }
        ),
    }
)

#https://pypi.org/project/django-channels/