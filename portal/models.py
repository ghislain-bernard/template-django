#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import uuid

import django.db.models

#----------------------------------------------------------------------------------------------------------------------#

class Element(django.db.models.Model):

  uuid: django.db.models.UUIDField = django.db.models.UUIDField(default=uuid.uuid4,
                                                                editable=False,
                                                                primary_key=True)

  name: django.db.models.CharField = django.db.models.CharField(max_length=128, unique=True)

  def __str__(self):
    return str(self.name)

  class Meta:
    ordering = ['name']

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
