# Backend-django project
This is a django project where the Django REST API framework is used.

This back-end is applied for a specific hockey website use case.

The goal is to to learn how to use the Django REST API powerful toolkit in order to build a Web API.

## Setup 
Clone the project
```bash
git clone https://github.com/mariasolomon/backend-django.git
```
Create and start a virtual environment
```bash
python -m venv path/to/env
source env/bin/activate
```
Install the project dependencies
```bash
pip install -r requirements.txt
```
Make a demo project just to copy the SECRET KEY generated by Django to the setting.py
```bash
django-admin startproject “name of the project”
```
Create an admin account
```bash
python manage.py createsuperuser
```
Preapre the DB migrations
```bash
python manage.py makemigrations hockey
```
Migrate 
```bash
python manage.py migrate hockey
```
Run the project 
```bash
python manage.py runserver 
```
