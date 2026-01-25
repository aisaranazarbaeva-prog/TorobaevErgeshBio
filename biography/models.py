from django.db import models

class Bio(models.Model):
    full_name = models.CharField(max_length=255)
    main_photo = models.ImageField(upload_to='bio/main_photos/')
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
    image = models.ImageField(upload_to='bio/items/', blank=True, null=True)

    def __str__(self):
        return f"{self.bio.full_name} - {self.item_type}"
