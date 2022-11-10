
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404

from django.utils.translation import gettext_lazy as _
from main.views import upload_image
 
admin.site.index_title = _('Constra')
admin.site.site_header = _('Constra Administration')
admin.site.site_title = _('Constra Management')

urlpatterns = i18n_patterns(
    path('upload_image/', upload_image),
    path('tinymce/', include('tinymce.urls')),

    path('', include('main.urls')),
    path('projects/', include('projects.urls')),
    path('news/', include('news.urls')),

    path('admin/', admin.site.urls),

    # If no prefix is given, use the default language
    prefix_default_language=False
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handling the 404 error
handler404 = "main.views.page_not_found_view"
