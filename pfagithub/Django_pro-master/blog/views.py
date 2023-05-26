from typing import Optional
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from newsapi import NewsApiClient
import requests
from .newsapi import get_football_news
# Create your views here.
posts=[
    {
        "author":"Botola Pro ",
        "title":"WAC   vs   MCO",
        "content":"Le Mouloudia Club d'Oujda est un club de football marocain basé dans la ville d'Oujda, dans le nord-est du Maroc. Il a été fondé en 1946 et joue actuellement en première division marocaine, la Botola Pro.Le Wydad Athletic Club est également un club de football marocain basé à Casablanca. Il a été fondé en 1937 et est l'un des clubs les plus populaires et les plus titrés du Maroc. Le WAC a remporté de nombreux titres nationaux et internationaux, notamment la Ligue des champions de la CAF en 2017.",
        "date_posted":"May 3, 2023",
    },
    {
        "author":"Premiere League",
        "title":"MUN   vs   ARS",
        "content":"I see you",
        "date_posted":"20 October, 2023"
    },
]



def home(request):
    context={
        "posts": Post.objects.all()
    }
    return render(request,"blog/home.html",context)

class PostListView(ListView):
    model=Post
    template_name="blog/home.html" # <app>/<model>_<viewtype>.html
    context_object_name="posts"
    ordering=["-date_posted"]

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=["title","content"]

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)    


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=["title","content"]    

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False  

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post 
    success_url= "/"

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False            

def Leagues(request):
    return render(request,"blog/Leagues.html",{"title":"Leagues"})
def Matches(request):
    return render(request,"blog/Matches.html",{"title":"Matches"})


def Latest_News(request):
    api_key = '2ea9549ba46e427a860139f9ad35729d'
    articles = get_football_news(api_key)

    context = {
        'articles': articles
    }

    return render(request, 'blog/Latest News.html', context)




