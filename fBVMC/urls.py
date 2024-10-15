# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<pk>/', views.customer_detail, name='customer_detail'),
    path('addressess/', views.address_list, name='address_list'),
    path('addressess/<pk>/', views.address_detail, name='address_detail'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<pk>/', views.blog_detail, name='blog_detail'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<pk>/', views.comment_detail, name='comment_detail'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<pk>/', views.course_detail, name='course_detail'),
    path('students/', views.student_list, name='student_list'),
    path('students/<pk>/', views.student_detail, name='student_detail'),
]
