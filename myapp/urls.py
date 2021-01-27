
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.testfctn,name='home'),
    path('admin',views.testfctn1,name='admin'),
    path('login',views.test,name='login'),
    path('home',views.test2,name='home')
]
