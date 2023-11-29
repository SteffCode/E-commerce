from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category ,related_name='categorie', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media')
    image3 = models.ImageField(upload_to='media')
    poids = models.FloatField()
    matiere = models.CharField(max_length=200)
    dimension = models.CharField(max_length=200)
    couleur =models.CharField(max_length=200)
    taille= models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    num = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']
    
    def __str__(self):
        return self.nom
    
class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    besoin = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.nom

class Newsletter(models.Model):
    new_email = models.EmailField()
    date_email = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_email']

    def __str__(self):
        return self.new_email
