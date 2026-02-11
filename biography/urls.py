from django.urls import path
from .views import home
from .views_qr import qr_with_logo


urlpatterns = [
    path('', home, name='home'),
    path('qr/', qr_with_logo, name='qr_with_logo'),
]
