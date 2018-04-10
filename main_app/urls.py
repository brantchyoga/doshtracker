from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('entercash/<user_name>/', views.entercash, name='entercash'),
	path('user/<user_name>/', views.profile, name='profile'),
	path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
	path('signup/', views.signup, name='signup'),
	path('<int:money_id>/edit/',views.edit_money, name='edit_money'),
	path('<user_name>/addMoney', views.add_money, name='add_money'),
]
