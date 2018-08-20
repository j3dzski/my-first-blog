"""  
	This is a newly created url pattern to be over write the 
existing and main Django default web page. In other words this url pattern will be called at jedzsite
url.py or imported to suite our custom web page

"""

from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
]