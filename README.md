
# Healthcare Backend API

A RESTful healthcare backend for managing patient records, doctor information, and patient-doctor assignments. Built with Django REST Framework, PostgreSQL, and JWT authentication.

## Tech Stack

- Python 3.11+
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)
- Environment variables (`.env`)

## Project Structure

```text
healthcare_api/
├── accounts/       # User registration and authentication
├── core/           # Project settings, routing, and exceptions
├── doctors/        # Doctor management
├── mappings/       # Patient-doctor assignments
├── patients/       # Patient management
├── .env.example    # Environment variable template
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
```

## Setup Instructions

### 1. Open the project directory

```powershell
cd healthcare_api
```

Replace `healthcare_api` with your actual folder name if necessary.

### 2. Create and activate a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file from `.env.example`:

```powershell
Copy-Item .env.example .env
```

Update `.env` with your local configuration:

```dotenv
SECRET_KEY=replace-with-a-local-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your-local-postgres-password
DB_HOST=localhost
DB_PORT=5432
```

Use your own PostgreSQL credentials. Never commit passwords or secret keys to version control.

### 5. Create the PostgreSQL database

Ensure PostgreSQL is installed and running. Connect using a PostgreSQL client and execute:

```sql
CREATE DATABASE healthcare_db;
```

Ensure the configured database user has permission to access the database.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

The server normally runs at:

`http://127.0.0.1:8000/`

If implemented, the health-check endpoint can be accessed at:

`http://127.0.0.1:8000/api/health/`

## API Endpoints

The following endpoints describe the intended API. Confirm their availability and permissions against the implementation.

### Authentication

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/api/auth/register/` | Register a user | Not required |
| POST | `/api/auth/login/` | Log in and obtain JWT tokens | Not required |

### Patients

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/patients/` | Create a patient |
| GET | `/api/patients/` | List the authenticated user's patients |
| GET | `/api/patients/<id>/` | Retrieve a patient |
| PUT | `/api/patients/<id>/` | Update a patient |
| DELETE | `/api/patients/<id>/` | Delete a patient |

### Doctors

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/doctors/` | Create a doctor |
| GET | `/api/doctors/` | List doctors |
| GET | `/api/doctors/<id>/` | Retrieve a doctor |
| PUT | `/api/doctors/<id>/` | Update a doctor |
| DELETE | `/api/doctors/<id>/` | Delete a doctor |

### Patient-Doctor Mappings

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/mappings/` | Assign a doctor to a patient |
| GET | `/api/mappings/` | List patient-doctor mappings |
| GET | `/api/mappings/patient/<patient_id>/` | Retrieve mappings for a patient |
| DELETE | `/api/mappings/<id>/` | Remove a mapping |

Protected endpoints require a valid JWT access token unless the implementation specifies otherwise.

## Authentication

Include the access token in the HTTP header when accessing protected endpoints:

```http
Authorization: Bearer <access_token>
```

Obtain the token through the login endpoint.

## Testing

If the repository includes a Postman collection:

1. Import the collection into Postman.
2. Set the base URL to `http://127.0.0.1:8000`.
3. Register a user and log in.
4. Use the returned access token for protected requests.

## Security Notes

- Store secret keys and database credentials in environment variables.
- Keep `.env` out of version control.
- Set `DEBUG=False` in production.
- Apply appropriate authentication and authorization checks to protected resources.

## Attribution

This project is based on an existing codebase. Refer to the original repository and its license where applicable, and document the changes made for this assignment.
