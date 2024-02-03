import uuid
from core.authors.models import AuthorInfo
from core.models import BaseModel
from django.db import models

# Create your models here.
MEDIA_CHOICES = (("IMAGE", "IMAGE"), ("VIDEO", "VIDEO"), ("", ""))


class Content(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)
    author = models.ForeignKey(
        AuthorInfo,
        on_delete=models.CASCADE,
        related_name="author",
        blank=True,
        null=True,
    )
    origin_url = models.URLField(max_length=4096, blank=True, null=True)

    @property
    def unique_id(self):
        return self.pk

    @property
    def unique_uuid(self):
        return self.uuid

    @property
    def origin_unique_id(self):
        return self.origin_url.split("/")[-1]


class Context(BaseModel):
    main_text = models.TextField(max_length=4096, null=True, blank="")
    token_count = models.IntegerField()
    tag_count = models.IntegerField()
    char_count = models.IntegerField()
    content = models.OneToOneField(
        Content,
        on_delete=models.CASCADE,
        related_name="content_context",
        blank=True,
        null=True,
    )


class Media(BaseModel):
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES, default="")
    content = models.OneToOneField(
        Content,
        on_delete=models.CASCADE,
        related_name="content_media",
        blank=True,
        null=True,
    )


class URL(BaseModel):
    url = models.URLField(max_length=4096, blank=True, null=True)
    media = models.ForeignKey(
        AuthorInfo,
        on_delete=models.CASCADE,
        related_name="media_urls",
        blank=True,
        null=True,
    )


class ContentStat(BaseModel):
    author = models.OneToOneField(
        Content,
        on_delete=models.CASCADE,
        related_name="content_stat",
        blank=True,
        null=True,
    )


class ContentLikesCount(models.Model):
    author_stat = models.OneToOneField(
        ContentStat,
        on_delete=models.CASCADE,
        related_name="content_stat_likes",
        blank=True,
        null=True,
    )
    id = models.IntegerField(primary_key=True)
    count = models.BigIntegerField()


class ContentViewsCount(models.Model):
    author_stat = models.OneToOneField(
        ContentStat,
        on_delete=models.CASCADE,
        related_name="content_stat_views",
        blank=True,
        null=True,
    )
    id = models.IntegerField(primary_key=True)
    count = models.BigIntegerField()


class ContentCommentsCount(models.Model):
    author_stat = models.OneToOneField(
        ContentStat,
        on_delete=models.CASCADE,
        related_name="content_stat_comments",
        blank=True,
        null=True,
    )
    id = models.IntegerField(primary_key=True)
    count = models.BigIntegerField()
