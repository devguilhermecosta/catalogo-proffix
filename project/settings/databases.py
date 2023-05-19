# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
import os


DATABASES = {
    'default': {
        'ENGINE': str(os.environ.get('DATABASE_ENGINE')),
        'NAME': str(os.environ.get('DATABASE_NAME')),
        'USER': str(os.environ.get('DATABASE_USER')),
        'PASSWORD': str(os.environ.get('DATABASE_PASSWORD')),
        'HOST': str(os.environ.get('DATABASE_HOST')),
        'PORT': str(os.environ.get('DATABASE_PORT')),
    }
}
