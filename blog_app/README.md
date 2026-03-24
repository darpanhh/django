# Blog App

A simple Django-based blog application that allows users to create, manage, and view blog posts.

## Features

- **User Authentication**: Sign up and log in functionality
- **Create Posts**: Authenticated users can create new blog posts
- **View Posts**: Browse all blog posts from all users
- **My Posts**: View your own published posts
- **User Management**: Built-in Django admin panel for user and post management

## Project Structure

```
blog_app/
├── manage.py                 # Django project management script
├── db.sqlite3               # SQLite database file
├── blog/                    # Main blog application
│   ├── models.py           # Database models (Posts model)
│   ├── views.py            # View logic (signup, login, post creation, etc.)
│   ├── urls.py             # URL routing for blog app
│   ├── admin.py            # Django admin configuration
│   ├── apps.py             # App configuration
│   ├── forms.py            # Form definitions
│   ├── tests.py            # Unit tests
│   ├── migrations/         # Database migrations
│   ├── templates/blog/     # HTML templates
│   └── static/image/       # Static image files
└── blog_app/               # Django project configuration
    ├── settings.py         # Project settings
    ├── urls.py             # Main URL configuration
    ├── asgi.py             # ASGI configuration
    └── wsgi.py             # WSGI configuration
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Navigate to the project directory**
   ```bash
   cd blog_app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Main blog: http://localhost:8000/home
   - Admin panel: http://localhost:8000/admin

## Available URLs

| URL | Description |
|-----|-------------|
| `/signup` | User registration page |
| `/login` | User login page |
| `/logout` | User logout |
| `/home` | View all posts |
| `/newpost` | Create a new post |
| `/mypost` | View user's own posts |
| `/admin` | Django admin panel |

## Database Models

### Posts Model
- **title**: CharField (max 100 characters)
- **content**: TextField
- **date_posted**: DateTimeField (auto-set to current time)
- **author**: ForeignKey to Django User model

## Usage

### Creating an Account
1. Navigate to `/signup`
2. Enter username, email, and password
3. Submit to create account
4. Log in with your credentials

### Creating a Post
1. Log in to your account
2. Click "New Post"
3. Enter post title and content
4. Submit to publish

### Viewing Posts
- **All Posts**: Visit `/home` to see all published posts
- **Your Posts**: Visit `/mypost` to see only your posts

## Admin Features

Access the Django admin panel at `/admin` using your superuser credentials to:
- Manage user accounts
- View and edit all blog posts
- Manage post deletion
- Monitor user activity

## Technologies Used

- **Django 5.2.11**: Web framework
- **SQLite**: Database
- **Python**: Programming language
- **HTML/CSS**: Frontend

## Future Enhancements

- Add post editing functionality
- Implement comments on posts
- Add post categories and tags
- Email notifications
- Search functionality
- Post like/dislike feature
- User profile pages

## Notes

- This is a development application. Never use `DEBUG = True` in production
- Change the `SECRET_KEY` in settings.py before deploying to production
- Consider using a more robust database (PostgreSQL) for production

## License

This project is open source and available under the MIT License.
