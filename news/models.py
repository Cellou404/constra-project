import uuid
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify 
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth.models import User

#================================ CATEGORY ========================#
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(verbose_name=_('full name'), max_length=150, blank=True, null=True)
    email = models.CharField(verbose_name=_('email'), max_length=150, blank=True, null=True)
    avatar = models.ImageField(upload_to='author/%Y/%m/%d/', blank=True, null=True)
    designation = models.CharField(verbose_name=_('designation'), max_length=150, blank=True, null=True)
    short_description = models.CharField(
        verbose_name=_('short description'), 
        help_text=_('Only 200 characters allowed'), 
        max_length=500, blank=True, null=True
        )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

#================================ CATEGORY ========================#
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name=_('title'), max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True,verbose_name=_('is active'), blank=True, null=True)

    #Utility fields
    slug = models.SlugField(verbose_name=_('slug'), max_length=250, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(verbose_name=_('created date'), blank=True, null=True)
    last_updated = models.DateTimeField(verbose_name=_('updated date'), blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.slug is None:
            self.slug = slugify(f"{self.title}-{self.id}")

        self.last_updated = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


#================================ CATEGORY ========================#
class Archive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.CharField(verbose_name=_('date'), help_text=_('Please use this format: November 2021'), max_length=16, null=True, blank=True)
    is_active = models.BooleanField(default=True,verbose_name=_('is active'), blank=True, null=True)

    #Utility fields
    slug = models.SlugField(verbose_name=_('slug'), max_length=250, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(verbose_name=_('created date'), blank=True, null=True)
    last_updated = models.DateTimeField(verbose_name=_('updated date'), blank=True, null=True)

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse('archive-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.slug is None:
            self.slug = slugify(f"{self.date}-{self.id}")

        self.last_updated = timezone.localtime(timezone.now())
        super(Archive, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Archive')
        verbose_name_plural = _('Archives')


#================================ POST ========================#
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name=_('title'), help_text=_('Only 200 characters allowed') ,max_length=200)
    author = models.ForeignKey(Author, verbose_name=_('author'), on_delete=models.CASCADE)
    thumbnail = models.ImageField(verbose_name=_('thumbnail'), upload_to='post/%Y/%m/%d/')
    detail = HTMLField(verbose_name=_('detail'))
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, default=_('miscellanous'), verbose_name=_('category'))
    year_completed = models.ForeignKey(Archive,related_name='posts', on_delete=models.CASCADE ,verbose_name=_('year completed'), blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_('is active'), default=False)

    #Utility fields
    slug = models.SlugField(verbose_name=_('slug'), max_length=250, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(verbose_name=_('created date'), blank=True, null=True)
    last_updated = models.DateTimeField(verbose_name=_('updated date'), blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.slug is None:
            self.slug = slugify(f"{self.title}")

        self.slug = slugify(f"{self.title}")
        self.last_updated = timezone.localtime(timezone.now())
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    @property
    def get_comments(self):
        return self.comments.all().order_by('-date-created')


#================================ COMMENT ========================#
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    #parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return ""