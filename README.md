# 🍋 Little Lemon Restaurant API

A simple Django & Django REST Framework (DRF) project from the **Meta Back-End Developer Professional Certificate**. This API allows users to manage restaurant menu items, bookings, and reservations, with authentication provided via tokens and Djoser.

---

## 📦 Project Features

- Django backend for restaurant reservations and menu management
- RESTful API using Django REST Framework
- Token-based authentication
- User registration and login with Djoser
- Dynamic frontend forms for reservations
- Admin panel for managing data

---

## ⚙️ Installation

1. Clone the repo and set up the environment:

```bash
git clone git@github.com:hvaluk/django_meta_coursera.git
cd django_meta_coursera


2. Set up virtual environment

pip install virtualenv
virtualenv myenv --python=python3
source myenv/bin/activate

3. Install dependencies

pip install django
pip install djangorestframework
pip install djoser
pip install djangorestframework-authtoken


🚀 Run the Project

1. Apply migrations

python manage.py makemigrations
python manage.py migrate


2.  Create superuser (optional)
 
python manage.py createsuperuser


3. Start development server

python manage.py runserver


4. Testing

python manage.py test    



Little Lemon Restaurant API

✅ Testable API endpoints:

1. /test/                       - Simple test view (returns "Hello, world!")
2. /menu/                      - List and create menu items (GET/POST)
3. /menu/<int:pk>/             - Retrieve, update, or delete a menu item (GET/PUT/DELETE)
4. /bookings/                  - Get bookings for a date or create a new booking (GET/POST)
5. /reservations/              - View bookings via frontend
6. /book/                      - Make a booking via form
7. /message/                   - Protected API view (requires token auth)
8. /api-token-auth/            - Get authentication token (POST with username & password)
9. /tables/                    - BookingViewSet (view, add, edit bookings via DRF viewset)
10. /auth/users/               - Djoser: register new users
11. /auth/token/login/         - Djoser: login and get token
12. /auth/token/logout/        - Djoser: logout and remove token

📌 Note:
- Some endpoints require authentication (`TokenAuthentication`).
- Use `/api-token-auth/` or `/auth/token/login/` to obtain a token.
- Use the token in the header: `Authorization: Token <your_token>`.
