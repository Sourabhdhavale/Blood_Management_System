from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Blood Management System Admin"
admin.site.site_title = "Blood Management System Admin Portal"
admin.site.index_title = "Welcome to Blood Management System"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)