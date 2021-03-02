import os
from pathlib import Path
from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env.str('host'),
        'PORT': env.int('port'),
        'NAME': env.str('name'),
        'USER': env.str('user'),
        'PASSWORD': env.str('password'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('secret_key')

DEBUG = env.bool('debug', default=False)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
