from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ArticlesForm
from .models import Articles

def articles_list(request: HttpRequest) -> HttpResponse:
  articles = Articles.objects.all()

  if articles.exists() == False:
    return redirect('articles_404_page')

  data = {
    'articles': articles
  }
  
  return render(request, 'list.html', data)

def articles_detail(request, id):
  article = get_object_or_404(Articles, id=id)
  return render(request, 'detail.html', {'article': article})

def articles_create(request: HttpRequest) -> HttpResponse:
  if request.method == 'GET':
    form = ArticlesForm()
    return render(request, 'creation.html', {'form': form})
  
  if request.method == 'POST':
    form = ArticlesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles_list')

def not_found_page(request: HttpRequest) -> HttpResponse:
  return render(request, '404.html')
