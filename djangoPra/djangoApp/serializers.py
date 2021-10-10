from .models import Note
from rest_framework import serializers
from django.forms import fields, forms


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = {
            'title', 'description'
        }
