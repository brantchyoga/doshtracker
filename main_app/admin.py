from django.contrib import admin
from .models import Money


class MoneyInline(admin.TabularInline):
    model = Money
    extra = 2


admin.site.register(Money)
