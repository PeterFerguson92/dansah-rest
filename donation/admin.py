from django.contrib import admin

from .models import Donation


# Register your models here.
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    fields = ("title", "description", "momo_number")
    list_display = (
        "title",
        "created_at",
    )
    list_filter = ("title",)
