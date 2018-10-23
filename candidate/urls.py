from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from candidate import views


urlpatterns = [
    url(r'^add_user/', views.add_user, name='add'),
    url(r'^delete_user/', views.delete_user, name='delete')
]