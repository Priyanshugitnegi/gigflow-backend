# GigFlow Backend

Backend API for the GigFlow Smart Leads Dashboard.

Built with Django REST Framework and JWT Authentication.

---

## Live Backend

https://web-production-c139e.up.railway.app

---

## Features

- JWT Authentication
- User Registration
- User Login
- Leads CRUD APIs
- Protected Routes
- REST API Structure

---

## API Endpoints

### Authentication

#### Register
POST `/api/auth/register/`

#### Login
POST `/api/auth/login/`

#### Refresh Token
POST `/api/auth/refresh/`

---

### Leads

#### Get Leads
GET `/api/leads/`

#### Create Lead
POST `/api/leads/`

#### Update Lead
PUT `/api/leads/<id>/`

#### Delete Lead
DELETE `/api/leads/<id>/`

---

## Backend Stack

- Django
- Django REST Framework
- JWT Authentication
- SQLite
- Railway

---

## Local Setup

```bash
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## Author

Priyanshu Negi
