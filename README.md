# Djangoblog

This is a headless Django Application for Blogs. It's based on Python Django Restframework, uses Postgres Database and Redis Caching. It's fully containerized.


## API Documentation
The application currently includes following Endpoints:

| Type | Endpoint                           | Is Cached | Description                        |
|------|------------------------------------|-----------|------------------------------------|
| GET  | /api/blog/preview                  | Yes       | Lists all blogposts in application |
| GET  | /api/blog/detail/{slug:title_slug} | Yes       | Full single Blog                   |


## Setup

There are two ways for setup:
1. General Python, Redis, Postgres Setup
2. Docker Setup

### General Setup
The application is based on
- Python v3.6 and higher
- Postgres
- Redis

Make sure that your system has everything installed and up for running.

For starting the application follow these steps:
1. install all required python packages e.g. by using `pip install -r requirements.txt`
2. start Postgres and Redis instances
3. Create `.env` file by copying `.env.example` and replace properties with your local settings
4. Add `.env` file to your executable path
5. Migrate database by using `python djangoblog/manage.py migrate`
6. Create Superuser for login. You could use Djangos default function `python djangoblog/manage.py createsuperuser` or a custom command from that project `python djangoblog/manage.py init_superuser`
7. Start the server by using `python djangoblog/manage.py runserver`

**Your Application will run at `http://localhost:8000/`**


### Docker Setup
Make sure that you have at least two application installed:
- docker
- docker-compose

1. For initializing the application you use
```
docker-compose -f docker-compose-initialization.yml up
```
That will automatically
- Install Python, Postgres and Redis in your docker instance
- Setting up the Django application
- Migrating database and create a superuser
- Start the application

2. For starting the application when it's already initialized:
```
docker-compose -f up
```
That will automatically
- Install Python, Postgres and Redis in your docker instance
- Setting up the Django application
- Start the application

**Your Application will run at `http://localhost:8000/`**
