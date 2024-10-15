# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/<pk>/', views.author_detail, name='author_detail'),
    path('books/', views.book_list, name='book_list'),
    path('books/<pk>/', views.book_detail, name='book_detail'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/<pk>/', views.car_detail, name='car_detail'),
    path('engines/', views.engine_list, name='engine_list'),
    path('engines/<pk>/', views.engine_detail, name='engine_detail'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<pk>/', views.movie_detail, name='movie_detail'),
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/<pk>/', views.actor_detail, name='actor_detail'),
]
