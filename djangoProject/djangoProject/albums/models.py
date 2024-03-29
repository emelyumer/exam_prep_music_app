from django.core.validators import MinValueValidator
from django.db import models

from djangoProject.profiles.models import Profile
class Genre(models.TextChoices):
    GENRE_POP = "Pop Music"
    GENRE_JAZZ = "Jazz Music"
    GENRE_ROCK = "Rock Music"
    GENRE_COUNTRY = "Country Music"
    GENRE_RNB = "R&B Music"
    GENRE_DANCE = "Dance Music"
    GENRE_HIP_HOP = "Hip Hop Music"
    GENRE_OTHER = "Other"

class Album(models.Model):
    # GENRE_CHOISES = (
    #     (GENRE_POP, GENRE_POP),
    #     (GENRE_JAZZ, GENRE_JAZZ),
    #     (GENRE_ROCK, GENRE_ROCK),
    #     (GENRE_COUNTRY, GENRE_COUNTRY),
    #     (GENRE_RNB, GENRE_RNB),
    #     (GENRE_DANCE, GENRE_DANCE),
    #     (GENRE_HIP_HOP, GENRE_HIP_HOP),
    #     (GENRE_OTHER, GENRE_OTHER)
    # )

    name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
        verbose_name="Album Name",
    )

    artist_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        verbose_name="Artist"
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        choices=Genre.choices,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL",
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(0.0),
        )
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
