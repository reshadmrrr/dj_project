from rest_framework.decorators import api_view
from .models import Content
from django.http.response import JsonResponse


@api_view(["GET"])
def get_contents(request):
    contents = Content.objects.prefetch_related(
        "content_context",
        "content_media",
        "media_urls",
        "content_stat",
        "content_stat__content_stat_views",
        "content_stat__content_stat_comments",
    )
    return JsonResponse({"contents": contents})
