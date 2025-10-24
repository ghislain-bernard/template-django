#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

# https://docs.djangoproject.com/en/5.2/ref/settings/#allowed-hosts

ALLOWED_HOSTS = ['*']

# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# https://docs.djangoproject.com/en/5.2/ref/settings/#installed-apps

INSTALLED_APPS = ['django.contrib.staticfiles', 'portal.apps.PortalConfig']

# https://docs.djangoproject.com/en/5.2/ref/settings/#root-urlconf

ROOT_URLCONF = 'project.urls'

# https://docs.djangoproject.com/en/5.2/ref/settings/#static-root

STATIC_ROOT = 'dist/static'

# https://docs.djangoproject.com/en/5.2/ref/settings/#static-url

STATIC_URL = 'static/'

# https://docs.djangoproject.com/en/5.2/ref/settings/#templates

TEMPLATES = [
  {
    "APP_DIRS": True,
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
  },
]

# https://docs.djangoproject.com/en/5.2/ref/settings/#secret-key

SECRET_KEY = 'aib9thaivahquaigi0woo4uol2Aid1ei'

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
