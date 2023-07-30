from django.contrib import admin

from .models import Event, HomeEvent


@admin.register(HomeEvent)
class HomeEventsAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("events",)
    fields = (
        "title",
        "events",
    )
    list_display = ("title", "created_at")
    list_filter = ("title", "created_at")


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "description_1",
        "description_2",
        "date",
        "time",
        "location",
        "home_display",
        "cover_image_path",
    )
    list_display = ("title", "date", "time", "location", "created_at")
    list_filter = ("title", "created_at")
