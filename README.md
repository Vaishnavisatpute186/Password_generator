Password_Generator

A simple and secure password generator web application built with *HTML, **CSS, and **Python (Django)*. It allows users to generate strong, random passwords of customizable length and complexity, ideal for protecting online accounts.

Features:
1. Generate random, secure passwords
2. Customize length and complexity
3. Include/exclude:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0–9)
  - Special characters (!@#$%^&*)
4. Instant password display
5. Simple and responsive UI

 Tech Stack:

- Frontend: HTML, CSS, Bootstrap
- Backend: Python, Django
- Database: SQLite (default Django DB)

Project Structure:

```bash
password_generator/
├── generator/               # Django app
│   ├── static/              # CSS files
│   ├── templates/           # HTML templates
│   ├── views.py             # Logic for password generation
│   └── urls.py              # URL routes
├── manage.py                # Django project runner
└── requirements.txt         # Python dependencies
