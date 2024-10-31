"""
URL configuration for gestcom project.
l
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_commande.views import  home,addProduit,ajouterProduit,produit,categorie,ajouterCategorie,addCategorie,deleteCategorie,modifierCategorie,updateCategorie
from app_commande.views import CategorieInfo,CategorieDetails

from gestcom.views import get_access_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('categorie/', categorie, name="categorie"),
    path('ajouterCategorie/',ajouterCategorie, name="ajouterCategorie"),
    path('addCategorie/',addCategorie, name="addCategorie"),
    path('deleteCategorie<str:id>/',deleteCategorie, name="deleteCategorie"),
    path('modifierCategorie<str:id>/',modifierCategorie, name="modifierCategorie"),
    path('updateCategorie<str:id>/',updateCategorie, name="updateCategorie"),
    
    #url produit
    
    path('produit/', produit, name="produit"),
    path('ajouterProduit/',ajouterProduit, name="ajouterProduit"),
    path('addProduit/',addProduit, name="addProduit"),
    
    path('categorieinfo/<str:id>',CategorieInfo.as_view(), name="categorieinfo"),
    
    path('categoriedetail/',CategorieDetails.as_view(), name="categoriedetail"),
    
    path('get_access_token/',get_access_token, name="get_access_token"),
    
    
    
    
    
    
    
    
    
    
    
     
     
     
    
    
    
    
]
