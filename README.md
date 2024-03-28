# E-Commerce Boost

## Overview
E-Commerce Boost is an e-commerce app made using Django 3, SQLite, and Bootstrap 4. It provides a platform for managing products, orders, and customer interactions. This app is equipped with features such as user registration, cart management, order placement, and invoice generation.

## Features
- User-friendly interface for browsing and purchasing electronic products.
- Admin dashboard for managing products and orders.
- User registration and authentication system.
- Cart functionality for adding and removing items.
- Dynamic product catalog with search and filtering options
- Secure payment processing for order transactions.
- Invoice generation for completed orders.

## Technologies Used
- Django 3 framework for backend development.
- SQLite database for storing product, order, and user information.
- Bootstrap 4 framework for responsive design.
- Several other packages including django-crispy-forms, django-filter, pillow, easy-thumbnails, and dj-database-url.

## Installation
1. Clone the repository: `git clone https://github.com/chaimaa-El/E-Commerce-Boost.git`
2. Navigate to the project directory: `cd e-commerce-boost`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a superuser: `python manage.py createsuperuser` and follow the prompts to set up your admin credentials.
5. Run migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`

## Usage
1. Visit the website at [http://localhost:8000/store](http://localhost:8000/store) in your browser to access the customer module.
2. Visit [http://localhost:8000/admin](http://localhost:8000/admin) for the admin module and log in using the superuser credentials.
3. Explore the app functionalities including product management, order processing, and user interactions.

