# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
import os

<<<<<<< HEAD
=======

load_dotenv()

>>>>>>> f1e8ba016923fe57ff9ec4d37ed7a2a877e7a2b0

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}
