"""from django.db import models

class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre"""
from django.db import models

class Actualite(models.Model):
    titre = models.CharField(max_length=500)  # Augmenté pour éviter les coupures
    contenu = models.TextField(blank=True, null=True)  #  Permettre les valeurs NULL et vides
    date_publication = models.DateTimeField(auto_now_add=True)
    lien = models.URLField(max_length=500, blank=True, null=True)  # Stocke le lien original
    image_url = models.URLField(max_length=500, blank=True, null=True)  # Stocke l'URL de l'image

    def __str__(self):
        return self.titre
