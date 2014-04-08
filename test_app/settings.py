DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

TIME_ZONE = 'Australia/Sydney'
LANGUAGE_CODE = 'en-AU'

USE_TZ = True
STATIC_URL = '/static/'

SECRET_KEY = '2bksb4rhbv7i1$!5xzux0&amp;&amp;sl2@de@k6sxb4(zlj4l)+xds#2i'

ROOT_URLCONF = 'test_app.urls'
WSGI_APPLICATION = 'test_app.wsgi.application'

INSTALLED_APPS = (
    'touchtechnology.public',

    'django.contrib.auth',
    'django.contrib.contenttypes',
)
