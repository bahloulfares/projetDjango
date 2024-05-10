from django.shortcuts import render
from .models import Produit
from .forms import ProduitForm
from .forms import FournisseurForm
from .models import Fournisseur
#from .models import Fournisseur
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie ,Produit
from magasin.serializers import CategorySerializer,ProduitSerializer
from rest_framework import viewsets
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class ProduitsAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

def vit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')  # Utilisation de redirect pour éviter les soumissions multiples
    else:
        form = ProduitForm()  # Créer un formulaire vide

    list = Produit.objects.all()  # Récupérer tous les produits de la base de données et les stocker dans la variable "list"
    return render(request, 'magasin/vitrine.html', {'list': list, 'form': form})

def index(request):
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html', context)

def nouveauFournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nouveauFour')  # Redirige vers la liste des fournisseurs après ajout
    else:
        form = FournisseurForm()
    list = Fournisseur.objects.all()
    return render(request, 'magasin/fournisseur.html', {'list': list,'form': form})

