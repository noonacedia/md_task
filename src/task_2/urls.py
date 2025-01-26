from django.urls import path

from task_2 import views

urlpatterns = [
    path('', views.GetJsonFileCalculation.as_view(), name='parse_json'),
]
