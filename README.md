# simple-notes-45737-45746

Simple Notes backend exposes a minimal RESTful API for creating, reading, updating, and deleting notes.

Run server (port is configured by environment in the preview; typical local usage shown):
- Apply migrations:
  - python notes_backend/manage.py migrate
- Start development server:
  - python notes_backend/manage.py runserver 0.0.0.0:3001

Migrations
- New changes include initial Note model migration: api/migrations/0001_initial.py
- Apply via: python notes_backend/manage.py migrate

API Base URL
- /api/

Health
- GET /api/health/
  - Response: {"message": "Server is up!"}

Notes Endpoints
- GET /api/notes/
- POST /api/notes/
  - Request JSON: {"title": "My note", "content": "Optional text"}
- GET /api/notes/{id}/
- PUT /api/notes/{id}/
  - Request JSON: {"title": "Updated title", "content": "Updated text"}
- PATCH /api/notes/{id}/
  - Request JSON: {"title": "Partial or content only"}
- DELETE /api/notes/{id}/

Validation and Errors
- title is required and must not be blank.
- On invalid input: HTTP 400 with error details.

Interactive Docs
- Swagger UI: /docs
- OpenAPI JSON: /swagger.json
- Redoc: /redoc