from django.urls import include, path
from . import views
from .views import CategoryAPIView ,ProduitsAPIView
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView
# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('produit', ProductViewset, basename='produit')

urlpatterns = [
    path('', views.index, name='index'),
    path('nouvFournisseur/', views.nouveauFournisseur, name='nouveauFour'),
    path('vitrine/', views.vit, name='vitrine'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitsAPIView.as_view()),
    path('api/', include(router.urls)),
]
