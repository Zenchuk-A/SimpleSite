from datetime import date

from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    age = (date.today() - value).days / 365
    if age < 1 or age > 120:
        raise ValidationError('Expected age from 1 to 120 years.')
