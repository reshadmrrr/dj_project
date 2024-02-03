from django.urls import path
from .views import get_contents


app_name = "contents"

urlpatterns = [
    path("/", get_contents),
]
