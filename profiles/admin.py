from django.contrib import admin

from .models import Profile, Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    search_fields = ("type__startswith",)
    fields = ("type", "description")
    list_display = (
        "type",
        "description",
        "created_at",
    )
    list_filter = (
        "type",
        "description",
        "created_at",
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("roles",)
    fields = (
        "title",
        "text",
        "roles",
        "cover_image_path",
    )
    list_display = ("title", "text", "created_at")
    list_filter = ("title", "text", "created_at")
