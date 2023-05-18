# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
import os


DATABASES = {
    'default': {
        'ENGINE': str(os.environ.get('DATABASE_ENGINE')),
        'NAME': str(os.environ.get('DATABASE_NAME')),
        'DATABASE_USER': str(os.environ.get('DATABASE_USER')),
        'DATABASE_PASSWORD': str(os.environ.get('DATABASE_PASSWORD')),
        'DATABASE_HOST': str(os.environ.get('DATABASE_HOST')),
        'DATABASE_PORT': str(os.environ.get('DATABASE_PORT')),
        }
}
