from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('edit/<str:primary_key>/', views.edit_do, name='edit'),
    path('delete/<str:primary_key>', views.delete_do, name="delete"),
]
