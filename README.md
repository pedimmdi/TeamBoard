# TeamBoard

TeamBoard is a multi-tenant SaaS project management platform designed for task tracking, team collaboration, role-based access control, and secure REST APIs.

## Features

### Accounts and Authentication
- Custom user model with email-based identification
- User profile management
- JWT-based authentication
- Access and refresh token lifecycle management
- Session tracking and session revocation
- Password change and password reset endpoints
- Email verification endpoints
- Request throttling for sensitive authentication operations
- Django Admin integration for account and session management

### API Documentation
- OpenAPI schema
- Swagger UI
- ReDoc

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- Docker and Docker Compose
- drf-spectacular

## Prerequisites

Install the following tools before running the project:

- Git
- Docker Desktop with Docker Compose
- A code editor

Docker Compose runs the backend and PostgreSQL database in containers.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/pedimmdi/teamboard.git
cd teamboard
```

### 2. Configure Environment Variables

Create a local environment file from the example:

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace the placeholder values, especially `SECRET_KEY` and `POSTGRES_PASSWORD`, with your own development values.

Never commit `.env` or expose real credentials in source control.

### 3. Build and Start the Services

```bash
docker compose up -d --build
```

Check the service status:

```bash
docker compose ps
```

### 4. Apply Database Migrations

```bash
docker compose exec backend python manage.py migrate
```

### 5. Create an Admin User

```bash
docker compose exec backend python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 6. Open the Application

- Django Admin: http://localhost:8000/admin/
- Swagger UI: http://localhost:8000/api/docs/
- OpenAPI Schema: http://localhost:8000/api/schema/
- ReDoc: http://localhost:8000/api/redoc/

The API documentation pages allow you to explore available endpoints and inspect their request and response schemas.

## API Overview

The API is versioned under `/api/v1/`.

### Accounts

The accounts API includes endpoints for:

| Functionality | Endpoint |
|---|---|
| Registration | `/api/v1/accounts/register/` |
| Login | `/api/v1/accounts/login/` |
| Token refresh | `/api/v1/accounts/refresh/` |
| Logout | `/api/v1/accounts/logout/` |
| Current user | `/api/v1/accounts/me/` |
| List sessions | `/api/v1/accounts/sessions/` |
| Revoke other sessions | `/api/v1/accounts/sessions/revoke-others/` |
| Revoke a specific session | `/api/v1/accounts/sessions/<session_id>/` |
| Change password | `/api/v1/accounts/password/change/` |
| Request password reset | `/api/v1/accounts/password/reset/` |
| Confirm password reset | `/api/v1/accounts/password/reset/confirm/` |
| Verify email | `/api/v1/accounts/email/verify/` |
| Resend verification email | `/api/v1/accounts/email/resend/` |

Use Swagger UI to inspect the supported HTTP methods, request payloads, authentication requirements, and response formats for each endpoint.

## Authentication

Protected endpoints use JWT bearer authentication.

Include the access token in the request header:

```http
Authorization: Bearer <access_token>
```

Access tokens are short-lived. Use the refresh endpoint to obtain a new access token according to the API's token lifecycle rules.

## Email Configuration

By default, the project uses Django's console email backend for development. Emails are written to the backend container's logs rather than delivered to a real inbox.

Email-related endpoints can be tested in this development setup without configuring an external email provider.

## Running Tests

Run the accounts test suite:

```bash
docker compose exec backend python manage.py test accounts
```

Run the full Django test suite:

```bash
docker compose exec backend python manage.py test
```

## Useful Docker Commands

Start services:

```bash
docker compose up -d
```

View service status:

```bash
docker compose ps
```

View backend logs:

```bash
docker compose logs -f backend
```

Stop services:

```bash
docker compose down
```

Stop services and remove the database volume:

```bash
docker compose down -v
```

**Warning:** The last command deletes the PostgreSQL volume and its stored database data. Do not run it unless you intentionally want to remove that data.

## Project Structure

```text
teamboard/
├── config/
│   ├── accounts/
│   ├── config/
│   └── manage.py
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

The `accounts` app contains user, profile, authentication, and session-related functionality. The inner `config` package contains Django settings and URL configuration.

## Development Notes

- The default email backend is intended for local development.
- Django's development server is used by the current Docker configuration.
- Development settings are not a production deployment configuration.
- Before deploying, configure production settings, secure environment variables, allowed hosts, HTTPS, email delivery, static files, logging, and an appropriate production application server.
- Never commit secrets, passwords, access tokens, or real environment files.

## License

No license has been specified yet.
