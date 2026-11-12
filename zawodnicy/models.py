from django.db import models

class Zawodnik(models.Model):
    imie_nazwisko = models.CharField(max_length=100, default="Brak")
    druzyna = models.CharField(max_length=50, default="Brak")
    numer_koszulki = models.IntegerField(null=True, blank=True)
    aktywny_w_grze = models.BooleanField(default=True)
    pozycja = models.CharField(max_length=30, default="Brak")
    
    wzrost = models.IntegerField(null=True, blank=True)
    kategoria = models.CharField(max_length=30, default="Senior")

    def __str__(self):
        return self.imie_nazwisko