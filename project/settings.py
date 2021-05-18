
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'kl_&f)s_ktgp8#q7i&mhmyv#sa4gv)ptoh1h0t1@)%i38d8v+b'

DEBUG = True

ALLOWED_HOSTS  = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'blog',
    'accounts',
    'crispy_forms',
    'django_countries',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'ckeditor',
    "bootstrap4",

    

]



AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    "django.contrib.auth.backends.ModelBackend",
    'accounts.backends.EmailBackend', #import emailbackend for login using email
)

SOCIAL_AUTH_GITHUB_KEY = '5bc3a315e0bc36eff2c3'
SOCIAL_AUTH_GITHUB_SECRET = 'cb6beb0fa74618b1c267d1dd4cc40b869ada5868'

SOCIAL_AUTH_FACEBOOK_KEY = '2551771398403752'
SOCIAL_AUTH_FACEBOOK_SECRET = '194331649cfe9dc09fa69f2c51aaf895' 


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES':(
#         'rest_framework.authentication.SessionAuthentication',
#     ),

# }
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema' } #for Swagger


CRISPY_TEMPLATE_PACK = 'bootstrap4'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR , "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR , "media")



LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'accounts:doctors'

CKEDITOR_UPLOAD_PATH = "uploads/"
