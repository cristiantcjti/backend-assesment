from django.shortcuts import redirect
from django.urls import include, path

from .app import api_v1

urlpatterns = [
    path("", lambda _: redirect("v1/docs", permanent=True)),
    path("v1/", api_v1.urls),
    path("health-check/", include("health_check.urls")),
]
