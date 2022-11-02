import uuid
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify 
from django.urls import reverse
from tinymce.models import HTMLField

# ============================ SERVICE =================================== #
class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name=_('title'), help_text=_('Only 200 characters allowed') ,max_length=200)
    overview = models.CharField(
        verbose_name=_('overview'), 
        help_text=_('Short description about this service. Only 500 characters allowed'), 
        max_length=500
    )
    icon = models.ImageField(verbose_name=_('icon'), upload_to='services/icon-image/%Y/%m/')
    thumbnail = models.ImageField(verbose_name=_('thumbnail'), upload_to='services/thumbnail/%Y/%m/')
    detail = HTMLField(verbose_name=_('detail'))
    is_active = models.BooleanField(verbose_name=_('is active'), default=False)

    #Utility fields
    slug = models.SlugField(verbose_name=_('slug'), max_length=250, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(verbose_name=_('created date'), blank=True, null=True)
    last_updated = models.DateTimeField(verbose_name=_('updated date'), blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.slug is None:
            self.slug = slugify(f"{self.title}-{self.id}")

        self.last_updated = timezone.localtime(timezone.now())

        super(Service, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

# ============================ TEAM =================================== #
class Team(models.Model):
    full_name = models.CharField(verbose_name=_('full name'), help_text=_('e.g: John Doe'), max_length=150)
    designation = models.CharField(verbose_name=_('designation'), max_length=50)
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to='team/%Y/%m/')
    short_description = models.CharField(
        verbose_name=_('short description'), 
        help_text=_('Only 100 characters allowed'), 
        max_length=100
    )

    facebook_link = models.CharField(verbose_name=_('facebook link'), max_length=1500, blank=True, null=True)
    twitter_link = models.CharField(verbose_name=_('twitter link'), max_length=1500, blank=True, null=True)
    linkedIn_link = models.CharField(verbose_name=_('linkedIn link'), max_length=1500, blank=True, null=True)
    googleplus_link = models.CharField(verbose_name=_('google+ link'), help_text=_('e.g: johndoe567@gmail.com'), max_length=1500, blank=True, null=True)

    #Utility fields
    is_active = models.BooleanField(verbose_name=_('is active'), default=False)
    date_created = models.DateTimeField(verbose_name=_('created date'), auto_now_add=True)
    last_updated = models.DateTimeField(verbose_name=_('updated date'), auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Team')


# ============================ TESTIMONIALS =================================== #    
class Testimonial(models.Model):
    full_name = models.CharField(verbose_name=_('full name'), help_text=_('e.g: John Doe'), max_length=150)
    designation = models.CharField(verbose_name=_('designation'), max_length=50)
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to='testimonial/%Y/%m/')
    short_message = models.CharField(
        verbose_name=_('short message'), 
        help_text=_('Only 150 characters allowed'), 
        max_length=150
    )

    #Utility fields
    is_active = models.BooleanField(verbose_name=_('is active'), default=False)
    date_created = models.DateTimeField(verbose_name=_('created date'), auto_now_add=True)
    last_updated = models.DateTimeField(verbose_name=_('updated date'), auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')
