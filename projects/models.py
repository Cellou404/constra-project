from django.utils import timezone
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse


# =========================== PROJECT IMAGE ============================= #
class ProjectCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, verbose_name=_('title'))
    slug = models.SlugField(verbose_name=_('slug'), max_length=250, unique=True, blank=True, null=True)

    #Utility fields
    is_active = models.BooleanField(verbose_name=_('is active'), default=False)
    date_created = models.DateTimeField(verbose_name=_('created date'), auto_now_add=True)
    last_updated = models.DateTimeField(verbose_name=_('updated date'), auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(f"{self.title}-{self.id}")

        super(ProjectCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Project Category')
        verbose_name_plural = _('Project Categories')

# =========================== PROJECT IMAGE ============================= #
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250, verbose_name=_('title'))
    thumbnail = models.ImageField(upload_to="projects/thumbnail/%Y/%m/%d/" ,verbose_name=_('thumbnail'), blank=True, null=True)
    short_description = models.CharField(
        verbose_name=_('short description'), 
        help_text=_('Give a short description to this project. 500 characters is given'), 
        max_length=500
    )
    client = models.CharField(verbose_name=_('client'), max_length=150)
    architect = models.CharField(verbose_name=_('architect'), max_length=150)
    location = models.CharField(verbose_name=_('location'), max_length=150)
    size = models.PositiveIntegerField(verbose_name=_('size'), help_text=_('Square feet (sqft)'),default=0)
    year_completed = models.PositiveIntegerField(verbose_name=_('year completed'))
    category = models.ForeignKey(ProjectCategory, related_name='projects', on_delete=models.CASCADE, verbose_name=_('category'))

    #Utility fields
    is_active = models.BooleanField(verbose_name=_('is active'), default=False)
    slug = models.SlugField(verbose_name=_('slug'), max_length=250, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(verbose_name=_('created date'), blank=True, null=True)
    last_updated = models.DateTimeField(verbose_name=_('updated date'), blank=True, null=True)

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'slug': self.slug})

    @property
    def get_images(self):
        return self.images.all().order_by('-date_created')

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.slug is None:
            self.slug = slugify(f"{self.title}")

        self.slug = slugify(f"{self.title}")
        self.last_updated = timezone.localtime(timezone.now())

        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


# =========================== PROJECT IMAGE ============================= #
class ProjectImage(models.Model):
    image = models.ImageField(upload_to="projects/%Y/%m/%d/" ,verbose_name=_('image'))
    project = models.ForeignKey(Project, verbose_name=_('Link to project'), related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    
    #Utility fields
    is_active = models.BooleanField(verbose_name=_('is active'), default=False)
    date_created = models.DateTimeField(verbose_name=_('created date'), auto_now_add=True)
    last_updated = models.DateTimeField(verbose_name=_('updated date'), auto_now=True)

    def __str__(self):
        return ''

    class Meta:
        verbose_name = _('Project Image')
        verbose_name_plural = _('Project Images')