from django.shortcuts import render
from django.http import JsonResponse
from .models import Zawodnik

def strona_glowna(request):
    return render(request, 'zawodnicy/index.html')

def api_zawodnicy(request):
    filtr_aktywnosci = request.GET.get('aktywny')
    zawodnicy_lista = Zawodnik.objects.all()

    if filtr_aktywnosci == 'true':
        zawodnicy_lista = zawodnicy_lista.filter(aktywny_w_grze=True)
    elif filtr_aktywnosci == 'false':
        zawodnicy_lista = zawodnicy_lista.filter(aktywny_w_grze=False)

    dane = {
        "items": [
            {
                "id": z.id,
                "imie_nazwisko": z.imie_nazwisko,
                "druzyna": z.druzyna,
                "pozycja": z.pozycja,
                "numer_koszulki": z.numer_koszulki,
                "aktywny": z.aktywny_w_grze
            }
            for z in zawodnicy_lista
        ]
    }
    return JsonResponse(dane)

def lista_zawodnikow_api(request):
    zawodnicy = Zawodnik.objects.filter(aktywny_w_grze=True).order_by('imie_nazwisko')[:5]
    dane = list(zawodnicy.values('imie_nazwisko', 'druzyna', 'pozycja', 'wzrost', 'kategoria'))
    return JsonResponse({'zawodnicy': dane})