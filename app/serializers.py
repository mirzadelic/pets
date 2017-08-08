# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from models import Owner, Pet, Dog, Cat
from managers import DOG_TYPE, CAT_TYPE


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ('id', 'name', 'birthday')


class DogSerializer(PetSerializer):

    class Meta(PetSerializer.Meta):
        model = Dog


class DogDetailSerializer(PetSerializer):

    class Meta(PetSerializer.Meta):
        model = Dog
        fields = ('id', 'name', 'birthday', 'owner')

    def create(self, validated_data):
        validated_data['pet_type'] = DOG_TYPE
        instance = super(DogDetailSerializer, self).create(validated_data)

        return instance


class CatSerializer(PetSerializer):

    class Meta(PetSerializer.Meta):
        model = Cat


class CatDetailSerializer(PetSerializer):

    class Meta(PetSerializer.Meta):
        model = Cat
        fields = ('id', 'name', 'birthday', 'owner')

    def create(self, validated_data):
        validated_data['pet_type'] = CAT_TYPE
        instance = super(DogDetailSerializer, self).create(validated_data)

        return instance


class BaseOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = (
            'first_name', 'last_name'
        )


class OwnerSerializer(BaseOwnerSerializer):
    dogs = DogSerializer(many=True)
    cats = CatSerializer(many=True)

    class Meta:
        model = Owner
        fields = (
            'first_name', 'last_name', 'dogs', 'cats'
        )

    def create(self, validated_data):
        dogs = validated_data.pop('dogs')
        cats = validated_data.pop('cats')

        instance = super(OwnerSerializer, self).create(validated_data)
        dogs = create_pets(instance, dogs, DOG_TYPE)
        cats = create_pets(instance, cats, CAT_TYPE)

        instance.save()

        return instance

    def update(self, instance, validated_data):
        dogs = validated_data.pop('dogs')
        cats = validated_data.pop('cats')

        instance = super(OwnerSerializer, self).update(
            instance, validated_data)

        instance.pets.all().delete()

        dogs = create_pets(instance, dogs, DOG_TYPE)
        cats = create_pets(instance, cats, CAT_TYPE)

        instance.save()

        return instance


def create_pets(owner, items, pet_type):
    print items
    bulk_items = []
    for item in items:
        item_obj = Pet(
            owner=owner,
            pet_type=pet_type,
            **item
        )
        bulk_items.append(item_obj)

    items = Pet.objects.bulk_create(bulk_items)
    return items
