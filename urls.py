from django.urls import path
from weather import views

urlpatterns = [
    path('', views.index),
    path('detail/<int:weather_id>/', views.detail, name='detail'),
]