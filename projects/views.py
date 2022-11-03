from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from projects.models import Project, ProjectCategory, ProjectImage

# Create your views here.

def projects(request):
    categories = ProjectCategory.objects.filter(is_active=True)
    projects = Project.objects.filter(is_active=True).order_by('-date_created')
    paginator = Paginator(projects, 6)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)

    context = {
        "categories": categories,
        "projects": paged_projects,
    }
    return render(request, 'projects/project-list.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    images = project.images.filter(is_active=True).order_by('-date_created')

    context = {
        "project": project,
        "images": images,
    }
    return render(request, 'projects/project-detail.html', context)
