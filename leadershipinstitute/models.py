import uuid
from django.db import models
from .leadershipInstitueuploadfiles import (
    leadership_institute_upload_image_path,
    leadership_institute_course_upload_image_path,
    leadership_institute_categories_upload_image_path,
)
from django.core.validators import FileExtensionValidator


LEVELS = (
    ("BASIC", "Basic"),
    ("INTERMEDIATE", "Intermediate"),
    ("ADVANCED", "Advanced"),
)


class Assesment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    description = models.TextField(
        "Description", max_length=1024, default="", blank=True
    )
    document = models.FileField(
        "Upload Assesment Document",
        upload_to="leadershipinstitute/materials/assesments",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["doc", "docx"])],
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name_plural = "Assesments"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"


class Assignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    description = models.TextField(
        "Description", max_length=1024, default="", blank=True
    )
    document = models.FileField(
        "Upload Assignment Document",
        upload_to="leadershipinstitute/materials/assignments",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["doc", "docx"])],
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name_plural = "Assignments"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"


class Reading(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    description = models.TextField(
        "Description", max_length=1024, default="", blank=False
    )
    document = models.FileField(
        "Upload Pdf",
        upload_to="leadershipinstitute/materials/readings",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name_plural = "Reading Materials"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    description = models.TextField(
        "Description", max_length=1024, default="", blank=False
    )
    link = models.CharField("Link", max_length=255)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name_plural = "Video Materials"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"


class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    videos = models.ManyToManyField(Video)
    readings = models.ManyToManyField(Reading)
    assesments = models.ManyToManyField(Assesment)
    assignments = models.ManyToManyField(Assignment)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = (
            "name",
            "created_at",
        )
        verbose_name_plural = "Materials"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    level = models.ForeignKey("Category", on_delete=models.CASCADE, blank=False)
    short_description = models.CharField(
        "Short Description", max_length=255, default="", blank=False
    )
    full_description = models.TextField(
        "Full Description", max_length=1024, default="", blank=False
    )
    cover_image_path = models.ImageField(
        "Cover image",
        upload_to=leadership_institute_course_upload_image_path,
        null=True,
        blank=True,
    )
    materials = models.ForeignKey(
        "Material", on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name_plural = "Courses"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    cover_image_path = models.ImageField(
        "Cover image",
        upload_to=leadership_institute_categories_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name}"


class LeadershipInstitute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(
        "Alias", max_length=255, default="leadership-institute", editable=False
    )
    title = models.CharField("Title", max_length=255)
    short_description = models.CharField("Short Description", max_length=255, blank=False)
    full_description = models.TextField("Full Description", max_length=1024, blank=True)
    categories = models.ManyToManyField(Category)
    cover_image_path = models.ImageField(
        "Cover image",
        upload_to=leadership_institute_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name_plural = "Leadership Institute"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"
