import json

from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from ebooking.models import Room, User, Booking


def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)

        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    return render(request, template_name='login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        context = {}
    return render(request, template_name='register.html')


@login_required
def change_password(request):
    context = {}
    if request.method == 'POST':
        user = request.user
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # check that the passwords match
        if password1 == password2:
            user.set_password(password1)
            user.save()
            
            logout(request)
            return redirect('login')
        else:
            context['error'] = 'Passwords do not match.'

    return render(request, template_name='change_password.html', context=context)

@login_required
def index(request):
    search = request.GET.get('search', '')

    # room_list = room.objects.filter(
    #     del_flag=False, title__icontains=search
    # ).annotate(question_count=Count('question')) # COUNT(*) GROUP BY

    context = dict()
    
    return render(request, template_name='ebooking/index.html', context=context)


@login_required
def detail(request, room_id):
    room = room.objects.get(pk=room_id)

    return render(request, 'ebooking/detail.html', { 'room': room })
