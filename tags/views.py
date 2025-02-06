from django.shortcuts import render, get_object_or_404
from .models import Tag
from projets.models import Projet  # Import du modèle Projet


def liste_tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags/liste_tags.html', {'tags': tags})


def contenu_par_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    projets = Projet.objects.filter(tags=tag)  # Projets associés au tag

    return render(request, 'tags/contenu_par_tag.html', {'tag': tag, 'projets': projets})




