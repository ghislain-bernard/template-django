#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import django.contrib.admin
import django.shortcuts
import django.urls

import portal.views

#----------------------------------------------------------------------------------------------------------------------#

urlpatterns = [
  django.urls.path('admin/', django.contrib.admin.site.urls),
  django.urls.path('favicon.ico', lambda _ : django.shortcuts.redirect('static/favicon.ico', permanent=True)),
  django.urls.path('', portal.views.home, name='home'),
]

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
