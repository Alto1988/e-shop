from django.conf import settings
from django.conf.urls.static import static
from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
]

#DO NOT SERVE STATIC FILES THIS WAY FOR PRODUCTION!!!!!!!!!!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
