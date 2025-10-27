#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import django.http
import django.shortcuts

import portal.models

#----------------------------------------------------------------------------------------------------------------------#

def home(request: django.http.HttpRequest):
  return django.shortcuts.render(request, 'index.html', {
    'elements': portal.models.Element.objects.all(),
  })

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
