from django.urls import path
from .views import Home, About

urlpatterns = [
    path('', Home.as_view(), name= 'blog-home'),
    path('about/', About.as_view(), name= 'blog-about'),
]
