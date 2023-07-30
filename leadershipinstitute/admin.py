from django.contrib import admin

from .models import (
    Course,
    Video,
    Assesment,
    Reading,
    Assignment,
    Category,
    Material,
    LeadershipInstitute,
)


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


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "level",
        "short_description",
        "full_description",
        "cover_image_path",
        "materials",
    )
    list_display = ("name", "level", "created_at")
    list_filter = ("name", "created_at")


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
