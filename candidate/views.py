from django.http import HttpResponse
# Create your views here.
from rest_framework import mixins, generics
from rest_framework.response import Response

from candidate.models import RecruitmentUser
from candidate.serializers import RecruitMentSerializer


class RecruitmentUsers(mixins.ListModelMixin, generics.GenericAPIView, mixins.CreateModelMixin,
                       mixins.DestroyModelMixin):
    serializer_class = RecruitMentSerializer
    queryset = RecruitmentUser.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        query = self.request.GET.get("name")
        if query:
            result = queryset.filter(username__icontains=query)
        else:
            return queryset
        return result

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username");
        email = request.POST.get("email");
        if username and email:
            return self.create(request, *args, **kwargs)
        else:
            return Response("Error")

    def delete(self, request, *args, **kwargs):
        return self.destroy(request)
