from django.shortcuts import render

# Create your views here.
from rest_framework import routers, serializers, viewsets

from candidate.models import RecruitmentUser
from candidate.serializers import RecruitmentUserSerializer


class RecruitmentUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RecruitmentUser.objects.all()
    serializer_class = RecruitmentUserSerializer
