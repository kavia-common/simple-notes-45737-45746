from rest_framework import serializers
from .models import Note

# PUBLIC_INTERFACE
class NoteSerializer(serializers.ModelSerializer):
    """Serializer for the Note model handling validation and representation."""

    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_title(self, value: str) -> str:
        """Ensure the title is not empty or whitespace."""
        if not value or not value.strip():
            raise serializers.ValidationError("Title is required.")
        return value
