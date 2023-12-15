from django.contrib import admin

# Register your models here.
from .models import Ministries, HomeMinistries


@admin.register(HomeMinistries)
class HomeMinistriesAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("ministries",)
    fields = (
        "title",
        "ministries",
    )
    list_display = (
        "title",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )


@admin.register(Ministries)
class MinistriesAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "slogan",
        "description",
        "cover_image_path",
        "gallery_image_path_1",
        "gallery_image_path_2",
        "gallery_image_path_3",
        "gallery_image_path_4",
    )
    list_display = (
        "name",
        "slogan",
        "created_at",
    )
    list_filter = ("name", "created_at")
