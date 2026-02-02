from django.contrib import admin
from .models import Bio, BioItem
from django.utils.html import format_html


class BioItemInline(admin.StackedInline):
    model = BioItem
    extra = 1
    fields = ('item_type', 'text', 'image', 'image_description', 'youtube_url', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="200" style="border-radius:12px;"/>',
                obj.image.url
            )
        return "Нет фото"

    image_preview.short_description = "Превью фото"


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    inlines = [BioItemInline]
    readonly_fields = ('main_photo_preview',)

    def main_photo_preview(self, obj):
        if obj.main_photo:
            return format_html(
                '<img src="{}" width="300" style="border-radius:15px;"/>',
                obj.main_photo.url
            )
        return "Нет фото"

    main_photo_preview.short_description = "Превью главного фото"
