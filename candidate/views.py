from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from rest_framework import routers, serializers, viewsets

from candidate.models import RecruitmentUser


def add_user(request):
    if request.method == 'POST':
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

    return render(request, 'add_recruitment_user.html')


def users(request):
    all_users = RecruitmentUser.objects.all()
    context = {'all_users': all_users}
    return render(request, 'users.html', context)


def user_detail(request, user_id):
    user = get_object_or_404(RecruitmentUser, pk=user_id)
    return render(request, 'user_detail.html', {'user': user})


def delete_user(request):
    return render(request, 'delete_recruitment_user.html')
