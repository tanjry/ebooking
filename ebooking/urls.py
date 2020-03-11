from django.contrib import admin
from django.urls import path

from . import views 

urlpatterns = [
    # path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('detail/<int:room_id>/', views.detail, name='booking_detail'),
]
