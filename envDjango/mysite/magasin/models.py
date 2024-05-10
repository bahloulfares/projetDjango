from django.db import models
from datetime import date


class Categorie(models.Model):
    TYPE_CHOICES = [
        ('Al', 'Alimentaire'), 
        ('Mb', 'Meuble'),
        ('Sn', 'Sanitaire'),
        ('Vs', 'Vaisselle'),
        ('Vt', 'Vêtement'),
        ('Jx', 'Jouets'),
        ('L', 'Linge de Maison'),
        ('Bj', 'Bijoux'),
        ('Dc', 'Décor'),
        ('Im','Immobilier'),
        ('Vt','Vêtement'),
        ('Prph','ParaPharmacie'),
        ('Em','Electroménager'),
        ('Tp','Tapis'),
        ('Fr','Frais')
    ]
    name = models.CharField(max_length=50, choices=TYPE_CHOICES, default="Alimentaire")
    
    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return f"Nom: {self.nom}, Adresse: {self.adresse}, Email: {self.email}, Téléphone: {self.telephone}"

    
class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    TYPE_CHOICES = [
        ('em', 'emballé'), 
        ('fr', 'Frais'), 
        ('cs', 'Conserve')
    ]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='em')
    Img  = models.ImageField (blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.libelle} - {self.description} - {self.prix} - {self.get_type_display()}"
    
class ProduitNC(Produit):
    duree_garantie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.libelle} ({self.duree_garantie})"

    
class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField(Produit)

    def __str__(self):
        return f"Commande du {self.dateCde}"
    


