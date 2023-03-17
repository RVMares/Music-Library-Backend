
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hj7d&mf3@2$7j!l*xv&dz+on-7)l2e$py)%9s8_u17(%(f8!bf'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'music_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password!',
    }
}
