"""from django.urls import path
from .views import liste_projets, detail_projet

urlpatterns = [
    path('', liste_projets, name='liste_projets'),  # Page listant les projets
    path('<int:projet_id>/', detail_projet, name='detail_projet'),  # Page détaillée d'un projet
]"""

"""from django.urls import path
from .views import liste_projets, detail_projet

urlpatterns = [
    path('', liste_projets, name='liste_projets'),  # Page des projets
    path('<int:projet_id>/', detail_projet, name='detail_projet'),  # Détails d’un projet
]"""
from django.urls import path
from .views import liste_projets, detail_projet, recherche_projets
from django.urls import path
from .views import upload_image




urlpatterns = [
    path('', liste_projets, name='liste_projets'),
    path('<int:projet_id>/', detail_projet, name='detail_projet'),
    path('recherche/', recherche_projets, name='recherche_projets'),  # Route pour la recherche
path('upload_image/', upload_image, name='upload_image'),

]
