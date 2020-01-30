from django.db import models

class Klient(models.Model):
    PESEL = models.IntegerField(primary_key=True)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Miejscowosc = models.CharField(max_length=45)
    owner = models.ForeignKey('auth.User', related_name='Klient', on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s %s' %(self.PESEL, self.Imie, self.Nazwisko, self.Miejscowosc)



class Ksiazka(models.Model):
    IdKsiazki = models.CharField(primary_key=True, max_length=45)
    Autor = models.CharField(max_length=45)
    Tytul = models.CharField(max_length=45)
    Dostepnosc = models.IntegerField()
    CenaZaMiesiac = models.FloatField()
    owner = models.ForeignKey('auth.User', related_name='Ksiazka', on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s %s %s' % (self.IdKsiazki, self.Autor, self.Tytul, self.Dostepnosc, self.CenaZaMiesiac)


class Pracownik(models.Model):
    idPracownik = models.IntegerField(primary_key=True)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Stanowisko = models.CharField(max_length=45)
    def __str__(self):
        return '%s %s %s %s' % (self.idPracownik, self.Imie, self.Nazwisko, self.Stanowisko)


class Wypozyczanie(models.Model):
    idWypozyczanie = models.IntegerField(primary_key=True)
    Klient_PESEL = models.ForeignKey(Klient, on_delete=models.CASCADE)
    Id_Ksiazki = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    Pracownik_idPracownika = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    Data_wydania = models.DateField()
    Data_oddania = models.DateField()
    Cena_za_wypozyczenie = models.FloatField()
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.idWypozyczanie, self.Klient_PESEL, self.Id_Ksiazki, self.Pracownik_idPracownika, self.Data_wydania,
                                   self.Data_oddania, self.Cena_za_wypozyczenie)
