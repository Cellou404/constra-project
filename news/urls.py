from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<slug:slug>/', views.news_detail, name='news-detail'),
    path('category-detail/<slug:slug>/', views.category_view, name='category-detail'),
    path('archive-detail/<slug:slug>/', views.archive_view, name='archive-detail'),
]