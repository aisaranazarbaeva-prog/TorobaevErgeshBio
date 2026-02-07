from django.contrib import admin
from .models import Bio, BioItem

# Inline для BioItem, чтобы редактировать элементы прямо в Bio
class BioItemInline(admin.TabularInline):  # Можно использовать StackedInline для вертикального вида
    model = BioItem
    extra = 1  # сколько пустых форм добавлять
    fields = ('item_type', 'text', 'image', 'image_description', 'youtube_url')
    readonly_fields = ()
    show_change_link = True

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'quote')  # поля для отображения в списке
    search_fields = ('full_name',)  # поиск по имени
    inlines = [BioItemInline]  # добавляем BioItem прямо в Bio
    list_per_page = 20  # сколько элементов на странице
    # fields = ('full_name', 'main_photo', 'quote')  # если нужны кастомные поля в форме

@admin.register(BioItem)
class BioItemAdmin(admin.ModelAdmin):
    list_display = ('bio', 'item_type', 'text', 'youtube_url')
    list_filter = ('item_type',)
    search_fields = ('bio__full_name', 'text', 'image_description', 'youtube_url')
    list_per_page = 20
