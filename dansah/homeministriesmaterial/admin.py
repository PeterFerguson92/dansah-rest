from django.contrib import admin

from .models import MinistriesMaterial, HomeMinistriesMaterial


@admin.register(HomeMinistriesMaterial)
class HomeMinistriesMaterialAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ('ministries_material',)
    fields = ("title",
              "sub_title",
              "text",
              "icon_image",
              "ministries_material",
              )
    list_display = ("title",
                    "sub_title",
                    "text",
                    "icon_image_path",
                    "created_at",
                    )
    list_filter = ("title",
                   "sub_title",
                   "created_at",
                   )


@admin.register(MinistriesMaterial)
class MinistriesMaterialAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "description",
              "image_path",
              "redirect_link"
              )
    list_display = ("title",
                    "description",
                    "image_path",
                    "redirect_link",
                    "created_at"
                    )
    list_filter = ("title",
                   "created_at"
                  )

