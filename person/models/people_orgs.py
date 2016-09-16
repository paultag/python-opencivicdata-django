import datetime
from django.db import models, transaction
from django.db.models import Q, QuerySet
from .base import OCDBase, LinkBase, RelatedBase, IdentifierBase
from .. import common

import uuid

# abstract models


class ContactDetailBase(RelatedBase):
    type = models.CharField(max_length=50, choices=common.CONTACT_TYPE_CHOICES)
    value = models.CharField(max_length=300)
    note = models.CharField(max_length=300, blank=True)
    label = models.CharField(max_length=300, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{}: {}'.format(self.get_type_display(), self.value)


class OtherNameBase(RelatedBase):
    name = models.CharField(max_length=500, db_index=True)
    note = models.CharField(max_length=500, blank=True)
    start_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10, blank=True)      # YYYY[-MM[-DD]]

    class Meta:
        abstract = True

    def __str__(self):
        return '{} ({})'.format(self.name, self.note)


class Person(OCDBase):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=300, db_index=True)
    sort_name = models.CharField(max_length=100, default='', blank=True)
    family_name = models.CharField(max_length=100, blank=True)
    given_name = models.CharField(max_length=100, blank=True)

    image = models.URLField(blank=True, max_length=2000)
    gender = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=500, blank=True)
    national_identity = models.CharField(max_length=300, blank=True)
    biography = models.TextField(blank=True)
    birth_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    death_date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]

    def __str__(self):
        return self.name

    def add_other_name(self, name, note=""):
        PersonName.objects.create(name=name,
                        note=note,
                        person_id=self.id)

    class Meta:
        verbose_name_plural = "people"


class PersonIdentifier(IdentifierBase):
    person = models.ForeignKey(Person, related_name='identifiers')


class PersonName(OtherNameBase):
    person = models.ForeignKey(Person, related_name='other_names')


class PersonContactDetail(ContactDetailBase):
    person = models.ForeignKey(Person, related_name='contact_details')


class PersonLink(LinkBase):
    person = models.ForeignKey(Person, related_name='links')


class PersonSource(LinkBase):
    person = models.ForeignKey(Person, related_name='sources')
