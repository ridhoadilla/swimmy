from django.urls import path
from . import views

app_name = 'pools'

urlpatterns = [
    path('', views.pool_list, name='pool_list'),
    path('pool/<int:pk>/', views.pool_detail, name='pool_detail'),
]
