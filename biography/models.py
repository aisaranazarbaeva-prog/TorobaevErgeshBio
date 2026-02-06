from django.db import models
from cloudinary.models import CloudinaryField


class Bio(models.Model):
    full_name = models.CharField(max_length=255)
    main_photo = CloudinaryField('image', blank=True, null=True)
    quote = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class BioItem(models.Model):
    ITEM_TYPES = (
        ('text', 'Text'),
        ('photo', 'Photo'),
        ('video', 'Video'),
    )

    bio = models.ForeignKey(Bio, related_name='items', on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES)

    text = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    image_description = models.TextField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.bio.full_name} - {self.item_type}"


# ===== ГАЛЕРЕЯ =====
class GalleryPhoto(models.Model):
    bio = models.ForeignKey(Bio, related_name="gallery_photos", on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.bio.full_name} - Gallery photo"


# ===== СОЦСЕТИ / ЛОГОТИПЫ =====
class SocialLink(models.Model):
    bio = models.ForeignKey(Bio, related_name="social_links", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    icon = CloudinaryField('image', blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return f"{self.bio.full_name} - {self.name}"
