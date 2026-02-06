from django.contrib import admin
from .models import Bio, BioItem, GalleryPhoto, SocialLink

class BioItemInline(admin.TabularInline):
    model = BioItem
    extra = 1
    fields = ('item_type', 'text', 'image', 'image_description', 'youtube_url')
    show_change_link = True

class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto
    extra = 1
    fields = ('image', 'description')

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1
    fields = ('name', 'icon', 'url')

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'quote')
    search_fields = ('full_name',)
    inlines = [BioItemInline, GalleryPhotoInline, SocialLinkInline]
    list_per_page = 20

@admin.register(BioItem)
class BioItemAdmin(admin.ModelAdmin):
    list_display = ('bio', 'item_type', 'text', 'youtube_url')
    list_filter = ('item_type',)
    search_fields = ('bio__full_name', 'text', 'image_description', 'youtube_url')
    list_per_page = 20

@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('bio', 'description')

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('bio', 'name', 'url')
