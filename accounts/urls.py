from django.contrib import admin
from django.urls import path
from . import views
app_name='accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loggedin, name='login'),
    path('logout/', views.loggedout, name='logout'),
]