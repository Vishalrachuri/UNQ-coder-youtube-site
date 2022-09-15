from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('viedo',views.search),
    path('playlist/', views.playlist),
    path('<str:playname>/<int:vno>/',views.viedo),
]