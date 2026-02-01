from django.contrib import admin
from .models import Bio, BioItem
from django.utils.html import format_html

class BioItemInline(admin.StackedInline):
    model = BioItem
    extra = 1

    # Показываем все возможные поля, превью для фото, описание и youtube
    fields = ('item_type', 'text', 'image', 'image_description', 'image_preview', 'youtube_url')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" style="border-radius:10px;"/>', obj.image.url)
        return ""
    image_preview.short_description = "Превью фото"

    # Скрываем поля в зависимости от item_type (админка без JS, просто чтобы не было лишнего)
    def get_fields(self, request, obj=None):
        fields = ['item_type']
        if obj:
            if obj.item_type == 'text':
                fields.append('text')
            elif obj.item_type == 'photo':
                fields.extend(['image', 'image_description', 'image_preview'])
            elif obj.item_type == 'video':
                fields.append('youtube_url')
        else:
            # для нового объекта показываем все поля
            fields.extend(['text', 'image', 'image_description', 'image_preview', 'youtube_url'])
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
