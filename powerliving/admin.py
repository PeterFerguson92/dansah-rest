from django.contrib import admin

from .models import Article, PowerLiving, MonthlyPowerLiving


@admin.register(PowerLiving)
class PowerLivingAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("monthly_power_living",)
    fields = (
        "title",
        "short_description",
        "full_description",
        "cover_image_path",
        "monthly_power_living",
    )
    list_display = (
        "title",
        "short_description",
        "created_at",
    )
    list_filter = ("title", "created_at")


@admin.register(MonthlyPowerLiving)
class MonthlyPowerLivingAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "description",
        "cover_image_path",
        "document",
        "articles",
    )
    filter_horizontal = ("articles",)
    list_display = (
        "title",
        "description",
        "cover_image_path",
        "document",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "quotation",
        "content",
    )
    list_display = (
        "title",
        "quotation",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )
