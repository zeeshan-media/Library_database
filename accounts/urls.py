from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('librarian/', views.librarian, name='librarian'),
    path('reader/', views.reader, name='reader'),
    path('logout/',views.logout, name="logout"),

]