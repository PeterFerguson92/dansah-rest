import csv
from django.http import HttpResponse
from django.contrib import admin

from .models import (
    Course,
    Video,
    Assesment,
    Reading,
    Assignment,
    Category,
    Material,
    Student,
    LeadershipInstitute,
)


class ExportCsvMixin:

    def export_student_as_csv(self, request, queryset):
        qs = Course.objects.prefetch_related("students")
        print(qs)

        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="export_file.csv"'

        writer = csv.writer(response)

        for rule in qs:
            writer.writerow([rule.name])
            for c in rule.students.all():
                writer.writerow(["-", c.name, c.surname, c.email])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "description",
        "document",
    )
    list_display = ("title", "description", "created_at")
    list_filter = ("title", "created_at")


@admin.register(Assesment)
class AssesmentAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "document",
        "description",
    )
    list_display = ("title", "description", "created_at")
    list_filter = ("title", "created_at")


@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "document",
        "description",
    )
    list_display = ("title", "description", "created_at")
    list_filter = ("title", "created_at")


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "description",
        "link",
    )
    list_display = ("title", "description", "created_at")
    list_filter = ("title", "created_at")


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    filter_horizontal = ("videos", "readings", "assesments", "assignments")
    fields = (
        "name",
        "videos",
        "readings",
        "assesments",
        "assignments",
    )
    list_display = (
        "name",
        "created_at",
    )
    list_filter = (
        "name",
        "created_at",
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "surname",
        "email",
    )
    list_display = ("name", "surname", "email", "created_at")
    list_filter = ("name", "surname", "email", "created_at")


@admin.register(Course)
class CourseAdmin(ExportCsvMixin, admin.ModelAdmin):
    search_fields = ("name__startswith",)
    filter_horizontal = ("students",)
    fields = (
        "name",
        "level",
        "short_description",
        "full_description",
        "cover_image_path",
        "materials",
        "students",
    )
    list_display = ("name", "level", "created_at")
    list_filter = ("name", "created_at")
    actions = ["export_student_as_csv"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "description",
        "cover_image_path",
    )
    list_display = ("name", "created_at")
    list_filter = ("name", "created_at")


@admin.register(LeadershipInstitute)
class LeadershipInstituteAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("categories",)
    fields = (
        "title",
        "short_description",
        "full_description",
        "cover_image_path",
        "categories",
    )
    list_display = (
        "title",
        "short_description",
        "cover_image_path",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )
