from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.demo1, name='demo1'),
    path('calculate/', views.calculate, name='calculation')

]
