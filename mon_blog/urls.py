from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from projets.views import upload_image  # Importer la vue pour l'upload d'images

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accueil.urls')),
    path('projets/', include('projets.urls')),
    path('contact/', include('contact.urls')),
    path('tags/', include('tags.urls')),
    path('tinymce/', include('tinymce.urls')),  # TinyMCE
    path('upload_image/', upload_image, name='upload_image'),  # Route pour l'upload d'images
]

# Servir les fichiers médias correctement en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
