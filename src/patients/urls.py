from django.urls import path

from src.patients import views

urlpatterns = [
    path('', views.GetPatients.as_view(), name='patients'),
]
