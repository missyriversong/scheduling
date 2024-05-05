from django.urls import path, include
from rest_framework import routers   #why isn't this registering...?  added in settings.py...?
from . import views
# from .views import UserViewSet, GroupViewSet, ClientViewSet, StaffViewSet, ApptViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'appts', views.ApptViewSet)


# #https://www.django-rest-framework.org/#installation

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls