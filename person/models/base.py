import re
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.core.validators import RegexValidator

from .. import common


class OCDBase(models.Model):
    """ common base fields across all top-level models """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    extras = JSONField(default=dict, blank=True)
    locked_fields = ArrayField(base_field=models.TextField(), blank=True, default=list)

    class Meta:
        abstract = True


class RelatedBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class LinkBase(RelatedBase):
    note = models.CharField(max_length=300, blank=True)
    url = models.URLField(max_length=2000)

    class Meta:
        abstract = True

    def __str__(self):
        return self.url


class MimetypeLinkBase(RelatedBase):
    media_type = models.CharField(max_length=100)
    url = models.URLField(max_length=2000)
    text = models.TextField(default='', blank=True)

    class Meta:
        abstract = True


class IdentifierBase(RelatedBase):
    identifier = models.CharField(max_length=300)
    scheme = models.CharField(max_length=300)

    class Meta:
        abstract = True

    def __str__(self):
        return self.identifier
