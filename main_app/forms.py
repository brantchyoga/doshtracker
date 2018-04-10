from django import forms
from .models import Money
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = ['date', 'day_wage', 'cash']
        widgets = {
        'date': forms.DateTimeInput(attrs={'class': 'datepicker','placeholder':'Enter date in MM/DD/YYYY'})
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='email is required')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')
