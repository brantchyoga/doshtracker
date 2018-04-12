from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('entercash/<user_name>/', views.entercash, name='entercash'),
	path('user/<user_name>/', views.profile, name='profile'),
	path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
	path('signup/', views.signup, name='signup'),
	path('chart/<user_name>/', views.chart, name='chart'),
	path('destroy/<user_name>/',views.destroy_user, name='destroy_user'),
	path('edit/<user_name>/', views.edit_user, name='edit_user'),
	path('edit/<user_name>/money/<int:money_id>', views.edit_money, name='views.edit_money'),
	path('destroy/<user_name>/money/<int:money_id>', views.delete_money, name='views.delete_money'),
]
