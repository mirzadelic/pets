# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from managers import OwnerManager, DogManager, CatManager, PET_TYPE, DOG_TYPE, CAT_TYPE


class Owner(AbstractUser):
    """
    Model for Owner
    """
    REQUIRED_FIELDS = []

    objects = OwnerManager()

    @property
    def dogs(self):
        return self.pets.filter(pet_type=DOG_TYPE)

    @property
    def cats(self):
        return self.pets.filter(pet_type=CAT_TYPE)


class Pet(models.Model):
    """
    Base Model for Pet
    """
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    owner = models.ForeignKey(Owner, related_name='pets')
    pet_type = models.IntegerField(choices=PET_TYPE)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = 'pet'
        verbose_name_plural = 'pets'


class Dog(Pet):
    """
    Proxy Model for Dog
    """
    objects = DogManager()

    class Meta:
        verbose_name = 'dog'
        verbose_name_plural = 'dogs'
        proxy = True


class Cat(Pet):
    """
    Proxy Model for Cat
    """
    objects = CatManager()

    class Meta:
        verbose_name = 'cat'
        verbose_name_plural = 'cats'
        proxy = True
