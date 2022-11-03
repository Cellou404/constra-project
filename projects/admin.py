from django.contrib import admin
from django.contrib.admin.options import TabularInline
from django.utils.html import format_html
from django import forms

from projects.models import Project, ProjectCategory, ProjectImage

# Register your models here.
# =================================== PROJECT CATEGORY ===================================== #
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'date_created')
    list_display_links = ('title',)
    search_fields = ('title',)


# =================================== PROJECT IMAGE ===================================== #
class ProjectImageAdmin(TabularInline):
    extra = 4
    model = ProjectImage

# =================================== PROJECT ===================================== #
class ProjectForm(forms.ModelForm):
    class Meta:
        widgets = {
            'title': forms.TextInput(attrs={'size':'80'}),
            'short_description': forms.Textarea(attrs={'rows':'4', 'cols':'80'}),
        }

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def project_thumbnail(self, object):
        return format_html('<img src={} width="40" height="40" style="border-radius: 50%" />'.format(object.thumbnail.url))

    list_display = ('project_thumbnail', 'title', 'client', 'location', 'category', 'size', 'is_active', 'year_completed')
    list_display_links = ('project_thumbnail', 'title')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'category', 'year_completed')
    date_hierarchy = 'date_created'
    inlines = (ProjectImageAdmin,)
    form = ProjectForm

    fieldsets = (
        (None, {
            'fields': ('title', 'short_description')
        }),
        ('INFOS', {
            'fields': (
                ('client','thumbnail'), 
                ('architect', 'location'), 
                ('category', 'size', 'year_completed'),
                'is_active'
                ),
                
        }),
    )