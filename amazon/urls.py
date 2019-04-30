from django.urls import path
from . import views

urlpatterns = [
# 	path('insert_data',views.insert_data,name='insert_data'),
# 	path('register',views.register,name='register'),
# 	path('sendSimpleEmail',views.sendSimpleEmail,name='sendSimpleEmail'),
# 	path('home',views.login,name='login'),
	path('main',views.main,name='main'),
	path('home',views.home,name='home'),

]