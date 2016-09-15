from django.core import urlresolvers
from django.contrib import admin
from .. import models
from .base import (ModelAdmin, ReadOnlyTabularInline, IdentifierInline,
                   ContactDetailInline, OtherNameInline)


class PersonIdentifierInline(IdentifierInline):
    model = models.PersonIdentifier


class PersonNameInline(OtherNameInline):
    model = models.PersonName


class PersonContactDetailInline(ContactDetailInline):
    model = models.PersonContactDetail


class PersonLinkInline(ReadOnlyTabularInline):
    readonly_fields = ('url', 'note')
    model = models.PersonLink


class PersonSourceInline(ReadOnlyTabularInline):
    readonly_fields = ('url', 'note')
    model = models.PersonSource


class MembershipInline(ReadOnlyTabularInline):
    model = models.Membership
    readonly_fields = ('id', 'organization', 'post', 'label', 'role', 'start_date',)
    fields = readonly_fields + ('end_date',)
    extra = 0
    can_delete = False


# TODO field locking
@admin.register(models.Person)
class PersonAdmin(ModelAdmin):
    search_fields = ['name']
    readonly_fields = ('id', 'name', 'extras')
    fields = (
        'name', 'id', 'image',
        ('birth_date', 'death_date'),
        ('gender', 'national_identity', 'sort_name', 'summary'),
        'biography', 'extras',
    )
    ordering = ('name',)
    inlines = [
        PersonIdentifierInline,
        PersonNameInline,
        PersonContactDetailInline,
        PersonLinkInline,
        PersonSourceInline,
        MembershipInline
    ]
