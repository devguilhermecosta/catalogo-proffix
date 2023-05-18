# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
from dotenv import load_dotenv
import os


load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'DATABASE_USER': os.environ.get('DATABASE_USER'),
        'DATABASE_PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'DATABASE_HOST': os.environ.get('DATABASE_HOST'),
        'DATABASE_PORT': os.environ.get('DATABASE_PORT'),
        }
}
