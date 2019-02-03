from django.contrib import admin
from django.urls import path
from . import views

app_name='comment'
urlpatterns = [
    path('', views.comment_listed, name='comment'),
    path('comment_create/', views.comment_create, name="comment_create"),
    path('replying/<int:comment_id>', views.replying, name="reply"),
    path('liking/', views.liking, name="like")
]