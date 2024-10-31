from django.db import models

# Create your models here.

class Categorie (models.Model):
    
    code = models.CharField(max_length=10,primary_key=True)
    libelle = models.CharField(max_length=100,null=False)
    
    def __str__(self):
        return self.libelle
    
    
class Produit(models.Model):
    
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=100,null=False)
    pu = models.DecimalField(max_digits=5,decimal_places=2)
    qte = models.IntegerField()
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,default=0)
    
    def __str__(self):
        return self.libelle
   
    
