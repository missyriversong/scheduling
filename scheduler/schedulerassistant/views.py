# from django.shortcuts import render

# # Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, Staff, Appt
from .permissions import IsOwnerOrReadOnly
from .serializers import GroupSerializer, UserSerializer, ClientSerializer, StaffSerializer, ApptSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by("last_name")   
    serializer_class = ClientSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by("last_name")
    serializer_class = StaffSerializer

class ApptViewSet(viewsets.ModelViewSet):
    queryset = Appt.objects.all().order_by('-date', '-start_time')
    serializer_class = ApptSerializer
    #mm not sure if this makes sense...oldest...filter by day?
        #https://www.w3schools.com/django/django_queryset_orderby.php
        #since you order here, would you class Meta for ordering..in models?


#https://www.youtube.com/watch?v=TmsD8QExZ84  serializer views...tutorial
#instead for @api get  - add url specific e.g. /task-list/    then specific tasklist query...put it in url patterns...maybe change it?


# #https://davenathanaeld.medium.com/design-pattern-django-rest-framework-1e8c17946bce not sure if helpful...



# # def index() return ()

# # get home page
# # get all clients, get client by name and type
#   # post new info
# # get all staff, get staff by name and type
#   # post new info

# # get schedule by day for all clients and staff, specific client, specific staff
#   # get avail appts for timeframe and staff type
#   # post status (? avail) appt for client, staff   
#   # delete status 
