from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
    path('myblog/', include('myblog.urls', namespace='myblog')),
    path('users/', include('users.urls', namespace='users')),
    path('sending/', include('sending.urls', namespace='sending'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
