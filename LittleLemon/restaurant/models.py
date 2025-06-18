from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Booking(models.Model):
    name = models.CharField(max_length=255, default="", blank=True
                            )
    no_of_guests = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)],
        default=1  
    )
    booking_time = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return f"Booking #{self.pk} for {self.name}"

class Menu(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        default="",
        blank=True)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)]
    )
    inventory = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=1  
    )

    def __str__(self):
        return self.title