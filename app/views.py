# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet
from serializers import OwnerSerializer, DogDetailSerializer, CatDetailSerializer
from models import Owner, Dog, Cat


class OwnerAPIView(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class DogAPIView(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogDetailSerializer


class CatAPIView(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatDetailSerializer
