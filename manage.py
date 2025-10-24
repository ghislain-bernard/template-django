#!/usr/bin/env python3
#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import sys

import django
import django.conf
import django.core.management

import project.settings

#----------------------------------------------------------------------------------------------------------------------#

def main():
  settings = {name: getattr(project.settings, name) for name in dir(project.settings) if name.isupper()}

  django.conf.settings.configure(**settings, DEBUG=True)
  django.setup()

  django.core.management.execute_from_command_line(sys.argv)

#----------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
  main()

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
