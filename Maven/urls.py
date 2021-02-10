from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url, static
from django.contrib.auth import views as auth_views
#from django.conf.urls import handler404, handler500

from . import views

def error404(request, exception=None):
    return render(request, '404.html', status=404)

def error500(request):
    return render(request, '500.html', status=500)

"""
Django Admin Rename
"""
admin.site.site_header = 'MavenBiz'
admin.site.site_title = ' MavenBiz Administration'
#admin.site.site_url = ''
admin.site.index_title = 'Home'
admin.empty_value_display = ''


urlpatterns = [
    path(
        '', include('Service.urls')
    ),
    path('admin/', admin.site.urls),
]

if not settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'Maven.views.error404'

handler500 = 'Maven.views.error500'
