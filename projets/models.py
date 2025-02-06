"""from django.db import models

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/', null=True, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre"""

"""from django.db import models
from tags.models import Tag  # Import du modèle Tag

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/', null=True, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='projets')  # Ajout des tags

    def __str__(self):
        return self.titre
"""
"""from django.db import models
from tags.models import Tag
from django_ckeditor_5.fields import CKEditor5Field  # Vérifie bien cet import

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = CKEditor5Field(config_name="default")  # CKEditor5Field au lieu de TextField
    image = models.ImageField(upload_to='projets/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='projets')

    def __str__(self):
        return self.titre"""
from django.db import models
from tinymce.models import HTMLField  # Import de TinyMCE
from PIL import Image
from tags.models import Tag

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = HTMLField()  # Utilisation de TinyMCE pour la description
    image = models.ImageField(upload_to='projets/', null=True, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='projets')
    image_url = models.URLField(blank=True, null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Enregistre l'image en premier

        if self.image:  # Vérifie si une image est présente
            img = Image.open(self.image.path)  # Ouvre l'image
            img = img.convert("RGB")  # Convertit en format compatible

            # Redimensionne l'image
            img = img.resize((400, 250), Image.LANCZOS)
            img.save(self.image.path)  # Sauvegarde l'image modifiée

    def __str__(self):
        return self.titre
