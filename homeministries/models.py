import uuid
from django.db import models

from .homeministriesuploadfiles import home_ministries_upload_image_path

# Create your models here.
class Ministries(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    slogan = models.CharField("Slogan", max_length=255)
    description = models.TextField("Description", max_length=1024)
    cover_image_path = models.ImageField(
        "Cover image",
        upload_to=home_ministries_upload_image_path,
        null=True,
        blank=True,
    )
    gallery_image_path_1 = models.ImageField(
        "Gallery image 1", upload_to=home_ministries_upload_image_path, null=True, blank=True
    )
    gallery_image_path_2 = models.ImageField(
        "Gallery image 2", upload_to=home_ministries_upload_image_path, null=True, blank=True
    )
    gallery_image_path_3 = models.ImageField(
        "Gallery image 3", upload_to=home_ministries_upload_image_path, null=True, blank=True
    )
    gallery_image_path_4 = models.ImageField(
        "Gallery image 4", upload_to=home_ministries_upload_image_path, null=True, blank=True
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name = "Ministry"
        verbose_name_plural = "Ministries"
        
    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name}"


class HomeMinistries(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default="Ministries")
    ministries = models.ManyToManyField(Ministries)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Home Ministry"
        verbose_name_plural = "Home Ministry"

    def __unicode__(self):
        return "%s: /n %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"