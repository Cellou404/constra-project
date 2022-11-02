from django.contrib import admin
from django.utils.html import format_html
from django.forms import TextInput, Textarea
from django import forms
from .models import *


# =================================== SERVICE ===================================== #
class ServiceForm(forms.ModelForm):
    class Meta:
        widgets = {
            'title': forms.TextInput(attrs={'size':'80'}),
            'overview': forms.Textarea(attrs={'rows':'4', 'cols':'80'}),
            'slug': forms.TextInput(attrs={'size':'80'}),
        }

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    def icon_img(self, object):
        return format_html('<img src={} width="40" style="border-radius: 50%" />'.format(object.icon.url))
    
    list_display = ['icon_img', 'title', 'is_active', 'date_created']
    list_display_links = ['icon_img', 'title']
    list_filter = ['is_active']
    search_fields = ['title']
    list_per_page = 10
    date_hierarchy = "date_created"
    form = ServiceForm


# =================================== TEAM ===================================== #
class TeamForm(forms.ModelForm):
    class Meta:
        widgets = {
            'short_description': forms.Textarea(attrs={'rows':'4', 'cols':'35'}),
        }

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src={} width="40" style="border-radius: 50%" />'.format(object.avatar.url))

    list_display = ['id', 'thumbnail', 'full_name', 'designation', 'is_active', 'date_created']
    list_display_links = ['id', 'thumbnail', 'full_name']
    search_fields = ['full_name', 'designation']
    list_filter = ['designation', 'is_active']
    list_per_page = 10
    date_hierarchy = "date_created"

    form = TeamForm

# =================================== TESTIMONIAL ===================================== #
class TestiForm(forms.ModelForm):
    class Meta:
        widgets = {
            'full_name': forms.TextInput(attrs={'size':'60'}),
            'designation': forms.TextInput(attrs={'size':'60'}),
            'short_message': forms.Textarea(attrs={'rows':'4', 'cols':'60'}),
        }

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src={} width="40" style="border-radius: 50%" />'.format(object.avatar.url))

    list_display = ['id', 'thumbnail', 'full_name', 'designation', 'is_active', 'date_created']
    list_display_links = ['id', 'thumbnail', 'full_name']
    search_fields = ['full_name', 'designation']
    list_filter = ['designation', 'is_active']
    list_per_page = 10
    date_hierarchy = "date_created"
    
    form = TestiForm