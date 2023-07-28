from django.contrib import admin

from .models import Media, SocialMedia


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("social_media",)
    fields = (
        "title",
        "social_media",
    )
    list_display = (
        "title",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title", "link")
    list_display = (
        "title",
        "link",
        "created_at",
    )
    list_filter = ("title", "created_at")
