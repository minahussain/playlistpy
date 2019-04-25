from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('delete/<list_id>', views.delete, name='delete'),
	path('logout', views.logout, name='logout'),
	path('', include('django.contrib.auth.urls')),
]