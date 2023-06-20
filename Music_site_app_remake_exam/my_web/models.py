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


def price_cannot_be_below_zero(value):
    ERROR_MESSAGE = 'The price cannot be below 0.0!'
    if value < 0:
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


class AlbumModel(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_CHOICES = (
        ("Pop Music", "1-Pop Music"),
        ("Jazz Music", "2-Jazz Music"),
        ("R&B Music", "3-R&B Music"),
        ("Rock Music", "4-Rock Music"),
        ("Country Music", "5-Country Music"),
        ("Dance Music", "6-Dance Music"),
        ("Hip Hop Music", "7-Hip Hop Music"),
        ("Other", "8-Other"),
    )

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
    )

    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[
            price_cannot_be_below_zero,
        ]
    )
