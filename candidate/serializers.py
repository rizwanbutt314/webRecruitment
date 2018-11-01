from rest_framework import serializers, fields

from candidate.models import RecruitmentUser


class RecruitMentSerializer(serializers.ModelSerializer):

   class Meta:
       model = RecruitmentUser
       fields = ('__all__')