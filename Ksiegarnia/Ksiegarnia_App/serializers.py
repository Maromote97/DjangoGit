from rest_framework import serializers

from .models import *


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'


class KsiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazka
        fields = '__all__'


class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = '__all__'


class WypozyczanieSerializer(serializers.ModelSerializer):
    ksiazka = KsiazkaSerializer(read_only=True, many=True)
    pracownik = PracownikSerializer(read_only=True, many=True)
    klient = KlientSerializer(read_only=True, many=True)

    class Meta:
        model = Wypozyczanie
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     Klient = KlientSerializer(many=True)
#     Ksiazka = KsiazkaSerializer(many=True)
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'Klient', 'Ksiazka']
