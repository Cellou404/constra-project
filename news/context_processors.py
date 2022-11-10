from django.shortcuts import get_object_or_404
from news.models import Post, Category, Archive


#Available in each template. (Sidebar)
def recent_news(request):
    recent_news = Post.objects.filter(is_active=True).order_by('-date_created')[:3]
    context = {'recent_news': recent_news}
    return context

def category_links(request):
    categories = Category.objects.filter(is_active=True).order_by('-date_created')[:6]

    return {'categories': categories}

def archive_links(request):
    dates = Archive.objects.filter(is_active=True).order_by('-date_created')[:6]
    #dates = Archive.objects.order_by('-date_created').values_list('date', flat=True).distinct()

    return {'dates': dates}
