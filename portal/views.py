#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import django.http
import django.shortcuts

#----------------------------------------------------------------------------------------------------------------------#

def home(request: django.http.HttpRequest):
  return django.shortcuts.render(request, 'index.html')

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
