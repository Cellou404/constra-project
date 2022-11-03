from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<slug:slug>', views.project_detail, name='project-detail')
]