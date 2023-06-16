from django.urls import path
from . import views

urlpatterns = [
    path('index/<str:pk>', views.index, name='index'),
    path('create/<str:pk>', views.create, name='create'),
    path('delete/<str:title>', views.delete, name='delete'),
    path('find', views.find, name='find'),
    path('', views.home, name='home'),
    path('logout', views.logout, name='logout'),
]