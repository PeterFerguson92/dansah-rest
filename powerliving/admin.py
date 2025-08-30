from django.contrib import admin
import calendar
from .models import Article, PowerLiving, MonthlyPowerLiving
from django.db.models.functions import ExtractMonth


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


class MonthListFilter(admin.SimpleListFilter):
    title = "Month"
    parameter_name = "month"

    def lookups(self, request, model_admin):
        # Build lookups from the current queryset so it's always accurate
        months = (
            model_admin.get_queryset(request)
            .exclude(date__isnull=True)
            .annotate(m=ExtractMonth("date"))
            .values_list("m", flat=True)
            .distinct()
            .order_by("m")
        )
        return [(m, calendar.month_name[m]) for m in months if m]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(date__month=int(self.value()))
        return queryset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "cover_image_path",
        "date",
        "title",
        "quotation",
        "content",
        "confession",
        "references",
        "prayer_point",
    )
    list_display = ("title", "date", "month_name", "created_at")
    list_filter = (MonthListFilter, "created_at")
    search_fields = ("title", "quotation", "references")
    date_hierarchy = "date"  # optional: adds year → month → day navigation

    def month_name(self, obj):
        return obj.month_name

    month_name.short_description = "Month"
