"""Define URL Pattern for Users """
from django.urls import path,include
from . import views


app_name = "users"
urlpatterns = [
    #default auth urls
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),

]