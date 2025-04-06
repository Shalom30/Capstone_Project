# Movie Review API

## Project Description
The **Movie Review API** is a Django-based web application built with Django REST Framework (DRF) that allows users to create, read, update, and delete (CRUD) movie reviews. It includes user management features, enabling authenticated users to submit and manage their own reviews while ensuring secure access through token-based authentication. The project combines a RESTful API for programmatic access with simple template-based views for a basic web interface.

## Problem Solved
This project addresses the need for a platform where movie enthusiasts can:
- Share and manage their personal movie reviews securely.
- Access a centralized database of reviews with filtering and search capabilities.
- Interact with the system via both a web interface and an API, catering to end-users and developers alike.

It solves the problem of disorganized or inaccessible movie opinions by providing a structured, user-specific, and API-driven solution.

## Overview of the Work
The application is built using:
- **Django**: For the core framework, models, and template views.
- **Django REST Framework (DRF)**: For creating RESTful APIs with serialization, authentication, and permissions.
- **Token Authentication**: To secure API endpoints, ensuring only authenticated users can perform actions like creating or modifying reviews.
- **SQLite**: As the default database (configurable to others like PostgreSQL).

Key features include:
- **User Management**: CRUD operations for users with unique usernames, emails, and passwords.
- **Review Management**: CRUD operations for reviews, restricted to the review’s owner for updates and deletions.
- **Filtering and Search**: API endpoints support filtering by movie title/rating and searching by title/content.
- **Web Interface**: Basic HTML templates for creating, updating, and deleting reviews (requires login).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd movie-review-project
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   (Ensure `requirements.txt` includes `django`, `djangorestframework`, `django-filter`.)
3. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```
5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```
   Access at `http://127.0.0.1:8000/`.

## API Endpoints
The API is accessible at `http://127.0.0.1:8000/api/`. All endpoints requiring authentication need an `Authorization: Token <your-token>` header.

### Authentication
- **Obtain Token**:
  - **Method**: POST
  - **URL**: `/api/api-token-auth/`
  - **Body**: `{"username": "john", "password": "pass123"}`
  - **Response**: `{"token": "<your-token>"}`
  - **Purpose**: Authenticates a user and returns a token for API access.

### User Management APIs
- **List Users**:
  - **Method**: GET
  - **URL**: `/api/users/`
  - **Response**: List of users (e.g., `[{"id": 1, "username": "john", "email": "john@example.com"}, ...]`)
  - **Purpose**: Retrieves all users (authenticated users only).
- **Retrieve User**:
  - **Method**: GET
  - **URL**: `/api/users/<id>/`
  - **Response**: Single user details
  - **Purpose**: Fetches a specific user’s info.
- **Create User**:
  - **Method**: POST
  - **URL**: `/api/users/`
  - **Body**: `{"username": "jane", "email": "jane@example.com", "password": "pass123"}`
  - **Response**: Created user details
  - **Purpose**: Registers a new user.
- **Update User**:
  - **Method**: PUT
  - **URL**: `/api/users/<id>/`
  - **Body**: `{"username": "john_updated", "email": "john.updated@example.com", "password": "newpass"}`
  - **Response**: Updated user details
  - **Purpose**: Modifies a user’s profile (owner or admin only).
- **Delete User**:
  - **Method**: DELETE
  - **URL**: `/api/users/<id>/`
  - **Response**: `204 No Content`
  - **Purpose**: Deletes a user (owner or admin only).

### Review Management APIs
- **List Reviews**:
  - **Method**: GET
  - **URL**: `/api/reviews/`
  - **Query Params**: `?movie_title=Inception`, `?rating=5`, `?search=movie`, `?ordering=-created_date`
  - **Response**: List of reviews
  - **Purpose**: Retrieves all reviews with filtering/search/ordering options (publicly accessible).
- **Retrieve Review**:
  - **Method**: GET
  - **URL**: `/api/reviews/<id>/`
  - **Response**: Single review details
  - **Purpose**: Fetches a specific review.
- **Create Review**:
  - **Method**: POST
  - **URL**: `/api/reviews/`
  - **Body**: `{"movie_title": "Inception", "review_content": "Great!", "rating": 5}`
  - **Response**: Created review with user info
  - **Purpose**: Adds a new review (authenticated users only).
- **Update Review**:
  - **Method**: PUT
  - **URL**: `/api/reviews/<id>/`
  - **Body**: `{"movie_title": "Inception", "review_content": "Updated", "rating": 4}`
  - **Response**: Updated review
  - **Purpose**: Modifies a review (owner only).
- **Delete Review**:
  - **Method**: DELETE
  - **URL**: `/api/reviews/<id>/`
  - **Response**: `204 No Content`
  - **Purpose**: Deletes a review (owner only).

## How the APIs Work
- **Authentication**: Use the token from `/api/api-token-auth/` in the `Authorization` header (e.g., `Authorization: Token 9944b091...`) for protected endpoints.
- **Permissions**:
  - Public: GET requests (list/retrieve) are open to all.
  - Authenticated: POST (create) requires a token.
  - Owner/Admin: PUT/DELETE (update/delete) restricted to the resource owner or admins.
- **Filtering/Search**: Review list supports query parameters for dynamic results (e.g., `/api/reviews/?search=Inception`).
- **Error Handling**: Returns `401` (unauthorized), `403` (forbidden), or `404` (not found) as needed.

## Usage
- **Web Interface**: Access `http://127.0.0.1:8000/` to view reviews, or log in to create/update/delete via templates.
- **API Testing**: Use Postman or curl with the endpoints above. Start by getting a token, then test CRUD operations.

## Future Improvements
- Add movie model for structured movie data.
- Implement user profiles with additional fields.
- Support JWT authentication for scalability.

---

### Notes
- Save this as `README.md` in your project root.
- Replace `<repository-url>` with your actual repo URL if hosted (e.g., GitHub).
- If you’re missing `requirements.txt`, create one with:
  ```
  django
  djangorestframework
  django-filter
  ```

Let me know if you’d like to tweak this further or add specific details (e.g., contributors, license)!