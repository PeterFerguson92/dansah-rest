import uuid
from django.db import models

from .homeslidersuploadfiles import home_sliders_upload_image_path


class HomeSlider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    image = models.ImageField(
        "Image", upload_to=home_sliders_upload_image_path, null=True, blank=True
    )
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Home Slider"
        verbose_name_plural = "Home Sliders"

    def __unicode__(self):
        return "%s: /n %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"


class Intro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description", max_length=1024)
    cover_image_path = models.ImageField(
        "Cover Image", upload_to=home_sliders_upload_image_path, null=True, blank=True
    )
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("id", "description", "created_at")
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def __unicode__(self):
        return "%s: /n %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"
