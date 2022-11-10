from django.contrib import admin
from django import forms
from faq.models import FAQ
# Register your models here.

# =================================== TESTIMONIAL ===================================== #
class FaqForm(forms.ModelForm):
    class Meta:
        widgets = {
            'question': forms.TextInput(attrs={'size':'80'}),
            'answer': forms.Textarea(attrs={'rows':'8', 'cols':'80'}),
        }

@admin.register(FAQ)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'subject','date_created']
    list_display_links = ['id', 'question']
    search_fields = ['question']

    form = FaqForm