#!/usr/bin/env python3
#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import os

import django.core.asgi

#----------------------------------------------------------------------------------------------------------------------#

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = django.core.asgi.get_asgi_application()

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
