from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
app_name='Friends'
urlpatterns = [
    path('friends/', views.friendlist, name='friend'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('detail/<slug>/', views.friend_detail, name='detail'),
]