import uuid
from core.models import BaseModel
from django.db import models


# Create your models here.
class AuthorInfo(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)
    user_name = models.TextField(max_length=512, null=False)
    name = models.TextField(max_length=512, null=False)
    abbreviation = models.TextField(max_length=32, null=False, default="")
    platform = models.TextField(max_length=512, null=False, default="")
    text = models.TextField(max_length=2048, null=False, default="")

    @property
    def unique_id(self):
        return self.pk

    @property
    def unique_uuid(self):
        return f"{self.abbreviation}_{self.user_name}"

    @property
    def orgin_unique_uuid(self):
        return f"{self.abbreviation}_{self.user_name}"

    @property
    def followers(self):
        return self.author_stat.author_stat_followers

    @property
    def avaters(self):
        return self.author_avater.all()


class AuthorAvater(BaseModel):
    url = models.URLField(max_length=4096, blank=True, null=True)
    author = models.ForeignKey(
        AuthorInfo,
        on_delete=models.CASCADE,
        related_name="author_avater",
        blank=True,
        null=True,
    )


class AuthorStat(BaseModel):
    author = models.OneToOneField(
        AuthorInfo,
        on_delete=models.CASCADE,
        related_name="author_stat",
        blank=True,
        null=True,
    )


class AuthorFollowersCount(models.Model):
    author_stat = models.OneToOneField(
        AuthorStat,
        on_delete=models.CASCADE,
        related_name="author_stat_followers",
        blank=True,
        null=True,
    )
    id = models.IntegerField(primary_key=True)
    count = models.BigIntegerField()
