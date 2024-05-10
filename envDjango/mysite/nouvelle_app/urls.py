from django.urls import path
from .views import liste_taches, ajouter_tache, marquer_termine,supprimer_tache

urlpatterns = [
    path('', liste_taches, name='liste_taches'),
    path('ajouter/', ajouter_tache, name='ajouter_tache'),
    path('marquer-termine/<int:tache_id>/', marquer_termine, name='marquer_termine'),
     path('supprimer/<int:tache_id>/', supprimer_tache, name='supprimer_tache'),
]
