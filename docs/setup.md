# Setup

# Django Setup Guide (Windows)

> These steps assume you're using **Windows PowerShell**, not Command Prompt.

## 1. Create a Project Directory

```powershell
mkdir django
cd django
```

## 2. Install Pipenv (Virtual Environment Manager)

```powershell
pip install pipenv
```

## 3. Install Django in a Virtual Environment

```powershell
pipenv install django
```

## 4. Activate the Virtual Environment

```powershell
pipenv shell
```

## 5. Start a New Django Project

```powershell
django-admin startproject myproject .
```

## 6. Run the Django Development SErver

```powershell
pipenv shell       # activate the virtual environment, if not already
python manage.py runserver
```
Then open a browser and go to: http://127.0.0.1:8000/

To stop the server, press CTRL + C.

## To make and apply migrations
python manage.py makemigrations
python manage.py migrate

## Notes

Always run pipenv shell to activate your environment before using Django commands.
Only run django-admin startproject once at the beginning. After that, use runserver, makemigrations, and migrate for ongoing development.