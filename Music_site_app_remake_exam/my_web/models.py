from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_username(value):
    ERROR_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'
    ALLOWED_CHARS = ['_', ]

    for char in value:
        if char in ALLOWED_CHARS:
            continue

        if not char.isalnum():
            raise ValidationError(ERROR_MESSAGE)


class ProfileModel(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2
    ERROR_MSG_MIN_LEN = 'Username must be at least 2 chars!'

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(USERNAME_MIN_LEN, message=ERROR_MSG_MIN_LEN),
            validate_username,
        ],
    )

    email = models.EmailField()
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
