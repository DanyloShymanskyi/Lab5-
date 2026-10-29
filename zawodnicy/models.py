from django.db import models

class Zawodnik(models.Model):
    imie_nazwisko = models.CharField(max_length=100)
    druzyna = models.CharField(max_length=100)
    pozycja = models.CharField(max_length=50)
    numer_koszulki = models.IntegerField()
    aktywny_w_grze = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.imie_nazwisko} ({self.druzyna})"