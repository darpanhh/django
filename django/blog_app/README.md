# Django Blog Application

A simple Django-based blogging application with a clean and intuitive interface.

## Features

- Create, read, update, and delete blog posts
- Organized blog templates with static file support
- SQLite database for data persistence
- Django admin panel for content management
- Responsive static file handling

## Project Structure

```
blog_app/
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
├── blog/                  # Main app directory
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── tests.py           # Unit tests
│   ├── templates/         # HTML templates
│   │   └── blog/          # Blog-specific templates
│   ├── static/            # Static files (CSS, images)
│   │   └── image/         # Image assets
│   └── migrations/        # Database migrations
└── blog_app/              # Project settings
    ├── settings.py        # Django settings
    ├── urls.py            # Main URL configuration
    ├── wsgi.py            # WSGI configuration
    └── asgi.py            # ASGI configuration
```

## Installation

1. **Clone or navigate to the project:**
   ```bash
   cd blog_app
   ```

2. **Create a virtual environment (if not already done):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required dependencies:**
   ```bash
   pip install django
   ```

## Usage

1. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser account (for admin panel):**
   ```bash
   python manage.py createsuperuser
   ```

3. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

4. **Access the application:**
   - Blog: `http://localhost:8000/blog/`
   - Admin: `http://localhost:8000/admin/`

## Admin Panel

Access the Django admin panel to manage blog posts:
- Navigate to `http://localhost:8000/admin/`
- Log in with your superuser credentials
- Manage blog posts, users, and other content

## Database

The application uses SQLite for data persistence:
- Database file: `db.sqlite3`
- Migrations are stored in `blog/migrations/`

## Customization

- **Models:** Edit `blog/models.py` to add or modify data structures
- **Templates:** Modify `blog/templates/blog/` for UI changes
- **Static Files:** Add CSS, images to `blog/static/` directory
- **Views:** Update `blog/views.py` for business logic

## Testing

Run tests to ensure application integrity:
```bash
python manage.py test
```

## Development Notes

- Debug mode is typically enabled in `settings.py` during development (set `DEBUG = True`)
- Static files should be collected before deployment
- Use `python manage.py collectstatic` to gather static files

## Deployment

For production deployment:
1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production server (Gunicorn, uWSGI)
4. Set up environment variables for sensitive data
5. Configure a production database (PostgreSQL, MySQL)

## License

This project is open source and available under the MIT License.

---

For more information about Django, visit [Django Documentation](https://docs.djangoproject.com/)
