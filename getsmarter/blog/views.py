from django.shortcuts import render
from .models import Article


def home(request):
    articles = Article.objects.filter(status='published').order_by('-create_at') #on prend seulement les articles publiés du plus récent au plus ancien
    return render(request, 'blog/home.html', {'articles': articles}) # on envoie les articles au fichier HTML


