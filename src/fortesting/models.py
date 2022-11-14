from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class DummyModel(models.Model):
    title = models.CharField(max_length=220)
    rating = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self) -> str:
        return self.title
