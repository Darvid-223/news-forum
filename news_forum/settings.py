from pathlib import Path
import os
import environ
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Set to False in production environments

# Hosts allowed to connect to the application
ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']

# Redirect URLs after login/logout
LOGIN_REDIRECT_URL = '/'  # Redirect to home after login
LOGOUT_REDIRECT_URL = '/'  # Redirect to home after logout


# Application definition: Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',  # Custom app for handling news posts
]


# Middleware configuration: handles requests/responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Handles static file caching
]


# URL configuration
ROOT_URLCONF = 'news_forum.urls'

# Templates settings: where Django will look for HTML templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add custom directories here if needed
        'APP_DIRS': True,  # Looks for templates inside app directories
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

# WSGI application configuration
WSGI_APPLICATION = 'news_forum.wsgi.application'


# Database configuration for development and production environments
if env('DJANGO_ENV') == 'development':
    # Local PostgreSQL configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'news_forum',  # Database name
            'USER': 'postgres',  # Database user
            'PASSWORD': env('DB_PASSWORD'),  # Database password from .env file
            'HOST': 'localhost',  # Localhost for development
            'PORT': '5432',  # Default PostgreSQL port
        }
    }
else:
    # Heroku PostgreSQL configuration
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600)  # Use Heroku's DATABASE_URL
    }


# Password validation settings
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


# Internationalization settings
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True  # Enable internationalization

USE_TZ = True  # Enable timezone support


# Static files configuration (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL for static files

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory for static files in production

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'news/static'),  # Additional static files directory
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Static file compression for production


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default field for auto-incrementing primary keys


# Email backend configuration for sending emails (e.g., password resets)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')  # Email account for sending messages
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')  # Email password from .env file
DEFAULT_FROM_EMAIL = 'darvidapi@gmail.com'  # Default email sender address


# Security settings
# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 31536000  # Ensure HSTS is enabled for one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow browsers to preload the site to always use HTTPS

# Cookies security settings
SESSION_COOKIE_SECURE = True  # Ensure session cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are only sent over HTTPS

# Additional security headers
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent the browser from interpreting files as a different MIME type
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS protection in browsers

# Clickjacking prevention
X_FRAME_OPTIONS = 'DENY'  # Prevent embedding the site in iframes

# Ensure all requests are redirected to HTTPS
SECURE_SSL_REDIRECT = True  # Set to True in production