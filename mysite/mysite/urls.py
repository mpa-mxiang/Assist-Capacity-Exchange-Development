from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("bugs/", include("bugs.urls")),
    path("admin/", admin.site.urls),
]