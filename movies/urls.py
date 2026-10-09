from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('movies/<int:pk>/recommendations/', views.recommendations, name='recommendations'),
]
