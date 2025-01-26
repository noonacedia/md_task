from django.urls import path

from patients import views

urlpatterns = [
    path('', views.GetPatients.as_view(), name='patients'),
]
