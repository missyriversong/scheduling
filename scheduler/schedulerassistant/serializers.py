from django.contrib.auth.models import Group, User
from .models import Client, Staff, Appt 
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'txtype', 'email', 'date_added']

class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'cert', 'email', 'date_added']

class ApptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appt
        fields = ['date', 'start_time', 'end_time', 'service', 'client', 'staff', 'date_added']


