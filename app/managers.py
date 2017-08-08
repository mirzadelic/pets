# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import UserManager
from django.db import models

DOG_TYPE = 1
CAT_TYPE = 2
PET_TYPE = (
    (DOG_TYPE, 'Dog'),
    (CAT_TYPE, 'Cat'),
)


class OwnerManager(UserManager):
    def create_superuser(self, username, password, **extra_fields):
        return super(OwnerManager, self).create_superuser(username, None, password, **extra_fields)


class DogManager(models.Manager):

    def get_queryset(self):
        qs = super(DogManager, self).get_queryset()
        return qs.filter(pet_type=DOG_TYPE)


class CatManager(models.Manager):

    def get_queryset(self):
        qs = super(CatManager, self).get_queryset()
        return qs.filter(pet_type=CAT_TYPE)
