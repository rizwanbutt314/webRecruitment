from django.urls import path

from candidate.views import RecruitmentUsers

urlpatterns = [
    path('add_user/', RecruitmentUsers.as_view(), name='add'),
    path('users/', RecruitmentUsers.as_view(), name='view_users'),
    path('delete_user/<pk>/', RecruitmentUsers.as_view(), name='delete'),
    path('search/', RecruitmentUsers.as_view(), name='search')
]