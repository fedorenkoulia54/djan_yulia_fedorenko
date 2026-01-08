from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app_templates.urls")),
    path("blog/", include("blog.urls")),
]
