from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django import forms

from .models import Author, Category, Archive, Post, Comment


#================================ AUTHOR ========================#
class AuthorForm(forms.ModelForm):
    class Meta:
        widgets = {
            'full_name': forms.TextInput(attrs={'size':'80'}),
            'email': forms.TextInput(attrs={'size':'80'}),
            'designation': forms.TextInput(attrs={'size':'80'}),
            'short_description': forms.Textarea(attrs={'rows':'4', 'cols':'80'}),
        }

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    def profile_picture(self, object):
        return format_html('<img src={} width="40" style="border-radius: 50%" />'.format(object.avatar.url))

    list_display = ('profile_picture', 'full_name', 'designation', 'email')
    search_fields = ('full_name', 'email')
    list_per_page = 10
    form = AuthorForm

    fieldsets = (
        (_('Choose the User & Avatar'), {
            'fields': ('user', 'avatar')
        }),
        (_('User informations'), {
            'fields': (
                'full_name',
                'email',
                'designation',
                'short_description'
                ),
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('date',)
    date_hierarchy = 'date_created'

    fieldsets = (
        (None, {
            'fields': ('date', 'is_active')
        }),
        (_('Utilities fileds (Not required). These fields will be automaticaly fulfilled'), {
            'fields': (
                'slug',
                ('date_created', 'last_updated')
                ),
                
        }),
    )
#================================ POST ========================#
class PostForm(forms.ModelForm):
    class Meta:
        widgets = {
            'title': forms.TextInput(attrs={'size':'80'}),
            'slug': forms.TextInput(attrs={'size':'80'}),
        }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def post_thumbnail(self, object):
        return format_html('<img src={} width="40" height="30" style="border-radius: 8px" />'.format(object.thumbnail.url))

    list_display = ('post_thumbnail', 'title', 'author', 'is_active', 'date_created')
    list_display_links = ('post_thumbnail', 'title')
    list_filter = ('is_active', 'author', 'date_created')
    search_fields = ('title', 'author')
    date_hierarchy = 'date_created'
    list_per_page = 10

    form = PostForm

    actions = ['publish_posts', 'unpublish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(is_active=True)

    def unpublish_posts(self, request, queryset):
        queryset.update(is_active=False)

    fieldsets = (
        (_('Title'), {
            'fields': ('title',)
        }),
        (_('Author & thumbnail'), {
            'fields': (('author', 'thumbnail'),)
        }),
        (_('Detail'), {
            'fields': ('detail',)
        }),
        (_('Category & Year completed'), {
            'fields': (('category', 'year_completed'),)
        }),
        (('Activate or Desactivate'), {
            'fields': ('is_active',)
        }),
        (_('Utilities fileds (Not required). These fields will be automaticaly fulfilled'), {
            'fields': (
                'slug',
                ('date_created', 'last_updated')
                ),
        }),
    )

#================================ COMMENT ========================#
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active', 'date_created')
    list_filter = ('is_active', 'date_created')
    search_fields = ('name', 'email')
    list_per_page = 10
    actions = ['approve_comments', 'desapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_active=True)
    
    def desapprove_comments(self, request, queryset):
        queryset.update(is_active=False)