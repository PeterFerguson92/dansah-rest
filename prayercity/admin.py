from django.contrib import admin
from .models import PrayerCity

# Register your models here.
@admin.register(PrayerCity)
class MonthlyPowerLivingAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "short_description",
              "full_description",
              "cover_image_path")
    list_display = ("title",
                    "short_description",
                    "created_at",
                    )
    list_filter = ("title",
                   "created_at",
                   )
