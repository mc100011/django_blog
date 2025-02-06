from django.urls import path
from .views import liste_tags, contenu_par_tag

urlpatterns = [
    path('', liste_tags, name='liste_tags'),  # Liste des tags
    path('<int:tag_id>/', contenu_par_tag, name='contenu_par_tag'),  # Contenu d'un tag
]