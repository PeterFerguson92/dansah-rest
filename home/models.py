import uuid
from django.db import models

from .homeuploadfiles import home_upload_image_path


class Home(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    top_logo_image_path = models.ImageField(
        "Top logo image",
        upload_to=home_upload_image_path,
        null=True,
        blank=True,
    )
    live_event_name = models.CharField("Live Event Name", default='default', max_length=255)
    url = models.CharField("Video Id", default='default', max_length=255)
    footer_address = models.CharField("Footer Address", max_length=255)
    footer_phone = models.CharField("Footer Phone", max_length=255)
    footer_email = models.CharField("Footer email", max_length=255)
    footer_logo_image_path = models.ImageField(
        "Footer logo image",
        upload_to=home_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("id", "created_at")
        verbose_name_plural = "Homepage Details"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.id, self.created_at)

    def __str__(self):
        return f"{self.id}"
