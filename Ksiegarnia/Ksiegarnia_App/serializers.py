from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User




class KlientSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    Pesel = serializers.IntegerField(required=True)
    Imie = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Nazwisko = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Miejscowosc = serializers.CharField(required=False, max_length=45)

    def create(self, validated_data):
        return Klient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Imie = validated_data.get('Imie', instance.Imie)
        instance.Nazwisko = validated_data.get('Nazwisko', instance.Nazwisko)
        instance.Miejscowosc = validated_data.get('Miejscowosc', instance.Miejscowosc)
        instance.save()
        return instance


class KsiazkaSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    Id_Ksiazki = serializers.IntegerField(required=True)
    Autor = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Tytul = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Dostepnosc = serializers.IntegerField(required=False)
    CenaZaMiesiac = serializers.FloatField(required=False)

    def create(self, validated_data):
        return Ksiazka.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Autor = validated_data.get('Autor', instance.Marka)
        instance.Tytul = validated_data.get('Tytul', instance.Model)
        instance.Dostepnosc = validated_data.get('Dostepnosc', instance.Dostepnosc)
        instance.CenaZaMiesiac = validated_data.get('CenaZaMiesiac', instance.CenaZaDobe)
        instance.save()
        return instance


class PracownikSerializer(serializers.Serializer):
    Id_Pracownik = serializers.IntegerField(required=True)
    Imie = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Nazwisko = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Stanowisko = serializers.CharField(required=False, allow_blank=True, max_length=45)

    def create(self, validated_data):
        return Pracownik.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Id_Pracownik = validated_data.get('idPracownik', instance.idPracownik)
        instance.Imie = validated_data.get('Imie', instance.Imie)
        instance.Nazwisko = validated_data.get('Nazwisko', instance.Nazwisko)
        instance.Stanowisko = validated_data.get('Stanowisko', instance.Stanowisko)
        instance.save()
        return instance


class WypozyczanieSerializer(serializers.Serializer):
    idWypozyczanie = serializers.IntegerField(required=True)
    Klient_Pesel = serializers.PrimaryKeyRelatedField(queryset=Klient.objects.all())
    Id_Ksiazki = serializers.PrimaryKeyRelatedField(queryset=Ksiazka.objects.all())
    Pracownik_IdPracownika = serializers.PrimaryKeyRelatedField(queryset=Pracownik.objects.all())
    Data_wydania = serializers.DateField(required=False)
    Data_oddania = serializers.DateField(required=False)
    Cena_za_wypozyczenie = serializers.FloatField(required=False)

    def create(self, validated_data):
        return Wypozyczanie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idWypozyczanie = validated_data.get('IdWypozyczanie', instance.idWypozyczanie)
        instance.Data_wydania = validated_data.get('Data_wydania', instance.Data_wydania)
        instance.Data_oddania = validated_data.get('Data_oddania', instance.Data_oddania)
        instance.Cena_za_wypozyczenie = validated_data.get('Cena_za_wypozyczenie', instance.Cena_za_wypozyczenie)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    Klient = serializers.PrimaryKeyRelatedField(many=True, queryset=Klient.objects.all())
    Ksiazka = serializers.PrimaryKeyRelatedField(many=True, queryset=Ksiazka.objects.all())

    class Ending:
        model = User
        fields = ['id', 'username', 'Klient', 'Ksiazka']