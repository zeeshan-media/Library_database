from django.urls import path, include
from .import views

urlpatterns = [
    path('addandshow/', views.add_show, name= 'addandshow'),
    path('delete/<int:book_id>/',views.deletes,name='deletesdata'),
    path('<int:book_id>/', views.updates, name='updatesdata'),
    path('logout/',views.log_out, name="logout"),
]