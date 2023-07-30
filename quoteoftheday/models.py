import uuid

from django.db import models


class QuoteOfTheDay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default="Quote Of The Day")
    text = models.TextField("text", max_length=1024)
    source = models.CharField("Source", max_length=255)
    quote_date = models.DateField("Date")
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "text", "created_at")
        verbose_name = "Quote of the day"
        verbose_name_plural = "Quotes of the day"

    def __unicode__(self):
        return "%s: /n %s  %s %s" % (self.title, self.text, self.created_at)

    def __str__(self):
        return f"{self.title} \n {self.text}"
