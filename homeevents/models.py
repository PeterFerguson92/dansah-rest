import uuid
from django.db import models

from .homeeventsuploadfiles import home_events_upload_image_path


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    description_1 = models.TextField("Description 1", max_length=1024)
    description_2 = models.TextField("Description 2", max_length=1024, blank=True)
    date = models.CharField("Date details", max_length=255)
    time = models.CharField("Time details ", max_length=255)
    location = models.CharField("Location details ", max_length=255)
    cover_image_path = models.ImageField(
        "Cover image", upload_to=home_events_upload_image_path, null=True, blank=True
    )
    home_display = models.BooleanField("Show In home", default=False)

    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "home_display", "created_at")
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"


class HomeEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default="Home Events")
    events = models.ManyToManyField(to=Event)
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Home Event"
        verbose_name_plural = "Home Events"

    def __unicode__(self):
        return "%s: /n %s  %s " % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"
