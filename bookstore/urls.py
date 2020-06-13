from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Djagno Admin
    path('admin/', admin.site.urls),

    # Users Management
    path('accounts/', include('allauth.urls')),

    # Local
    path('orders/', include('orders.urls')),
    path('', include('books.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )