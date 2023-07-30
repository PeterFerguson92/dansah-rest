from django.contrib import admin

from .models import QuoteOfTheDay


@admin.register(QuoteOfTheDay)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "text",
        "source",
        "quote_date",
    )
    list_display = ("title", "source", "created_at")
    list_filter = (
        "title",
        "source",
        "created_at",
    )
