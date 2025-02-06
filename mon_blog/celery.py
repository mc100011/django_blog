import os
from celery import Celery

# Définir les paramètres Django pour Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mon_blog.settings")

# Initialisation de Celery
celery_app = Celery("mon_blog")

# Charger les paramètres depuis Django settings
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Détecter automatiquement les tâches dans les apps Django
celery_app.autodiscover_tasks()



"""
==================================================
🚀 Script de gestion de Celery et Celery Beat pour Django
==================================================

Ce script contient toutes les commandes utiles pour :

1️⃣ Lancer Celery Worker
2️⃣ Lancer Celery Beat
3️⃣ Vérifier et gérer les tâches périodiques avec Django Celery Beat
4️⃣ Redémarrer Celery et Celery Beat en cas de problème

💡 Utilisation : Copie-colle ces commandes dans le terminal Django.
"""

# ==============================
# 1️⃣ Démarrer Celery Worker
# ==============================
# Ouvre un terminal et exécute :
"""
celery -A mon_blog worker --loglevel=info
"""

# ==============================
# 2️⃣ Démarrer Celery Beat
# ==============================
# Ouvre un autre terminal et exécute :
"""
celery -A mon_blog beat --loglevel=info &
"""

# ==============================
# 3️⃣ Vérifier que Celery tourne bien
# ==============================
# Liste les processus Celery actifs
"""
ps aux | grep celery
"""

# ==============================
# 4️⃣ Vérifier que Celery Beat tourne bien
# ==============================
"""
ps aux | grep beat
"""

# ==============================
# 5️⃣ Redémarrer Celery Beat (si nécessaire)
# ==============================
# Stopper Celery Beat
"""
pkill -f "celery beat"
"""

# Relancer Celery Beat
"""
celery -A mon_blog beat --loglevel=info &
"""

# ==============================
# 6️⃣ Supprimer une ancienne tâche périodique (si nécessaire)
# ==============================
# Ouvre le shell Django
"""
python manage.py shell
"""

# Puis, exécute ces commandes dans le shell Django :
"""
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

# Supprime les anciennes tâches (modifie le nom si nécessaire)
PeriodicTask.objects.filter(name="fetch_news_every_8_hours").delete()
PeriodicTask.objects.filter(name="fetch_news_every_2_minutes").delete()

# Créer un nouvel intervalle de 2 minutes
schedule, created = IntervalSchedule.objects.get_or_create(
    every=2,
    period=IntervalSchedule.MINUTES,
)

# Créer une nouvelle tâche périodique pour exécuter fetch_and_store_articles toutes les 2 minutes
PeriodicTask.objects.create(
    interval=schedule,
    name="fetch_news_every_2_minutes",
    task="accueil.tasks.fetch_and_store_articles",
    args=json.dumps([]),
)

print("✅ La tâche a été créée et va s'exécuter toutes les 2 minutes.")
"""

# ==============================
# 7️⃣ Vérifier que les tâches sont bien enregistrées
# ==============================
"""
from django_celery_beat.models import PeriodicTask
print(PeriodicTask.objects.all())
"""

# ==============================
# 8️⃣ Forcer l'exécution d'une tâche pour tester manuellement
# ==============================
"""
from accueil.tasks import fetch_and_store_articles
fetch_and_store_articles.delay()
"""

# ==============================
# ✅ Fin du script - Celery et Celery Beat doivent être fonctionnels 🎯
# ==============================