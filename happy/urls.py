from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('instituicoes/', views.instituicoes, name='instituicoes'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('doacao/', views.doacao, name='doacao'),
    path('detail_institution/<int:pk>/', views.detail_institution, name='detail_institution'),
    #path('cadastro2/', cadastro2, name='cadastro2'),
    #path('create/', create, name='create'),
    #path('create2/', create2, name='create2'),
    #path('edit/<int:pk>/', edit, name='edit'),
    #path('update/<int:pk>/', update, name='update'),
    #path('edit2/<int:pk>/', edit2, name='edit2'),
    #path('update2/<int:pk>/', update2, name='update2'),
    #path('delete/<int:pk>/', delete, name='delete'),
    #path('delete2/<int:pk>/', delete2, name='delete2'),
    #path('createDoacao/', createDoacao, name='createDoacao'),
    #path('editDoacao/<int:pk>/', editDoacao, name='editDoacao'),
    #path('updateDoacao/<int:pk>/', updateDoacao, name='updateDoacao'),
    #path('deleteDoacao/<int:pk>/', deleteDoacao, name='deleteDoacao'),
    #path('map/<int:pk>/', map.views.map, name='map'),
]