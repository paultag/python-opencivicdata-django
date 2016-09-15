"""
Module for declaration of common constants available throughout Open Civic Data code.
"""

# helper for making options-only lists
_keys = lambda allopts: [opt[0] for opt in allopts]


# NOTE: this list explicitly does not include RFC 6350s 'cell' as that is redundant with
# voice and the distinction will only lead to confusion.  contact_detail.note can be
# used to indicate if something is a home, work, cell, etc.
CONTACT_TYPE_CHOICES = (
    ('address', 'Postal Address'),
    ('email', 'Email'),
    ('url', 'URL'),
    ('fax', 'Fax'),
    ('text', 'Text Phone'),
    ('voice', 'Voice Phone'),
    ('video', 'Video Phone'),
    ('pager', 'Pager'),
    ('textphone', 'Device for people with hearing impairment'),
)
CONTACT_TYPES = _keys(CONTACT_TYPE_CHOICES)


ORGANIZATION_CLASSIFICATION_CHOICES = (
    ('legislature', 'Legislature'),
    ('executive', 'Executive'),
    ('upper', 'Upper Chamber'),
    ('lower', 'Lower Chamber'),
    ('party', 'Party'),
    ('committee', 'Committee'),
    ('commission', 'Commission'),
    ('corporation', 'Corporation'),
    ('agency', 'Agency'),
    ('department', 'Department'),
)
ORGANIZATION_CLASSIFICATIONS = _keys(ORGANIZATION_CLASSIFICATION_CHOICES)
