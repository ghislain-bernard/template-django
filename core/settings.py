#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

# https://docs.djangoproject.com/en/5.2/ref/settings/#allowed-hosts

ALLOWED_HOSTS = ['*']

# https://docs.djangoproject.com/en/5.2/ref/settings/#installed-apps

INSTALLED_APPS = ['django.contrib.staticfiles', 'core.portal']

# https://docs.djangoproject.com/en/5.2/ref/settings/#root-urlconf

ROOT_URLCONF = 'core.urls'

# https://docs.djangoproject.com/en/5.2/ref/settings/#static-url

STATIC_URL = 'static/'

# https://docs.djangoproject.com/en/5.2/ref/settings/#staticfiles-dirs

STATICFILES_DIRS = ['static']

# https://docs.djangoproject.com/en/5.2/ref/settings/#templates

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'],
  },
]

# https://docs.djangoproject.com/en/5.2/ref/settings/#secret-key

SECRET_KEY = 'aib9thaivahquaigi0woo4uol2Aid1ei'

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
