import uuid
from django.db import models
from .prayerconnectuploadfiles import prayer_connect_upload_image_path

class PrayerConnectDirector(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")

    def __unicode__(self):
        return u'%s: /n %s  %s' % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name}"
    
class PrayerConnectCenter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region = models.CharField("Region", max_length=255)
    directors = models.ManyToManyField(PrayerConnectDirector)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("region", "created_at")

    def __unicode__(self):
        return u'%s: /n %s  %s' % (self.region, self.created_at)

    def __str__(self):
        return f"{self.region}"
    
class PrayerConnect(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField("Name", max_length=255)
    title = models.CharField("Title", max_length=255)
    short_description = models.CharField("Short Description", max_length=255)
    full_description = models.TextField("Full Description", max_length=1024, blank=False)
    action_text = models.CharField("Action Text", max_length=255, blank=True)
    image_path = models.ImageField("Icon image", upload_to=prayer_connect_upload_image_path, null=True, blank=True)
    centers = models.ManyToManyField(PrayerConnectCenter)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")

    def __unicode__(self):
        return u'%s: /n %s  %s' % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"    