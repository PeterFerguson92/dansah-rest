import uuid
from django.db import models


class Donation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description", max_length=1024)
    momo_number = models.CharField("MoMo Number", max_length=255, blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("id",)
        verbose_name = "Donation"
        verbose_name_plural = "Donation Page"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.id, self.created_at)

    def __str__(self):
        return f"{self.id}"
