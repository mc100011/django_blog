"""from celery import shared_task
import requests
from .models import Actualite
from googletrans import Translator
from datetime import datetime
from accueil.key import API_key
translator = Translator()

@shared_task
def fetch_and_store_articles():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_key}"
    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json().get("articles", [])
        for article in articles[:5]:  # On limite à 5 articles
            titre_en = article["title"]
            contenu_en = article.get("description", "No description available")

            # Traduction en français
            try:
                titre_fr = translator.translate(titre_en, src="en", dest="fr").text
                contenu_fr = translator.translate(contenu_en, src="en", dest="fr").text
            except Exception as e:
                titre_fr = titre_en
                contenu_fr = contenu_en

            # Vérifier si l'article existe déjà
            if not Actualite.objects.filter(titre=titre_fr).exists():
                Actualite.objects.create(
                    titre=titre_fr,
                    contenu=contenu_fr,
                    date_publication=datetime.now()
                )
    else:
        print("Erreur lors de la récupération des articles:", response.status_code)"""
from celery import shared_task
import requests
from .models import Actualite
from googletrans import Translator
from datetime import datetime
from accueil.key import API_key

translator = Translator()

@shared_task
def fetch_and_store_articles():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_key}"
    response = requests.get(url)

    if response.status_code == 200:
        # 🔥 Supprime toutes les anciennes actualités
        Actualite.objects.all().delete()
        print("🗑️ Suppression des anciennes actualités")

        articles = response.json().get("articles", [])
        for article in articles[:5]:  # On limite à 5 articles
            titre_en = article.get("title", "Sans titre")
            contenu_en = article.get("description", "Pas de description")
            lien = article.get("url", "")  # URL de l'article original
            image_url = article.get("urlToImage", "")  # URL de l’image associée

            # Traduction en français
            try:
                titre_fr = translator.translate(titre_en, src="en", dest="fr").text
                contenu_fr = translator.translate(contenu_en, src="en", dest="fr").text
            except Exception:
                titre_fr = titre_en
                contenu_fr = contenu_en

            # ✅ Ajoute l'article directement (plus besoin de vérifier l'existence)
            Actualite.objects.create(
                titre=titre_fr,
                contenu=contenu_fr,
                date_publication=datetime.now(),
                lien=lien,
                image_url=image_url
            )
            print(f"✅ Enregistrement de l'actualité: {titre_fr}")

    else:
        print("❌ Erreur lors de la récupération des articles:", response.status_code)