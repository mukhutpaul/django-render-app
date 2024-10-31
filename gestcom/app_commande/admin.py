from django.contrib import admin
from app_commande.models import Categorie
from app_commande.models import Produit

# Register your models here.


admin.site.register(Categorie,list_display=['code','libelle'])
admin.site.register(Produit,list_display=['code','libelle','pu','qte','categorie'])
