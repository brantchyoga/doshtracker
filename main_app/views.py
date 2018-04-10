from django.shortcuts import render, redirect, get_object_or_404
from .models import Money
from .forms import MoneyForm, LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import requests
from datetime import datetime, timedelta
import time
from decimal import *

def index(request):
    return render(request, 'index.html')

def profile(request, user_name):
    user = User.objects.get(username=user_name)
    return render(request, 'profile.html', {'username':user_name})

def entercash(request, user_name):
    print(request.POST, user_name)
    if  request.method == 'POST':
        form = MoneyForm(request.POST)

        if form.is_valid():
            money = form.save(commit=False)
            money.user = request.user
            money.save()
            return HttpResponseRedirect('/')
    else:
        user = User.objects.get(username=user_name)
        money_form = MoneyForm()
        return render(request, 'entercash.html', {'username':user_name, 'form':money_form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'profile.html', {'user':user})
                else:
                    print('This account has been disabled')
            else:
                print('The username and or password is incorrect')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def add_money(request, user_name):
    pastdate = datetime.today()
    startdate = pastdate - timedelta(days=60)
    start_time = int(time.mktime(datetime(2012, 6, 1).timetuple()) * 1000)
    print(start_time)
    money = Money.objects.filter(date__range=[startdate, pastdate])
    cash_list = []
    date_list = []
    for cash in money:
        cash_thing = cash.cash*1
        print(cash_thing, cash.cash, str(cash.cash))
        cash_list.append(str(cash_thing))
        print((int(time.mktime(cash.date.timetuple()))))
        date_list.append(int(time.mktime((cash.date).timetuple())))
    print(cash_list, 'cashlist')
    date_list.sort()
    print(date_list)
    chartdata = {'x': date_list, 'y': cash_list}
    charttype = "lineChart"
    chartcontainer = 'linechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render(request, 'index.html', data)

def edit_money(request, user_name):
    user = User.objects.get(username=user_name)
    instance = Money.objects.filter(date__range=[startdate, pastdate])
    # instance = get_object_or_404(money, 'date'=money_date)
    form = MoneyForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('show', money_id)
    return render(request, 'edit_money.html', {'money': instance,'form':form})
