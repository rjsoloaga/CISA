from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import re_path
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('login/', include('users.urls')),
    path('institutos/', include('institutos.urls')),
    path('serviceworker.js', TemplateView.as_view(
        template_name="layouts/serviceworker.js", 
        content_type='application/javascript'
    ), name='serviceworker'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

