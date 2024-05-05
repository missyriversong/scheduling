"""
URL configuration for scheduler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('client/:id>', views.client_info, name='client_info')   is /:id the right format? 
    # path(staff...)
    # path('schedule/', views.schedule, name='schedule') this would not be easy to read  maybe schedule/<:id>
    #  or include('schedule.urls')  
    path('', include("schedulerassistant.urls")),
]

#include all rest apis