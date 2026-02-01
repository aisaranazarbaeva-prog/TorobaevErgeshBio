from django.contrib import admin
from .models import Bio, BioItem
from django.utils.html import format_html


class BioItemInline(admin.StackedInline):
    model = BioItem
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" style="border-radius:10px;"/>', obj.image.url)
        return ""

    image_preview.short_description = "Превью фото"

    # Отображаем поля в зависимости от типа BioItem
    def get_fields(self, request, obj=None):
        fields = ['item_type', 'text', 'image', 'image_description', 'youtube_url', 'image_preview']
        if obj:
            if obj.item_type == 'text':
                # Для текста убираем поля изображения и YouTube
                fields.remove('image')
                fields.remove('image_description')
                fields.remove('youtube_url')
            elif obj.item_type == 'photo':
                # Для фото убираем текст и youtube
                fields.remove('text')
                fields.remove('youtube_url')
            elif obj.item_type == 'video':
                # Для видео убираем текст и поля изображения
                fields.remove('text')
                fields.remove('image')
                fields.remove('image_description')
        return fields


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    inlines = [BioItemInline]

    readonly_fields = ('main_photo_preview',)

    def main_photo_preview(self, obj):
        if obj.main_photo:
            return format_html('<img src="{}" width="300" style="border-radius:15px;"/>', obj.main_photo.url)
        return ""

    main_photo_preview.short_description = "Превью главного фото"
