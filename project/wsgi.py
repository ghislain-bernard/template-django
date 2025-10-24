#!/usr/bin/env python3
#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import os

import django.core.wsgi

#----------------------------------------------------------------------------------------------------------------------#

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = django.core.wsgi.get_wsgi_application()

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
