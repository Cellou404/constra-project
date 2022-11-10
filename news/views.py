from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from news.models import Post, Comment, Category, Archive
from .forms import CommentForm

# Create your views here.

# ========== NEWS PAGE VIEW =============
def news(request):
    news = Post.objects.filter(is_active=True).order_by('-date_created')
    paginator = Paginator(news, 3)
    page = request.GET.get('page')
    paged_news = paginator.get_page(page)

    context = {
        'news': paged_news,
    }
    return render(request, 'news/news.html', context)

# ========== NEWS DETAIL PAGE VIEW =============
def news_detail(request, slug):
    single_news = get_object_or_404(Post, slug=slug)
    comments = single_news.comments.filter(is_active=True).order_by('-date_created')

    #Comment poste
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = single_news
            new_comment.save()

            messages.success(request, _("Your comment have been sent succesful"))
            return redirect('news-detail', single_news.slug)
        else:
            messages.error(request, _("Ooops..! Something went wrong. Please try again!"))
            return redirect('news-detail', single_news.slug)
    else:
        comment_form = CommentForm()

    context = {
        'obj': single_news,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'news/news-single.html', context)


# ========== CATEGORY PAGE VIEW =============
def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    news = Post.objects.prefetch_related().filter(category=category, is_active=True).order_by('-date_created')
    paginator = Paginator(news, 3)  # 2 posts in each page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        queryset = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'news': queryset,
        'page': page
    }
    return render(request, 'news/news-categorised.html', context)
    
# ========== ARCHIVE PAGE VIEW =============
def archive_view(request, slug):
    year_completed = get_object_or_404(Archive, slug=slug)
    news = Post.objects.filter(year_completed=year_completed, is_active=True).order_by('-date_created')
    paginator = Paginator(news, 3)  # 2 posts in each page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        queryset = paginator.page(paginator.num_pages)
    print(news)
    context = {
        'year_completed': year_completed,
        'news': queryset,
        'page': page
    }
    return render(request, 'news/archives.html', context)


