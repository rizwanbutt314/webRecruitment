from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from candidate import views
from candidate.views import RecruitmentUsers

urlpatterns = [
    path('add_user/', RecruitmentUsers.as_view(), name='add'),
    path('users/', RecruitmentUsers.as_view(), name='view_users'),
    path('delete_user/<int:user_id>/', RecruitmentUsers.as_view(), name='delete'),
    path('search/<str:name>/', RecruitmentUsers.as_view(), name='search')
]