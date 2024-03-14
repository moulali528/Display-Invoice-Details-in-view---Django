from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.invoiceList, name ='Details'),
    path('<int:pk>/', views.invoiceDetails, name = 'datails'), 
]