from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:bug_id>/", views.detail, name="detail"),
    path("<int:bug_id>/results/", views.results, name="results")
]