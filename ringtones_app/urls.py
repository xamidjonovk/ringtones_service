# ringtones_app/urls.py
from django.urls import path
from .views import api

urlpatterns = [
    path("", api.urls),  # Include all API endpoints
]
