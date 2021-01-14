from django.contrib import admin
from django.urls import path
import CamApp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", CamApp.views.index, name="index"),
    path("feed/", CamApp.views.feed, name="feed"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
