from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='comunes/base.html'), name='home'),
    path('app1/', include('apps.app1.urls')),
    path('app2/', include('apps.app2.urls')),
]


# STATIC FILES
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
