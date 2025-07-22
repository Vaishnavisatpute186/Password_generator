SECRET_KEY = 'django-insecure-passwordgen'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'generator',
]

MIDDLEWARE = []

ROOT_URLCONF = 'passwordgen.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['generator/templates'],
    'APP_DIRS': True,
    'OPTIONS': {},
}]

WSGI_APPLICATION = 'passwordgen.wsgi.application'

STATIC_URL = '/static/'
STATICFILES_DIRS = ['generator/static']