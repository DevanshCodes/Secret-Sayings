from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addtodo,name='add'),
    path('complete/<todo_id>', views.completed, name='complete'),
    path('like/<todo_id>',views.like,name="like"),
]