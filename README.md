# FastAPI TodoJob Application

This is a RESTful Todo application built using FastAPI. The project is organized using the MVC (Model-View-Controller) architecture. The application allows users to create, read, update, and delete tasks (todos) in a database, and it supports detailed task management, including descriptions, deadlines, and tracking of estimated and actual work hours.
Based on this project https://github.com/ktechhub/fastapi_todo

## Features

- **CRUD Operations:**
  - Create new tasks.
  - Read existing tasks (single or multiple).
  - Update task details.
  - Delete tasks.

- **Task Management:**
  - Track task names, descriptions, deadlines (due dates), estimated hours, actual hours, and completion status.
  - Automatically tracks task creation and update timestamps.

- **Database Integration:**
  - Uses SQLAlchemy for ORM.
  - Alembic for database migrations.

## Project Structure

```plaintext
.
├── alembic/                 # Alembic migration files
├── app/                     # Application code
│   ├── __init__.py
│   ├── api/                 # API routes (Controllers)
│   │   ├── __init__.py
│   │   └── v1/              # Versioned API endpoints
│   │       ├── __init__.py
│   │       ├── todos/       # Todo-related API endpoints
│   │       │   ├── create.py
│   │       │   ├── read.py
│   │       │   ├── update.py
│   │       │   └── delete.py
│   ├── core/                # Core settings and configurations
│   │   ├── __init__.py
│   │   └── config.py
│   ├── database/            # Database connection setup
│   │   ├── __init__.py
│   │   └── base_class.py    # Base class for SQLAlchemy models
│   ├── main.py              # Application entry point
│   ├── models/              # Database models (Models)
│   │   ├── __init__.py
│   │   └── todo.py          # Todo model definition
│   ├── schemas/             # Pydantic schemas for request/response validation
│   │   ├── __init__.py
│   │   └── todo.py          # Todo-related schemas
│   └── tests/               # Unit tests
├── requirements.txt         # Python dependencies
├── alembic.ini              # Alembic configuration file
└── README.md                # Project documentation
```

## Database Model

The application uses a `Todo` table in the database with the following schema:

| Column           | Type         | Description                                  |
|------------------|--------------|----------------------------------------------|
| `id`            | Integer      | Primary key                                  |
| `task_name`     | String(120)  | Title or name of the task                    |
| `description`   | String(255)  | Description of the task                      |
| `due_date`      | DateTime     | Deadline for the task                        |
| `estimated_hours` | Integer     | Estimated time to complete the task (hours) |
| `actual_hours`   | Integer      | Actual time spent on the task (hours)       |
| `is_completed`  | Boolean      | Status of the task (completed or not)        |
| `created_at`    | DateTime     | Timestamp of task creation                   |
| `updated_at`    | DateTime     | Timestamp of last task update                |

## How to Run

### Prerequisites

- Python 3.8+
- MySQL or any other supported database
- `pip` for dependency management

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Lgithubprogram/todo--your--job.git
   cd todo--your--job
   ```

2. Create and activate a virtual environment:
   ```bash
    conda create -n your_env_name python = 3.12
    conda activate your_env_name 
    conda activate your_env_name
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your database connection in `app/core/config.py`.

### Database Migration

1. Initialize the Alembic migrations:
   ```bash
   alembic init alembic
   ```

2. Autogenerate the initial migration:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

3. Apply the migrations:
   ```bash
   alembic upgrade head
   ```

### Run the Application

Start the FastAPI development server:
```bash
uvicorn app.main:app --reload
```

The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### API Documentation

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Common Issues and Debugging

1. **Database Errors:**
   - Ensure the database is running and the connection string in `app/core/config.py` is correct.
   - If Alembic reports missing revisions, clear the `alembic_version` table and recreate the migrations.

2. **Dependency Issues:**
   - Run `pip install email-validator` if prompted.

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

