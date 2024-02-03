from django.urls import path


from views import get_authors

app_name = "authors"

urlpatterns = [
    path("/", get_authors),
]
