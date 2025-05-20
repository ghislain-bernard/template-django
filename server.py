#!/usr/bin/env python3
#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import sys

import django
import django.conf
import django.core.handlers.wsgi
import django.core.management

import core.settings

#----------------------------------------------------------------------------------------------------------------------#

settings = {name: getattr(core.settings, name) for name in dir(core.settings) if name.isupper()}

django.conf.settings.configure(**settings, DEBUG=__name__ == '__main__')
django.setup()

#----------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
  django.core.management.execute_from_command_line(sys.argv)
else:
  application = django.core.handlers.wsgi.WSGIHandler()

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
