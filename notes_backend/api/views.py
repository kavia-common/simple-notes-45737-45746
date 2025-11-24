from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from .models import Note
from .serializers import NoteSerializer


@api_view(["GET"])
def health(request):
    """
    Health check endpoint.

    Returns:
        200 OK with a simple message.
    """
    return Response({"message": "Server is up!"})


class NoteViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for notes.

    Routes:
    - GET /api/notes/            -> list notes
    - POST /api/notes/           -> create note
    - GET /api/notes/{id}/       -> retrieve note
    - PUT/PATCH /api/notes/{id}/ -> update note
    - DELETE /api/notes/{id}/    -> delete note
    """
    queryset = Note.objects.all().order_by("-updated_at")
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="notes_list",
        operation_summary="List notes",
        operation_description="Retrieve a list of notes ordered by most recently updated.",
        responses={200: NoteSerializer(many=True)},
        tags=["notes"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="notes_create",
        operation_summary="Create a note",
        operation_description="Create a new note with a required title and optional content.",
        request_body=NoteSerializer,
        responses={
            201: NoteSerializer,
            400: "Validation error when title is missing or invalid",
        },
        tags=["notes"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="notes_retrieve",
        operation_summary="Retrieve a note",
        operation_description="Retrieve a note by its ID.",
        responses={200: NoteSerializer, 404: "Note not found"},
        tags=["notes"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="notes_update",
        operation_summary="Update a note",
        operation_description="Fully update a note by its ID.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer, 400: "Validation error", 404: "Note not found"},
        tags=["notes"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="notes_partial_update",
        operation_summary="Partially update a note",
        operation_description="Partially update a note by its ID.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer, 400: "Validation error", 404: "Note not found"},
        tags=["notes"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="notes_delete",
        operation_summary="Delete a note",
        operation_description="Delete a note by its ID.",
        responses={204: "Deleted", 404: "Note not found"},
        tags=["notes"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
