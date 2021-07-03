from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('edit/<str:primary_key>/', views.edit_do, name='edit'),
]
