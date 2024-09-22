from django.urls import path
from . import views

urlpatterns = [
  path('', views.articles_list, name='articles_list'),
  path('<int:id>/', views.articles_detail, name='articles_detail'),
  path('new/', views.articles_create, name='articles_create'),
  path('404', views.not_found_page, name='articles_404_page'),
]