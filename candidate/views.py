from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from candidate.models import RecruitmentUser


class RecruitmentUsers(View):
    all_users = RecruitmentUser.objects.all()
    all_users = serializers.serialize('json', all_users)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RecruitmentUsers, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse(self.all_users, content_type="application/json")

    def get(self, request, name):
        queryset = RecruitmentUser.objects.filter(username__icontains=name)
        result = serializers.serialize('json', queryset)
        return HttpResponse(result, content_type="application/json")

    def post(self, request):
        username = request.POST.get("username");
        email = request.POST.get("email");
        is_hr = request.POST.get("is_hr");
        is_admin = request.POST.get("is_admin");
        is_interviewer = request.POST.get("is_interviewer");
        is_manager = request.POST.get("is_manager");
        if username and email:
            user = RecruitmentUser()
            user.username = username
            user.email = email
            if is_hr:
                user.is_hr = is_hr
            if is_admin:
                user.is_admin = is_admin
            if is_interviewer:
                user.is_interviewer = is_interviewer
            if is_manager:
                user.is_manager = is_manager
            user.save()
            user = serializers.serialize('json', [user])
            return HttpResponse(user, content_type="application/json")

    def delete(self, request, user_id):
        RecruitmentUser.objects.filter(pk=user_id).delete()
        return HttpResponse("User deleted successfully")
