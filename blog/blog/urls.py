from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from .views import index
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
path('', include('apps.posts.urls')),
path('', include('apps.contacto.urls')),

]  +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
