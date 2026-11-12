from django.contrib import admin
from django.urls import path
from zawodnicy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.strona_glowna, name='strona_glowna'),
    path('api/obiekty/', views.api_zawodnicy, name='api_zawodnicy'),
    path('api/zawodnicy/', views.lista_zawodnikow_api, name='lista_zawodnikow_api'),
]