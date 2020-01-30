from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('klienci/', views.KlientList.as_view(), name='KlientList'),
    path('klienci/<int:pk>/', views.KlientDetail.as_view(), name='KlientDetail'),

    path('ksiazki/', views.KsiazkaList.as_view(), name='KsiazkaList'),
    path('ksiazki/<int:pk>/', views.KsiazkaDetail.as_view(), name='KsiazkaDetail'),

    path('pracownicy/', views.PracownikList.as_view(), name='PracownikList'),
    path('pracownicy/<int:pk>/', views.PracownikDetail.as_view(), name='PracownikDetail'),

    path('wypozyczanie/', views.WypozyczanieList.as_view(), name='WypozyczanieList'),
    path('wypozyczanie/<int:pk>/', views.WypozyczanieDetail.as_view(), name='WypozyczanieDetail'),
]
