from django.shortcuts import render
from app_commande.models import Categorie,Produit
from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import CategorieSerializer
from .models import *



  

def home(request):
    
    nrcategorie = Categorie.objects.all().count()
    nbrproduit = Produit.objects.all().count()
    
    ctx ={
        'nrcategorie':nrcategorie,
        'nbrproduit':nbrproduit
    }
    
    return render(request,'home.html',ctx)

def categorie(request):
    
    cats = Categorie.objects.all()
    
    cxt = {
        'cats':cats
    }
    
    return render(request, 'categorie.html',cxt)

def ajouterCategorie(request):
    
    return render(request, 'ajouterCategorie.html')


def addCategorie(request):
    message = None
    if request.method == 'POST':
        codecat = request.POST["code"]
        libcat = request.POST["libelle"]
            
        rs_cat = Categorie.objects.filter(code=codecat)

        if len(rs_cat)>0:
            message ="Ce code catégorie existe"    
        else:
            cates = Categorie(
                  
                  code = codecat,
                  libelle = libcat,
            )  
          
            cates.save()
            message ="catégorie enregistrée  avec succès"
            
    ctx ={
        'message':message
    }
    return render(request,'ajouterCategorie.html',ctx)

def deleteCategorie(request,id):
    
    cat = Categorie.objects.get(pk=id)
    cat.delete()
        
    return redirect('/categorie/')

def modifierCategorie(request,id):
    c = Categorie.objects.get(pk=id)
      
    ctx= {
          'c':c
      }
    return render(request,'modifierCategorie.html',ctx)

def updateCategorie(request,id):
    c = Categorie.objects.get(pk = id)
    lib = request.POST["libelle"]
         
    c.libelle  = lib
      
      #print(f.intfrais,f.montant,f.codefrais)
    c.save()
    return redirect('/categorie/')

#view produit

def produit(request):
    data =[]
    pr = Produit.objects.all()
    
    for p in pr:
        data.append({
            'code':p.code,
            'lebelle':p.libelle,
            'qte': p.qte,
            'pu': p.pu,
            'prtotal': p.pu * p.qte,
            'categorie':p.categorie
            
            
        })
        
    
    cxt = {
        'pr':data
    }
    
    return render(request, 'produit.html',cxt)

def ajouterProduit(request):
    
    cats = Categorie.objects.all()
    
    ctx ={
        'cats': cats
    }
    
    return render(request, 'ajouterProduit.html',ctx)

def addProduit(request):
    message = None
    if request.method == 'POST':
        code = request.POST["code"]
        libcat = request.POST["libelle"]
        qte = request.POST["qte"]
        pu = request.POST["pu"]
        categorie = request.POST["categorie"]
            
        rs_pr = Produit.objects.filter(code=code)
        cat = Categorie.objects.get(code=categorie)

        if len(rs_pr)>0:
            message ="Ce code produit existe"    
        else:
            prod = Produit(
                  
                  code = code,
                  libelle = libcat,
                  pu = pu,
                  qte = qte,
                  categorie = cat,
            )  
          
            prod.save()
            message ="produit enregistré  avec succès"
            
    ctx ={
        'message':message
    }
    return render(request,'ajouterProduit.html',ctx)


## CRéation des APIS pour le modele Cate

class CategorieDetails(APIView):
    def get(self,request):
        obj = Categorie.objects.all()
        serializer = CategorieSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = CategorieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)

class CategorieInfo(APIView):
    
    def get(self,request,id):
        try:
            obj = Categorie.objects.get(pk=id)
        except:
            msg={"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorieSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            obj = Categorie.objects.get(pk=id)
            
        except Categorie.DoesNotExist:
            msg={"msg":"not found error"}
            
            return Response(msg, status = status.HTTP_404_NOT_FOUND)
        
        serializer = CategorieSerializer(obj,data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        try:
            obj = Categorie.objects.get(pk=id)
            
        except Categorie.DoesNotExist:
            msg={"msg":"not found error"}
            
            return Response(msg, status = status.HTTP_404_NOT_FOUND)
        
        serializer = CategorieSerializer(obj,data = request.data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj = Categorie.objects.get(pk=id)
        
        except Categorie.DoesNotExist:
            msg = {"msg":"not found"}
            
            return Response(msg, status = status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
