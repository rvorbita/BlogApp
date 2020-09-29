"""Blogs URL Patterns"""
from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    #home
    path('', views.index, name='index'),
    #new blog
    path('new_blog', views.new_blog, name='new_blog'),
    #edit blog
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    #delete blog
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),

]