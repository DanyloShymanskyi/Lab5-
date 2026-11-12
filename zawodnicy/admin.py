from django.contrib import admin
from .models import Zawodnik

@admin.register(Zawodnik)
class ZawodnikAdmin(admin.ModelAdmin):
    list_display = ('imie_nazwisko', 'druzyna', 'numer_koszulki', 'pozycja', 'wzrost', 'kategoria', 'aktywny_w_grze')