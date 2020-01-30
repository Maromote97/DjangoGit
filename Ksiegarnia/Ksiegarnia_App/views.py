from django.shortcuts import render
from Wypozyczalnia_App.models import *
from Wypozyczalnia_App.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from Ksiegarnia_App.permissions import *


class KlientList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class KsiazkaList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class PracownikDetail(generics.RetrieveAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class WypozyczanieList(generics.ListCreateAPIView):
    queryset = Wypozyczanie.objects.all()
    serializer_class = WypozyczanieSerializer


class WypozyczanieDetail(generics.RetrieveDestroyAPIView):
    queryset = Wypozyczanie.objects.all()
    serializer_class = WypozyczanieSerializer

class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer