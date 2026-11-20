# Akash B — Django Portfolio

A responsive personal portfolio website built with Django, HTML, CSS and JavaScript.

## 1. Setup

```bash
# Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 2. Run the project

```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## 3. Project structure

```text
akash_django_portfolio/
├── manage.py
├── requirements.txt
├── README.md
├── portfolio_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── portfolio/
    ├── __init__.py
    ├── apps.py
    ├── urls.py
    ├── views.py
    ├── templates/
    │   └── portfolio/
    │       └── index.html
    └── static/
        └── portfolio/
            ├── css/
            │   └── style.css
            └── js/
                └── main.js
```

## 4. Customize

Update the personal details and portfolio content in `portfolio/views.py`.
Update styles in `portfolio/static/portfolio/css/style.css`.

The contact form uses a `mailto:` link to open the visitor's email application. It does not store messages in a database or send email from the server.
