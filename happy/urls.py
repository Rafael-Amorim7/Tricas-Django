from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('instituicoes/', views.instituicoes, name='instituicoes'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('doacao/', views.doacao, name='doacao'),
    path('detail_institution/<int:pk>/', views.detail_institution, name='detail_institution'),
    path('map/<str:location>', views.map, name='map'),
]