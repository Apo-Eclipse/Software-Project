from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('classroom/', views.classroom, name='classroom')
]