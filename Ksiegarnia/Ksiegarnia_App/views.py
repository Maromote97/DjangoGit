from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.permissions import *

from .serializers import *


def index(request):
    return HttpResponse("index")


class KlientList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,
                          DjangoModelPermissionsOrAnonReadOnly]
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer

    def perform_create(self, serializer):
        serializer.save()


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = KlientSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Klient.objects.filter(pk=pk)

    def perform_create(self, serializer):
        serializer.save()


class KsiazkaList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer

    def perform_create(self, serializer):
        serializer.save()


class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KsiazkaSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Ksiazka.objects.filter(pk=pk)


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class PracownikDetail(generics.RetrieveAPIView):
    serializer_class = PracownikSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Pracownik.objects.filter(pk=pk)


class WypozyczanieList(generics.ListCreateAPIView):
    queryset = Wypozyczanie.objects.all()
    serializer_class = WypozyczanieSerializer


class WypozyczanieDetail(generics.RetrieveDestroyAPIView):
    serializer_class = WypozyczanieSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Wypozyczanie.objects.filter(pk=pk)
