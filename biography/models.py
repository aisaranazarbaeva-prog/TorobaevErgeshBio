from django.db import models
from cloudinary.models import CloudinaryField

class Bio(models.Model):
    full_name = models.CharField(max_length=255)
    main_photo = CloudinaryField('image', blank=True, null=True)  # теперь можно загружать фото
    quote = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class BioItem(models.Model):
    ITEM_TYPES = (
        ('text', 'Text'),
        ('photo', 'Photo'),
    )

    bio = models.ForeignKey(Bio, related_name='items', on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES)
    text = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)  # поле для загрузки фото

    def __str__(self):
        return f"{self.bio.full_name} - {self.item_type}"
