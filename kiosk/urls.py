from django.contrib import admin
from django.urls import path, include
import CamApp.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static
from kiosk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CamApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('menu_list/', views.menu_list),
    path('menu_register/', views.menu_register,name='menu_register'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('menu_list/<int:menu_id>/menu_delete',views.menu_delete,name='menu_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
