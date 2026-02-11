from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from biography.views import home
from .views_qr import qr_with_logo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('qr/', qr_with_logo, name='qr_with_logo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
