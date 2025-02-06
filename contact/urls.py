from django.urls import path
from .views import formulaire_contact

urlpatterns = [
    path('', formulaire_contact, name='contact'),
]