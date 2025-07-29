🍽️ FoodPlaza – Online Food Ordering System

FoodPlaza is a full-stack web application built with Django that allows users to browse food items, add them to the cart, and place orders online. It includes user and admin functionalities, secure authentication, and a responsive interface.

Features

User Registration and Login

Browse and Search Food Items

Add to Cart and Place Orders

Order History with Real-Time Status

Admin Panel to Manage Menu, Orders, and Users

Order Status: Pending → Preparing → Delivered

Responsive UI with Bootstrap

Technologies Used

Backend: Django, Python
Frontend: HTML, CSS, Bootstrap
Database: SQLite (or MySQL)
Version Control: Git, GitHub
Tools: Django Admin, Postman (optional)

Project Structure

FoodPlaza/
│
├── foodapp/ → Main app with models, views, templates
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ └── urls.py
│
├── FoodPlaza/ → Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.sqlite3 → Default SQLite database
├── manage.py → Django CLI
└── requirements.txt → Dependencies

How to Run the Project Locally

Clone the repository:
git clone https://github.com/your-username/FoodPlaza.git
cd FoodPlaza

Create and activate a virtual environment:
python -m venv env
source env/bin/activate (For Windows: env\Scripts\activate)

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the server:
python manage.py runserver

Open in browser:
Visit http://127.0.0.1:8000/ to access the application.

