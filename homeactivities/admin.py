from django.contrib import admin

from .models import HomeActivity


@admin.register(HomeActivity)
class HomeActivitiesAdmin(admin.ModelAdmin):
    fields = ("leadership_institute", "prayer_city", "power_living", "prayer_connect")

    list_display = (
        "id",
        "created_at",
    )
    list_filter = ("leadership_institute",)
