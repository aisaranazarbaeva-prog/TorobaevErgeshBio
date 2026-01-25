from rest_framework import serializers
from .models import Bio, BioItem

class BioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioItem
        fields = ['id', 'item_type', 'text', 'image']

class BioSerializer(serializers.ModelSerializer):
    items = BioItemSerializer(many=True, read_only=True)  # вложенные элементы BioItem

    class Meta:
        model = Bio
        fields = ['id', 'full_name', 'main_photo', 'quote', 'items']
