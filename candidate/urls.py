from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from candidate import views


urlpatterns = [
    url(r'^add_user/', views.add_user, name='add'),
    url(r'^users/', views.users, name='view_users'),
    path(r'<int:user_id>/', views.user_detail, name='detail'),
    url(r'^delete_user/', views.delete_user, name='delete')
]