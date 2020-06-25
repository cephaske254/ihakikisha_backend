from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone(value):
    if not value.startswith('+'):
        raise ValidationError(
    'Phone Numbers must have a country code!'
    )

    if value.startswith('+') and len(value.replace('+','')) <12:
        raise ValidationError(
        'Enter a valid length!'
    )        

    if len(value) < 10:
        raise ValidationError(
        'Enter a valid length!'
    )
    if not value.replace('+','').isnumeric():
        raise ValidationError(
        'Numbers 0-9 and + only are acceptable!'
    )
