from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('edit/<pk>/', views.edit_form, name='edit'),
    path('delete/<pk>/', views.delete_med, name='delete'),
]
