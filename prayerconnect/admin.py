from django.contrib import admin
from .models import PrayerConnect, PrayerConnectCenter, PrayerConnectDirector


@admin.register(PrayerConnectDirector)
class PrayerConnectDirectorsAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("name",)
    list_display = ("name", "created_at")
    list_filter = ("name", "created_at")


@admin.register(PrayerConnectCenter)
class PrayerConnectCentersAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("directors",)
    fields = (
        "region",
        "directors",
    )
    list_display = ("region", "created_at")
    list_filter = ("region", "created_at")


@admin.register(PrayerConnect)
class PrayerConnectAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("centers",)
    fields = (
        "title",
        "short_description",
        "full_description",
        "cover_image_path",
        "centers",
    )
    list_display = (
        "title",
        "short_description",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )
