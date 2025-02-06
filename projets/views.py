import os
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Projet


# ✅ Affichage des 10 derniers projets
def liste_projets(request):
    projets = Projet.objects.order_by('-date_publication')[:10]
    return render(request, 'projets/liste_projets.html', {'projets': projets})


# ✅ Affichage du détail d’un projet spécifique
def detail_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    return render(request, 'projets/detail_projet.html', {'projet': projet})


# ✅ Recherche de projets par titre
def recherche_projets(request):
    query = request.GET.get('q')
    projets = Projet.objects.filter(titre__icontains=query) if query else []
    return render(request, 'projets/recherche.html', {'projets': projets, 'query': query})


@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        image = request.FILES['file']
        print(f"Image reçue : {image.name}")  # Debugging

        try:
            path = default_storage.save(os.path.join('projets/', image.name), ContentFile(image.read()))
            image_url = f"{request.build_absolute_uri('/media/')}{path}"  # Générer une URL complète
            return JsonResponse({'location': image_url})
        except Exception as e:
            return JsonResponse({'error': f"Échec de l'upload : {str(e)}"}, status=500)

    return JsonResponse({'error': 'Aucun fichier reçu'}, status=400)