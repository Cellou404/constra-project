import uuid
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify 
from django.urls import reverse


class FAQ(models.Model):
    CHOICES = (
        ('CONSTRUCTION', 'Construction General'),
        ('SAFETY', 'Safety'),
    )
    question = models.CharField(verbose_name=_('question'), max_length=250)
    answer = models.TextField(verbose_name=_('answer'))
    subject = models.CharField(verbose_name=_('subject'), max_length=250, choices=CHOICES)
    is_active = models.BooleanField(default=True,verbose_name=_('is active'), blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
