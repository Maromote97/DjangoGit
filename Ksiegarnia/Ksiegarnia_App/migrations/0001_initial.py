# Generated by Django 2.2.7 on 2020-01-30 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PESEL', models.CharField(max_length=45)),
                ('Imie', models.CharField(max_length=45)),
                ('Nazwisko', models.CharField(max_length=45)),
                ('Miejscowosc', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Klienci',
            },
        ),
        migrations.CreateModel(
            name='Ksiazka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Autor', models.CharField(max_length=45)),
                ('Tytul', models.CharField(max_length=45)),
                ('Dostepnosc', models.IntegerField()),
                ('CenaZaMiesiac', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Ksiazki',
            },
        ),
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=45)),
                ('Nazwisko', models.CharField(max_length=45)),
                ('Stanowisko', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Pracownicy',
            },
        ),
        migrations.CreateModel(
            name='Wypozyczanie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_wydania', models.DateField()),
                ('Data_oddania', models.DateField()),
                ('Cena_za_wypozyczenie', models.FloatField()),
                ('Id_Ksiazki', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ksiegarnia_App.Ksiazka')),
                ('Id_klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ksiegarnia_App.Klient')),
                ('Pracownik_idPracownika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ksiegarnia_App.Pracownik')),
            ],
            options={
                'verbose_name_plural': 'Wypozyczenia',
            },
        ),
    ]