from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [path('', views.index, name='splash'),
               path('books/', views.book_list, name='book_list'),
               path('books/book_detail/', views.book_detail, name='book_detail')]
