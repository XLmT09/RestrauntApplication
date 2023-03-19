from django.contrib import messages
import sys, os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%(#liaxcky(isq_(lz48gbxu5439cfbd+9a7@fpwk#8$o_5r*i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # The main app for the website
    'project',
    # These are the other custom apps we have created
    # This app contains the user login/signup components
    'account.apps.AccountConfig',
    # This app contains the waiter page and functionality
    'waiter.apps.WaiterConfig',
    # This app contains the kitchen staff page and functionality
    'kitchen.apps.KitchenConfig',
    # A built in djnago form we are using to make form styling easier
    'crispy_forms', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database

# KEEP THIS CODE IF WE EVER WANT TO USE THE SQL DATABASE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#THIS CODE CONNECTS DATABSE WITH AN BIT.IO DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zkac226/restaurantDB',
        'USER': 'zkac226',
        'PASSWORD': 'v2_3yDhd_4vkmgPmQcRBh3RBQKEZzLvy',
        'HOST': 'db.bit.io',
        'PORT': '5432',
    }
}

# This is the test db to be used during testing.
# db is automatically created and deleted when running the test command.
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase'
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# Every app will always check there own static file
STATIC_URL = 'static/'

# In addition every app will check the following static files in the list below
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'project/static'),
]

# Add class names to custom pop up messages
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# After user login it redirects them to the home page.
LOGIN_REDIRECT_URL = '/'

#After user logs out, they are redirected to the home page
LOGOUT_REDIRECT_URL = '/'

# If user tries to access a page that requires an account they get sent to the login page
LOGIN_URL = 'account-login'

# forms use bootstrap 4 css
CRISPY_TEMPLATE_PACK = 'bootstrap4'
