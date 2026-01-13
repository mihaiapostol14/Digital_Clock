# Digital Clock

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-5.2.5-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](#)  
![Digital Clock Preview](https://github.com/mihaiapostol14/Digital_Clock/blob/4cfb83afc9511ac3780e51c7607be0da1a965ec7/assets/preview.png) 

A small, responsive Django application that displays a live digital clock in the browser. The project demonstrates a minimal Django site with a single app (`clock_app`) and uses static assets (CSS/JS) to render and update the clock in real time.

---

## Table of Contents

- [Digital Clock](#digital-clock)
  - [Table of Contents](#table-of-contents)
  - [Tech Stack](#tech-stack)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project structure](#project-structure)
  - [Development notes](#development-notes)
  - [Contributing](#contributing)
  - [License](#license)
  - [Author](#author)

---

## Tech Stack

- Python: 3.11+ (recommended)
- Framework: Django 5.2.5
- Frontend: HTML / CSS / Vanilla JavaScript (static files served by Django)
- Database: SQLite (default development DB configured)

Key dependency:
- Django==5.2.5

If you add further third-party packages, pin them in `requirements.txt`.


## Installation

These commands assume you will work from the repository root. The main Django project is located in the `Clock` folder, so the instructions cd into that directory.

1. Clone the repository (if you haven't already):

```bash
git clone https://github.com/mihaiapostol14/Digital_Clock.git
cd Digital_Clock
```
2. Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows
```

3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Change into the Django project directory:

```bash
cd Clock
```

## Usage

Run the development server:

```bash
python manage.py runserver
```

Then open your browser and navigate to [Local Testing Server](http://127.0.0.1:8000/)

The root URL serves the digital clock view.

Useful commands:

- Run tests (if/when tests are added):

```bash
python manage.py test
```

- Create admin user:

```bash
python manage.py createsuperuser
```

- Collect static files for production:

```bash
python manage.py collectstatic
```

---

## Project structure

Top-level view of the repository (relevant files and folders):

```
Digital_Clock/
├── Clock/                       # Django project directory (cd into this folder)
│   ├── Clock/                   # Project configuration module
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── clock_app/               # Main app: clock_app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── utils.py
│   ├── templates/
│   │   ├── base.html
│   │   └── clock_app/
│   │       └── clock.html
│   ├── static/
│   │   └── clock_app/
│   │       ├── css/
│   │       │   └── clock.css
│   │       └── js/
│   │           └── clock.js
│   ├── manage.py
│   └── db.sqlite3                # (optional / not committed typically)
├── README.md
```

---

## Development notes

- Settings:
  - The project was created with Django 5.2.5 (see `Clock/Clock/settings.py`).
  - Default DB config uses SQLite. For production, configure `DATABASES` and `ALLOWED_HOSTS` in `settings.py`.
  - MEDIA_URL / MEDIA_ROOT and STATICFILES_DIRS are configured for serving media and static assets.

- Static assets:
  - The clock UI is implemented using static CSS and JavaScript under `Clock/static/clock_app/`.
  - The JS file updates the DOM every second to show the current time.

- Security:
  - Do not use `DEBUG = True` in production. Replace the secret key and secure settings for deployment.

---

## Contributing

Contributions are welcome. Typical workflow:

1. Fork the repo
2. Create a feature branch
3. Make changes and add tests
4. Open a pull request

Please add a concise PR description and run linters/tests locally before submitting.

---

## License

This repository currently has no explicit license file. Add a LICENSE file (for example, MIT) if you want to permit reuse. The badges at the top assume MIT — update as appropriate.

## Author

[Mihai Apostol](https://github.com/mihaiapostol14)