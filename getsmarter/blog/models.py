from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES =(
        ('draft', 'brouillon'), #('valeur_stocké','valeur affichée')
        ('published', 'publié')
    )
    category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name='articles',      
    blank=True
)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add= True)
    published_at = models.DateTimeField(null=True, blank=True) #null = true : autorise une valeur vide dans la bd; blank=true: autorise un champs vide dans les formulaires
    status = models.CharField(
        max_length = 10,
        choices = STATUS_CHOICES,
        default="draft"
    ) 

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField()
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name
    

