from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .models import Money
from .forms import MoneyForm, LoginForm, SignUpForm, ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import requests
from datetime import datetime, timedelta
import time
from decimal import *
import operator
import random

def index(request):
    print('index def')
    return render(request, 'index.html')

def profile(request, user_name):
    print('profile def')
    day = 30
    pastdate = datetime.today()
    startdate = pastdate - timedelta(days=day)
    if request.method == 'POST':
        pastdate = request.POST['start_date']
        startdate = request.POST['past_date']
        print(pastdate,startdate)
    user = User.objects.get(username=user_name)

    print(startdate, pastdate)
    all_moneys = Money.objects.filter(user=user.id,date__range=[startdate, pastdate])
    all_moneyss = all_moneys.values()
    all_money = sorted(all_moneyss, key=operator.itemgetter('date'))


    return render(request, 'profile.html', {'allMoney':all_money,'username':user})

def destroy_user(request, user_name):
    user = User.objects.get(username=user_name).delete()
    return redirect('index')

def edit_user(request, user_name):
    print('edit_user')
    instance = get_object_or_404(User, username=user_name)
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('profile',user_name)
    return render(request, 'edit_user.html', {'form':form})

def entercash(request, user_name):
    print('entercash def')
    print(request.POST, user_name)
    if  request.method == 'POST':
        form = MoneyForm(request.POST)
        # print(form,'form')
        if form.is_valid():
            print('validated')
            money = form.save(commit=False)
            money.user = request.user
            money.save()
            return HttpResponseRedirect('/user/'+user_name)
    else:
        user = User.objects.get(username=user_name)
        money_form = MoneyForm()
        return render(request, 'entercash.html', {'username':user_name, 'form':money_form})

def login_view(request):
    print('login def')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/user/'+user.username)
                else:
                    print('This account has been disabled')
            else:
                print('The username and or password is incorrect')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    print('logout def')
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    print('signup def')
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

def edit_money(request, user_name, money_id):
    print('edit money def')
    instance = Money.objects.get(id=money_id)
    # user = User.objects.get(id=instance.user)
    print(instance.user.id)
    form = MoneyForm(request.POST or None, instance=instance)
    print(form.is_valid(),form)
    if form.is_valid():
        print('form valid')
        form.save()
        return redirect('/user/'+instance.user.username)
    return render(request, 'edit_money.html', {'money': instance,'form':form, 'user':instance.user})

def delete_money(request, user_name, money_id):
    instance = Money.objects.get(id=money_id)
    Money.objects.get(pk=money_id).delete()
    return redirect('/user/'+instance.user.username)

def chart(request, user_name):
    print('chart def')
    day=30
    if request.method == 'POST':
        print(request.POST['days'])
        day = int(request.POST['days'])
    user = User.objects.get(username=user_name)
    pastdate = datetime.today()
    startdate = pastdate - timedelta(days=day)
    print(startdate, pastdate)
    all_moneys = Money.objects.filter(user=user.id,date__range=[startdate, pastdate])
    all_moneyss = all_moneys.values()
    all_money = sorted(all_moneyss, key=operator.itemgetter('date'))
    cash_list = []
    date_list = []
    for cash in all_money:
        cash_thing = int(cash['cash'])
        cash_list.append(cash_thing)
        print(cash['date'])
        date_list.append(int(time.mktime((cash['date']).timetuple()))*1000)
    print(date_list)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"},
                   "date_format": tooltip_date}
    chartdata = {'x': date_list, 'name1': 'Cash', 'y1': cash_list, 'extra1': extra_serie}
    charttype = "lineChart"
    chartcontainer = "linechart_container"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': "%d %b %Y",
            'tag_script_js': True,
            'jquery_on_ready': False,
            },
        'user':user
    }
    return render(request, 'chart.html', data)
