from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # hlavní stránka s recepty
    path('recepty/', views.seznam_receptu, name='seznam_receptu'),
    path('recepty/<int:pk>/', views.detail_receptu, name='detail_receptu'),
    path('kuchari/', views.seznam_kucharu, name='seznam_kucharu'),
    path('kuchar/<int:pk>/', views.detail_kuchare, name='detail_kuchare'),
]
