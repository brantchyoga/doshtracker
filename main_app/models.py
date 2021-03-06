from django.db import models
from django.contrib.auth.models import User
import datetime

class Money(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    day_wage = models.DecimalField(max_digits=6, decimal_places=2)
    cash = models.DecimalField(max_digits=6, decimal_places=2)
