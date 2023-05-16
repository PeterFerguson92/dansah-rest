import uuid
from datetime import date

from django.db import models


class Devotional(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    devotion_title = models.CharField("Devotion title", max_length=255)
    devotion_message = models.TextField("Devotion message", max_length=2048)
    devotion_date = models.DateField("Devotion date", default=date.today())
    devotion_created_at = models.DateTimeField(auto_now_add=True)
    devotion_updated_at = models.DateTimeField()
    devotion_monthly = models.BooleanField("Monthly devotion", default=False)

    class Meta:
        ordering = ("devotion_title", "devotion_date")

    def __unicode__(self):
        return u'%s: /n %s' % (self.devotion_title, self.devotion_message)
