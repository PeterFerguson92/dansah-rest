import uuid
from django.db import models

from .homeministriesmaterialuploadfiles import (
    home_ministries_material_upload_image_path,
)


class MinistriesMaterial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    description = models.CharField("Description", max_length=1024)
    cover_image_path = models.ImageField(
        "Cover image",
        upload_to=home_ministries_material_upload_image_path,
        null=True,
        blank=True,
    )
    redirect_link = models.CharField("Link", max_length=255)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "description", "created_at")

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.description, self.created_at)

    def __str__(self):
        return f"{self.title}"


class HomeMinistriesMaterial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default="Ministries Material")
    materials = models.ManyToManyField(MinistriesMaterial)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Home Ministry Material"
        verbose_name_plural = "Home Ministries Materials"

    def __unicode__(self):
        return "%s: /n %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"
