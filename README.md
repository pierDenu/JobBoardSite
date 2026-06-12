# JobBoard

A Django web application for posting and browsing job listings, with separate roles for employers and job seekers.

## Features

- Custom user authentication (employer / job seeker roles)
- Job listing creation and browsing
- City search with autocomplete (populated from Wikipedia)
- PostgreSQL database

## Tech Stack

- Python 3.12, Django 5.1
- PostgreSQL
- Bootstrap 4 + django-crispy-forms

## Setup

1. Clone the repository and create a virtual environment:
   ```bash
   git clone <repo-url>
   cd JobBoard
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and fill in your values:
   ```bash
   cp .env.example .env
   ```

3. Apply migrations and run:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
