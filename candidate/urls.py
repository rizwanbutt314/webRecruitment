from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from candidate import views

router = routers.DefaultRouter()
router.register(r'users', views.RecruitmentUserViewSet)

urlpatterns = [
] + router.urls