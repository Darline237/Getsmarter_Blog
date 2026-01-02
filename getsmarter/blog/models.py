from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    STATUS_CHOICES =(
        ('draft', 'brouillon'), #('valeur_stocké','valeur affichée')
        ('published', 'publié')
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
