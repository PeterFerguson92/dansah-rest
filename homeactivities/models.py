import uuid
from django.db import models

from .homeactivitiesuploadfiles import home_activities_upload_image_path
from leadershipinstitute.models import LeadershipInstitute
from prayercity.models import PrayerCity
from powerliving.models import PowerLiving
from prayerconnect.models import PrayerConnect


class HomeActivity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    leadership_institute = models.OneToOneField(
        LeadershipInstitute, on_delete=models.SET_NULL, null=True
    )
    prayer_city = models.OneToOneField(PrayerCity, on_delete=models.SET_NULL, null=True)
    power_living = models.OneToOneField(
        PowerLiving, on_delete=models.SET_NULL, null=True
    )
    prayer_connect = models.OneToOneField(
        PrayerConnect, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("id",)
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.id, self.created_at)

    def __str__(self):
        return f"{self.id}"
