"""from django.shortcuts import render
from .models import Actualite

def page_accueil(request):
    actualites = Actualite.objects.order_by('-date_publication')[:5]  # Dernières actualités

    return render(request, 'accueil/index.html', {
        'actualites': actualites,
    })"""

from django.shortcuts import render
from .models import Actualite
from projets.models import Projet  # ✅ Import du modèle Projet

def page_accueil(request):
    actualites = Actualite.objects.order_by('-date_publication')[:5]  # Dernières actualités
    projets = Projet.objects.order_by('-date_publication')[:5]  # Derniers projets

    return render(request, 'accueil/index.html', {
        'actualites': actualites,
        'projets': projets,
    })