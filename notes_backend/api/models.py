from django.db import models


class Note(models.Model):
    """
    Represents a simple note with a title and content.

    Fields:
    - title: Short text title for the note (required).
    - content: Full text content for the note (optional).
    - created_at: Timestamp when the note was created (auto-set).
    - updated_at: Timestamp when the note was last updated (auto-updated).
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}: {self.title}"
