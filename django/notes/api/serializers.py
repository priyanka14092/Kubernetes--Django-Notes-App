from rest_framework import serializers
from .models import Note

# Create your serializer here.
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'text')