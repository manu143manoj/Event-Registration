import traceback

from django.shortcuts import render

# Create your views here.
import random
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import json
from datetime import datetime
from django.urls import reverse
from .forms import RegisterForm
from EventRegistrationHEApp.models import ErRegisteredUsers


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("Account not Active!")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid Login details supplied")

    else:
        return render(request, 'EventRegistrationHEApp/login.html')


@login_required
def dashboard(request):
    countself = ErRegisteredUsers.objects.filter(registration_type='Self').count()
    Group = ErRegisteredUsers.objects.filter(registration_type='Group').count()
    Corporate = ErRegisteredUsers.objects.filter(registration_type='Corporate').count()
    Others = ErRegisteredUsers.objects.filter(registration_type='Others').count()
    results = [countself, Group, Corporate, Others]
    return render(request, 'EventRegistrationHEApp/dashboard.html', context={'a':results})


def home(request):
    return render(request, 'EventRegistrationHEApp/home.html')


@login_required
def ER_Registered_User(request):
    allusers = ErRegisteredUsers.objects.all().order_by('user_id')
    page = request.GET.get('page', 1)
    paginator = Paginator(allusers, 12)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'EventRegistrationHEApp/RegisteredUsers.html', context={'users': users})


@login_required
def ER_Registered_User_details(request, value):
    if request.method == "GET":
        try:
            value = str(value)
            userd = ErRegisteredUsers.objects.get(registration_id=value)
        except ErRegisteredUsers.DoesNotExist:
            userd = None
        return render(request, 'EventRegistrationHEApp/userdetails.html', context={'u': userd})


def thankyou(request):
    cursor = connection.cursor()
    cursor.execute('SELECT "Registration_ID" FROM "EventRegistrationHEApp_erregisteredusers" ORDER BY "User_ID" DESC LIMIT 1')
    regid = cursor.fetchone()
    return render(request, 'EventRegistrationHEApp/thankyou.html', context={'ID': regid[0]})


def registerdata(request):
    if request.method == "POST":
        register_form = RegisterForm(data=request.POST)
        print(register_form.is_valid())
        if register_form.is_valid():
            try:
                ruser = register_form.save(commit=False)
                cursor = connection.cursor()
                cursor.execute('SELECT MAX("User_ID")+1 from "EventRegistrationHEApp_erregisteredusers"')
                x = cursor.fetchone()
                if x[0] == 'NULL' or x[0] == 'null' or x[0] == None:
                    ruser.user_id = 1
                else:
                    ruser.user_id = x[0]
                ruser.registration_id = 'A' + str(random.randrange(1000, 99999999))
                ruser.registration_date = datetime.now()
                if 'id_cards' in request.FILES:
                    ruser.id_cards = request.FILES['id_cards']
                ruser.save()
                return HttpResponseRedirect(reverse('thankyou'))
            except Exception as e:
                print(e)
                traceback.format_exc()
        else:
            print(register_form.errors)
    else:
        register_form = RegisterForm()
    return render(request, 'EventRegistrationHEApp/registerform.html', {'register_form': register_form})