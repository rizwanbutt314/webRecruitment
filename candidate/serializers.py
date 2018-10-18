from rest_framework import serializers

from candidate.models import RecruitmentUser


class RecruitmentUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecruitmentUser
        fields = ('username', 'email', 'is_admin', 'is_hr', 'is_interviewer', 'is_manager')
