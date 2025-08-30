import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

from .powerlivinguploadfiles import power_living_upload_image_path

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cover_image_path = models.ImageField(
        "Cover image", upload_to=power_living_upload_image_path, null=True, blank=True
    )
    date = models.DateField(blank=True, null=True)
    title = models.CharField("Title", max_length=255, editable=True)
    quotation = models.CharField(
        "Quotation", max_length=255, editable=True, blank=True, null=True
    )
    content = models.TextField("Content", blank=True)
    confession = models.TextField("Confession", blank=True)
    references = models.CharField(
        "Scripture References", max_length=255, editable=True, blank=True, null=True
    )
    prayer_point = models.TextField("Prayer Points", blank=True)
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __unicode__(self):
        return "%s: /n %s" % (self.title, self.created_at)

    def __str__(self):
        return "%s: - %s " % (self.title, self.date)
    
     # ---- Derived month helpers (auto-linked to `date`) ----
    @property
    def month(self):
        """Numeric month (1–12) derived from `date`, or None."""
        return self.date.month if self.date else None

    @property
    def month_name(self):
        """Month name (e.g., 'January') derived from `date`, or None."""
        return self.date.strftime("%B") if self.date else None


class MonthlyPowerLiving(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Monthly Power Living title", max_length=255)
    description = models.TextField("Description", max_length=1024, blank=True)
    cover_image_path = models.ImageField(
        "Cover image", upload_to=power_living_upload_image_path, null=True, blank=True
    )
    document = models.FileField(
        "File upload",
        upload_to="powerlivingfiles/pdfs/",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
    )
    articles = models.ManyToManyField(to=Article, blank=True)
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Monthly Power Living"
        verbose_name_plural = "Monthly Power Living"

    def __unicode__(self):
        return "%s: /n %s " % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"


class PowerLiving(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(
        "Alias", max_length=255, default="power-living", editable=False
    )
    title = models.CharField(
        "Title", max_length=255, default="Power Living", editable=True
    )
    short_description = models.CharField(
        "Short Description", max_length=255, blank=False
    )
    full_description = models.TextField("Full Description", max_length=1024, blank=True)
    cover_image_path = models.ImageField(
        "Cover Image", upload_to=power_living_upload_image_path, null=True, blank=True
    )
    monthly_power_living = models.ManyToManyField(to=MonthlyPowerLiving)
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Power Living"
        verbose_name_plural = "Power Living"

    def __unicode__(self):
        return "%s: /n %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"
