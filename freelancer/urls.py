from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import  static


urlpatterns = [
    path('', views.free, name="free"),

    path('home/', views.home, name="home"),

    path('payment/', views.payment, name="payment"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    ]