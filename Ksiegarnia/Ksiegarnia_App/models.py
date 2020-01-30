from django.db import models


class Klient(models.Model):
    PESEL = models.CharField(max_length=45)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Miejscowosc = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'Klienci'

    def __str__(self):
        return '%s %s %s %s' % (self.PESEL, self.Imie, self.Nazwisko, self.Miejscowosc)


class Ksiazka(models.Model):
    Autor = models.CharField(max_length=45)
    Tytul = models.CharField(max_length=45)
    Dostepnosc = models.IntegerField()
    CenaZaMiesiac = models.FloatField()

    class Meta:
        verbose_name_plural = 'Ksiazki'

    def __str__(self):
        return '%s %s %s %s' % (self.Autor, self.Tytul, self.Dostepnosc, self.CenaZaMiesiac)


class Pracownik(models.Model):
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Stanowisko = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'Pracownicy'

    def __str__(self):
        return '%s %s %s' % (self.Imie, self.Nazwisko, self.Stanowisko)


class Wypozyczanie(models.Model):
    Id_klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    Id_Ksiazki = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    Pracownik_idPracownika = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    Data_wydania = models.DateField()
    Data_oddania = models.DateField()
    Cena_za_wypozyczenie = models.FloatField()

    class Meta:
        verbose_name_plural = 'Wypozyczenia'

    def __str__(self):
        return '%s %s %s %s %s %s' % (
            self.Id_klient, self.Id_Ksiazki, self.Pracownik_idPracownika, self.Data_wydania,
            self.Data_oddania, self.Cena_za_wypozyczenie)
