from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClockView.as_view(), name='clock'),
]
