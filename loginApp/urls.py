from django.contrib import admin
from django.urls import path
from loginApp import views

urlpatterns = [
    path('',views.login),
]
