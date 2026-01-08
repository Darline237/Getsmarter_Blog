from django.shortcuts import render, get_object_or_404
from .models import Article, Contact


def home(request):
    articles = Article.objects.filter(status='published').order_by('-create_at') #on prend seulement les articles publiés du plus récent au plus ancien
    return render(request, 'blog/home.html', {'articles': articles}) # on envoie les articles au fichier HTML


def presentation_article(request):
    articles = Article.objects.order_by('-create_at')
    return render(request, 'blog/presentation_article.html', {'articles': articles})

def details_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/details_article.html', {'article': article})


def contact(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        email= request.POST.get("email")
        message=request.POST.get("message")
        
        Contact.objects.create(name= name,email=email,message=message) # extencier la classe

        
    
    return render(request,'blog/contact.html')
