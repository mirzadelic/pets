# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Owner, Pet, Dog, Cat
from managers import DOG_TYPE, CAT_TYPE


class OwnerPetInline(admin.TabularInline):
    model = Pet
    extra = 0
    fields = ('name', 'birthday', 'pet_type')


class OwnerAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'username', 'first_name', 'last_name', 'dogs_count', 'cats_count')
    readonly_fields = ('dogs_count', 'cats_count')
    exclude = ('groups', 'last_login', 'is_superuser',
               'is_admin', 'user_permissions', 'is_staff')
    inlines = (OwnerPetInline,)

    def dogs_count(self, obj):
        return obj.dogs.count()
    dogs_count.short_description = 'Dogs'

    def cats_count(self, obj):
        return obj.cats.count()
    cats_count.short_description = 'Cats'


class PetAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('name', 'birthday', 'owner')
    search_fields = ('name', )
    exclude = ('pet_type', )


class DogAdmin(PetAdmin):

    def save_model(self, request, obj, form, change):
        obj.pet_type = DOG_TYPE
        super(DogAdmin, self).save_model(request, obj, form, change)


class CatAdmin(PetAdmin):

    def save_model(self, request, obj, form, change):
        obj.pet_type = CAT_TYPE
        super(CatAdmin, self).save_model(request, obj, form, change)


admin.site.register(Dog, DogAdmin)
admin.site.register(Cat, CatAdmin)
admin.site.register(Owner, OwnerAdmin)
