from rest_framework.decorators import api_view
from .models import AuthorInfo
from django.http.response import JsonResponse


# Create your views here.
@api_view(["GET"])
def get_authors(request):
    author_info = AuthorInfo.objects.prefetch_related(
        "author_avater", "author_stat", "author_stat__author_stat_followers"
    )
    return JsonResponse({"authors": author_info})
