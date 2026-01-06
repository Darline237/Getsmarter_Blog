from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Article', views.presentation_article, name='presentation_article'),
    path('Description/<int:id>/', views.details_article, name='details_article'),
]
