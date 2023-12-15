from django.contrib import admin

from .models import Home


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    fields = (
        "top_logo_image_path",
        "url",
        "footer_address",
        "footer_phone",
        "footer_email",
        "footer_logo_image_path",
    )
    list_display = ("id",)
    list_filter = ("id", "created_at")
