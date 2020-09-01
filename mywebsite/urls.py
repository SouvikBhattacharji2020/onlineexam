# djangotemplates/example/urls.py

from django.urls import path		# same in every App
from . import views					# same app views is using

urlpatterns = [
    path('', views.index, name='index'),							# in views the def include index.
    path('about/', views.about, name='about'),						# 
    path('splshscreen/', views.splshscreen, name='splshscreen'),	#
    path('loginpanel/', views.loginpanel, name='loginpanel'),		#
      
]
