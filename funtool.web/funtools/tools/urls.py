from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('joke/', views.joke_generator, name='joke'),
    path('number/', views.number_generator, name='number'),
    path('date/', views.date_generator, name='date'),
]
