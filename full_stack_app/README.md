# Full Stack Application

This is a complete full-stack application combining a modern frontend and a Django REST API backend.

## Project Structure

```
full_stack_app/
├── frontend/               # React/Vue.js frontend application
│   ├── src/               # Source code
│   ├── public/            # Static assets
│   ├── package.json       # Dependencies and scripts
│   ├── vite.config.js     # Vite configuration
│   ├── eslint.config.js   # ESLint configuration
│   └── README.md          # Frontend documentation
│
└── backend/               # Django REST API backend
    ├── crud_operations/   # Main Django project
    ├── employee/          # Employee management app
    ├── manage.py          # Django management script
    └── db.sqlite3         # SQLite database
```

## Getting Started

### Prerequisites

- Node.js 16.x or higher (for frontend)
- Python 3.8 or higher (for backend)
- pip (Python package manager)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (if not already created):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Apply database migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

The backend API will be available at `http://localhost:8000/`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend application will be available at `http://localhost:5173/` (or as shown in the terminal)

## Features

### Backend
- **Employee Management**: CRUD operations for employee records
- **REST API**: Fully RESTful API endpoints
- **Database**: SQLite for development
- **Admin Panel**: Django admin interface at `/admin/`

### Frontend
- **Modern UI**: Built with Vite for fast development
- **ESLint**: Code quality and consistency checks
- **Responsive Design**: Mobile-friendly interface

## API Documentation

### Employee Endpoints
- `GET /api/employees/` - Get all employees
- `POST /api/employees/` - Create a new employee
- `GET /api/employees/<id>/` - Get employee by ID
- `PUT /api/employees/<id>/` - Update employee
- `DELETE /api/employees/<id>/` - Delete employee

## Development

### Running Both Servers

For development, you'll need to run both frontend and backend servers:

1. Terminal 1 - Backend:
```bash
cd backend
python manage.py runserver
```

2. Terminal 2 - Frontend:
```bash
cd frontend
npm run dev
```

### Building for Production

**Frontend:**
```bash
cd frontend
npm run build
```

**Backend:**
```bash
cd backend
python manage.py collectstatic
```

## Important Notes

- The frontend and backend run on different ports during development (frontend: 5173, backend: 8000)
- Configure CORS in backend settings if needed for production
- Keep the database migrations updated when modifying models
- Use `.gitignore` files to exclude node_modules and Python cache directories

## License

This project is part of the Django learning series.
