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
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]