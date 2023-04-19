from . import views
from django.urls import path

app_name = 'financeapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('siteadmin/', views.siteadmin, name='admin'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.uploading_data, name='feedback'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('details/', views.details, name='details'),
]
