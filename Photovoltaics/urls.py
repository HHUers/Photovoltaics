from django.contrib import admin
from django.urls import path, re_path, include
from apps.web.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include('apps.web.urls', namespace='web')),
]

handler404 = page_not_found
