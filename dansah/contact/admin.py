from django.contrib import admin

from .models import Location, Contact


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "name",
        "address",
        "phone_number",
    )
    list_display = (
        "name",
        "address",
        "phone_number",
        "created_at",
    )
    list_filter = ("name", "address", "phone_number", "created_at")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("locations",)
    fields = (
        "name",
        "locations",
    )
    list_display = (
        "name",
        "created_at",
    )
    list_filter = (
        "name",
        "locations",
        "created_at",
    )
