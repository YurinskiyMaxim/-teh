from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('equipment/<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('request/success/', views.request_success, name='request_success'),
]
